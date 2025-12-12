from pathlib import Path
import seedir as sd

# The aim is to end up with a directory listing (clickable) which goes like (we could try creating a folder with simlinks ??)
# Cyber EPQ 2024-25 - Student Work/
#      CyberEPQ Full Project/
#             Anisa Khan/ (Version 16)
#             Ehsan Mohammed/ (Version 8)

def mask(x):
    if x.is_dir() and ("Student Work" in str(x)):
        if "Enrichment" in str(x) or "Club" in str(x) :
            return False
        if len(x.parts) > 5 :
            if "Submitted files" in str(x):
                if len(x.parts) > 8:
                    if "Version" in str(x): # x.parts[-1]
                        next_folder = x.parents[0] / ("Version "+ str(int(x.parts[-1].split(" ")[1]) + 1))
                        return not next_folder.exists()
                    else:
                        return False
                else:
                    return True
            return False
        else:
            return True    
    return False


path = Path.joinpath(Path.home(), "UTC Sheffield")

tree = sd.seedir(path, depthlimit=5, mask=mask, printout=False)

#print(tree)
g = sd.fakedir_fromstring(tree)
g.seedir()