# Simple Web Scraper

This project is a simple Python-based web scraper that extracts data from a public website and stores it in a CSV file.

## Features  
- Fetches HTML content from a given URL  
- Parses and extracts specific data  
- Saves results to a CSV file  

## Requirements  
- Python 3.8+  
- Install dependencies from "requirements.txt"  

## Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/RomanRochniak/demo-scraper.git  
   cd demo-scraper  
   ```

2. Create a virtual environment (optional but recommended):  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  ## Linux/Mac  
   venv\Scripts\activate     ## Windows  
   ```

3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```

## Usage  

1. Update the "URL" variable inside "main.py" with the website you want to scrape.  
2. Run the scraper:  
   ```bash  
   python main.py  
   ```  
3. The output will be saved as "output.csv".  
## Example  
Example command:  
    ```bash  
    python main.py  
    ``` 

Example output in "output.csv":  
```  
Title, Link  
Example Item 1, https://example.com/1  
Example Item 2, https://example.com/2  
```  

## License  
This project is licensed under the MIT License.