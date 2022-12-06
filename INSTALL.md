## Requirements and Instructions
Specifies all requirements to run the discord bot

### Prerequisites

* [git](https://git-scm.com/)
* [Python 3.7+](https://www.python.org)
* [npm](https://www.npmjs.com/)

### Steps for Installation

1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/vamsitadikonda/slash
cd slash
```
#### Backend Installation steps
2. This project uses Python 3.7, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled with the updated versions. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those.
```
pip3 install -r requirements.txt
```
3. Once all the requirements are installed, you will have to ```cd``` into the ```src/api``` folder. Once in the ```src``` folder.
```
cd src/api
````
4. To run the CLI version of the application, use the python command to run the ```slash.py``` file.
```
For Mac
python3 slash.py --search icecream

For Windows
python slash.py --search icecream
```
5. Inorder to run Slash REST API, use the ```flask``` command
```
flask run
```

#### Frontend Installation Steps
6. This project uses React JS for the front end, so make sure that [React](https://reactjs.org/) and [npm](https://www.npmjs.com/) are preinstalled with the updated versions. Move to the directory ```src/slash-react-app```
```
cd  src/slash-react-app
```
7. Try installing all the packages 
```
npm install

// if npm install fails, try this
npm install --legacy-peer-deps

```

8. Try building the package directly using the ```build run``` command.
```
npm run build
```
9. If there are any issues with step 8, Use npm to install the below packages and retry step 7. Otherwise skip this step.
```
npm install @material-ui/icons
npm install @material-ui/core
npm install react-numeric-input --save
```
9. To run the development server use the ```npm start``` command.
```
npm start
```
