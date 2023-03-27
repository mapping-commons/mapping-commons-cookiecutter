###Configuration
#
# These are standard options to make Make sane:
# <http://clarkgrubb.com/makefile-style-guide#toc2>

MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

VERSION_MAKEFILE = 				0.1
TODAY ?=                    	$(shell date +%Y-%m-%d)
ROBOT =							robot
ONTOLOGY_DIR = 					ontologies
MAPPING_DIR = 					mappings
TMP_DIR = 						tmp
SSSOM_TOOLKIT = 				sssom
TSVALID = 						tsvalid


$(ONTOLOGY_DIR)/ $(MAPPING_DIR)/ $(TMP_DIR)/:
	mkdir -p $@

#######################################
##### Mapping maintenance  ############
#######################################

mapping-%:
	make $(MAPPING_DIR)/$*.sssom.tsv -B

.PHONY: mappings
mappings:
	make $(shell grep local_name registry.yml | sed 's/local_name: /$(MAPPING_DIR)\//' )

#######################################
##### Mapping validation  #############
#######################################

validate-%:
	tsvalid $(MAPPING_DIR)/$*.ols.sssom.tsv --comment "#"
	$(SSSOM_TOOLKIT) validate $(MAPPING_DIR)/$*.ols.sssom.tsv
	$(SSSOM_TOOLKIT) convert $(MAPPING_DIR)/$*.ols.sssom.tsv -o $(MAPPING_DIR)/$*.ols.sssom.ttl

MAPPINGS=$(notdir $(wildcard $(MAPPING_DIR)/*.ols.sssom.tsv))
VALIDATE_MAPPINGS=$(patsubst %.ols.sssom.tsv, validate-%, $(notdir $(wildcard $(MAPPING_DIR)/*.ols.sssom.tsv)))

validate-mappings: 
	$(MAKE) $(VALIDATE_MAPPINGS)

##################################
##### Utilities ###################
##################################

.PHONY: test
test: validate-mappings

.PHONY: clean
clean:
	[ -n "$(TMP_DIR)" ] && [ $(TMP_DIR) != "." ] && [ $(TMP_DIR) != "/" ] && [ $(TMP_DIR) != ".." ] && [ -d ./$(TMP_DIR) ] && rm -rf ./$(TMP_DIR)/*
	[ -n "$(ONTOLOGY_DIR)" ] && [ $(ONTOLOGY_DIR) != "." ] && [ $(ONTOLOGY_DIR) != "/" ] && [ $(ONTOLOGY_DIR) != ".." ] && [ -d ./$(ONTOLOGY_DIR) ] && rm -rf ./$(ONTOLOGY_DIR)/*

.PHONY: version
version:
	echo "Mapping Commons Makefile version: $(VERSION_MAKEFILE) (this is the version of the Mapping Commons Toolkit with which this Makefile was generated)" &&\
	echo "ROBOT version: " && $(ROBOT) --version

.PHONY: update_repo
update-repo:
	echo "The $* command is not currently implemented" && fail

.PHONY: public_release
public-release:
	echo "The $* command is not currently implemented" && fail

.PHONY: help
help:
	@echo "$$data"

define data
Usage: [IMAGE=(odklite|odkfull)] [ODK_DEBUG=yes] sh odk.sh make command

----------------------------------------
	Command reference
----------------------------------------

Core commands:
* mappings:						Rebuild all mapping files
* validate-mappings:					Running all validation tests
* version:						Show the current version of the Mapping Commons Makefile and ROBOT.
* help:							Print Mapping Commons Usage information
* public-release:					Uploads the release file to a release management system, such as GitHub releases. Must be configured.

Mapping management:
* mapping-%:						Updates the mapping with the id %.
* validate-%:						Validates the mapping with the id %.

Repo management:
* update-repo:						Update the Mapping Commons repository setup using the config file registry.yaml
* clean:						Delete all temporary files

Examples: 
* sh run.sh make mappings
* sh run.sh make update_repo
* sh run.sh make test

Tricks:
* Add -B to the end of your command to force re-running it even if nothing has changed
* Use the IMAGE parameter to the run.sh script to use a different image like odklite
* Use ODK_DEBUG=yes sh run.sh make ... to print information about timing and debuggingYUY

endef
export data

include {{cookiecutter.__project_slug}}.Makefile