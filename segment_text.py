from datetime import datetime

def iterative_segment_messages(messages, max_tokens = 3850):
    segments = [messages]
    while True:
        num_segments = len(segments)
        for i in range(num_segments):
            segment = segments[i]
            if len(segment) <= 1:
                continue
            timestamps, messages = zip(*segment)
            intervals = [int((timestamps[j+1] - timestamps[j]).total_seconds()) for j in range(len(timestamps)-1)]
            max_interval_idx = max(range(len(intervals)), key=lambda i: intervals[i])
            if intervals[max_interval_idx] < 120:
                continue
            left_segment = segment[:max_interval_idx+1]
            right_segment = segment[max_interval_idx+1:]
            segments[i:i+1] = [left_segment, right_segment]
        if len(segments) == num_segments:
            break
    compact_segments = []
    current_segment = []
    current_size = 0
    len_of_segments = [sum(len(message) + 1 for timestamp, message in segment) for segment in segments]
    for segment, len_of_segment in zip(segments, len_of_segments):
        if current_size + len_of_segment <= max_tokens:
            current_segment.extend(segment)
            current_size += len_of_segment
        else:
            if current_segment:
                compact_segments.append(current_segment)
            current_segment = segment
            current_size = len_of_segment
    if current_segment:
        compact_segments.append(current_segment)
    return compact_segments
