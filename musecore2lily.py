import xml.etree.ElementTree as ET

def note2pitch(note, accidental):
  return str(note) + accidental

def printNote(note):
  pitches = note.findall('pitch')
  accidentals = note.findall('Accidental/subtype')

  pitch = 0
  accidental = ""
  if( not (pitches is None) and len(pitches) > 0):
    pitch = pitches[0].text

  if( not (accidentals is None) and len(accidentals) > 0):
    accidental = accidentals[0].text

  pitchString = note2pitch(pitch, accidental)
  print(pitchString)
  

def printChord (chord):
  duration = chord.findall('durationType')
  print(duration[0].text)
  for note in chord.findall('Note'):
    printNote(note)

def convert () :
  root = ET.parse('kotta.mscx').getroot()
  print(root)
  for staff in root.findall('Score/Staff'):
      print("===============")    
      print("Staff " + staff.get('id'))
      print("===============")
      measureNumber=1
      for measure in staff.findall('Measure'):
        print(str(measureNumber))
        measureNumber = measureNumber + 1
        for voice in measure.findall('voice'):
          for child in voice.getchildren():
            if(child.tag == "Chord"):
              printChord(child)
            if(child.tag == "Rest"):
              print(child.tag)             

convert()
 


