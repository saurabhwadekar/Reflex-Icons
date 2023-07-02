
def wraped(name):
    return f"""class {name}(rx.Component):
    library = "react-icons/cg"
    tag = "{name}"
"""

with open("css_gg.html","r") as f:
    file = f.readlines()

with open("css_gg.py","w") as pyf:
    pyf.write("import reflex as rx\n\n")
    for i in file:
        first = i.find('<div class="name">')
        last = i.find('</div>')
        if i[first:last] != "":
            print(i[first+len('<div class="name">'):last])
            wrap = wraped(i[first+len('<div class="name">'):last])+"\n\n"
            pyf.write(wrap)
