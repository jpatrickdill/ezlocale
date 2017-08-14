import ezlocale

ezlocale.DEST = ezlocale.get_language(input("Language > "))
_ = ezlocale.gettext

name = input(_("What's your name? > "))

print(_("Hello, %s!" % name))
