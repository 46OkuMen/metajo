import os
from romtools.disk import Disk

#SystemDisk = Disk(DEST_DISK_SYSTEM)
DemoDisk = Disk(os.path.join('patched', 'Zai Metajo.hdi'))

filename = 'HJ001.UGP'

filepath = os.path.join('patched', filename)
    
DemoDisk.insert(filepath, path_in_disk='GRAPHIC/')
