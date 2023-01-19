# Load tables from an Excel file, and write to a markdown file

import pytablereader as ptr
import pytablewriter as ptw
import os
import sys


def main():

    # infname = "C:/pythondev/ExPECA-lab-inventory-test.xlsx"  # Input Excel file name, full path
    # outfname = "C:/pythondev/ExPECA-lab-inventory-test"      # Output markdown file name, full path, minus the .md extension

    # Command line input parameters
    argc = len(sys.argv)
 
    # It has to be 2 command line parameters
    if argc != 3:
        exit(0)
    
    infname = sys.argv[1]                             # Input Excel file name, full path
    outfname = sys.argv[2]                            # Output markdown file name, full path, minus the .md extension

    status = "ok"

    loader = ptr.ExcelTableFileLoader(infname)
    writer = ptw.MarkdownTableWriter()

    i = 0
    try:
        for table_data in loader.load():
            writer.from_tabledata(table_data, is_overwrite_table_name = True)
            writer.dump(outfname + "-" + str(i) + ".md")
            i += 1
    except:
        status = "nok"

    if status == "ok":
        with open(outfname + ".md", 'w') as outfile:
            for j in range(i):
                with open(outfname + "-" + str(j) + ".md") as infile:
                    outfile.write(infile.read())
                os.remove(outfname + "-" + str(j) + ".md")
    else:
        for j in range(i):
            os.remove(outfname + "-" + str(j) + ".md")


if __name__ == "__main__":
    main()


