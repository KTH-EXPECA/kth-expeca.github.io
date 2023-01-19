# Load tables from an Excel file, and write to a markdown file

import pytablereader as ptr
import pytablewriter as ptw
import sys


def main():

    # infname = "C:/pythondev/ExPECA-lab-inventory-test.xlsx"  # Input Excel file name, full path
    # outfname = "C:/pythondev/ExPECA-lab-inventory-test.md"      # Output markdown file name, full path

    # Command line input parameters
    # It has to be 2 command line parameters
    argc = len(sys.argv)
    if argc != 3:
        exit(0)  
    infname = sys.argv[1]                             # Input Excel file name, full path
    outfname = sys.argv[2]                            # Output markdown file name, full path

    loader = ptr.ExcelTableFileLoader(infname)
    writer = ptw.MarkdownTableWriter()

    with open(outfname, "w") as f:
        writer.stream = f
        for table_data in loader.load():
            writer.from_tabledata(table_data, is_overwrite_table_name = True)
            writer.write_table()

    return

if __name__ == "__main__":
    main()


