import re
import requests
import fontTools.merge as mg

#(?<=')(.*?)(/ttf/)(.*?)(/.*?)(?=')
#https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/$3/hinted/ttf/$3-Regular.ttf

fontlist = [
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoNastaliqUrdu/hinted/ttf/NotoNastaliqUrdu-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSans/hinted/ttf/NotoSans-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansAvestan/hinted/ttf/NotoSansAvestan-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansBalinese/hinted/ttf/NotoSansBalinese-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansBatak/hinted/ttf/NotoSansBatak-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansBengali/hinted/ttf/NotoSansBengali-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansBhaiksuki/hinted/ttf/NotoSansBhaiksuki-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansBrahmi/hinted/ttf/NotoSansBrahmi-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansBuginese/hinted/ttf/NotoSansBuginese-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansBuhid/hinted/ttf/NotoSansBuhid-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansChakma/hinted/ttf/NotoSansChakma-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansCham/hinted/ttf/NotoSansCham-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansDevanagari/hinted/ttf/NotoSansDevanagari-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansGrantha/hinted/ttf/NotoSansGrantha-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansGujarati/hinted/ttf/NotoSansGujarati-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansGunjalaGondi/hinted/ttf/NotoSansGunjalaGondi-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansGurmukhi/hinted/ttf/NotoSansGurmukhi-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansHanifiRohingya/hinted/ttf/NotoSansHanifiRohingya-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansHanunoo/hinted/ttf/NotoSansHanunoo-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansJavanese/hinted/ttf/NotoSansJavanese-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansKaithi/hinted/ttf/NotoSansKaithi-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansKannada/hinted/ttf/NotoSansKannada-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansKayahLi/hinted/ttf/NotoSansKayahLi-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansKharoshthi/hinted/ttf/NotoSansKharoshthi-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansKhmer/hinted/ttf/NotoSansKhmer-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansKhojki/hinted/ttf/NotoSansKhojki-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansKhudawadi/hinted/ttf/NotoSansKhudawadi-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansLao/hinted/ttf/NotoSansLao-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansLepcha/hinted/ttf/NotoSansLepcha-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansLimbu/hinted/ttf/NotoSansLimbu-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansLisu/hinted/ttf/NotoSansLisu-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansMahajani/hinted/ttf/NotoSansMahajani-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansMalayalam/hinted/ttf/NotoSansMalayalam-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansMarchen/hinted/ttf/NotoSansMarchen-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansMasaramGondi/hinted/ttf/NotoSansMasaramGondi-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansMeeteiMayek/hinted/ttf/NotoSansMeeteiMayek-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansModi/hinted/ttf/NotoSansModi-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansMro/hinted/ttf/NotoSansMro-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansMultani/hinted/ttf/NotoSansMultani-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansMyanmar/hinted/ttf/NotoSansMyanmar-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansNandinagari/hinted/ttf/NotoSansNandinagari-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansNewTaiLue/hinted/ttf/NotoSansNewTaiLue-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansNewa/hinted/ttf/NotoSansNewa-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansOlChiki/hinted/ttf/NotoSansOlChiki-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansOldPersian/hinted/ttf/NotoSansOldPersian-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansOriya/hinted/ttf/NotoSansOriya-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansPhagsPa/hinted/ttf/NotoSansPhagsPa-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansRejang/hinted/ttf/NotoSansRejang-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansSaurashtra/hinted/ttf/NotoSansSaurashtra-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansSharada/hinted/ttf/NotoSansSharada-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansSiddham/hinted/ttf/NotoSansSiddham-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansSinhala/hinted/ttf/NotoSansSinhala-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansSoraSompeng/hinted/ttf/NotoSansSoraSompeng-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansSoyombo/hinted/ttf/NotoSansSoyombo-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansSundanese/hinted/ttf/NotoSansSundanese-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansSylotiNagri/hinted/ttf/NotoSansSylotiNagri-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansSyriac/hinted/ttf/NotoSansSyriac-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansTagalog/hinted/ttf/NotoSansTagalog-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansTagbanwa/hinted/ttf/NotoSansTagbanwa-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansTaiLe/hinted/ttf/NotoSansTaiLe-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansTaiTham/hinted/ttf/NotoSansTaiTham-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansTaiViet/hinted/ttf/NotoSansTaiViet-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansTakri/hinted/ttf/NotoSansTakri-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansTamil/hinted/ttf/NotoSansTamil-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansTelugu/hinted/ttf/NotoSansTelugu-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansThaana/hinted/ttf/NotoSansThaana-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansThai/hinted/ttf/NotoSansThai-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansTirhuta/hinted/ttf/NotoSansTirhuta-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansWancho/hinted/ttf/NotoSansWancho-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansWarangCiti/hinted/ttf/NotoSansWarangCiti-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansZanabazarSquare/hinted/ttf/NotoSansZanabazarSquare-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSerif/hinted/ttf/NotoSerif-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSerifAhom/hinted/ttf/NotoSerifAhom-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSerifBalinese/hinted/ttf/NotoSerifBalinese-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSerifDogra/hinted/ttf/NotoSerifDogra-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSerifGrantha/hinted/ttf/NotoSerifGrantha-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSerifGujarati/hinted/ttf/NotoSerifGujarati-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSerifKhmer/hinted/ttf/NotoSerifKhmer-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSerifTibetan/hinted/ttf/NotoSerifTibetan-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSerifHebrew/hinted/ttf/NotoSerifHebrew-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSerifKhojki/hinted/ttf/NotoSerifKhojki-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansUgaritic/hinted/ttf/NotoSansUgaritic-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansSyriac/hinted/ttf/NotoSansSyriac-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansSogdian/hinted/ttf/NotoSansSogdian-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansOldSogdian/hinted/ttf/NotoSansOldSogdian-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansOldSouthArabian/hinted/ttf/NotoSansOldSouthArabian-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansSamaritan/hinted/ttf/NotoSansSamaritan-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansInscriptionalParthian/hinted/ttf/NotoSansInscriptionalParthian-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansPhoenician/hinted/ttf/NotoSansPhoenician-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansPsalterPahlavi/hinted/ttf/NotoSansPsalterPahlavi-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansInscriptionalPahlavi/hinted/ttf/NotoSansInscriptionalPahlavi-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansPalmyrene/hinted/ttf/NotoSansPalmyrene-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansNabataean/hinted/ttf/NotoSansNabataean-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansOldNorthArabian/hinted/ttf/NotoSansOldNorthArabian-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansManichaean/hinted/ttf/NotoSansManichaean-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansHatran/hinted/ttf/NotoSansHatran-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansElymaic/hinted/ttf/NotoSansElymaic-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansEgyptianHieroglyphs/hinted/ttf/NotoSansEgyptianHieroglyphs-Regular.ttf',
  'https://cdn.jsdelivr.net/gh/notofonts/notofonts.github.io/fonts/NotoSansImperialAramaic/hinted/ttf/NotoSansImperialAramaic-Regular.ttf'
]


