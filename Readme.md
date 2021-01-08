# Dataset
Download and place the dataset in files folder of project root.

Folder structure -
```shell
- mnist
  - files
      - dataset
        - test.csv
        - train.csv
```
Location: ```https://www.kaggle.com/c/digit-recognizer/data```

# Project Setup
On local machine
```shell
    pip3 install -r requirements.txt
```
With docker-compose
```shell
  docker-compose up --build -d
```

# Running
```shell
    python main.py --mode train
    python main.py --mode test
```

# 98.103 % accuracy on first submission

# Kaggle Result
![alt text](https://github.com/mrscp/mnist/blob/master/kaggle-result.png?raw=true)