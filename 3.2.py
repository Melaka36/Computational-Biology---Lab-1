from Bio import Entrez 
 
def search_pubmed(query, max_results=10): 
    Entrez.email = "pasindupathiranagama@gmail.com"   
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results) 
    record = Entrez.read(handle) 
    handle.close() 
    return record 
 
def fetch_pubmed_details(id_list): 
    ids = ",".join(id_list) 
    handle = Entrez.efetch(db="pubmed", id=ids, rettype="medline", 
    retmode="text") 
    records = handle.read() 
    handle.close() 
    return records 
 
def parse_pubmed_records(records): 
    authors_list = [] 
    for record in records.split("\n\nPMID")[1:]: 
        authors = [] 
        for line in record.split('\n'): 
            if line.startswith('AU  - '): 
                authors.append(line[6:]) 
        authors_list.append(authors) 
    return authors_list 
 
if __name__ == "__main__": 
    query = "Alzheimer's" 

search_results = search_pubmed(query) 

total_articles = int(search_results["Count"]) 
print(f"Total number of articles related to Alzheimer's: {total_articles}") 
 
id_list = search_results["IdList"][:10]   
pubmed_records = fetch_pubmed_details(id_list) 

authors_list = parse_pubmed_records(pubmed_records) 
 
for i, authors in enumerate(authors_list, 1): 
    print(f"\nAuthors for Article {i}:") 
    for author in authors: 
        print(f" - {author}") 
