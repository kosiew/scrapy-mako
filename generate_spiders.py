import json
import os
from urllib.parse import urlparse

from mako.template import Template

# Load JSON configuration
with open("sources.json") as f:
    sources = json.load(f)

# Set up the Mako template
template_path = "templates/spiders/quote_template.mako"
with open(template_path) as f:
    template_content = f.read()
template = Template(template_content)

# Folder where you want to save the spider file
scrapy_project_name = "spiders_automation"
folder_name = f"{scrapy_project_name}/spiders"

for config in sources:
    # Extract values and manipulate strings
    spidername = config["spidername"].title().replace(" ", "")
    spiderclass = spidername.capitalize() + "Spider"
    start_urls = config["start_urls"]
    parsed_url = urlparse(start_urls[0])
    allowed_domains = parsed_url.netloc

    # Render the template with values
    output = template.render(
        spiderclass=spiderclass,
        spidername=spidername,
        allowed_domains=allowed_domains,
        start_urls=start_urls,
        quote_div_main=config["quote_div_main"],
        title_selector=config["title_selector"],
        author_selector=config["author_selector"],
    )

    # Ensure the folder exists
    os.makedirs(folder_name, exist_ok=True)

    # Save the rendered template to a new Python file in the specified folder
    file_path = os.path.join(folder_name, f"{spiderclass}.py")
    with open(file_path, "w") as f:
        f.write(output)

    print(f"Spider generated: {file_path}")
