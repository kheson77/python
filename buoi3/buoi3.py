from operator import mod
import module
import module2

from package.module import Cong
from package.subpackage import submodule

import markdown
from extract_face import extract_face




# module.method()
# print(f"Ket qua la: {module2.Nhan()}")
# print(dir(module2))
# print(Cong())
_markdown = """---

# h1 Heading 8-)
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading


## Horizontal Rules

___"""
# html = markdown.markdown(_markdown)
a = extract_face(image_path = 'image.jpg')
# print(a)