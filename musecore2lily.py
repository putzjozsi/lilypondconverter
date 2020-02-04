import xml.etree.ElementTree as ET

SHARP = "#"
DOUBLE_SHARP = "##"
FLAT = "b"
DOUBLE_FLAT = "bb"
NATURAL = "n"

def getPitchName(pitch, accidental):
  if(pitch == 0):
    if(accidental == SHARP):
      return 'his'
    if(accidental == DOUBLE_FLAT):
      return "deses"
    return 'c'

  if(pitch == 1):
    if(accidental == SHARP):
      return 'cis'
    if(accidental == FLAT):
      return 'des'
    if(accidental == DOUBLE_SHARP):
      return "hisis"

  if(pitch == 2):
    if(accidental == DOUBLE_SHARP):
      return 'cisis'
    if(accidental == DOUBLE_FLAT):
      return "eses"
    return 'd'

  if(pitch == 3):
    if(accidental == SHARP):
      return 'dis'
    if(accidental == FLAT):
      return 'es'
    if(accidental == DOUBLE_FLAT):
      return "feses"

  if(pitch == 4): 
    if (accidental == FLAT):
      return "fes"
    if(accidental == DOUBLE_SHARP):
      return 'disis'
    return 'e'

  if(pitch == 5):
    if(accidental == SHARP):
      return 'eis'
    if(accidental == DOUBLE_FLAT):
      return "geses"
    return 'f'

  if(pitch == 6):
    if(accidental == SHARP):
      return 'fis'
    if(accidental == FLAT):
      return 'ges'
    if(accidental == DOUBLE_SHARP):
      return 'eisis'

  if(pitch == 7):
    if(accidental == DOUBLE_SHARP):
      return "fisis"
    if(accidental == DOUBLE_FLAT):
      return "asas"
    return 'g'

  if(pitch == 8):
    if(accidental == SHARP):
      return 'gis'
    if(accidental == FLAT):
      return 'as'
    if(accidental == DOUBLE_SHARP):
      return "gisis"

  if(pitch == 9):
    if(accidental == DOUBLE_SHARP):
      return "gisis"
    if(accidental == DOUBLE_FLAT):
      return "heses"
    return 'a'

  if(pitch == 10):
    if(accidental == SHARP):
      return 'ais'
    if(accidental == FLAT):
      return 'b'
    if(accidental == DOUBLE_FLAT):
      return "ceses"
   
  if(pitch == 11):
    if(accidental == FLAT):
      return "ces"
    if(accidental == DOUBLE_SHARP):
      return "aisis"
    return 'h'

def getAccidentalSymbol(accidental):
  if(accidental == "accidentalSharp"):
    return SHARP
  if(accidental == "accidentalFlat"):
    return FLAT
  if(accidental == "accidentalNatural"):
    return NATURAL
  if(accidental == "accidentalDoubleSharp"):
    return DOUBLE_SHARP
  if(accidental == "accidentalDoubleFlat"):
    return DOUBLE_FLAT
    
    
def note2pitch(note, accidental):
  pitch = int(note) % 12
  #octave = "'"

  accidentalSymbol = getAccidentalSymbol(accidental)
  pitchName = getPitchName(pitch, accidentalSymbol)
 
  if(accidentalSymbol is None):
    accidentalSymbol = ""
  
  return "{0}".format(pitchName)

def getNote(note):
  pitches = note.findall('pitch')
  accidentals = note.findall('Accidental/subtype')

  pitch = 0
  accidental = ""
  if(len(pitches) > 0):
    pitch = pitches[0].text

  if(len(accidentals) > 0):
    accidental = accidentals[0].text

  pitchString = note2pitch(pitch, accidental)

  return pitchString
  

def getDuration(durationType):
  if(durationType == "whole"): return "1" 
  if(durationType == "half"): return "2"
  if(durationType == "quarter"): return "4"
  if(durationType == "eighth"): return "8"
  if(durationType == "16th"): return "16"
  if(durationType == "32th"): return "32"
  if(durationType == "64th"): return "64"
  if(durationType == "128th"): return "128"


def getChord (chord):
  result = " "
  
  for note in chord.findall('Note'):
    noteString = getNote(note)
    result += " " + noteString
  
  durationType = chord.findall('durationType')
  duration = getDuration(durationType[0].text)

  # Dot
  dotsType = chord.findall('dots')
  if(len(dotsType) > 0):
    duration += '.'

  # Tie
  tie = chord.findall('Note/Spanner/Tie')
  if(len(tie) > 0):
    duration += '~'

  result += str(duration)
  return result

def getRest (rest):  
  durationType = rest.findall('durationType')
  duration = getDuration(durationType[0].text)

  if(duration is None):
    return ''

  dotsType = rest.findall('dots')
  if(len(dotsType) > 0):
    duration += '.'

  result = " r" + str(duration)
  return result

def convert (file) :
  root = ET.parse(file).getroot()
  print(root)
  lilypondCode = ""
  for staff in root.findall('Score/Staff'):
      staffId = staff.get('id')
      print("===============")    
      print("Staff " + staffId)
      print("===============")
      lilypondCode += "staff" + staffId + " = {"
      measureNumber=1
      for measure in staff.findall('Measure'):
        lilypondCode += ' \n' + '% ' + str(measureNumber) +  ' \n'
        measureNumber = measureNumber + 1
        for voice in measure.findall('voice'):
          for child in list(voice):
            if(child.tag == "Chord"):
              chord = getChord(child)
              lilypondCode += chord
            if(child.tag == "Rest"):
              rest = getRest(child)
              lilypondCode += rest
           
      lilypondCode += " }"             
  print(lilypondCode)

#convert('accidentals.mscx')
convert('szunetek-pontzott.mscx')

 


