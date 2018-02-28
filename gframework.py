import pandas as pd
from generator_framework.generator import Generator
from generator_framework.generator_config import GeneratorConfig, Poisson, Weibull
from datetime import datetime
from resources.config import RESOURCES_DIR
from resources import db_config
from pydoc import locate
import sys
from os import path, remove
from root import ROOT_DIR
sys.path.append(path.join(ROOT_DIR,'CPacket-Common-Modules'))
from io_framework.csv_writer import CsvWriter


class TrafficGenerator:
    _data_writer = None

    def __init__(self, database='generated_data'):
        self.gen_config = GeneratorConfig()
        self.generator = Generator()
        self._selected_model = None
        self._data_writer = CsvWriter(host=db_config.host, port=db_config.port, username=db_config.username,
                                      password=db_config.password, database=database)

    def main(self):
        print("Welcome to the Traffic Generator!")
        print("Default generator configuration:")
        print("Default database: {}".format(self.gen_config.get_database()))
        print("Default number of days: {}".format(self.gen_config.get_days()))
        print("Default high max: {}".format(self.gen_config.get_high_max()))
        print("Default high min: {}".format(self.gen_config.get_high_min()))
        print("Default low max: {}".format(self.gen_config.get_low_max()))
        print("Default low min: {}".format(self.gen_config.get_low_min()))
        print("Default business hours: {}".format(self.gen_config.get_business_hours()))
        print("Default shape: {}".format(self.gen_config.get_shape()))
        print("Default start date: {}".format(self.gen_config.get_start_date()))
        print("Default work hour start: {}".format(self.gen_config.get_work_hour_start()))
        print("Default scale: {}".format(self.gen_config.get_scale()))
        print("Default function type: {}".format(self.gen_config.get_func_type()))
        print("Would you like to set the parameters for generator first? [y]/[n]")
        selection = input("Prompt: ")
        if selection.lower() == 'y':
            selection = input("Choose number of days to generate: ")
            self.gen_config.set_days(int(selection))
            selection = input("Choose high max: ")
            self.gen_config.set_high_max(float(selection))
            selection = input("Choose high min: ")
            self.gen_config.set_high_min(float(selection))
            selection = input("Choose low max: ")
            self.gen_config.set_low_max(float(selection))
            selection = input("Choose low min: ")
            self.gen_config.set_low_min(float(selection))
            selection = input("Choose business hours: ")
            self.gen_config.set_business_hours(int(selection))
            selection = input("Choose shape: ")
            self.gen_config.set_shape(float(selection))
            selection = input("Choose start date (YYYY-MM-DD): ")
            self.gen_config.set_start_date(datetime.strptime(selection, '%Y-%m-%d'))
            selection = input("Choose work hour start: ")
            self.gen_config.set_work_hour_start(int(selection))
            selection = input("Choose scale: ")
            self.gen_config.set_scale(int(selection))
            selection = input("Choose function type: ")
            self.gen_config.set_func_type(int(selection))
        input("Generator configuration is set. Press any key to continue...")

        self.generator = Generator(self.gen_config)

        print("Finished generating the traffic. Do you want to write it to database: {}? [y]/[n]".
              format(self.gen_config.get_database()))
        print("If [n], the data will be stored in csv file")
        selection = input("Prompt: ")
        if selection == 'y':
            self.generator.write_data_to_database()
        else:
            self.generator.write_data_to_csv()
