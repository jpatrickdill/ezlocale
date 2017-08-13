import ezlocale

ezlocale.DEST = ezlocale.language.ES
_ = ezlocale.gettext

name = input(_("What's your name? > "))

print(_("Hello, %s!" % name))
