def edgelist_to_graph(df):
    import networkx as nx
    import pandas as pd
    import spacy
    import json
    import demoji
    df=df[['source','target']].fillna("X")
    df.columns=['source','target']
    edgelist=df
    edgelist.drop_duplicates(keep='first')
    print("Graph generation: ")
    G9=nx.from_pandas_edgelist(edgelist,source='source',target='target',create_using=nx.MultiDiGraph())
    print("Whole Graph size: ", G9.size(),"number of nodes:",G9.number_of_nodes())
    print(nx.info(G9))
    print("\n [*] All data loaded, Graph generated!")
    flnm="graph"+"-"+filename[37:]+".gexf"
    path='/root/jupyter/TM-Hunting/Eolas/files/'+flnm
    nx.write_gexf(G9, path)
    print(path," saved!")
    return path," saved!"