# fundamentus-stats
🌎[versão em português](/README.pt.md)
## 📌 Summary

Simple stock market fundamental analysis project built with Python and pandas. The main focus is to perform basic filtering of companies with potentially interesting indicators for personal study and learning purposes.

## 🎯 Objective
* Practice data analysis with pandas;
* Learn DataFrame manipulation;
* Create a simple stock ranking system based on fundamental indicators;
* Assist in the initial selection of stocks for further analysis.

## 🛠️ Tools Used
* Python
* Pandas
* CSV/Excel files for data input

## ☑️ How It Works

The script reads a CSV file containing Brazilian stock market fundamental indicators and applies filters/rankings based on metrics such as:

* P/E Ratio
* Dividend Yield
* Price-to-Book Ratio
* ROE
* Liquidity
* Revenue Growth

Each stock receives a score according to the criteria defined in the code.

## ▶️ How to Use
1. Clone the repository:
2. git clone <https://github.com/budnyy/fundamentus_stats.git>
3. Access:

 [Fundamentus](https://www.fundamentus.com.br/resultado.php)

4. Copy the table containing stocks and indicators;
5. Paste it into Excel;
6. Save the file as .csv;
7. Place the CSV file inside the project folder;
8. Change the file_name variable in the script to the relative path of the CSV file;
9. Run the Python script.

## 🚧 Possible Improvements
* Implement web scraping to automatically fetch financial data;
* Integrate with sources such as:
    * B3
    * CVM
* Create more professional visualizations using:
    * Plotly
    * Streamlit
* Improve filtering and ranking criteria;
* Add a graphical interface or web dashboard;
* Automate data updates.
