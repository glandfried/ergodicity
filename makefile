bib:
	git submodule update --init ./biblio/
	- ln -s -f biblio/biblio.bib biblio.bib
	- ln -s -f biblio/download.sh download.sh

pdf:
	sh download.sh yaari2010-cooperationEvolution
	sh download.sh peters2015-evolutionaryAdvantageOfCooperation
	sh download.sh peters2019-ergodicityEconomics
	sh download.sh nowak2006-rulesForCooperation 
	sh download.sh meder2019-ergodicityBreaking
push:
	git submodule update --init biblio/
	cp biblio/topic/ergodicity.bib ergodicity.bib
	git add ergodicity.bib
	git commit -m "$(m)"
	git push origin master

