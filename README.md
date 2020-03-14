# Information-Retrieval-System using Elasticsearch

This project revolves around the use of Elasticsearch's API and how we can retrieve useful information from an online collection of files.
This project was assigned to me during my Bachelor's curriculum. 

First, I was given a collection of xml files (Parsed Files) which were faulty and needed to be altered. The goal was to remove the <text> tab and, without losing information, add an <objective> and a <title> tab. In order to complete that task I created the programm fix_xml.py. 
  
Then, in order to add the collection on the Elasicsearch online tool, I needed to convert the xml files into json files (Collection). In order to complete that task I created the programm convert.py. 

After creating a custom index (Elasticsearch_Analyzer.json), I uploaded the collection on Elasticsearch. In order to complete that task I created the programm createcollection.py. 

Finally, I was given a text file (testingQueries) with 10 questions to test out my collection. In order to use the text file, I created the programm query.py which asks the user which question he wants to choose and how many results he wants to receive. After the user has given his input, the programm creates/alters the file Elasticsearch_Query.json, asks the collection the question and writes down the results in the file Results.txt.  
