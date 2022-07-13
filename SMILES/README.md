# SMILES
root: SMLES
- canonical_SMILES.py: 从puhchem上爬底物的SMILES图
- data-process.py: 生成input_file.tsv，以#号分割
- data-show.py: 展示模型预测结果，附加上分布图片和预测数据
- pnas.py: 文献原始数据操作，同时爬去酶的fasta序列
- test-requests.py: 测试爬虫，爬去SMILES信息
- unit.py: Args, Log
- verity-sub.py: 验证底物信息
- data dir: 
  - EFI-Image: 存放不同酶数据分布图片（实验值和预测值，R2 & RMSE）
  - fasta: 爬取的fasta序列，以EFI-ID命名
  - input_file.tsv: 生成的模型输入数据
  - kcat.xlsx: 生成的结果数据（copy pnas.xlsx，附加上分布图片和预测数据
  - output.tsv: 模型的生成的结果数据
  - pnas.1423570112.sd01.xlsx: 底物信息
  - pnas.xlsx: 文献原始数据
  - substrate.xlsx: 生成底物信息
    - sheet0: 底物和对应的SMILES信息（canonical_SMILES.py 生成）
    - sheet1: 底物分布图
    - sheet2: 原始底物信息

流程：
- 获取底物对应的SMILES信息: canonical_SMILES.py
- 生成预测数据，模型预测，显示结果
- 


