# Chatbot-Testing
 BERT Analisys on Chatbot data



![](https://raw.githubusercontent.com/georgecristian97/Logo/main/logo/python-logo.png)![](https://raw.githubusercontent.com/georgecristian97/Logo/main/logo/pycharm-logo.png)![](https://raw.githubusercontent.com/georgecristian97/Logo/main/logo/scikit-logo.png)





:package:	[Install python](https://www.python.org/downloads/release/python-370/)

:hammer:	Edit with:

[Download PyCharm: Python IDE for Professional Developers by JetBrains](https://www.jetbrains.com/pycharm/download/#section=windows)

:wrench: 	Add stopwords in specific location :	

​		Command line installation

The downloader will search for an existing `nltk_data` directory to install NLTK data. If one does not exist it will attempt to create one in a central location (when using an administrator account) or otherwise in the user’s filespace. If necessary, run the download command from an administrator account, or using sudo. The recommended system location is:

- `C:\nltk_data` (Windows) ;
- `/usr/local/share/nltk_data` (Mac) and
- `/usr/share/nltk_data` (Unix).

You can use the -d flag to specify a different location (but if you do this, be sure to set the NLTK_DATA environment variable accordingly).

- Run the command `python -m nltk.downloader all`
- To ensure central installation, run the command: `sudo python -m nltk.downloader -d /usr/local/share/nltk_data all`
- But really they should say: `sudo python -m nltk.downloader -d $NLTK_DATA all`



:gear:	You need those packages:

pip install ntlk

pip install git+https://github.com/scikit-learn/scikit-learn

pip install sentence-transformers

pip install pandas

pip install colorama



- [First input data vs input Dataset](https://github.com/georgecristian97/Chatbot-Testing/blob/main/IvsI.py)

- [Input vs output Chat](https://github.com/georgecristian97/Chatbot-Testing/blob/main/IvsOchat.py)

- [Input vs output Dataset](https://github.com/georgecristian97/Chatbot-Testing/blob/main/IvsOdata.py)



