# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

# !! This is the configuration of Nikola. !! #
# !!  You should edit it to your liking.  !! #


# ! Some settings can be different in different languages.
# ! A comment stating (translatable) is used to denote those.
# ! There are two ways to specify a translatable setting:
# ! (a) BLOG_TITLE = "My Blog"
# ! (b) BLOG_TITLE = {"en": "My Blog", "es": "Mi Blog"}
# ! Option (a) is used when you don't want that setting translated.
# ! Option (b) is used for settings that are different in different languages.


# Data about this site
BLOG_AUTHOR = "Will"  # (translatable)
BLOG_TITLE = "artcontrol.me"  # (translatable)
# This is the main URL for your site. It will be used
# in a prominent link
SITE_URL = "http://artcontrol.me/"
# This is the URL where nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "http://artcontrol.me/"
BLOG_EMAIL = "hammersmake@gmail.com"
BLOG_DESCRIPTION = "Artwork of William Mckee"  # (translatable)

# Nikola is multilingual!
#
# Currently supported languages are:
#
# en     English
# bg     Bulgarian
# ca     Catalan
# cs     Czech [ALTERNATIVELY cz]
# de     German
# el     Greek [NOT gr]
# eo     Esperanto
# es     Spanish
# et     Estonian
# eu     Basque
# fa     Persian
# fi     Finnish
# fr     French
# hi     Hindi
# hr     Croatian
# it     Italian
# ja     Japanese [NOT jp]
# nb     Norwegian Bokmål
# nl     Dutch
# pl     Polish
# pt_br  Portuguese (Brasil)
# ru     Russian
# sk     Slovak
# sl     Slovene
# tr     Turkish [NOT tr_TR]
# ur     Urdu
# zh_cn  Chinese (Simplified)
#
# If you want to use Nikola with a non-supported language you have to provide
# a module containing the necessary translations
# (cf. the modules at nikola/data/themes/base/messages/).
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.

# What is the default language?
DEFAULT_LANG = "en"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# What will translated input files be named like?

# If you have a page something.rst, then something.pl.rst will be considered
# its Polish translation.
#     (in the above example: path == "something", ext == "rst", lang == "pl")
# this pattern is also used for metadata:
#     something.meta -> something.pl.meta

TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"

# Links for the sidebar / navigation bar.
# You should provide a key-value pair for each used language.
# (the same way you would do with a (translatable) setting.)
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/archive.html", "Archives"),
        ("/categories/index.html", "Tags"),
        ("/rss.xml", "RSS feed"),
    ),
}

# Name of the theme to use.
THEME = "bootstrap3"

# Below this point, everything is optional

# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (eg. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use the ISO 8601/RFC 3339 format (ex. 2012-03-30T23:00:00+02:00)
TIMEZONE = "UTC"

# If you want to use ISO 8601 (also valid RFC 3339) throughout Nikola
# (especially in new_post), set this to True.
# Note that this does not affect DATE_FORMAT.
# FORCE_ISO8601 = False

# Date format used to display post dates.
# (str used by datetime.datetime.strftime)
# DATE_FORMAT = '%Y-%m-%d %H:%M'

# While nikola can select a sensible locale for each language,
# sometimes explicit control can come handy.
# In this file we express locales in the string form that
# python's locales will accept in your OS, by example
# "en_US.utf8" in unix-like OS, "English_United States" in Windows.
# LOCALES = dict mapping language --> explicit locale for the languages
# in TRANSLATIONS. You can ommit one or more keys.
# LOCALE_FALLBACK = locale to use when an explicit locale is unavailable
# LOCALE_DEFAULT = locale to use for languages not mentioned in LOCALES; if
# not set the default Nikola mapping is used.

# POSTS and PAGES contains (wildcard, destination, template) tuples.
#
# The wildcard is used to generate a list of reSt source files
# (whatever/thing.txt).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and optionally translated files (example for spanish, with code "es"):
#     whatever/thing.es.txt and whatever/thing.es.meta
#
#     This assumes you use the default TRANSLATIONS_PATTERN.
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combinated with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds and are considered part of a blog, while PAGES are
# just independent HTML pages.
#

POSTS = (
            ("posts/*.wp", "posts", "post.tmpl"),
        )
PAGES = (
            ("stories/*.wp", "stories", "story.tmpl"),
        )

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of "source" "relative destination".
# Default is:
# FILES_FOLDERS = {'files': '' }
# Which means copy 'files' into 'output'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is html and just copies it
COMPILERS = {
        "rest": ('.txt', '.rst'),
        "markdown": ('.md', '.mdown', '.markdown', '.wp'),
        "html": ('.html', '.htm')
        }
        

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# If this is set to True, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# If this is set to False, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# Formerly known as HIDE_UNTRANSLATED_POSTS (inverse)
# SHOW_UNTRANSLATED_POSTS = True

# Nikola supports logo display.  If you have one, you can put the URL here.
# Final output is <img src="LOGO_URL" id="logo" alt="BLOG_TITLE">.
# The URL may be relative to the site root.
# LOGO_URL = ''

