# Load tables from an Excel file, and write to a markdown file

import pytablereader as ptr
import pytablewriter as ptw
import sys


def excel_to_md(infname, outfname):
    loader = ptr.ExcelTableFileLoader(infname)
    writer = ptw.MarkdownTableWriter()

    with open(outfname, "w") as f:
        f.write("# Hardware Discovery\n")
        f.write("\n")
        f.write("*{{ git_revision_date_localized }}*\n")
        f.write("\n")
        writer.stream = f
        for table_data in loader.load():
            writer.from_tabledata(table_data, is_overwrite_table_name = True)
            writer.write_table()

    return


# Fix header levels
def fix_headers(outfname):
    with open(outfname, "r") as f:
        linelist = f.read().splitlines()
    
    newlinelist = []
    hlevel = 1
    for line in linelist:
        if len(line) > 0:
            if line[0] == '#':
                if hlevel == 1:
                    hlevel = 2
                else:
                    line = '#' + line
        newlinelist.append(line)

    with open(outfname, "w") as f:
        for line in newlinelist:
            f.write(line + "\n")

    return




def main():

    # infname = "A:/Documents/expeca/lab-inventory/ExPECA-HW-Discovery.xlsx"  # Input Excel file name, full path
    # outfname = "A:/Documents/expeca/lab-inventory/ExPECA-HW-Discovery.md"      # Output markdown file name, full path

    # Command line input parameters
    # It has to be 2 command line parameters
    argc = len(sys.argv)
    if argc != 3:
        exit(0)  
    infname = sys.argv[1]                             # Input Excel file name, full path
    outfname = sys.argv[2]                            # Output markdown file name, full path

    excel_to_md(infname, outfname)
    fix_headers(outfname)

    return

if __name__ == "__main__":
    main()


