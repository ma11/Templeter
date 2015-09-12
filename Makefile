#!/bin/bash

#################################################################
## FILENAME   : Makefile
## AUTHOR     : ma11
## DATE       : Wed Jun 18 00:46:16 2014
## COPYRIGHT  : 
## PROJECT    : 
## DESCRIPTION: 
#################################################################

#############
# VARIABLES #
#############
EXEC=Proj
prefix=${HOME}
INSTALL = install

#########
# RULES #
#########

.PHONY: all install

all: 
	

install: ${EXEC}
	${INSTALL} -d ${prefix}/bin
	${INSTALL} -d ${prefix}/share/templates
	${INSTALL} ${EXEC} ${prefix}/bin/${EXEC}
	${INSTALL} -t ${prefix}/share/templates templates/*