# If you want to hide the title of your website (for example, if your logo
# already contains the text), set this to False.
# SHOW_BLOG_TITLE = True

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
# TAG_PATH = "categories"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = False

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# INDEX_PATH = ""

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
# CREATE_SINGLE_ARCHIVE = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# Number of posts in RSS feeds
# FEED_LENGTH = 10

# Slug the Tag URL easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = [["drawing-around-wellington/index.html", "/posts/drawing-around-wellington.html"], ["eye-glow-digital/index.html", "/posts/eye-glow-digital.html"], ["kobo-mini-drawing/index.html", "/posts/kobo-mini-drawing.html"], ["auxweltak/index.html", "/posts/auxweltak.html"], ["vincents-life-drawing-lee-thursday/index.html", "/posts/vincents-life-drawing-lee-thursday.html"], ["promarkerny/index.html", "/posts/promarkerny.html"], ["yeah-yeah-yeah-colored-pencils/index.html", "/posts/yeah-yeah-yeah-colored-pencils.html"], ["eow-frozen-pass-pencil-drawings/index.html", "/posts/eow-frozen-pass-pencil-drawings.html"], ["westfield-auckland-sketch/index.html", "/posts/westfield-auckland-sketch.html"], ["underpainting/index.html", "/posts/underpainting.html"], ["bacon-game-jam-landscape-painting/index.html", "/posts/bacon-game-jam-landscape-painting.html"], ["dark-places/index.html", "/posts/dark-places.html"], ["concept-pencil-cuba-2/index.html", "/posts/concept-pencil-cuba-2.html"], ["september-vincents-life-drawing/index.html", "/posts/september-vincents-life-drawing.html"], ["i-wear-black-on-the-outside-cos-black-is-how-i-feel-on-the-inside/index.html", "/posts/i-wear-black-on-the-outside-cos-black-is-how-i-feel-on-the-inside.html"], ["lightsoff-pixel-ideas/index.html", "/posts/lightsoff-pixel-ideas.html"], ["toy-landscape/index.html", "/posts/toy-landscape.html"], ["file-infigment-bill-thoughts/index.html", "/posts/file-infigment-bill-thoughts.html"], ["reddit-december-paintings/index.html", "/posts/reddit-december-paintings.html"], ["girl-in-front-of-office-building/index.html", "/posts/girl-in-front-of-office-building.html"], ["redditgetsdrawn-library-portraits/index.html", "/posts/redditgetsdrawn-library-portraits.html"], ["landscape-of-the-day/index.html", "/posts/landscape-of-the-day.html"], ["roguelike-python/index.html", "/posts/roguelike-python.html"], ["redditgetsdrawn-new-years-day/index.html", "/posts/redditgetsdrawn-new-years-day.html"], ["digital-portraits-4chan/index.html", "/posts/digital-portraits-4chan.html"], ["thursday-blender-renders/index.html", "/posts/thursday-blender-renders.html"], ["friday-redditgetsdrawn/index.html", "/posts/friday-redditgetsdrawn.html"], ["hello-world-2/index.html", "/posts/hello-world-2.html"], ["redditgetsdrawn-sunday-afternoon/index.html", "/posts/redditgetsdrawn-sunday-afternoon.html"], ["ham-sketchbook/index.html", "/posts/ham-sketchbook.html"], ["russel-friday-life-drawings/index.html", "/posts/russel-friday-life-drawings.html"], ["bellez-rat/index.html", "/posts/bellez-rat.html"], ["charcoal-colorzz-friday-model/index.html", "/posts/charcoal-colorzz-friday-model.html"], ["sd-enviormen/index.html", "/posts/sd-enviormen.html"], ["church-levin-mall-sketch/index.html", "/posts/church-levin-mall-sketch.html"], ["826/index.html", "/posts/826.html"], ["power-pole-giants/index.html", "/posts/power-pole-giants.html"], ["redditgetsdrawn-xmas-painting/index.html", "/posts/redditgetsdrawn-xmas-painting.html"], ["levin-cinema-painting/index.html", "/posts/levin-cinema-painting.html"], ["wellington-figure-and-landscape/index.html", "/posts/wellington-figure-and-landscape.html"], ["wellington-water/index.html", "/posts/wellington-water.html"], ["digital-nudes/index.html", "/posts/digital-nudes.html"], ["lily-allen/index.html", "/posts/lily-allen.html"], ["bell-water/index.html", "/posts/bell-water.html"], ["sit-model-look-left/index.html", "/posts/sit-model-look-left.html"], ["digital-takaka-nudes/index.html", "/posts/digital-takaka-nudes.html"], ["random-ch-sketchbook/index.html", "/posts/random-ch-sketchbook.html"], ["chch-cbd-park-drawings/index.html", "/posts/chch-cbd-park-drawings.html"], ["trademe-and-portraits/index.html", "/posts/trademe-and-portraits.html"], ["more-paintings/index.html", "/posts/more-paintings.html"], ["old-paintings/index.html", "/posts/old-paintings.html"], ["beautiful-red-dress-painting/index.html", "/posts/beautiful-red-dress-painting.html"], ["final-friday-term-1-2012/index.html", "/posts/final-friday-term-1-2012.html"], ["lights-out-bacongamejam-5-third-painting-redditgetsdrawn/index.html", "/posts/lights-out-bacongamejam-5-third-painting-redditgetsdrawn.html"], ["may-monday-life-drawing/index.html", "/posts/may-monday-life-drawing.html"], ["mask/index.html", "/posts/mask.html"], ["three-angry-figures/index.html", "/posts/three-angry-figures.html"], ["wellington-rail-remake/index.html", "/posts/wellington-rail-remake.html"], ["waihi-digital-face/index.html", "/posts/waihi-digital-face.html"], ["2h-pencil-works/index.html", "/posts/2h-pencil-works.html"], ["court-garden/index.html", "/posts/court-garden.html"], ["welly-blend/index.html", "/posts/welly-blend.html"], ["president-of-redditgetsdrawn/index.html", "/posts/president-of-redditgetsdrawn.html"], ["anna-new-color-sample/index.html", "/posts/anna-new-color-sample.html"], ["badly-painted-microsoft-paint-works/index.html", "/posts/badly-painted-microsoft-paint-works.html"], ["hutt-envro-paint/index.html", "/posts/hutt-envro-paint.html"], ["redditdrawnportraits/index.html", "/posts/redditdrawnportraits.html"], ["sunday-morning/index.html", "/posts/sunday-morning.html"], ["oil-paint-portrait-tree/index.html", "/posts/oil-paint-portrait-tree.html"], ["seven-deadly-sins-gluttony/index.html", "/posts/seven-deadly-sins-gluttony.html"], ["happy-birthday-mum/index.html", "/posts/happy-birthday-mum.html"], ["character-swipe-blend/index.html", "/posts/character-swipe-blend.html"], ["redditgetsdrawn-wild-thing/index.html", "/posts/redditgetsdrawn-wild-thing.html"], ["far-north-drawing/index.html", "/posts/far-north-drawing.html"], ["alcemy-landscape/index.html", "/posts/alcemy-landscape.html"], ["hell-earth-title/index.html", "/posts/hell-earth-title.html"], ["new-tablet-dynamic-setup/index.html", "/posts/new-tablet-dynamic-setup.html"], ["strangegrace-illustration/index.html", "/posts/strangegrace-illustration.html"], ["lights-out-bacongamejam-character-concept/index.html", "/posts/lights-out-bacongamejam-character-concept.html"], ["inkscape-tuesday-redditgetsdrawn/index.html", "/posts/inkscape-tuesday-redditgetsdrawn.html"], ["blackhead-sitting/index.html", "/posts/blackhead-sitting.html"], ["levin-plants-and-cars/index.html", "/posts/levin-plants-and-cars.html"], ["punk-jam/index.html", "/posts/punk-jam.html"], ["hastings-imagine-painting/index.html", "/posts/hastings-imagine-painting.html"], ["envelope-characters/index.html", "/posts/envelope-characters.html"], ["cuba-sunsets/index.html", "/posts/cuba-sunsets.html"], ["sketchdaily-monsters-and-digital-street-dev/index.html", "/posts/sketchdaily-monsters-and-digital-street-dev.html"], ["takaka-life-drawing-murry/index.html", "/posts/takaka-life-drawing-murry.html"], ["ca-skl/index.html", "/posts/ca-skl.html"], ["frozen-path-eow-wip/index.html", "/posts/frozen-path-eow-wip.html"], ["levin-street-school/index.html", "/posts/levin-street-school.html"], ["cafrins-mask-collaborative-2/index.html", "/posts/cafrins-mask-collaborative-2.html"], ["auckland-waterfront-concept-paint/index.html", "/posts/auckland-waterfront-concept-paint.html"], ["wellington-draw/index.html", "/posts/wellington-draw.html"], ["knight-tattoo/index.html", "/posts/knight-tattoo.html"], ["dott/index.html", "/posts/dott.html"], ["dzhokar-redditgetsdrawn-portraits/index.html", "/posts/dzhokar-redditgetsdrawn-portraits.html"], ["iograph-artworks/index.html", "/posts/iograph-artworks.html"], ["notes-speech-for-nana/index.html", "/posts/notes-speech-for-nana.html"], ["sketchbook-palmerston-north/index.html", "/posts/sketchbook-palmerston-north.html"], ["immigration-landscape/index.html", "/posts/immigration-landscape.html"], ["ra1nz-weekend-life-drawinz/index.html", "/posts/ra1nz-weekend-life-drawinz.html"], ["weltak/index.html", "/posts/weltak.html"], ["horse/index.html", "/posts/horse.html"], ["grim-fandango/index.html", "/posts/grim-fandango.html"], ["pencil-levin-mall/index.html", "/posts/pencil-levin-mall.html"], ["redditgetsdrawn-promarker-christmas/index.html", "/posts/redditgetsdrawn-promarker-christmas.html"], ["march-concept-title/index.html", "/posts/march-concept-title.html"], ["nightmare-sketches/index.html", "/posts/nightmare-sketches.html"], ["to-follow-a-blog-or-not/index.html", "/posts/to-follow-a-blog-or-not.html"], ["life-drawing-octnov-tlc/index.html", "/posts/life-drawing-octnov-tlc.html"], ["life-paint-gouache-brendon/index.html", "/posts/life-paint-gouache-brendon.html"], ["ggj-artwork-2d/index.html", "/posts/ggj-artwork-2d.html"], ["regina-spektor-and-characters-on-the-wall/index.html", "/posts/regina-spektor-and-characters-on-the-wall.html"], ["welaklpencilwrk/index.html", "/posts/welaklpencilwrk.html"], ["explore-takaka-drawings/index.html", "/posts/explore-takaka-drawings.html"], ["alley-darkness/index.html", "/posts/alley-darkness.html"], ["global-game-jam-painting/index.html", "/posts/global-game-jam-painting.html"], ["wel-true/index.html", "/posts/wel-true.html"], ["double-female-model-monday/index.html", "/posts/double-female-model-monday.html"], ["hello-world/index.html", "/posts/hello-world.html"], ["les-barany-advice/index.html", "/posts/les-barany-advice.html"], ["levin-water/index.html", "/posts/levin-water.html"], ["crush/index.html", "/posts/crush.html"], ["lightsout-bacon-jam-5-first-painting/index.html", "/posts/lightsout-bacon-jam-5-first-painting.html"], ["andrew-a6-doodles/index.html", "/posts/andrew-a6-doodles.html"], ["takaka-drawing-class/index.html", "/posts/takaka-drawing-class.html"], ["reddit-sketchdaily-end-sept/index.html", "/posts/reddit-sketchdaily-end-sept.html"], ["old-master-techniques/index.html", "/posts/old-master-techniques.html"], ["cuba-street-painting-october/index.html", "/posts/cuba-street-painting-october.html"], ["levin-rose/index.html", "/posts/levin-rose.html"], ["blender-animation-test/index.html", "/posts/blender-animation-test.html"], ["clem-and-city-photo-studies/index.html", "/posts/clem-and-city-photo-studies.html"], ["janelles-party-drawings/index.html", "/posts/janelles-party-drawings.html"], ["well-boat-painting/index.html", "/posts/well-boat-painting.html"], ["circling-wellington-building-painting/index.html", "/posts/circling-wellington-building-painting.html"], ["vincents-tuesday-april/index.html", "/posts/vincents-tuesday-april.html"], ["bacon-game-jam-07-hungry/index.html", "/posts/bacon-game-jam-07-hungry.html"], ["concept-art-railway/index.html", "/posts/concept-art-railway.html"], ["chocolate-cup-sketch/index.html", "/posts/chocolate-cup-sketch.html"], ["memory-tlc-staff-exhibition/index.html", "/posts/memory-tlc-staff-exhibition.html"], ["spyro-the-dragon-breathing-fire/index.html", "/posts/spyro-the-dragon-breathing-fire.html"], ["da-draw-plz-june/index.html", "/posts/da-draw-plz-june.html"], ["cuban-water/index.html", "/posts/cuban-water.html"], ["space-hangar-and-levin-street-dev/index.html", "/posts/space-hangar-and-levin-street-dev.html"], ["cafrins-mask-collaborative/index.html", "/posts/cafrins-mask-collaborative.html"], ["napier-gouache-paintings/index.html", "/posts/napier-gouache-paintings.html"], ["vector-logo-mall/index.html", "/posts/vector-logo-mall.html"], ["robert-monday-term-1-2012/index.html", "/posts/robert-monday-term-1-2012.html"], ["lorde-portrait/index.html", "/posts/lorde-portrait.html"], ["kids/index.html", "/posts/kids.html"], ["reddit-gets-drawn-group/index.html", "/posts/reddit-gets-drawn-group.html"], ["redditgetsdrawn-color-saturday/index.html", "/posts/redditgetsdrawn-color-saturday.html"], ["lighting-particle-testz/index.html", "/posts/lighting-particle-testz.html"], ["vincents-negative-space/index.html", "/posts/vincents-negative-space.html"], ["new-scene-tests/index.html", "/posts/new-scene-tests.html"], ["monster-under-the-bed/index.html", "/posts/monster-under-the-bed.html"], ["print-digital-strd/index.html", "/posts/print-digital-strd.html"], ["just-two-colours/index.html", "/posts/just-two-colours.html"], ["sketchy-sketchy-levin/index.html", "/posts/sketchy-sketchy-levin.html"], ["yeah-town/index.html", "/posts/yeah-town.html"], ["mia-portrait/index.html", "/posts/mia-portrait.html"], ["painting-cuba-st-videos/index.html", "/posts/painting-cuba-st-videos.html"], ["color-explored-with-redditgetsdrawn-paintings/index.html", "/posts/color-explored-with-redditgetsdrawn-paintings.html"], ["model-mask/index.html", "/posts/model-mask.html"], ["angelique-portrait/index.html", "/posts/angelique-portrait.html"], ["napier-horror/index.html", "/posts/napier-horror.html"], ["street-sign/index.html", "/posts/street-sign.html"], ["lvn-rework/index.html", "/posts/lvn-rework.html"], ["napier/index.html", "/posts/napier.html"], ["roger-friday-lee-model/index.html", "/posts/roger-friday-lee-model.html"], ["auckland-characters/index.html", "/posts/auckland-characters.html"], ["basement-landscape/index.html", "/posts/basement-landscape.html"], ["digital-landscape-red/index.html", "/posts/digital-landscape-red.html"], ["dune-painting/index.html", "/posts/dune-painting.html"], ["wainui-sketech/index.html", "/posts/wainui-sketech.html"], ["redditgetsdrawn-kobo-sketches/index.html", "/posts/redditgetsdrawn-kobo-sketches.html"], ["gjgj/index.html", "/posts/gjgj.html"], ["nude-wellington/index.html", "/posts/nude-wellington.html"], ["whatcha/index.html", "/posts/whatcha.html"], ["janelle-figure/index.html", "/posts/janelle-figure.html"], ["erik-birthday-card/index.html", "/posts/erik-birthday-card.html"], ["skullgirl/index.html", "/posts/skullgirl.html"], ["lvn-skate/index.html", "/posts/lvn-skate.html"], ["color-painting-of-kikis-delivery-service/index.html", "/posts/color-painting-of-kikis-delivery-service.html"], ["pencil-drawings-from-wellington/index.html", "/posts/pencil-drawings-from-wellington.html"], ["blender-animation-update/index.html", "/posts/blender-animation-update.html"], ["lights-out-bacongamejam-secondpainting/index.html", "/posts/lights-out-bacongamejam-secondpainting.html"], ["landscape-binge-braid/index.html", "/posts/landscape-binge-braid.html"], ["figurative-expressions-russel/index.html", "/posts/figurative-expressions-russel.html"], ["digital-mall-time/index.html", "/posts/digital-mall-time.html"], ["maya-building/index.html", "/posts/maya-building.html"], ["redditgetsdrawn-feb-dig-guy/index.html", "/posts/redditgetsdrawn-feb-dig-guy.html"], ["redditgetsdrawn-zombie/index.html", "/posts/redditgetsdrawn-zombie.html"], ["sketchbook-travels/index.html", "/posts/sketchbook-travels.html"], ["fail-first/index.html", "/posts/fail-first.html"], ["levin-church/index.html", "/posts/levin-church.html"], ["levin-updates/index.html", "/posts/levin-updates.html"], ["robot-animation-tests/index.html", "/posts/robot-animation-tests.html"], ["got-digdraw/index.html", "/posts/got-digdraw.html"], ["da-drawplz-august/index.html", "/posts/da-drawplz-august.html"], ["redditdrawn-doubles/index.html", "/posts/redditdrawn-doubles.html"], ["milv-paint/index.html", "/posts/milv-paint.html"], ["dads-hens/index.html", "/posts/dads-hens.html"], ["hamilton-building/index.html", "/posts/hamilton-building.html"], ["concept-pencil-cuba/index.html", "/posts/concept-pencil-cuba.html"], ["lynn-mall-to-blender-model/index.html", "/posts/lynn-mall-to-blender-model.html"], ["robert-tuesday-term-1-2012/index.html", "/posts/robert-tuesday-term-1-2012.html"], ["lee-digital-works/index.html", "/posts/lee-digital-works.html"], ["digital-levin-start-eow-doodle/index.html", "/posts/digital-levin-start-eow-doodle.html"], ["vert-landscape/index.html", "/posts/vert-landscape.html"], ["redditgetsdrawn-friday-night-lines/index.html", "/posts/redditgetsdrawn-friday-night-lines.html"], ["cuba-street-fish/index.html", "/posts/cuba-street-fish.html"], ["portrait-skins/index.html", "/posts/portrait-skins.html"], ["red-lake/index.html", "/posts/red-lake.html"], ["triger-concept-drawings/index.html", "/posts/triger-concept-drawings.html"], ["figure-weekend/index.html", "/posts/figure-weekend.html"], ["ludum-dare-pencil-sketches/index.html", "/posts/ludum-dare-pencil-sketches.html"], ["portrait-batman-chch/index.html", "/posts/portrait-batman-chch.html"], ["maydog-kiss/index.html", "/posts/maydog-kiss.html"], ["doodle-pixellovely-perspective/index.html", "/posts/doodle-pixellovely-perspective.html"], ["chch-sketches-sketchbook/index.html", "/posts/chch-sketches-sketchbook.html"], ["ra1n-particle/index.html", "/posts/ra1n-particle.html"], ["cafrin/index.html", "/posts/cafrin.html"], ["light-throw-tests/index.html", "/posts/light-throw-tests.html"], ["redditgetsdrawn-mums-office/index.html", "/posts/redditgetsdrawn-mums-office.html"], ["board-acrylic-takaka/index.html", "/posts/board-acrylic-takaka.html"], ["old-paintings-part-two/index.html", "/posts/old-paintings-part-two.html"], ["update-iograph/index.html", "/posts/update-iograph.html"], ["wall-paint-levin/index.html", "/posts/wall-paint-levin.html"], ["art-journal-flip-may-2012/index.html", "/posts/art-journal-flip-may-2012.html"], ["icons-web/index.html", "/posts/icons-web.html"], ["auckland-pencil-drawings/index.html", "/posts/auckland-pencil-drawings.html"], ["lights-camera-3rd-person/index.html", "/posts/lights-camera-3rd-person.html"], ["creature-modeling/index.html", "/posts/creature-modeling.html"], ["life-model-monday/index.html", "/posts/life-model-monday.html"], ["wellington-habor/index.html", "/posts/wellington-habor.html"], ["sketchdaily-works-4th-to-6th-oct-redditgetsdrawn/index.html", "/posts/sketchdaily-works-4th-to-6th-oct-redditgetsdrawn.html"], ["artcontrol-wmckee-jan2013-windowsweb/index.html", "/posts/artcontrol-wmckee-jan2013-windowsweb.html"], ["cuba-painting-uv/index.html", "/posts/cuba-painting-uv.html"], ["3d-render/index.html", "/posts/3d-render.html"], ["levin-tower/index.html", "/posts/levin-tower.html"], ["unity-1st-and-3rd-cam-experiments/index.html", "/posts/unity-1st-and-3rd-cam-experiments.html"], ["georgette-monday-cloth/index.html", "/posts/georgette-monday-cloth.html"], ["wellington-street-draw-halloween/index.html", "/posts/wellington-street-draw-halloween.html"], ["april-block-blender-tests/index.html", "/posts/april-block-blender-tests.html"], ["sketchdaily-enviroments/index.html", "/posts/sketchdaily-enviroments.html"], ["email-to-my-mentor/index.html", "/posts/email-to-my-mentor.html"], ["eow-birth-of-a-god-development/index.html", "/posts/eow-birth-of-a-god-development.html"], ["palmy-skate/index.html", "/posts/palmy-skate.html"], ["friday-model-geogette/index.html", "/posts/friday-model-geogette.html"], ["rgd-jan/index.html", "/posts/rgd-jan.html"], ["saturday-morning/index.html", "/posts/saturday-morning.html"], ["christena-wednesday-drawings/index.html", "/posts/christena-wednesday-drawings.html"], ["vampire-weekend-paintin/index.html", "/posts/vampire-weekend-paintin.html"], ["blender-testing-action/index.html", "/posts/blender-testing-action.html"], ["iograph-days-of-dots/index.html", "/posts/iograph-days-of-dots.html"], ["redditgetsdrawn-sunday-night-painting/index.html", "/posts/redditgetsdrawn-sunday-night-painting.html"], ["july-portrait/index.html", "/posts/july-portrait.html"], ["your-brain/index.html", "/posts/your-brain.html"], ["levin-tower-seq/index.html", "/posts/levin-tower-seq.html"], ["levin-sketched-finals/index.html", "/posts/levin-sketched-finals.html"], ["marc-thursday-landscape/index.html", "/posts/marc-thursday-landscape.html"], ["reddit-sketchdaily-bonus-da/index.html", "/posts/reddit-sketchdaily-bonus-da.html"], ["redditgets-drawn-part-two/index.html", "/posts/redditgets-drawn-part-two.html"], ["three-figures-in-library/index.html", "/posts/three-figures-in-library.html"], ["panic-life-paint/index.html", "/posts/panic-life-paint.html"], ["promarker-vincents-thursday/index.html", "/posts/promarker-vincents-thursday.html"], ["auckland-waterfont-plus-train-wait/index.html", "/posts/auckland-waterfont-plus-train-wait.html"], ["path-of-exile/index.html", "/posts/path-of-exile.html"]]

