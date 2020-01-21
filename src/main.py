import yaml
from pathlib import Path
from utils import skip_run
from hdf_converters.subject_hdf_convertor.subject_hdf import subject_hdf
from hdf_converters.feature_hdf_convertor.feature_hdf import feature_hdf
from feature_extraction.feature_extraction_main import feature_extraction

config_path = Path(__file__).parents[1] / 'src/config.yml'
config = yaml.load(open(str(config_path)), Loader=yaml.SafeLoader)


with skip_run('run', 'Create Subject hdf Dictionary') as check, check():
    subject_hdf()

with skip_run('run', 'Feature Extraction') as check, check():
    feature_extraction()

with skip_run('run', 'Create feature hdf Dictionary') as check, check():
    feature_hdf()