

# Quote Crawl Project

This project is a web scraping application built using Scrapy to crawl and extract quotes from various websites. The project includes custom spiders, pipelines, and settings to manage the scraping process.


## Setup

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**
    Create a venv environment using the following command:

    ```sh
    python -m venv venv
    ```
    Activate the virtual environment using the following command:

    ```sh
    source venv/bin/activate
    ```
    

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Generating Spiders

To generate spiders based on the configuration in [`sources.json`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fkosiew%2FGitHub%2Fscrapy-mako%2Fsources.json%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/kosiew/GitHub/scrapy-mako/sources.json"), run:

```sh
python generate_spiders.py
```

This will create spider files in the spiders_automation/spiders directory using the Mako template located at templates/spiders/quote_template.mako.

## Running Spiders
To run a specific spider, use the scrapy crawl command followed by the spider's name. For example:

```
cd quote_crawl
scrapy crawl QuotationsPage
```

## Configuration
The Scrapy settings for this project are located in quote_crawl/quote_crawl/settings.py. Key settings include:

BOT_NAME: The name of the bot.
SPIDER_MODULES: The modules where spiders are located.
NEWSPIDER_MODULE: The module for new spiders.
ROBOTSTXT_OBEY: Whether to obey robots.txt rules.
DOWNLOAD_DELAY: Delay between requests to the same website.

## Pipelines
The project includes custom pipelines such as FilterQuotesPipelineLoveOrLife to process the scraped data.