def downloadFiles():
  for i, font in enumerate(fontlist):
    fontname = font.split('/')[-1].replace('?raw=true', '')
    print('Downloading ' + fontname + ' ' + str(len(fontlist) - i))

    try:
        r = requests.get(font)
    except Exception:
      print('Cannot download')

    with open('./' + fontname, 'wb') as f:
      f.write(r.content)

def mergeFiles():
  merger = mg.Merger()
  for i, font in enumerate(fontlist):
    fontname = font.split('/')[-1].replace('?raw=true', '')
    print('Merging ' + str(len(fontlist) - i))
    try:
      if "NotoSans" or "NotoNast" in fontname:
        merged = merger.merge(fontfiles=[fontname, "NotoSans-Regular.ttf"])
      elif "NotoSerif" in fontname:
        merged = merger.merge(fontfiles=[fontname, "NotoSerif-Regular.ttf"])
      else:
        merged = merger.merge(fontfiles=[fontname, "NotoSans-Regular.ttf"])
      merged.save("./merged/" + fontname)
    except Exception as e:
      print(e)
      print('Merging ' + fontname + ' failed')

def writeCSS():
  cssContent = ''
  cssContentMerged = ''

  for i, font in enumerate(fontlist):
    fontfilename = font.split('/')[-1].replace('?raw=true', '')
    fontname = " ".join(re.split('(Noto|Sans|Serif|Nastaliq)', fontfilename.replace('.ttf', '').replace('-Regular', ''))).strip().replace("  ", " ")
    cssContent += '''
@font-face {
  font-family: ''' + "'" + fontname + "'" + ''';
  src: url(''' + "'" + font + "'" + ''')
}
  '''
    cssContentMerged += '''
@font-face {
  font-family: ''' + "'" + fontname + " '" + ''';
  src: url(''' + "'" + font.replace('hinted', 'full') + "'" + ''')
}
  '''
    with open('aksharamukha-notomirror.css', 'w') as f:
      f.write(cssContent)
    with open('aksharamukha-notomirror-merged.css', 'w') as f:
      f.write(cssContentMerged)

print('Starting font download')
downloadFiles()
print('Font download complete')

print('Starting font merging')
#mergeFiles()
print('Font merging complete')

print('Creating CSS file')
writeCSS()
print('Creating CSS file complete')

