"""
    This code is released under an MIT license
"""
from generator_framework.generator import Generator
from generator_framework.generator_config import GeneratorConfig
from datetime import datetime
# from resources.config import RESOURCES_DIR
from resources import db_config
# from pydoc import locate
import sys
from os import path
from root import ROOT_DIR
sys.path.append(path.join(ROOT_DIR, 'CPacket-Common-Modules'))
from io_framework.csv_writer import CsvWriter


class TrafficGenerator:
    _data_writer = None

    def __init__(self, database='generated_data'):
        self.gen_config = GeneratorConfig()
        # Don't run default generator on init
        self.generator = None
        self._selected_model = None
        # is this line needed?
        self._data_writer = CsvWriter(host=db_config.host, port=db_config.port, username=db_config.username,
                                      password=db_config.password, database=database)

    def main(self):
        # Using f string format and getattribute for safety
        print(f"""Welcome to the Traffic Generator!
Default generator configuration:
    Default database: {self.gen_config.__getattribute__('Database')}
    Default number of days: {self.gen_config.__getattribute__('Days')}
    Default high max: {self.gen_config.__getattribute__('High_Max')}
    Default high min: {self.gen_config.__getattribute__('High_Min')}
    Default low max: {self.gen_config.__getattribute__('Low_Max')}
    Default low min: {self.gen_config.__getattribute__('Low_Min')}
    Default business hours: {self.gen_config.__getattribute__('Business_Hours')}
    Default shape: {self.gen_config.__getattribute__('Shape')}
    Default start date: {self.gen_config.__getattribute__('Start_Date')}
    Default work hour start: {self.gen_config.__getattribute__('Work_Hour_Start')}
    Default scale: {self.gen_config.__getattribute__('Scale')}
    Default function type: {self.gen_config.Func_Type.Name}
    """)
        print("Would you like to set the parameters for generator first? [y]/[n]")
        selection = input("Prompt: ")
        if selection.lower() == 'y':
            selection = input("Choose number of days to generate: ")
            self.gen_config.__setattr__("Days", int(selection))
            selection = input("Choose high max: ")
            self.gen_config.__setattr__("High_Max", float(selection))
            selection = input("Choose high min: ")
            self.gen_config.__setattr__("High_min", float(selection))
            selection = input("Choose low max: ")
            self.gen_config.__setattr__("Low_Max", float(selection))
            selection = input("Choose low min: ")
            self.gen_config.__setattr__("Low_Min", float(selection))
            selection = input("Choose business hours: ")
            self.gen_config.__setattr__("Business_Hours", int(selection))
            selection = input("Choose shape: ")
            self.gen_config.__setattr__("Shape", float(selection))
            selection = input("Choose start date (YYYY-MM-DD): ")
            self.gen_config.__setattr__("Start_Date", datetime.strptime(selection, '%Y-%m-%d'))
            selection = input("Choose work hour start: ")
            self.gen_config.__setattr__("Work_Hour_Start", int(selection))
            selection = input("Choose scale: ")
            self.gen_config.__setattr__("Scale", int(selection))
            selection = input("Choose function type: ")
            self.gen_config.set_func_type(selection)
        input("Generator configuration is set. Press any key to continue...")
        self.generator = Generator(self.gen_config)
        print("Finished generating the traffic. Do you want to write it to database: {}? [y]/[n]".
              format(self.gen_config.__getattribute__("Database")))
        print("If [n], the data will be stored in csv file")
        selection = input("Prompt: ")
        if selection == 'y':
            self.generator.write_data_to_database()
        else:
            self.generator.write_data_to_csv()
