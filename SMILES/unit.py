import os
import sys
import time


class Args:
    def __init__(self):
        # 获取当前文件路径
        self._curr_dir, _curr_file_name = os.path.split(os.path.abspath(__file__))  # unit path.py
        # 根目录
        self._root = self._curr_dir

        # data 文件夹
        self.data_dir = os.path.join(self._root, 'data')

        # 源文件
        self._source_xlsx = 'pnas.xlsx'
        self.pnas_xlsx = os.path.join(self.data_dir, self._source_xlsx)
        if not os.path.exists(self.pnas_xlsx):
            print(f'error: {self.pnas_xlsx} 文件不存在')
            raise

        # 底物数据
        self.substrate = 'substrate.xlsx'
        self.substrate = os.path.join(self.data_dir, self.substrate)
        if not os.path.exists(self.substrate):
            print(f'error: {self.substrate} 文件不存在')
            raise

        # 日志文件
        self.log = "log.txt"
        self.log = os.path.join(self.data_dir, self.log)

        # fasta文件夹
        self.fasta = os.path.join(self.data_dir, 'fasta')
        if not os.path.exists(self.fasta):
            os.makedirs(self.fasta)

        # efi image dir
        self.efi_image = os.path.join(self.data_dir, 'EFI-Image')
        if not os.path.exists(self.efi_image):
            os.makedirs(self.efi_image)

        # 生成文件
        self.input_file = "input_file.tsv"
        self.input_file = os.path.join(self.data_dir, self.input_file)

        self.pnas_kcat = 'kcat.xlsx'
        self.pnas_kcat = os.path.join(self.data_dir, self.pnas_kcat)

        self.output_tsv = "output.tsv"
        self.output_tsv = os.path.join(self.data_dir, self.output_tsv)
        if not os.path.exists(self.output_tsv):
            print(f'error: {self.output_tsv} 文件不存在')
            raise


class Log:
    def __init__(self, log_file_path):
        self._file = log_file_path

    def delete_log(self):
        if os.path.exists(self._file):
            os.remove(self._file)

    def append(self, mess):
        print(mess)
        with open(self._file, "a", encoding="utf-8") as w:
            strs = f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())},{mess} \n'
            w.write(strs)
