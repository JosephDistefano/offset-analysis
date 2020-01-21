import os
import logging
import pyxdf


class Xdf_file_read:
    def Xdf_Load(path):
        logging.basicConfig(level=logging.DEBUG)  # Use logging.INFO to reduce output.
        fname = path
        streams, fileheader = pyxdf.load_xdf(fname)

        print("Found {} streams:".format(len(streams)))
        for ix, stream in enumerate(streams):
            print("Stream {}: {} - type {} - uid {} - shape {} at {} Hz (effective {} Hz)".format(
                ix + 1, stream['info']['name'][0],
                stream['info']['type'][0],
                stream['info']['uid'][0],
                (int(stream['info']['channel_count'][0]), len(stream['time_stamps'])),
                stream['info']['nominal_srate'][0],
                stream['info']['effective_srate'])
            )
            if any(stream['time_stamps']):
                print("\tDuration: {} s".format(stream['time_stamps'][-1] - stream['time_stamps'][0]))
        print("Done.")
        return streams, fileheader