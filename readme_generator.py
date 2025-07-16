from InquirerPy import prompt
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
import os

console = Console()

licenses = [
    "MIT License",
    "Apache License 2.0",
    "GNU General Public License (GPL v3)",
    "GNU Lesser General Public License (LGPL v3)",
    "Mozilla Public License 2.0 (MPL 2.0)",
    "Creative Commons License (CC0, CC BY, etc.)",
    "Unlicense"
]

questions = [
    {"type": "input", "name": "title", "message": "Project Title:"},
    {"type": "input", "name": "description", "message": "Project Description:"},
    {"type": "input", "name": "installation", "message": "Installation Instructions:"},
    {"type": "input", "name": "usage", "message": "Usage Instructions:"},
    {"type": "list", "name": "license", "message": "Choose a License:", "choices": licenses},
    {"type": "input", "name": "author", "message": "Author / Contact Info:"}
]

answers = prompt(questions)
readme_content = f"""# {answers['title']}
## Description
{answers['description']}

## Installation
{answers['installation']}

## Usage
{answers['usage']}

## License
This project is licensed under the **{answers['license']}**.

## Author
{answers['author']}
"""
try: 
  with open("readme.md", "w") as file:
    file.write(readme_content)
  console.print(Panel("[bold green] readme.md successfully created![/bold green]"))
  console.print(Panel(Markdown(readme_content), title="README Preview", border_style="cyan"))

except Exception as e:
   console.print(f"[bold.red] Error creating readme.md:[/bold red] {e}")
