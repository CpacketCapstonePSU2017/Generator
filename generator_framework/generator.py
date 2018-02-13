'''
    Author:
'''

from generator_config import *
import sys
sys.path.append('../resources')
from resources.weibull import *
from os import path, remove
from resources.config import RESOURCES_DIR
from resources import db_config
sys.path.append(path.join(ROOT_DIR, 'CPacket-Common-Modules'))
from io_framework.csv_writer import CsvWriter


class Generator:
    def __init__(self):
        self._Config = GeneratorConfig()
        # TODO: This can be converted to only self._Config.**** No need to make copies
        self._Columns = 'avg_hrcrx_max_byt'
        self._data_writer = CsvWriter(host=db_config.host, port=db_config.port, username=db_config.username,
                                      password=db_config.password, database=self._Config.Database)
        self.Dist_Array = self._Config.Func_Type.generate()


    def nparray_to_dataframe(self):
        indexes = pd.DataFrame(self.Dist_Array[:, 0])
        indexes[0] = pd.to_datetime(indexes[0], format='%Y-%m-%d %H:%M:%S')
        cols = [self._Columns]
        df = pd.DataFrame(data=self.Dist_Array[0:, 1:],
                          index=indexes[0],
                          columns=cols)
        return df

    def write_data_to_csv(self):
        df = self.nparray_to_dataframe()
        model_name = self._Config.Func_Type.Name
        if not isinstance(df, pd.DataFrame):
            print("Error reading the data from database. Please test this query in Chronograf/Grafana.")
        df.to_csv(path.join(RESOURCES_DIR, model_name + "_generated.csv"))

    def write_data_to_database(self):
        df = self.nparray_to_dataframe()
        model_name = self._Config.Func_Type.Name
        df.to_csv(path.join(RESOURCES_DIR, model_name + "_generated.csv"))
        self._data_writer.csv_file_to_db(measurement_to_use=model_name + '_generated',
                                         new_csv_file_name=path.join(RESOURCES_DIR, model_name + "_generated.csv"))
        remove(path.join(RESOURCES_DIR, model_name + "_generated.csv"))


# Test Code - Delete later
test_generator = Generator()
test_generator.write_data_to_csv()
test_generator.write_data_to_database()

