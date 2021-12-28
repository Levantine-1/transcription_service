import logging
from logging.handlers import RotatingFileHandler
import config, transcriber, line_compiler

# Setup logging
logfile = config.get['logging']['logfile']
log_lvl = config.get['logging']['loglevel']
log_out = config.get['logging']['log_stream_to_console']
max_bytes = int(config.get['logging']['maxBytes'])
backup_count = int(config.get['logging']['backupCount'])

my_handler = RotatingFileHandler(logfile, mode='a', maxBytes=max_bytes,
                                 backupCount=backup_count, encoding=None,
                                 delay=False)
my_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: %(message)s'))
l = logging.getLogger()
l.setLevel(log_lvl.upper())
l.addHandler(my_handler)
if log_out.upper() == 'TRUE':
    l.addHandler(logging.StreamHandler())

l.info("Initializing Server...")


def function1():
    # wav_file = "../jfk-moon-speech.wav"
    wav_file = "../obama.wav"
    raw_transcript = transcriber.transcribe(wav_file=wav_file)
    # raw_transcript = [('<s>', 0.0, 0.23194322296137607, 22), ('i', 0.24248609673234772, 0.4006292032969223, 15), ('believe', 0.41117207706789394, 0.8750585229906461, 44), ('that(2)', 0.8856013967616178, 1.0753731246391074, 18), ('it', 1.085915998410079, 1.28623060005854, 19), ('made', 1.2967734738295118, 1.5076309492489444, 20), ('him', 1.5181738230199162, 1.7290312984393488, 20), ('to', 1.7395741722103204, 2.0874890066523846, 33), ('men', 2.098031880423356, 2.256174986987931, 15), ('itself', 2.2667178607589027, 2.7727758017655413, 48), ('<sil>', 2.783318675536513, 3.2893766165431515, 48), ('which(2)', 3.299919490314123, 3.574034208359386, 26), ('he', 3.5845770821303575, 3.8586918001756203, 26), ('made', 3.869234673946592, 4.069549275595053, 19), ('all', 4.080092149366025, 4.702121701853351, 59), ('<sil>', 4.712664575624323, 5.007865041211529, 28), ('before(2)', 5.018407914982501, 5.429579992050394, 39), ('this', 5.440122865821365, 5.640437467469828, 19), ('decade', 5.650980341240799, 6.157038282247438, 48), ('is', 6.167581156018409, 6.315181388812012, 14), ('out', 6.325724262582985, 6.6209247281701895, 28), ('[SPEECH]', 6.631467601941161, 6.779067834734764, 14), ('<sil>', 6.7896107085057364, 7.169154164260715, 36), ('of', 7.179697038031686, 7.2956686495123755, 11), ('line', 7.306211523283347, 7.654126357725411, 33), ('in', 7.664669231496382, 7.738469347893184, 7), ('the', 7.749012221664155, 7.812269464289985, 6), ('minimum', 7.822812338060956, 8.455384764319255, 60), ('own', 8.465927638090227, 8.87709971515812, 39), ('and', 8.887642588929094, 8.982528452867838, 9), ('returning(2)', 8.993071326638809, 9.50967214141642, 49), ('him(2)', 9.520215015187391, 9.72052961683585, 19), ('<sil>', 9.731072490606824, 9.847044102087512, 11), ('safely', 9.857586975858483, 10.374187790636094, 49), ('to(2)', 10.384730664407064, 10.469073654574839, 8), ('the(2)', 10.47961652834581, 10.67993112999427, 19), ('other', 10.690474003765242, 11.11218895460411, 40), ('<sil>', 11.122731828375079, 11.681504138236578, 53), ('<sil>', 11.692047012007547, 12.177019205472243, 46), ('noting', 12.187562079243216, 12.683077146478883, 47), ('most', 12.693620020249856, 12.967734738295118, 26), ('basic', 12.978277612066087, 13.326192446508154, 33), ('clinton', 13.336735320279125, 13.958764872766452, 59), ('is', 13.969307746537423, 14.106365105560055, 13), ('the(2)', 14.116907979331025, 14.422651318689203, 29), ('and(2)', 14.433194192460174, 14.686223162963493, 24), ('<sil>', 14.696766036734466, 14.970880754779728, 26), ('the(2)', 14.9814236285507, 15.03413799740556, 5), ('more', 15.04468087117653, 15.297709841679849, 24), ('impressive', 15.308252715450822, 15.88811077285426, 55), ('committing', 15.898653646625233, 16.362540092547984, 44), ('a(2)', 16.373082966318957, 16.3941687138609, 2), ('crime', 16.404711587631873, 16.98456964503531, 55), ('<sil>', 16.995112518806284, 17.321941605706403, 31), ('or', 17.332484479477376, 17.48008471227098, 14), ('want(2)', 17.490627586041953, 17.901799663109845, 39), ('what(2)', 17.912342536880814, 18.228628750009964, 30), ('move', 18.239171623780937, 18.52382921559717, 27), ('along', 18.534372089368144, 18.935001292665067, 38), ('with', 18.945544166436036, 19.061515777916725, 11), ('the(2)', 19.072058651687698, 19.198573136939356, 12), ('end', 19.20911601071033, 19.66245958286211, 43), ('<sil>', 19.673002456633082, 19.694088204175024, 2), ('latest', 19.704631077945994, 20.305574882891378, 57), ('d.', 20.31611775666235, 20.621861096020528, 29), ('c.', 20.6324039697915, 20.88543294029482, 24), ('</s>', 20.89597581406579, 20.969775930462593, 7)]
    transcript = line_compiler.compile_pocket_phynx_lines(raw_transcript)


if __name__ == '__main__':
    function1()