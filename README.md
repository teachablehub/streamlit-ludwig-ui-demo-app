![Ludwig TeachableHub Streamlit and Heroku](https://media-blog.sashido.io/content/images/2021/08/th-sklearn-ludwig-demo-cover.png)

<h1>
  <p align="center">
    <a href="https://th-ludwig-demo.herokuapp.com/" target="_blank">DEMO</a>
  </p>
</h1>
<br /><br />

# Local Development

#### 1. Clone this repo on your computer

```
git clone https://github.com/teachablehub/streamlit-ludwig-ui-demo-app.git
cd streamlit-ludwig-ui-demo-app
```

#### 2. Setup python virtualenv (optional)

- https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b
- https://docs.python-guide.org/dev/virtualenvs/

```
virtualenv -p python3.7 --no-site-packages venv
source venv/bin/activate
```

#### 3. Install the dependencies

```
pip install -r requirements.txt
```

#### 4. Run the Streamlit app

```
streamlit run app.py
```

# Deploy on Heroku

Heroku is a free hosting service for hosting small projects. Easy setup and deploy from the command line via git.

## Install Heroku

1. Create an account on https://heroku.com. This should be pretty straight forward.
2. Install the Heroku CLI on your computer: [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli).

After completing the steps above, check that you have the `heroku-cli` installed by checking the version number in your terminal:

```
heroku --version
```

3. Connect the `Heroku CLI` to your account by writing the following command in your terminal and follow the instructions on the command line:

```
heroku login
```

## Deploy

#### 1. Clone this repo on your computer

```
git clone https://github.com/teachablehub/streamlit-ludwig-ui-demo-app.git
cd streamlit-ludwig-ui-demo-app
```

#### 2. Create a remote Heroku project
Creating a Heroku project, kinda like creating a git repository on GitHub. This will create a project on Heroku with a random name. If you want to name your app you have to supply your own name like `heroku create project-name`. The command below will just create a random name:

```
heroku create
```

#### 3. Setup you TeachableHub credentials as Environment Variables.

More information about the credentials you can find in your Teachable Docs at `https://app.teachablehub.com/<user>/<teachable>/docs`

```
heroku config:set \
  TH_TEACHABLE=user/teachable \
  TH_ENVIRONMENT=production \
  TH_SERVING_KEY=your-serving-key-here
```

#### 4. Push your app to Heroku

Pushing the app to **Heroku** like pushing to GitHub expect for `origin` you have `heroku` (you will see a wall of code).

```
git push heroku master
```

#### 5. Visit your newly create app by opening it via heroku:

```
heroku open
```

If you are getting errors you can view the error logs by running this command:

```
heroku logs --tail
```
