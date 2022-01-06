import logging, json

import config

l = logging.getLogger(__name__)


def compile_pocket_sphinx_lines(raw_transcript):
    constructed_lines = []
    raw_transcript_indexes = (len(raw_transcript))
    raw_transcript_last_index = 1
    output_index = 0
    while raw_transcript_last_index < (raw_transcript_indexes - 1):
        raw_transcript_current_index, \
            line_start_time, \
            line_end_time, \
            line_duration, \
            line = compile_pocket_sphinx_line(raw_transcript,
                                             start_index=raw_transcript_last_index,
                                             indexes=raw_transcript_indexes)

        line_entry = {"index": output_index,
                      "line_start_time": line_start_time,
                      "line_end_time": line_end_time,
                      "line_duration": line_duration,
                      "line": line
                      }

        raw_transcript_last_index = raw_transcript_current_index
        output_index = output_index + 1

        if line == '':
            continue

        constructed_lines.append(line_entry)
    return constructed_lines

def compile_pocket_sphinx_line(raw_transcript, start_index, indexes):
    ignore_words = json.loads(config.get['pocket_sphinx']['ignore_words'])
    sil_str = config.get['pocket_sphinx']['sil_str']
    line = []
    line_start_time = raw_transcript[start_index][1]

    sil_encountered = False
    for x in range(start_index, indexes):
        entry = raw_transcript[x]
        word = entry[0]
        start = entry[1]
        end = entry[2]
        duration = entry[3]
        index = x

        if word in ignore_words:
            continue
        elif word != sil_str:
            word = truncate_string(word)
            line.append(word)
        elif word == sil_str:
            if sil_encountered == False:
                l.debug("First sil string encountered, skipping...")
                sil_encountered = True
                continue
            elif sil_encountered == True:
                l.debug("Second sil string encountered, ending this line.")
                sil_encountered = False
                break
        l.debug("Word: " + word + " Start: " + str(start) + " End: " + str(end) + " Duration: " + str(duration))
    line_end_time = end
    line_duration = line_end_time - line_start_time

    line = concat_list_to_string(list_of_string=line)
    return index, line_start_time, line_end_time, line_duration, line


def truncate_string(string):
    truncate_list = json.loads(config.get['pocket_sphinx']['truncate_words'])
    for entry in truncate_list:
        string = string.replace(entry, '')
    return string


def concat_list_to_string(list_of_string):
    newlist = " "
    final_list = newlist.join(list_of_string)
    l.debug(final_list)
    return final_list


