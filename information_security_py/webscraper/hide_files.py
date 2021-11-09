# Hide files or directory.

# Author: @andvsilva
# date 2021-11-09
import ctypes

attribute_hide  = 0x02

return_ = ctypes.windll.kernel32.SetFileAttributesW('hide_file', attribute_hide)

if return_:
    print("File was hidden.")
else:
    print("File was not hidden.")