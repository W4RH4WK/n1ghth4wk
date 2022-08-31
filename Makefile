SRC = index.html style.css

all: N1ghth4wk.pdf N1ghth4wk-book.pdf

clean:
	$(RM) N1ghth4wk.pdf N1ghth4wk-book.pdf

N1ghth4wk.pdf: $(SRC)
	weasyprint $< $@

%-book.pdf: %.pdf
	pdfbook2 --paper=a4paper -n $<
