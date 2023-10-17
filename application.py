import requests

#ask for the input
stock_symbol = input("Enter the Stock Symbol: ")
chart_type = input("Enter the chart type (line/bar/...): ")


if response.status.code == 200:
    data = response.json()

    if chart_type == "line":
        #create a line chart
    elif chart_type == "bar": 
        #create a bar chart
    else:
        print("Invalid Chart Type")
else:
    print("API request failed")
