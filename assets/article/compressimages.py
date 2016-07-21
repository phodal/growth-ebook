from PIL import Image, ImageFile
from sys import exit, stderr
from os.path import getsize, isfile, isdir, join
from os import remove, rename, walk, stat
from stat import S_IWRITE
from shutil import move
from argparse import ArgumentParser
from abc import ABCMeta, abstractmethod
 
class ProcessBase:
    """Abstract base class for file processors."""
    __metaclass__ = ABCMeta
 
    def __init__(self):
        self.extensions = []
        self.backupextension = 'compressimages-backup'
 
    @abstractmethod
    def processfile(self, filename):
        """Abstract method which carries out the process on the specified file.
        Returns True if successful, False otherwise."""
        pass
 
    def processdir(self, path):
        """Recursively processes files in the specified directory matching
        the self.extensions list (case-insensitively)."""
 
        filecount = 0 # Number of files successfully updated
 
        for root, dirs, files in walk(path):
            for file in files:
                # Check file extensions against allowed list
                lowercasefile = file.lower()
                matches = False
                for ext in self.extensions:
                    if lowercasefile.endswith('.' + ext):
                        matches = True
                        break
                if matches:
                    # File has eligible extension, so process
                    fullpath = join(root, file)
                    if self.processfile(fullpath):
                        filecount = filecount + 1
        return filecount
 
class CompressImage(ProcessBase):
    """Processor which attempts to reduce image file size."""
    def __init__(self):
        ProcessBase.__init__(self)
        self.extensions = ['jpg', 'jpeg', 'png']
 
    def processfile(self, filename):
        """Renames the specified image to a backup path,
        and writes out the image again with optimal settings."""
        try:
            # Skip read-only files
            if (not stat(filename)[0] & S_IWRITE):
                print 'Ignoring read-only file "' + filename + '".'
                return False
            
            # Create a backup
            backupname = filename + '.' + self.backupextension
 
            if isfile(backupname):
                print 'Ignoring file "' + filename + '" for which existing backup file is present.'
                return False
 
            rename(filename, backupname)
        except Exception as e:
            stderr.write('Skipping file "' + filename + '" for which backup cannot be made: ' + str(e) + '\n')
            return False
 
        ok = False
 
        try:
            # Open the image
            with open(backupname, 'rb') as file:
                img = Image.open(file)
 
                # Check that it's a supported format
                format = str(img.format)
                if format != 'PNG' and format != 'JPEG':
                    print 'Ignoring file "' + filename + '" with unsupported format ' + format
                    return False
 
                # This line avoids problems that can arise saving larger JPEG files with PIL
                ImageFile.MAXBLOCK = img.size[0] * img.size[1]
                
                # The 'quality' option is ignored for PNG files
                img.save(filename, quality=90, optimize=True)
 
            # Check that we've actually made it smaller
            origsize = getsize(backupname)
            newsize = getsize(filename)
 
            if newsize >= origsize:
                print 'Cannot further compress "' + filename + '".'
                return False
 
            # Successful compression
            ok = True
        except Exception as e:
            stderr.write('Failure whilst processing "' + filename + '": ' + str(e) + '\n')
        finally:
            if not ok:
                try:
                    move(backupname, filename)
                except Exception as e:
                    stderr.write('ERROR: could not restore backup file for "' + filename + '": ' + str(e) + '\n')
 
        return ok
 
class RestoreBackupImage(ProcessBase):
    """Processor which restores image from backup."""
 
    def __init__(self):
        ProcessBase.__init__(self)
        self.extensions = [self.backupextension]
 
    def processfile(self, filename):
        """Moves the backup file back to its original name."""
        try:
            move(filename, filename[: -(len(self.backupextension) + 1)])
            return True
        except Exception as e:
            stderr.write('Failed to restore backup file "' + filename + '": ' + str(e) + '\n')
            return False
 
class DeleteBackupImage(ProcessBase):
    """Processor which deletes backup image."""
 
    def __init__(self):
        ProcessBase.__init__(self)
        self.extensions = [self.backupextension]
 
    def processfile(self, filename):
        """Deletes the specified file."""
        try:
            remove(filename)
            return True
        except Exception as e:
            stderr.write('Failed to delete backup file "' + filename + '": ' + str(e) + '\n')
            return False
 
if __name__ == "__main__":
    # Argument parsing
    modecompress = 'compress'
    moderestorebackup = 'restorebackup'
    modedeletebackup = 'deletebackup'
    parser = ArgumentParser(description='Reduce file size of PNG and JPEG images.')
    parser.add_argument(
        'path',
         help='File or directory name')
    parser.add_argument(
        '--mode', dest='mode', default=modecompress,
        choices=[modecompress, moderestorebackup, modedeletebackup],
        help='Mode to run with (default: ' + modecompress + '). '
            + modecompress + ': Compress the image(s). '
            + moderestorebackup + ': Restore the backup images (valid for directory path only). '
            + modedeletebackup + ': Delete the backup images (valid for directory path only).')
 
    args = parser.parse_args()
 
    # Construct processor requested mode
    if args.mode == modecompress:
        processor = CompressImage()
    elif args.mode == moderestorebackup:
        processor = RestoreBackupImage()
    elif args.mode == modedeletebackup:
        processor = DeleteBackupImage()
 
    # Run according to whether path is a file or a directory
    if isfile(args.path):
        if args.mode != modecompress:
            stderr.write('Mode "' + args.mode + '" supported on directories only.\n')
            exit(1)
        processor.processfile(args.path)
    elif isdir(args.path):
        filecount = processor.processdir(args.path)
        print '\nSuccessfully updated file count: ' + str(filecount)
    else:
        stderr.write('Invalid path "' + args.path + '"\n')
        exit(1)