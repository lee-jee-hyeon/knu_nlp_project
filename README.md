# project_mini_nlp

경북대 빅데이터 분석가 양성과정 자연어 처리 미니프로젝트 1조

## Dataset

- reviews_1647645839.csv : 네이버 영화 평점 및 리뷰 크롤링 데이터
  - df_notk : 위의 전처리한 데이터
- ratings*.txt : 네이버 영화 감성분석 데이터
- stopwords.txt : 불용어 사전 [출처](https://deep.chulgil.me/hangugeo-bulyongeo-riseuteu/)
- train_sample : rating_train 샘플링 데이터 (40000 rows)
- test_sample : rating_test 샘플링 데이터 (10000 rows)
  
- SubSets : (processed 이하), 위의 데이터셋을 전처리한 파일

## Models

- ANN
- LSTM
- Bi-LSTM
- KoBERT
- bert base multilingual cased model(from Hugging Face)

### used packages (dependancy not always)

- padnas
- numpy
- seaborn
- matplot
- konlpy
  - okt
  - kkm
  - khaiii
- Spacing
- tensorflow
- pytorch
- tqdm
- transformers
- sentencepiece
- tensorflow_addons
