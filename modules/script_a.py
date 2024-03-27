from pandas import DataFrame 

def printer(val: str)-> None:
    print(val)


def addition(a:int, b: int)-> int:
    return a + b


class fakePandas(DataFrame ):
    
    def head(self, *args, **kwargs):
        print(""""
              Ola and Mayowa's Custom Pandas
              
              """)
        ans = super().head(*args, **kwargs)
        return ans
    
    def columns(self, *args, **kwargs):
        ans = super().columns
        print('these are the columns', ans)
        return ans

class DataFrame:

    def create_df(self):
        print('creating DataFrame')