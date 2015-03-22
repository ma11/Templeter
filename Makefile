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
prefix=/usr/bin

#########
# RULES #
#########

.PHONY: all install

all: 
	

install: ${EXEC}
	install ${EXEC} ${prefix}/bin/${EXEC}