# Commands to execute to deploy. Can be anything, for example,
# you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola install_plugin ping`).
# To do manual deployment, set it to []
# DEPLOY_COMMANDS = []

# For user.github.io/organization.github.io pages, the DEPLOY branch
# MUST be 'master', and 'gh-pages' for other repositories.
# GITHUB_SOURCE_BRANCH = 'master'
# GITHUB_DEPLOY_BRANCH = 'gh-pages'

# The name of the remote where you wish to push to, using github_deploy.
# GITHUB_REMOTE_NAME = 'origin'

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, there are no filters.
#
# Many filters are shipped with Nikola.  A list is available in the manual:
# <http://getnikola.com/handbook.html#post-processing-filters>
# FILTERS = {
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# Compiler to process LESS files.
# LESS_COMPILER = 'lessc'

# A list of options to pass to the LESS compiler.
# Final command is: LESS_COMPILER LESS_OPTIONS file.less
# LESS_OPTIONS = []

# Compiler to process Sass files.
# SASS_COMPILER = 'sass'

# A list of options to pass to the Sass compiler.
# Final command is: SASS_COMPILER SASS_OPTIONS file.s(a|c)ss
# SASS_OPTIONS = []

# #############################################################################
# Image Gallery Options
# #############################################################################

# Galleries are folders in galleries/
# Final location of galleries will be output / GALLERY_PATH / gallery_name
# GALLERY_PATH = "galleries"
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []
#
# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to 'old posts, page %d' or 'page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
# INDEXES_TITLE = ""         # If this is empty, defaults to BLOG_TITLE
# INDEXES_PAGES = ""         # If this is empty, defaults to '[old posts,] page %d' (see above)
# INDEXES_PAGES_MAIN = False # If True, INDEXES_PAGES is also displayed on
#                            # the main (the newest) index page (index.html)

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of autumn borland bw colorful default emacs friendly fruity manni
# monokai murphy native pastie perldoc rrt tango trac vim vs
# CODE_COLOR_SCHEME = 'default'

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONFIG_SUBTHEME = 'sky'
# You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions
# between the slides
# THEME_REVEAL_CONFIG_TRANSITION = 'cube'
# You can also use: page/concave/linear/none/default

