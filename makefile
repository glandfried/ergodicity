bib:
	git submodule update --init ./biblio/
	cp biblio/biblio.bib biblio.bib
	cp biblio/download.sh download.sh

download:
	sh download.sh yaari2010-cooperationEvolution
	sh download.sh peters2015-evolutionaryAdvantageOfCooperation


push:
	git submodule update --init biblio/
	cp biblio/topic/ergodicity.bib ergodicity.bib
	git add ergodicity.bib
	git commit -m "$(m)"
	git push origin master

