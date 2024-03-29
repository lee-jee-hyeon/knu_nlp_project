import pandas as pd
from typing import Set
import numpy as np
from pykospacing import Spacing

STOP_WORDS:Set[str] = set(pd.read_csv('./data/stopwords.txt',sep='\n').to_numpy().reshape(1,-1).tolist()[0])
spacer = Spacing()
                 
def preprocessing_only_korean(df:pd.DataFrame,col_name:str) -> pd.DataFrame:
    this_df = df.copy()
    
    print('\n\n전처리 전 차원 : ',this_df.shape)
    
    this_df.loc[:,col_name] = this_df[col_name].str.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','',regex=True) # 한글 또는 공백이 아닌 문자 제거
    this_df.loc[:,col_name] = this_df[col_name].str.replace('^ +','') # 문자 앞 공백 제거(데이터에 맞춰진 형식, 수정 요)
    this_df[col_name].replace('', np.nan, inplace=True) # 공백 None으로
    this_df.dropna(inplace=True,subset=[col_name])
    
    print('전처리 후 차원 : ',this_df.shape,end='\n\n')
    
    return this_df