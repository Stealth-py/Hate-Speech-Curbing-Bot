# onlyFANS.py
### This project was submitted to Byld+WiT Hackthon 2021
A discord bot made by our team only**FANS** for the Byld + WIT Hackathon 2021.
<br>
<img src = "logo.jpeg"/>
## Languages Used
<img src = "https://img.shields.io/badge/python%20-%236C0101.svg?style=for-the-badge&logo=python&logoColor=white" alt="python"/> <img src = "https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white" alt = "css"/> <img src = "https://img.shields.io/badge/HTML-orange?style=for-the-badge&logo=html5&logoColor=white" alt = "html"/>

## How to run
- Visit [our website](https://stealth-py.github.io/onlyFANS.py/Website/hackathon.html)
- Invite the bot by clicking on "Add Bot to Discord"
- Enjoy

## Bot Commands
- $jumble - Play the Jumble Words game
- $hangman - Play the Hangman game
- $help - Get Help

## Hosting
- For hosting our bot on our given GitHub repository, you can use Heroku and follow the steps given below:
  - Fork our repository.
  - Sign In to your heroku account.
  - Create a new app on heroku.
  - Click on the app present in the menu, and then click on Deploy.
  - After that you'll see various options of deploying the app, but for now, we'll be using "Deploy using GitHub".
  - After that, you'll be redirected to sign in to your GitHub account to connect it with your current Heroku App.
  - Then, you'll be required to type in the name of the repository you want to deploy.
  - After that, it's upto you if you want to Enable Automatic Deploys or not, it's basically whenever you make a change to your repository, it automatically gets deployed after the changes are committed and pushed.
  - If automatic deployed is disabled, you can use manual deploy to deploy your project/bot by choosing the appropriate branch and then clicking on Deploy Branch.
  - After this, go to Settings -> Config Vars -> Reveal Config Vars, and add the following, KEY = "token" and VALUE = "<your-discord-bot-token>", which you can find from your discord applications page of your bot. Click Add and you are done.
  - Now, you just need to go to Resources and turn the switch in the Edit Dyno Formations tab, and your bot will be deployed.

## Key Features
- Offers multiple games such as Hangman and Guess the Word
- Has a hate speech filter which uses libraries such as NLTK and Text Blob alongside perspective API to detect hate speeches and alters them to make them funny. Does not need any commands to run, it keeps on running side-by-side.

## Libraries, Technologies & Data used
- [Natural Language Toolkit](https://www.nltk.org/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [Perspective API](https://www.perspectiveapi.com/)
- [Pandas](https://pandas.pydata.org/)
- [funny_words](https://github.com/sethblack/funny-words)
- [Google API Client](https://pypi.org/project/google-api-python-client/)
- [Data Set of Abusive Words](https://github.com/uds-lsv/lexicon-of-abusive-words/blob/master/Lexicons/expandedLexicon.txt)

## Researches References
- [A Thematic Analysis of Suicide Notes](https://www.researchgate.net/publication/12748208_A_Thematic_Analysis_of_Suicide_Notes)
- [Detecting suicidal posts with Natural Language Processing](https://towardsdatascience.com/goodbye-world-4cc844197d51)
- [Detection of Suicide Ideation in Social Media Forums Using Deep Learning](https://www.mdpi.com/1999-4893/13/1/7/htm)

## Team Members
- Mohammad **F**aizan Haider
  - GitHub Profile: [FaizanHaider20083](https://github.com/FaizanHaider20083)
  - LinkedIn: [Mohammad Faizan Haider](https://www.linkedin.com/in/faizan-haider-ab65ba200/)
  - Instagram: [faizan.lazy](https://www.instagram.com/faizan.lazy/)
- Mohammad **A**flah Khan
  - GitHub Profile: [aflah02](https://github.com/aflah02)
  - LinkedIn: [Mohammad Aflah Khan](https://www.linkedin.com/in/mohammad-aflah-khan/)
  - Instagram: [life_levelling](https://www.instagram.com/life_levelling/)
- **N**eemesh Yadav
  - GitHub Profile: [Stealth-py](https://github.com/Stealth-py)
  - LinkedIn: [Neemesh Yadav](https://www.linkedin.com/in/neemesh-yadav-743baa1b8/)
  - Instagram: [stealth.py](https://www.instagram.com/stealth.py/)
- **S**aumik Shashwat
  - GitHub Profile: [saumiks](https://github.com/saumiks)
  - LinkedIn: [Saumik Shashwat](https://www.linkedin.com/in/saumiks/)
  - Instagram: [saumik.shashwat](https://www.instagram.com/saumik.shashwat/)
