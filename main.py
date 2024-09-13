# This code is written in python 
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell175.csv")

firstCountryBooleanList = lwd["country_name"] =="Pakistan"
firstCountryData = lwd.loc[firstCountryBooleanList] 

secondCountryBooleanList = lwd["country_name"] =="Colombia"
secondCountryData = lwd.loc[secondCountryBooleanList]  

# Print out the number of rows and columns
print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
plt.scatter(x= "year", y = "ED_attainment_no_educ_p",data = firstCountryData, color="magenta")
plt.scatter(x= "year", y = "ED_attainment_no_educ_p",data = secondCountryData, color="blue")

# add a title to the plot
plt.title("Women with no education \n Colombia (blue) & Pakistan (pink)")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Women with no education (%)")

# show the plot

#plt.ylim(0,83)
#plt.show()

print("The story takes place in the year 2015 in Colombia and Pakistan, two countries with unique stories behind them.\n")

input("Press enter to continue\n")

print("Pakistan is bordered by Iran, Afghanistan, China, India, and the Arabian Sea. The country features the Himalayas, Karakoram, and Hindu Kush ranges. Pakistan's climate is mostly arid with hot summers, mild winters, and a monsoon season.\n")

input("Press enter to continue\n")

print("Colombia is bordered by Panama, Venezuela, Brazil, Peru, Ecuador, the Caribbean Sea, and the Pacific Ocean. It includes the Amazon rainforest, the Andes mountains, and the Magdalena River, with a climate that ranges from tropical rainforests to high-altitude tundra.\n")

input("Press enter to continue\n")

print("The data represents women from various age groups in Colombia and Pakistan. Typically, these women range from young adults (18+) to middle-aged (up to 60). The data highlights the percentage of women with no education.\n")

input("Press enter to continue\n")

print("Maria, a 30-year-old teacher from rural Colombia, enjoys the benefits of her education and financial independence, actively participating in community projects and making her own decisions. She feels empowered and responsible for supporting her family and community.\n")

input("Press enter to continue\n")

print("In contrast, Maryam, a 35-year-old woman from a village in Pakistan, struggles with limited education and minimal control over her income decisions due to cultural barriers, leading to frustration and helplessness. She feels isolated and unconnected to her community, struggling to find support and resources.\n")

input("Press enter to continue\n")

print("To support Maria, implementing a better educational system can help her find better job opportunities and access high-quality education. To support Maryam, implementing more educational programs and establishing finance and vocational training could help her foster greater autonomy.\n")

input("Press enter to continue\n")

print("From 1990 to 2015, the percentage of women with no education in Colombia has decreased to almost 0%, while in Pakistan it has also decreased but remains at approximately 40%.\n")

input("Press enter to continue\n")

print("In Colombia, women like Maria often enjoy educational opportunities and financial independence, though they still navigate a balance between work and family life. Socially, there is a growing recognition of women’s contributions to both professional and community roles. Historically, Colombia has made significant strides toward gender equality, supported by predominantly Christian traditions that are increasingly embracing gender equity. Despite progress, challenges like income inequality and lingering social norms persist, though there are expanding pathways for women’s higher education and career growth.\n")

input("Press enter to continue\n")

print("In Pakistan, women like Maryam face substantial barriers, including limited access to education due to traditional family roles and cultural expectations, which consequently influences their financial independence. Women encounter social constraints that emphasize traditional duties over professional aspirations, influenced by a conservative historical backdrop and Islamic cultural practices. Financial instability and fewer job opportunities further hinder women’s independence, with limited resources available for education and vocational training.\n")

input("Press enter to continue\n")

print("How does access to education affect women’s work opportunities and financial independence in Colombia and Pakistan?\n")

input("Press enter to continue\n")

print("Thank you for reading this data story! Here is the graph I created for you!\n")
plt.ylim(0,83)
plt.show()