# FAVICONS contains (name, file, size) tuples.
# Used for create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# FAVICONS = {
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# }

# Show only teasers in the index pages? Defaults to False.
# INDEX_TEASERS = False

# HTML fragments with the Read more... links.
# The following tags exist and are replaced for you:
# {link}                        A link to the full post page.
# {read_more}                   The string “Read more” in the current language.
# {reading_time}                An estimate of how long it will take to read the post.
# {remaining_reading_time}      An estimate of how long it will take to read the post, sans the teaser.
# {min_remaining_read}          The string “{remaining_reading_time} min remaining to read” in the current language.
# {paragraph_count}             The amount of paragraphs in the post.
# {remaining_paragraph_count}   The amount of paragraphs in the post, sans the teaser.
# {{                            A literal { (U+007B LEFT CURLY BRACKET)
# }}                            A literal } (U+007D RIGHT CURLY BRACKET)

# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the RSS_FEED, if RSS_TEASERS is True (translatable)
RSS_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = ""
# I recommend using the Creative Commons' wizard:
# http://creativecommons.org/choose/
# LICENSE = """
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/2.5/ar/">
# <img alt="Creative Commons License BY-NC-SA"
# style="border-width:0; margin-bottom:12px;"
# src="http://i.creativecommons.org/l/by-nc-sa/2.5/ar/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="http://getnikola.com" rel="nofollow">Nikola</a>         {license}'

