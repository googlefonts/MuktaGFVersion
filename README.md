# Mukta Families for Google Fonts
by Multiple Designers

This repository hot fixes the binary sources for [Mukta](https://github.com/EkType/Mukta)

## Changes from source
1. Change font names to fit within Google Font's api. We can only have weights from Thin to Black.
2. Autohint fonts using ttfautohint.


## Building fonts
```
$ cd build
$ sh build.sh
```

## Dependencies
[FontTools](https://github.com/fonttools/fonttools)
[Font Bakery](https://github.com/googlefonts/fontbakery)
[ttfautohint](https://www.freetype.org/ttfautohint/)