

import re
txt = "Nursultan, is, the, capital, of, KZ."
print(re.sub("[ ,.]", ":", txt))
#sub -> function replaces the matches
# with the text of your choice