# Things that will be passed to CONTENT_FOOTER.format().  This is done
# for translatability, as dicts are not formattable.  Nikola will
# intelligently format the setting properly.
# The setting takes a dict. The keys are languages. The values are
# tuples of tuples of positional arguments and dicts of keyword arguments
# to format().  For example, {'en': (('Hello'), {'target': 'World'})}
# results in CONTENT_FOOTER['en'].format('Hello', target='World').
# WARNING: If you do not use multiple languages with CONTENT_FOOTER, this
#          still needs to be a dict of this format.  (it can be empty if you
#          do not need formatting)
# (translatable)
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

# To use comments, you can choose between different third party comment
# systems.  The following comment systems are supported by Nikola:
#   disqus, facebook, googleplus, intensedebate, isso, livefyre, muut
# You can leave this option blank to disable comments.
COMMENT_SYSTEM = "disqus"
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = "nikolademo"

# Enable annotations using annotateit.org?
# If set to False, you can still enable them for individual posts and pages
# setting the "annotations" metadata.
# If set to True, you can disable them for individual posts and pages using
# the "noannotations" metadata.
# ANNOTATIONS = False

# Create index.html for story folders?
# STORY_INDEX = False
# Enable comments on story pages?
# COMMENTS_IN_STORIES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
# INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
# (Note: This was briefly STRIP_INDEX_HTML in v 5.4.3 and 5.4.4)
# Default = False
# STRIP_INDEXES = False

