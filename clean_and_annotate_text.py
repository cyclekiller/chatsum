import re
from segment_text import iterative_segment_messages
from datetime import datetime

def extract_username(input_str):
    # Split the input string by space, underscore, or bracket
    split_str = re.split('[\s_(（]+', input_str)
    # The username is the first element in the split string
    username = split_str[0]
    return username

username_idx = []
datetimes = []
def clean_text(lines):
    cleaned_lines = []

    user_line = True
    i = 0
    while i < len(lines):
        line = lines[i].strip('\n\ufeff')
        if not user_line: # TODO: handle multiline message
            if not line:
                user_line = True
            cleaned_lines.append(line)
            i += 1
            continue
        else: # this line should contain username
            if not re.findall(r'20[\d-]{8}\s[\d:]{7,8}\s+[^\n]+(?:\d{5,11}|@[\.\w]+\.[comnet]{2,3}[\>\)])', line): # someone posted an empty line
                i += 1
                continue
            if not lines[i + 1].strip('\n\ufeff') and not lines[i + 2].strip('\n\ufeff'): # re.findall(r'20[\d-]{8}\s[\d:]{7,8}\s+[^\n]+(?:\d{5,11}|@[\.\w]+\.[comnet]{2,3}[\>\)])', line):
                i += 3
                continue # a image or some media, no text

        user_line = False
        spt = line.split(' ', 2)
        dt = spt[:2] # datetime
        username = spt[2]
        if username[-1] == ')':
            username = username.rsplit('(', 1)[0]
        elif username[-1] == '>':
            username = username.rsplit('<', 1)[0]

        username_idx.append(len(cleaned_lines))
        cleaned_lines.append(username)
        datetimes.append(dt)
        i += 1
    
    # Join the cleaned lines back into a string
    cleaned_text = '\n'.join(cleaned_lines)
    return cleaned_text

def add_said(lines):
    added_lines = []
    added_times = []
    for i, idx in enumerate(username_idx):
        username = lines[idx].strip('\n')
        if username == '系统消息':
            continue
        username = re.sub(r'【..】', '', username)
        added_lines.append(re.sub(r'/..', '', username) + '说：')
        # if lines[idx + 1].startswith('@'):
        #     to_user, content = lines[idx + 1].split(' ', 1)
        #     if len(to_user) > 1:
        #         lines[idx + 1] = content
        #         to_user = to_user[1:]
        #         if username == to_user:
        #             added_lines[-1] = added_lines[-1][:-2] + '继续说：'
        #         else:
        #             added_lines[-1] = added_lines[-1][:-2] + '对' + to_user + '说：'
        added_lines += lines[idx + 1] # only the first line for multi-line messages
        added_times.append(datetimes[i][0] + 'T' + f'{datetimes[i][1]:0>8}')
    print('\n'.join(added_times), file=open(f'{folder}/times_{filename}.txt', 'w'))
    return ''.join(added_lines)

# def segment_time(times):
    

folder = 'data'
filename = "ChatRWKV技术研发群0401"

cleaned_text = clean_text(open(f'{folder}/{filename}.txt', 'r', encoding='utf-8').readlines())
with open(f'{folder}/cleaned_{filename}.txt', 'w', encoding='utf-8') as f:
    print(cleaned_text, file=f)

with open(f'{folder}/added_{filename}.txt', 'w', encoding='utf-8') as f:
    print(add_said(open(f'{folder}/cleaned_{filename}.txt', 'r', encoding='utf-8').readlines()), file=f)

with open(f'{folder}/times_{filename}.txt', 'r', encoding='utf-8') as f:
    times = f.readlines()
with open(f'{folder}/added_{filename}.txt', 'r', encoding='utf-8') as f:
    messages = f.readlines()
compact_segments = iterative_segment_messages([(datetime.fromisoformat(time.strip('\n')), message.strip('\n')) for time, message in zip(times, messages)])
print(f'{len(compact_segments)} segments in total.')
str_segments = [[str(time) + ' ' + message for time, message in segment] for segment in compact_segments]
for segment in compact_segments:
    print(f'from {segment[0][0]} to {segment[-1][0]}: ')
with open(f'{folder}/segment_with_time{filename}.txt', 'w', encoding='utf-8') as f:
    print('\n\n\n'.join(['\n'.join(segment) for segment in str_segments]), file=f)
message_segments = [[message for _, message in segment] for segment in compact_segments]
with open(f'{folder}/segment_{filename}.txt', 'w', encoding='utf-8') as f:
    print('\n\n\n'.join(['\n'.join(segment) for segment in message_segments]), file=f)
with open(f'{folder}/segment_one_line{filename}.txt', 'w', encoding='utf-8') as f:
    print('\n\n\n'.join(['   '.join(segment) for segment in message_segments]), file=f)