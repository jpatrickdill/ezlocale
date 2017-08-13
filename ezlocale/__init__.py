"""
Copyright (c) 2017 James Patrick Dill

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import faste
import googletrans

from .langs import language

__author__ = "Patrick Dill"
__version__ = "0.1"

DEST = language.EN

_translators = {}


class Translator(object):
    def __init__(self, dest, src="en", max_cache_size=128):
        self.translator = googletrans.Translator()

        self.src = src
        self.dest = dest

        self.cache = faste.caches.LFUCache(max_cache_size)

    def translate(self, text):
        if not isinstance(text, str):
            raise TypeError("Text to translate must be str")

        if text not in self.cache:
            self.cache[text] = self.translator.translate(text, dest=self.dest, src=self.src).text

        return self.cache[text]


def gettext(text, dest=None):
    """
    Gets text in specified language.

    :param text: Text to translate
    :param dest: (keyword) Destination language. Defaults to :attr:`ezlocale.DEST`
    :return:
    """
    dest = dest or DEST

    if dest not in _translators:
        _translators[dest] = Translator(dest.value)

    return _translators[dest].translate(str(text))


def clear_cache():
    """
    Clears translator caches.
    """
    for translator in _translators.values():
        translator.cache.clear()
