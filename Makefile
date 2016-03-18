include_dir=build
source=chapters/*.md
title='Growth'
filename='growth'


all: html epub rtf pdf mobi

markdown:
	awk 'FNR==1{print ""}{print}' $(source) > $(filename).md

html: markdown
	pandoc -s $(filename).md -t html5 -o index.html -c style.css \
		--include-in-header $(include_dir)/head.html \
		--include-before-body $(include_dir)/author.html \
		--include-before-body $(include_dir)/share.html \
		--include-after-body $(include_dir)/stats.html \
		--title-prefix "Growth: 全栈工程师学习手册" \
		--normalize \
		--smart \
		--toc

epub: markdown
	pandoc -s $(filename).md --normalize --smart -t epub -o $(filename).epub \
		--epub-metadata $(include_dir)/metadata.xml \
		--epub-stylesheet epub.css \
		--epub-cover-image img/cover.png \
		--title-prefix $(title) \
		--normalize \
		--smart \
		--toc

rtf: markdown
	pandoc -s $(filename).md -o $(filename).rtf \
		--title-prefix $(title) \
		--normalize \
		--smart

pdf: markdown
	# OS X: http://www.tug.org/mactex/
	# Then find its path: find /usr/ -name "pdflatex"
	# Then symlink it: ln -s /path/to/pdflatex /usr/local/bin
	pandoc -s $(filename).md -o $(filename).pdf \
		--title-prefix $(title) \
		--template=template/template.tex \
		--normalize \
		--smart \
		--toc \
		--latex-engine=`which xelatex`

mobi: epub
	# Symlink bin: ln -s /path/to/kindlegen /usr/local/bin
	kindlegen $(filename).epub