# Should the sitemap list directories which only include other directories
# and no files.
# Default to True
# If this is False
# e.g. /2012 includes only /01, /02, /03, /04, ...: don't add it to the sitemap
# if /2012 includes any files (including index.html)... add it to the sitemap
# SITEMAP_INCLUDE_FILELESS_DIRS = True

# List of files relative to the server root (!) that will be asked to be excluded
# from indexing and other robotic spidering. * is supported. Will only be effective
# if SITE_URL points to server root. The list is used to exclude resources from
# /robots.txt and /sitemap.xml, and to inform search engines about /sitemapindex.xml.
# ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

# Instead of putting files in <slug>.html, put them in
# <slug>/index.html. Also enables STRIP_INDEXES
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata
# PRETTY_URLS = False

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts by default
# SCHEDULE_ALL = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you are using the compile-ipynb plugin, just add this one:
# MATHJAX_CONFIG = """
# <script type="text/x-mathjax-config">
# MathJax.Hub.Config({
#     tex2jax: {
#         inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#         displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ]
#     },
#     displayAlign: 'left', // Change this to 'center' to center equations.
#     "HTML-CSS": {
#         styles: {'.MathJax_Display': {"margin": 0}}
#     }
# });
# </script>
# """

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuracion you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter':{'template_file': 'toggle'}}

