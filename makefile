push:
	git submodule update --init biblio/
	cp biblio/topic/ergodicity.bib ergodicity.bib
	git add ergodicity.bib
	git commit -m "$(m)"
	git push origin master
	cd ..
	git add ./ergodicity/
	git commit -m "Update ergodicity"
	git push origin master

	
