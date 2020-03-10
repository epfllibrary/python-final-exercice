import pandas as pd

def average_percountry(dataframe):
    list_country=dataframe["country"].unique()
    outlist=[]
    for country in list_country:
        subset=dataframe[dataframe['country']==country]
        mean=subset.loc[:, "2011 mean":"2017 mean"].mean().mean()
        std=subset.loc[:, "2011 sd":"2017 sd"].mean().mean()

        outlist.append([mean,std])
    df=pd.DataFrame(outlist, index=list_country,columns=["average","std"])
    return df[df["average"]>0]
file="./data/score_benzoylecgonine_wastewater_loads_2011_2017"
data=pd.read_csv(file+".csv",delimiter=";",index_col=0)
avg_df=average_percountry(data)
avg_df.to_csv(file+"_meanpercountry.csv")