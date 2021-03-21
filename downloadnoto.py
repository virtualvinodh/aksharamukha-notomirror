import re
import requests
import fontTools.merge as mg

fontlist = [
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoNastaliqUrdu/NotoNastaliqUrdu-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSans/NotoSans-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansAvestan/NotoSansAvestan-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansBalinese/NotoSansBalinese-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansBatak/NotoSansBatak-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansBengali/NotoSansBengali-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansBhaiksuki/NotoSansBhaiksuki-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansBrahmi/NotoSansBrahmi-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansBuginese/NotoSansBuginese-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansBuhid/NotoSansBuhid-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansChakma/NotoSansChakma-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansCham/NotoSansCham-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansDevanagari/NotoSansDevanagari-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansGrantha/NotoSansGrantha-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansGujarati/NotoSansGujarati-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansGunjalaGondi/NotoSansGunjalaGondi-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansGurmukhi/NotoSansGurmukhi-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansHanifiRohingya/NotoSansHanifiRohingya-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansHanunoo/NotoSansHanunoo-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansJavanese/NotoSansJavanese-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansKaithi/NotoSansKaithi-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansKannada/NotoSansKannada-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansKayahLi/NotoSansKayahLi-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansKharoshthi/NotoSansKharoshthi-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansKhmer/NotoSansKhmer-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansKhojki/NotoSansKhojki-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansKhudawadi/NotoSansKhudawadi-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansLao/NotoSansLao-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansLepcha/NotoSansLepcha-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansLimbu/NotoSansLimbu-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansLisu/NotoSansLisu-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansMahajani/NotoSansMahajani-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansMalayalam/NotoSansMalayalam-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansMarchen/NotoSansMarchen-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansMasaramGondi/NotoSansMasaramGondi-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansModi/NotoSansModi-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansMro/NotoSansMro-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansMultani/NotoSansMultani-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansMyanmar/NotoSansMyanmar-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansNewTaiLue/NotoSansNewTaiLue-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansNewa/NotoSansNewa-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansOlChiki/NotoSansOlChiki-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansOldPersian/NotoSansOldPersian-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansOriya/NotoSansOriya-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansPhagsPa/NotoSansPhagsPa-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansRejang/NotoSansRejang-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansSaurashtra/NotoSansSaurashtra-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansSharada/NotoSansSharada-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansSiddham/NotoSansSiddham-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansSinhala/NotoSansSinhala-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansSoraSompeng/NotoSansSoraSompeng-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansSoyombo/NotoSansSoyombo-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansSundanese/NotoSansSundanese-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansSylotiNagri/NotoSansSylotiNagri-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansSyriac/NotoSansSyriac-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansTagalog/NotoSansTagalog-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansTagbanwa/NotoSansTagbanwa-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansTaiLe/NotoSansTaiLe-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansTaiTham/NotoSansTaiTham-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansTaiViet/NotoSansTaiViet-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansTakri/NotoSansTakri-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansTamil/NotoSansTamil-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansTelugu/NotoSansTelugu-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansThaana/NotoSansThaana-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansThai/NotoSansThai-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansTirhuta/NotoSansTirhuta-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansWancho/NotoSansWancho-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansWarangCiti/NotoSansWarangCiti-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansZanabazarSquare/NotoSansZanabazarSquare-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSerif/NotoSerif-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSerifAhom/NotoSerifAhom-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSerifBalinese/NotoSerifBalinese-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSerifDogra/NotoSerifDogra-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSerifGrantha/NotoSerifGrantha-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSerifGujarati/NotoSerifGujarati-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSerifKhmer/NotoSerifKhmer-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSerifTibetan/NotoSerifTibetan-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSerifHebrew/NotoSerifHebrew-Regular.ttf?raw=true',
  'https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSerifKhojki/NotoSerifKhojki-Regular.ttf?raw=true'
]


def downloadFiles():
  for i, font in enumerate(fontlist):
    fontname = font.split('/')[-1].replace('?raw=true', '')
    print('Downloading ' + fontname + ' ' + str(len(fontlist) - i))

    r = requests.get(font)
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
  src: url('https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha-notomirror/''' + fontfilename + "'" + ''')
}
  '''
    cssContentMerged += '''
@font-face {
  font-family: ''' + "'" + fontname + " '" + ''';
  src: url('https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha-notomirror/merged/''' + fontfilename + "'" + ''')
}
  '''
    with open('aksharamukh-notomirror.css', 'w') as f:
      f.write(cssContent)
    with open('aksharamukh-notomirror-merged.css', 'w') as f:
      f.write(cssContent)

print('Starting font download')
downloadFiles()
print('Font download complete')

print('Starting font merging')
mergeFiles()
print('Font merging complete')

print('Creating CSS file')
writeCSS()
print('Creating CSS file complete')

