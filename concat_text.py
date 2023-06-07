folder = 'data'
filename = 'ChatRWKV技术研发群0401'

with open(f'{folder}/segment_{filename}.txt', 'w', encoding='utf-8') as f:
    print('\n\n\n'.join(['\n'.join(segment) for segment in message_segments]), file=f)