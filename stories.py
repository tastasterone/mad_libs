"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

dict_of_stories = {
    'long-time': """Once upon a time in a long-ago {place}, there lived a
                large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
    'planet': """On a planet far far away called the {place}, there lived a
                {adjective} {noun}. Everyday they like to {verb} {plural_noun}.""",
    'ocean': """In the deapth of the ocean the is a {place}, among the sharks lived
                a {adjective} {noun}. Everyday it would {verb} {plural_noun}.""",
    'swamp': """There is a secret swamp hidden in {place}, among the living creatures there was
                a {adjective} {noun}. Nothing stopped them from {verb} {plural_noun}.""",
    'kingdom': """There is a kingdom called {place}, and it was rulled by 
                a {adjective} {noun}. Who frequently likes to {verb} {plural_noun}."""

}

story_key_words = ["place", "noun", "verb", "adjective", "plural_noun"]
