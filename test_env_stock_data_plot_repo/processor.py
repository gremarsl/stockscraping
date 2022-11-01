import os

import pandas as pd


class Processor:
    @staticmethod
    def merge_csv_files(file_list, symbol_list):
        try:
            for idx, symbol in enumerate(symbol_list):
                destination_file_path = os.getcwd() + "\\total_data_" + symbol + ".csv"

                frames = [pd.read_csv(f) for f in file_list]
                combined_csv = pd.concat(frames, axis="columns")
                combined_csv.to_csv(destination_file_path, index=True, encoding='utf-8-sig')
                print("merge was successful")
                return destination_file_path
        except:
            print("merge failed!")
