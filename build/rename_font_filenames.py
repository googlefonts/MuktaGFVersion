import os

REMAP_FONTS = [
    ("Mukta-Bold.ttf", "Mukta-Bold.ttf.renamed"),
    ("Mukta-ExtraBold.ttf", "Mukta-ExtraBold.ttf.renamed"),
    ("Mukta-ExtraLight.ttf", "Mukta-ExtraLight.ttf.renamed"),
    ("Mukta-Light.ttf", "Mukta-Light.ttf.renamed"),
    ("Mukta-Medium.ttf", "Mukta-Medium.ttf.renamed"),
    ("Mukta-Regular.ttf", "Mukta-Regular.ttf.renamed"),
    ("Mukta-Semibold.ttf", "Mukta-SemiBold.ttf.renamed"),

    ("EkMukta-Bold.ttf", "EkMukta-Bold.ttf.renamed"),
    ("EkMukta-ExtraBold.ttf", "EkMukta-ExtraBold.ttf.renamed"),
    ("EkMukta-ExtraLight.ttf", "EkMukta-ExtraLight.ttf.renamed"),
    ("EkMukta-Light.ttf", "EkMukta-Light.ttf.renamed"),
    ("EkMukta-Medium.ttf", "EkMukta-Medium.ttf.renamed"),
    ("EkMukta-Regular.ttf", "EkMukta-Regular.ttf.renamed"),
    ("EkMukta-Semibold.ttf", "EkMukta-SemiBold.ttf.renamed"),

    ("MuktaMalar-Bold.ttf", "MuktaMalar-Bold.ttf.renamed"),
    ("MuktaMalar-ExtraBold.ttf", "MuktaMalar-ExtraBold.ttf.renamed"),
    ("MuktaMalar-ExtraLight.ttf", "MuktaMalar-ExtraLight.ttf.renamed"),
    ("MuktaMalar-Light.ttf", "MuktaMalar-Light.ttf.renamed"),
    ("MuktaMalar-Medium.ttf", "MuktaMalar-Medium.ttf.renamed"),
    ("MuktaMalar-Regular.ttf", "MuktaMalar-Regular.ttf.renamed"),
    ("MuktaMalar-Semibold.ttf", "MuktaMalar-SemiBold.ttf.renamed"),

    ("MuktaVaani-Bold.ttf", "MuktaVaani-Bold.ttf.renamed"),
    ("MuktaVaani-ExtraBold.ttf", "MuktaVaani-ExtraBold.ttf.renamed"),
    ("MuktaVaani-ExtraLight.ttf", "MuktaVaani-ExtraLight.ttf.renamed"),
    ("MuktaVaani-Light.ttf", "MuktaVaani-Light.ttf.renamed"),
    ("MuktaVaani-Medium.ttf", "MuktaVaani-Medium.ttf.renamed"),
    ("MuktaVaani-Regular.ttf", "MuktaVaani-Regular.ttf.renamed"),
    ("MuktaVaani-Semibold.ttf", "MuktaVaani-SemiBold.ttf.renamed"),
]

for old_name, new_name in REMAP_FONTS:
    if old_name in os.listdir('.'):
        os.rename(os.path.join('.', old_name), os.path.join('.', new_name))
        print 'renamed %s to %s' % (old_name, new_name)
print 'Done renaming'
