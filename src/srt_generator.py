from datetime import timedelta
import srt, logging, config, line_compiler
l = logging.getLogger(__name__)

def generate_srt(transcript):
    l.info("Generating SRT file")
    result = []
    for i in range(len(transcript)):
        index = transcript[i]['index']
        start = timedelta(transcript[i]['line_start_time'])
        end = timedelta(transcript[i]['line_end_time'])
        content = transcript[i]['line']
        subs = [
            srt.Subtitle(index=index, start=start, end=end, content=content),
        ]
        compose = srt.compose(subs, start_index=index)
        result.append(compose)

    return result

def save_result_to_file(filename, data):
    l.info("Saving SRT file to: " + filename)
    outfile = open(filename, "w")
    for line in data:
        outfile.write(line)
    outfile.close()
    return True
