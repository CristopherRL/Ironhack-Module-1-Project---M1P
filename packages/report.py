######################################### IMPORTING LIBRARIES #################################################
import matplotlib.pyplot as plt

def plotting_data(table,top):

    meanW_GDPP = table

    #x = list(meanW_GDPP.country)
    #y = list(meanW_GDPP.ratio_MUSD)

    fig = meanW_GDPP.plot(kind='barh', x='country', y='ratio_MUSD').get_figure()

    plt.xlabel('ratio_MUSD')
    plt.ylabel('countries')
    plt.title(f'TOP {top} - Comparing Billionaries with GDP by Country')
    plt.grid(True)

    fig.savefig(f'data/results/TOP{top}-Billionaries_by_Industry.png')
    print(f'Process finished! The plot is located in: data/results/TOP{top}-Billionaries_by_Country.png')