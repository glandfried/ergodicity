bib:
	make pull -C ./biblio/
	cp biblio/topic/ergodicity.bib biblio.bib
	cp biblio/download.sh download.sh

download:
	sh download.sh	


push:
	git submodule update --init biblio/
	cp biblio/topic/ergodicity.bib ergodicity.bib
	git add ergodicity.bib
	git commit -m "$(m)"
	git push origin master

