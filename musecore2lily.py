import xml.etree.ElementTree as ET

SHARP = "#"
FLAT = "b"
NATURAL = "n"

def getPitchName(pitch, accidental):
  if(pitch == 0):
    return 'c'
  if(pitch == 1):
    return 'cis'
  if(pitch == 2):
    return 'd'
  if(pitch == 4):
    return 'e'
  if(pitch == 5):
    return 'f'
  if(pitch == 7):
    return 'g'
  if(pitch == 9):
    return 'a'
  if(pitch == 11):
    return 'h'

def getAccidentalSymbol(accidental):
  if(accidental == "accidentalSharp"):
    return SHARP
  if(accidental == "accidentalFlat"):
    return FLAT
  if(accidental == "accidentalNatural"):
    return NATURAL
    
def note2pitch(note, accidental):
  pitch = int(note) % 12
  octave = int(int(note) / 12)

  accidentalSymbol = getAccidentalSymbol(accidental)
  pitchName = getPitchName(pitch, accidentalSymbol)

  return "{0} {1} {2}".format(pitchName, octave, accidentalSymbol)

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
  

def printChord (chord):
  duration = chord.findall('durationType')
  print(duration[0].text)
  for note in chord.findall('Note'):
    note  = getNote(note)
    print(note)

def convert () :
  root = ET.parse('skala.mscx').getroot()
  print(root)
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
              printChord(child)
           # if(child.tag == "Rest"):
             # print(child.tag)             

convert()
 


