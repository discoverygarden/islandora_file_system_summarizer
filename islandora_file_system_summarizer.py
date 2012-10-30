'''
    @file
        This file is the CLI for creating an summary of a directory's contents
        for the Islandora Ingester object.
    Created on 29/10/2012
    
    @author
        William Panting
'''

import sys, os
from islandoraUtils.ingest.sumarizer import summarize_directory

if __name__ == '__main__':
    '''
        Entry point!
        @param string sys.argv[1]
            directory_to_report_on
        @param string sys.argv[2]
            file_name_to_write
    '''
    
    if len(sys.argv) == 2:
        directory_to_report_on = sys.argv[1]
        file_name_to_write = 'Islandora_report.csv'
    elif len(sys.argv) == 3:
        directory_to_report_on = sys.argv[1]
        file_name_to_write = sys.argv[2]
    else:
        file_name_to_write = 'Islandora_report.csv'
        directory_to_report_on = os.getcwd()
    
    print('Directory_to_report_on: {0}'.format(directory_to_report_on))
    
    report_path = summarize_directory(os.path.abspath(directory_to_report_on), file_name_to_write)
    
    print('Report completed at {0}.'.format(report_path))
