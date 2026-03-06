import sys 
import os
import argparse
from analysis_tool import analyze,write_report

# importing and taking direct arguments( file name) frm terminal
"""
if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Usage:python main.py<file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    #if not file_name.endswith(".txt"):
        #file_name+=".txt"
    

    if not os.path.exists(file_name):
        print("File not there")
        sys.exit(1)
    result=ana_numb(file_name)

    out_report(file_name,result)
"""
if __name__ == "__main__":
    parser =argparse.ArgumentParser(description="Analyze no.from a file and generate report")
    parser.add_argument("file_name",help="input file name")
    parser.add_argument("--output",help="custom outputfile name")
    parser.add_argument("--verbose",action="store_true",help="Print analysis details in terminal")

    args=parser.parse_args()
    file_name=args.file_name     
    if not os.path.exists(file_name):
        print("File does not exist.")
        exit(1)
    result=analyze(file_name)
    
    if args.verbose:
        print("Analysis report")
        print(f"Total:{result['total']}")
        print(f"Count:{result['count']}")
        print(f"Largest:{result['largest']}")
        print(f"Average:{result['average']}")
        

    output_file=write_report(file_name,result,args.output)

    print(f"Report saved as:{output_file}")