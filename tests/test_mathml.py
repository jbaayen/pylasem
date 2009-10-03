import lasem
import cairo

mathml = "<math xmlns='http://www.w3.org/1998/Math/MathML' display='inline'><mrow><mo>(</mo><mstyle scriptlevel=\"2\"><mrow><mtable rowspacing=\"0.5ex\"><mtr><mtd><mn>0 </mn></mtd> <mtd><mn>1 </mn></mtd></mtr> <mtr><mtd><mn>1 </mn></mtd> <mtd><mn>0 </mn></mtd></mtr></mtable></mrow></mstyle><mo>)</mo></mrow></math>"
doc = lasem.dom_document_new_from_memory(mathml, len(mathml))

view = doc.create_view()

surface = cairo.SVGSurface("test_mathml.svg", *view.get_size())
cr = cairo.Context(surface)

view.set_cairo(cr)
view.render(0, 0)

surface.finish()
