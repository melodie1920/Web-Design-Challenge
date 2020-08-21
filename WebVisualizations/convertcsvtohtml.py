import pandas as pd 
  
# to read csv file named "samplee" 
df = pd.read_csv("Resources/cities.csv") 
  
# to save as html file 
# named as "Table" 
df.to_html("data.html", index=False) 
  
# assign it to a  
# variable (string) 
html_file = df.to_html() 