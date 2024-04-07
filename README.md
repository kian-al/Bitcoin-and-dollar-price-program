This script fetches and extracts cryptocurrency (Bitcoin) prices as well as the USD to Iranian Rial exchange rates from two different URLs. Let's break down the code and understand each part:

Importing Libraries: The script imports necessary libraries including requests for making HTTP requests, BeautifulSoup for parsing HTML content, re for regular expressions, OrderedDict for maintaining the order of key-value pairs, and Fore from colorama for colored text output.

Bitcoin Price Extraction: It sends a GET request to the URL "https://www.tgju.org/profile/crypto-bitcoin" to fetch the webpage content. Then, it uses BeautifulSoup to parse the HTML content. It searches for the table containing Bitcoin prices and extracts the data using a regular expression pattern. The extracted data is then stored in an ordered dictionary.

Displaying Bitcoin Prices: It prints the Bitcoin prices with colored text using a for loop to iterate over the items in the dictionary.

USD to Iranian Rial Exchange Rate Extraction: Similar to Bitcoin price extraction, it sends a GET request to the URL "https://www.tgju.org/profile/price_dollar_rl" to fetch the webpage content. It then parses the HTML content, extracts the data using a regular expression pattern, and stores it in another ordered dictionary.

Displaying USD to Iranian Rial Exchange Rates: It prints the exchange rates with colored text using a for loop to iterate over the items in the dictionary.

Separating Sections: It adds a colored separator between the sections for better readability.

Overall, this script provides a simple way to fetch and display cryptocurrency prices (Bitcoin) and USD to Iranian Rial exchange rates from the webpages.
