import re
from Functions import set_cover
'''
 Midterm 2020
 Algorithms 5410
 Available jobs with each company, some companies have more than a job, and there are common jobs between companies.
 The user will check the which companies available for his multiple inputs (the desired job or jobs),
 then check the minimum number of companies for his desired jobs and which they are.
 Project by:Amgad Morsy.
 Supervised by: Dr. Jonathan Lee
'''

def process_file(fname, enc):
    with open(fname, 'r', encoding=enc) as file:
        dat = file.read()
    return (dat)

# reprtive remove form job and companines
def unique_by_first_n(n, coll):
        seen = set()
        for item in coll:
            compare = tuple(item[:n])
            if compare not in seen:
                seen.add(compare)
                yield item

#list to list of lists
def extractDigits(lst):
    res = []
    for el in lst:
        sub = el.split(', ')
        res.append(sub)
    return (res)

#make list of inputs
def listOfinputs(Numerofinputs,ListOfInputs):
    for w in range(Numerofinputs):
        Input_job = input("Please type a job :")
        ListOfInputs.append(Input_job)
    return ListOfInputs

def companiesAndJobs(words,Numerofinputs,ListOfInputs,ListOfCompaniesAndJobs):
# scan the data for only one time to get a list of both companies and jobs depends on the user inputs
    for eachline in words.splitlines():
         for i in range(Numerofinputs):
           find= re.findall(str(ListOfInputs[i]), eachline)
           if find:
              companyAndJob = list(eachline.split('\t'))
              q = companyAndJob[0:2]
              ListOfCompaniesAndJobs.append(q)
    return ListOfCompaniesAndJobs
#arrang subsets for swt cover
def subsetmake(Numerofinputs,ListOfCompaniesAndJobs,ListOfInputs):
    list1 = []
    list2 = []
    list3 = []
    # make a list of sets for the companies that cover each job, "list for each job with companies, then set for all lists"
    for i in range(Numerofinputs):
        for eachjob in ListOfCompaniesAndJobs:
            find = re.findall(str(ListOfInputs[i]), eachjob[0])
            if (find):
                list1.append(eachjob[1])
                list2.append((list1[:]))
                list1.clear()
    subset = []

    for w in list2:  # pick first one
        list3.append(w[0])
    list14 = extractDigits(list3)

    for rr in list14:
        subset.append(set(rr))
    return subset
def main():

    words = process_file("final.txt", "utf-8")
    Numerofinputs= int(input(" Please enter the number of jobs: "))
    ListOfInputs = []
    ListOfCompaniesAndJobs=[]
    listOfinputs(Numerofinputs,ListOfInputs)
    companiesAndJobs(words,Numerofinputs,ListOfInputs,ListOfCompaniesAndJobs)
    filtered_list = list(unique_by_first_n(1, ListOfCompaniesAndJobs))
    FlatList = [item for sublist in filtered_list for item in sublist]
    OnlyCompanies = FlatList[1::2]
    universe = set(OnlyCompanies)
    subsets = subsetmake(Numerofinputs,ListOfCompaniesAndJobs,ListOfInputs)
    cover = set_cover(universe, subsets)
    print("the minimum companies to cover the jobe are", cover)

if __name__ == '__main__':
    while True:
      main()

