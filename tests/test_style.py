import lasem
import cairo

itex = r"$$\frac{B + \sqrt{- A C + B^{2}}}{A}$$"
doc = lasem.mathml_document_new_from_itex(itex, len(itex))

root = doc.get_root_element()
style = root.get_default_style()
style.set_math_size_pt(30)
style.set_math_color(1.0, 0.0, 0.0, 1.0)
root.set_default_style(style)

view = doc.create_view()

surface = cairo.SVGSurface("test_style.svg", *view.get_size())
cr = cairo.Context(surface)

view.set_cairo(cr)
view.render(0, 0)

surface.finish()
