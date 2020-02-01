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
    return 'c'
  if(pitch == 1):
    if(accidental == SHARP):
      return 'cis'
    if(accidental == FLAT):
      return 'des'
  if(pitch == 2):
    return 'd'
  if(pitch == 3):
    if(accidental == SHARP):
      return 'dis'
    if(accidental == FLAT):
      return 'es'
  if(pitch == 4): 
    if (accidental == FLAT):
      return "fes"
    return 'e'
  if(pitch == 5):
    if(accidental == SHARP):
      return 'eis'
    return 'f'
  if(pitch == 6):
    if(accidental == SHARP):
      return 'fis'
    if(accidental == FLAT):
      return 'ges'
  if(pitch == 7):
    return 'g'
  if(pitch == 8):
    if(accidental == SHARP):
      return 'gis'
    if(accidental == FLAT):
      return 'as'
  if(pitch == 9):
    return 'a'
  if(pitch == 10):
    if(accidental == SHARP):
      return 'ais'
    if(accidental == FLAT):
      return 'bes'
  if(pitch == 11):
    if(accidental == FLAT):
      return "ces"
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
  octave = int(int(note) / 12) # ezt hangnevbol kell kiszamolni

  accidentalSymbol = getAccidentalSymbol(accidental)
  pitchName = getPitchName(pitch, accidentalSymbol)
 
  if(accidentalSymbol is None):
    accidentalSymbol = ""
  
  return "{0}{1}".format(pitchName, accidentalSymbol)

def getNote(note):
  pitches = note.findall('pitch')
  accidentals = note.findall('Accidental/subtype')

  pitch = 0
  accidental = ""
  if( not (pitches is None) and len(pitches) > 0):
    pitch = pitches[0].text

  if( not (accidentals is None) and len(accidentals) > 0):
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

  result += str(duration)
  return result

def convert (file) :
  root = ET.parse(file).getroot()
  print(root)
  lilypondCode = ""
  for staff in root.findall('Score/Staff'):
      print("===============")    
      print("Staff " + staff.get('id'))
      print("===============")
      measureNumber=1
      for measure in staff.findall('Measure'):
       # print(str(measureNumber))
        measureNumber = measureNumber + 1
        for voice in measure.findall('voice'):
          for child in list(voice):
            if(child.tag == "Chord"):
              chord = getChord(child)
              lilypondCode += chord + " "
           # if(child.tag == "Rest"):
             # print(child.tag)             
  print(lilypondCode)

convert('accidentals.mscx')
 