# What Markdown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# Note: most Nikola-specific extensions are done via the Nikola plugin system,
#       with the MarkdownExtension class and should not be added here.
# MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite']

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty.
# (translatable)
# SOCIAL_BUTTONS_CODE = """
# <!-- Social buttons -->
# <div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">
# <a class="addthis_button_more">Share</a>
# <ul><li><a class="addthis_button_facebook"></a>
# <li><a class="addthis_button_google_plusone_share"></a>
# <li><a class="addthis_button_linkedin"></a>
# <li><a class="addthis_button_twitter"></a>
# </ul>
# </div>
# <script src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>
# <!-- End of social buttons -->
# """

# Show link to source for the posts?
# Formerly known as HIDE_SOURCELINK (inverse)
# SHOW_SOURCELINK = True
# Copy the source files for your pages?
# Setting it to False implies SHOW_SOURCELINK = False
# COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# By default, Nikola generates RSS files for the website and for tags.
# Set this to False to disable all that.
# GENERATE_RSS = True

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a feedburner feed or something else.
# RSS_LINK = None

# Show only teasers in the RSS feed? Default to True
# RSS_TEASERS = True

# Strip HTML in the RSS feed? Default to False
# RSS_PLAIN = False

# A search form to search this site, for the sidebar. You can use a google
# custom search (http://www.google.com/cse/)
# Or a duckduckgo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# (translatable)
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
# SEARCH_FORM = """
# <!-- Custom search -->
# <form method="get" id="search" action="//duckduckgo.com/"
#  class="navbar-form pull-left">
# <input type="hidden" name="sites" value="%s"/>
# <input type="hidden" name="k8" value="#444444"/>
# <input type="hidden" name="k9" value="#D51920"/>
# <input type="hidden" name="kt" value="h"/>
# <input type="text" name="q" maxlength="255"
#  placeholder="Search&hellip;" class="span2" style="margin-top: 4px;"/>
# <input type="submit" value="DuckDuckGo Search" style="visibility: hidden;" />
# </form>
# <!-- End of custom search -->
# """ % SITE_URL
#
# If you prefer a google search form, here's an example that should just work:
# SEARCH_FORM = """
# <!-- Custom search with google-->
# <form id="search" action="//www.google.com/search" method="get" class="navbar-form pull-left">
# <input type="hidden" name="q" value="site:%s" />
# <input type="text" name="q" maxlength="255" results="0" placeholder="Search"/>
# </form>
# <!-- End of custom search -->
#""" % SITE_URL

