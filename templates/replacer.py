#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# reader: read a file containing tags associations
# Inputs: filename: address of tag file
# Outputs: replace: tags association dictionnary
def reader(filename):
    replace={}
    taglines = open(filename,'r').readlines()

    for li in taglines:
        #print 'line length: ',li.__len__()
        if li[0]=='#' or li.__len__()==1:
            continue

        [tag,sep,value]= li[:-1].partition(':')

        if value.__len__() != 0:
            if value[0]=='#':
                exec(value[1:],globals())
                value=result

        replace[tag]=value

    return replace

# replace: actualy replace tags in input file and write a new file with tags replaced
# Inputs: inputfile: address of file to read and replace tags
#         outputfile: address of the file to write
#         replacement_table: dictionnary containing tags ddefinition
# Outputs: None
def replace(inputfile,outputfile,replacement_table):
	out=open(inputfile).read()
	for key in replacement_table:
	    out=out.replace(key,replacement_table[key])
	open(outputfile,'w').write(out)

if __name__ == '__main__':

    # Everything recquired for parsing option.
    from optparse import OptionParser
    parser = OptionParser()
    parser.set_description("Read input file and write output file by replacing tags contained in input and known in tag file")

    parser.add_option("-i","--input-file",dest="inputfile",help="Template file to read",metavar="FILE")
    parser.add_option("-o","--output-file",dest="outputfile",help="File to write",metavar="FILE")
    parser.add_option("-t","--tags-file",dest="tagfile",help="File containing tags",metavar="FILE",default='./tags')

    (options,args)=parser.parse_args()
    inputfile=options.inputfile
    outputfile=options.outputfile
    tagfile=options.tagfile

    replacement_table = reader(tagfile)
    #print 'replacement_table:',replacement_table

    replace(inputfile,outputfile,replacement_table)

