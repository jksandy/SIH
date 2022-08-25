# Import the modules
import repet
import matplotlib.pyplot as plt
import os
import shutil
# define class
class mp3_converter():

  # the "init" function is called when the instance is
  # created and ready to be initialized
  def __init__(self, path, ext, dirName):
      """Class that takes folder of music files of one file type, 
      converts them to mp3 and creates a new directory and moves them into it
      Input path of files that you would like to convert
      Extension of files you would like to convert i.e. WAV
      Folder name of the new directory you would like to create
      """
      self.path = path
      self.ext = ext
      self.dirName = dirName
  
  # create instance methods
  def lower_underscore(self):
      """
      Converts all files in path to lowercase
      Replaces all spaces in filename with _
      """
      print("lower")
      directory = self.path
      [os.rename(os.path.join(directory, f), os.path.join(directory, f).replace(' ', '_').lower()) for f in os.listdir(directory)]

  def mp3(self):
      """
      Converts all files in path with entered extension to mp3
      """
      print("convert")
      directory = self.path
      for f in os.listdir(directory):
          if (f.endswith(self.ext)):
              os.system("ffmpeg -i {} -ar 44100 -ac 2 -b:a 320k {}/{}.mp3".format(
                  os.path.join(directory, f), directory, os.path.splitext(f)[0]))

  def make_dir(self):
      """
      Creates a directory for mp3's and moves all 
      previously created mp3's into it
      """
      print("makdir")
      mp3_directory = self.path + "/" + self.dirName
      if not os.path.exists(mp3_directory):
          os.makedirs(mp3_directory)
      for filename in os.listdir(self.path):
          if (filename.endswith(".mp3")):
              source = os.path.join(self.path, filename)
              shutil.move(source, mp3_directory)

def seperate():
    # Read the audio signal (normalized) with its sampling frequency in Hz
    audio_signal, sampling_frequency = repet.wavread("media/file.wav")

    # Estimate the background signal, and the foreground signal
    background_signal = repet.sim(audio_signal, sampling_frequency)
    foreground_signal = audio_signal-background_signal

    # Write the background and foreground signals
    repet.wavwrite(background_signal, sampling_frequency, "seperated/background_signal.wav")
    repet.wavwrite(foreground_signal, sampling_frequency, "seperated/foreground_signal.wav")
    print("Seperating")
    conv = mp3_converter('seperated','.wav','mp3')
    conv.lower_underscore()
    conv.mp3()
    
    return 1