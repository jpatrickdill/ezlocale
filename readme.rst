EzLocale
========

EzLocale is a language library that makes translation easier (hence the name).

Throw gettext in the trash, because you'll never need to manually translate again.


Using EzLocale
--------------

.. code-block:: python

    import ezlocale

    # set default language to Spanish
    ezlocale.DEST = ezlocale.language.ES

    # easier translation
    _ = ezlocale.gettext

    name = input(_("What's your name? > "))

    print(_("Hello, %s!" % name))

Example usage:

``
¿Cuál es tu nombre? > Patrick
¡Hola, Patrick!
``

You can also use a different language with each call.

.. code-block:: python

    >>> _("Hello!", ezlocale.language.LA)
    'Salve!'

EzLocale uses an LFU cache for each language to make sure resources aren't wasted. http://pypi.org/project/faste/

It's powered by google translate, with the googletrans module. https://github.com/ssut/py-googletrans