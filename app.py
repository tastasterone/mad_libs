from flask import Flask, render_template, request
from stories import Story, dict_of_stories, story_key_words

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', user_prompts = story_key_words)

@app.route('/story')
def story():
    story_setting = request.args.get('setting')
    story = Story(
        story_key_words,
        dict_of_stories[story_setting]
    )
    new_story = story.generate(request.args)
    return render_template('story.html', story = new_story)


if __name__ == '__main__':
    app.run(debug=True)


