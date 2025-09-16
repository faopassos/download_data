import sys
import json
import logging
from download_embracedata import Embrace_Data

get_data = Embrace_Data()

def download_files(instrument, settings):
    instrument = instrument.upper()
    if instrument == "CALLISTO":
        get_data.Callisto(**settings[instrument])
    elif instrument == "IMAGER":
        get_data.Imager(**settings[instrument])
    elif instrument == "IONOSONDE":
        get_data.Ionosonde(**settings[instrument])
    elif instrument == "LIDAR":
        get_data.Lidar(**settings[instrument])
    elif instrument == "MAGNETOMETER":
        get_data.Magnetometer(**settings[instrument])
    elif instrument == "MAGNETOMETER_SEG":
        get_data.MagnetometerSeg(**settings[instrument])
    elif instrument == "SCINTILLATION":
        get_data.Scintillation(**settings[instrument])
    else:
        logging.error(f"Instrument '{instrument}' not recognized.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <instrument>")
        sys.exit(1)

    with open("config.json", "r") as f:
        settings = json.load(f)

    instrument = sys.argv[1]
    download_files(instrument, settings)
