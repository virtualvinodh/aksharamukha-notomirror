# aksharamukha-notomirror

Mirroring the Noto fonts used by Aksharamukha (http//aksharamukha.appspot.com).

Google (for mysterious reasons) does not yet provide a CDN to load their under development Noto fonts. Since jsDelivr has a 50 MB package limit, loading the fonts directly from Google's Github account is very unreliable.

The respository (~20 MB Zipped) should allow jsDelivr to work without any issues.

# Merged Fonts #
Again (for myserious reasons) Google does not include (or even make an alternate version) even common punctuations in many of these Noto fonts. This makes them absolutely useless for day-to-day typesetting using systems such as LaTeX or PDFMake that lack a reliable fallback mechanism.

The merged folder has the fonts individual fonts merged with Noto Sans (or Noto Serif) and could be used for typesetting without any fallback issues.

# CSS files #
aksharamukha-notomirror.css has the relevantt @font-face information to load the fonts using JSDelivr as CDN.

You could include the CSS using CDN with the following URL:

https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha-notomirror/aksharamukha-notomirror.css