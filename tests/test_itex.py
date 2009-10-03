import lasem
import cairo

itex = r"$$\frac{B + \sqrt{- A C + B^{2}}}{A}$$"
doc = lasem.mathml_document_new_from_itex(itex, len(itex))

view = doc.create_view()

surface = cairo.SVGSurface("test_itex.svg", *view.get_size())
cr = cairo.Context(surface)

view.set_cairo(cr)
view.render(0, 0)

surface.finish()
