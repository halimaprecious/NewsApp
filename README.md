# QuickUpdates

An application that consumes the News - API and displays news sources and articles.

## Live Link
https://quick-updates.herokuapp.com/

## Author
## Precious Halima

## Technology used
* Python
* Flask
* HTML
* CSS

## Requirements
An IDE such as VS code with Python version 3 installed,a terminal and a browser. 

## Setup and Instruction
1. Clone the repository at [here](https://github.com/halimaprecious/QuickUpdates.git).
2. Extract and open the folder on VS code or navigate to the folder on your terminal.
3. On the terminal, create a virtual environment 
```bash
python3 -m venv virtual
``` 
and activate it:
 ```bash
source virtual/bin/activate
```
 NB **virtual** is the name of the environment.

4. Pip install dependancies highlighted on the **requirements.txt** by running 
```bash
pip install -r requirements.txt
```
5. Create a **start.sh** file in the root directory of the folder and define the **api key**. You can generate the api key from the News API [here](https://newsapi.org/)
6. Running the application

  ```bash
  chmod a+x start.sh

  ./start.sh
  ```
7. Testing the application
  ```bash
  python3.6 manage.py test
  ```
8. View the application on your browser through `http://127.0.0.1:5000`.




## Behaviour Driven Development

BDD focuses on how the user will interact with the application.

What you will see and experience:
1. A navbar on the landing page and news sources
2. The navbar contains links with various types of news articles. Click on the **Articles** link and get redirected to news articles. 
3. The **visit site** link  redirects you to the sources official website.
4. The news articles are displayed on cards, with a title, a brief description and published date. Click on **See more from source**  to get redirected to the main article or video on the source website. 
## Development
To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request

## Known Bugs

If you find a bug or would like to request a new function, reach out to me via Email: halimaprecious3@gmail.com or on [LinkedIn](https://www.linkedin.com/in/precious-halima)

## License

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2022 **Precious** **Halima**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.