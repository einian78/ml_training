# ml_training


#install winiconda from https://docs.conda.io/en/latest/miniconda.html
#create a working directory (for example: c:\MyML)
#run anaconda(miniconda) consule in administrator setting

conda install -c conda-forge git spyder pandas matplotlib lightgbm segyio tqdm opencv pandas-datareader scikit-learn py-xgboost seaborn scikit-image Pyinstaller tensorflow 

pip install keras


cd c:\MyML

git clone https://github.com/BehrangK/ml_training.git
cd ml_training

#When running bellow command, the first time you pull or push from the remote repository, you'll get asked about the username and password.Afterwards, for consequent communications with the remote repository you don't have to provide the username and password.
git config --global credential.helper store   

#to add modifed file to your git project:
git add *.*
or
git add nameofyourfile

#to commit with git:  
git commit -m " your comment here"

#to pull from git repository:
git pull

#push to github
git pull

#Checking the status of the repository
git status