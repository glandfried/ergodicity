
biblio/.git:
	git submodule update --init ./

bib:
	cd biblio
	git pull origin master
	cp biblio/topic/ergodicity.bib ergodicity.bib
	cd ..

push: biblio/.git
	bib
	git commit -m "$(m)"
	git push origin master

	