# Use content distribution networks for jquery, twitter-bootstrap css and js,
# and html5shiv (for older versions of Internet Explorer)
# If this is True, jquery and html5shiv is served from the Google and twitter-
# bootstrap is served from the NetDNA CDN
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Extra things you want in the pages HEAD tag. This will be added right
# before </head>
# (translatable)
# EXTRA_HEAD_DATA = ""
# Google Analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# (translatable)
# BODY_END = ""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Open Graph Protocol data for enhancing link sharing and
# discoverability of your site on Facebook, Google+, and other services.
# Open Graph is enabled by default.
# USE_OPEN_GRAPH = True

# Nikola supports Twitter Card summaries
# Twitter cards are disabled by default. They make it possible for you to
# attach media to Tweets that link to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit
# https://dev.twitter.com/form/participate-twitter-cards
#
# Uncomment and modify to following lines to match your accounts.
# Specifying the id for either 'site' or 'creator' will be preferred
# over the cleartext username. Specifying an ID is not necessary.
# Displaying images is currently not supported.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards
#     # 'site': '@website',  # twitter nick for the website
#     # 'site:id': 123456,  # Same as site, but the website's Twitter user ID
#                           # instead.
#     # 'creator': '@username',  # Username for the content creator / author.
#     # 'creator:id': 654321,  # Same as creator, but the Twitter user's ID.
# }

# If webassets is installed, bundle JS and CSS to make site loading faster
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
# EXTRA_PLUGINS_DIRS = []

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
# DEMOTE_HEADERS = 1

# You can configure the logging handlers installed as plugins or change the
# log level of the default stderr handler.
# WARNING: The stderr handler allows only the loglevels of 'INFO' and 'DEBUG'.
#          This is done for safety reasons, as blocking out anything other
#          than 'DEBUG' may hide important information and break the user
#          experience!

LOGGING_HANDLERS = {
    'stderr': {'loglevel': 'INFO', 'bubble': True},
    # 'smtp': {
    #     'from_addr': 'test-errors@example.com',
    #     'recipients': ('test@example.com'),
    #     'credentials':('testusername', 'password'),
    #     'server_addr': ('127.0.0.1', 25),
    #     'secure': (),
    #     'level': 'DEBUG',
    #     'bubble': True
    # }
}

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}
