# Modify the Overpass family for Google Fonts. 
# Sources available here: http://www.latofonts.com/2014/02/27/lato-2-0-released/

# WARNING: Font Bakery is needed for this script to run, https://github.com/googlefonts/fontbakery

# We may also need to add symlinks for certain scripts. FB should do this by default, if not, add the following symlinks:
#
# $ ln -s /your/path/to/fontbakery/fontbakery-nametable-from-filename.py /usr/local/bin/fontbakery-nametable-from-filename.py
# $ ln -s /your/path/to/fontbakery/fontbakery-check-bbox.py /usr/local/bin/fontbakery-check-bbox.py
# $ ln -s /your/path/to/fontbakery/fontbakery-fix-vertical-metrics.py /usr/local/bin/fontbakery-fix-vertical-metrics.py
#
# Permissions may need to be changed on these symlinks as well. To do this:
# $ chmod 744 /usr/local/bin/font-bakery-script


set -e # Stop script if we have any critical errors
cp -R ../src/. ../fonts
cd ../fonts

FONTS=$(ls *.ttx)

# Convert otfs to ttf
for font in $FONTS
do
    echo converting $font
    ttx $font
done

# Delete old .otfs
rm *.ttx


# We still need to backwards support the EkMukta fonts.
# Mukta is just a renamed version of EkMukta

# Duplicate Mukta fonts and rename to EkMukta.
cp Mukta-Bold.ttf EkMukta-Bold.ttf
cp Mukta-ExtraBold.ttf EkMukta-ExtraBold.ttf
cp Mukta-ExtraLight.ttf EkMukta-ExtraLight.ttf
cp Mukta-Light.ttf EkMukta-Light.ttf
cp Mukta-Medium.ttf EkMukta-Medium.ttf
cp Mukta-Regular.ttf EkMukta-Regular.ttf
cp Mukta-Semibold.ttf EkMukta-Semibold.ttf

FONTS=$(ls *.ttf)

# Rename the font filenames to fit within our GF api Thin -> Black
echo Renaming font files
python ../build/rename_font_filenames.py

# Delete old ttfs and rename .ttf.renamed -> ttf
python ../build/cleanup.py

# Since fonts have been renamed we need to reassign the variable
FONTS=$(ls *.ttf) 
fontbakery-nametable-from-filename.py $FONTS

echo tidying up font files
# change .ttf.fix -> .ttf
python ../build/cleanup.py

# Autohint fonts
FONTS=$(ls *.ttf)
echo autohinting fonts
for font in $FONTS
do
    ttfautohint -x 0 $font $font.fix
done

python ../build/cleanup.py

# Add fake dsigs to fonts
echo Adding dummy dsigs
fontbakery-fix-dsig.py $FONTS --autofix

# Increase version numbers from 2.203 to 2.204
fontbakery-update-version.py $FONTS 2.203 2.204
# Mukta and Mukta Vaani both have name table version strings of 2.204,
# but their head fontRevision is 2.203, if we run the script again,
# it will update the head to 2.204
fontbakery-update-version.py $FONTS 2.204 2.204
python ../build/cleanup.py


echo Testing new fonts
cd ../build
python test.py
