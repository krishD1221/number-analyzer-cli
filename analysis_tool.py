import os

def analyze(file_name):
    total=0
    count=0
    largest=0
    average=0
    try:
        with open(file_name,"r") as file:
            numbers=[float(line.strip()) for line in file if line.strip()] 
            total=sum(numbers)
            count=len(numbers)
            largest=max(numbers)
            average=total/count if count>0 else 0
            return{
                "status":"success",
                "total":total,
                "count":count,
                "largest":largest,
                "average":average
            }
    except Exception as e :
        return{"status":"error","message":str(e)}
def write_report(file_name,result,output_file=None):
    base_name=os.path.splitext(file_name)[0]

    if not output_file:
        if result["status"]=="success":
            output_file=f"{base_name}_report.txt"
        else:
            output_file=f"{base_name}_error.txt"

    if result["status"]=="success":
        content=f"""Analysis Report
        --------------
        Total:{result['total']}
        count:{result['count']}
        largest:{result['largest']}
        Average:{result['average']:.2f}
        """
    else:
        content=f"""Error Report
        ------------
        {result['message']}"""

    with open(output_file,"w") as file:
        file.write(content)
    return output_file