
.PHONY: all

all: content build

content:
	@python -m pptonator.cli generate --out configs/dos.yaml

build:
	@python -m pptonator.cli build --input configs/dos.yaml --out ppts/dos.ppt