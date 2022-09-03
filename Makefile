SRC = index.html css/style.css

all: resources/n1ghth4wk.pdf resources/n1ghth4wk-book.pdf

resources/n1ghth4wk.pdf: $(SRC)
	weasyprint $< $@

%-book.pdf: %.pdf
	pdfbook2 --paper=a4paper -n $<
