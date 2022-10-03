## climatechange_2022
Climate change reporter 2022

A website where all the climate change related articles are placed and rendered in the form of graph. Useful for climate enthusiasts!)
![Screenshot 2022-10-03 at 22 24 32](https://user-images.githubusercontent.com/66202956/193675164-b485771c-9922-49a4-ac7a-d5681be372c5.png)

## Features
- Display of Climate change related nodes
- Display of Climate change related articles with the nodes using a relationship
- User can search for his preferred climate label related articles
- User can view the relationship details by clicking on the arrow
- He/She can navigate to the article using the URL displayed in the details window
- User can filter articles using calendar according to years

## How to start/access this website?
Firstly the Neo4j has to be prepared as follows:
- Start with a blank Neo4j instance(you can either use [Neo4j browser](https://neo4j.com/docs/operations-manual/current/installation/neo4j-browser/#:~:text=Neo4j%20Browser%20is%20a%20tool,Neo4j%20Server%20and%20Neo4j%20Desktop.) or spin up a blank [Neo4j Sandbox](https://neo4j.com/sandbox/)and then load the Climate change dataset and run the cypher queries as below:

```
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Hina-samreen/climatechange_2022/main/Data_set/relations_message_version3_withyear.csv'AS row  
MERGE (src:Climate {name: row.subjects})  
MERGE (tgt:Climate {name: row.objects})  
MERGE (src)-[r:has{relation:row.relationships,date:row.dates,year:row.Year,title:row.titles}]->(tgt) 

```

We have precalculated community detection algorithm to assign community ids for each Character. So we can load that next using the below cypher query:

```
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Hina-samreen/climatechange_2022/main/Data_set/names_message_version3.csv' AS row  
MATCH (c:Climate {name: row.name})  
SET c.community = toInteger(row.community) 

```
Our graph consists of Climate nodes that are connected by a 'has' relationship. We can visualize the whole graph in Neo4j Browser by running the following cypher:
```
MATCH p = (:Climate)-[:has]->(:Climate)
RETURN p
```
![Screenshot 2022-10-02 at 19 49 01](https://user-images.githubusercontent.com/66202956/193468473-cfdfb56e-f6c1-4a3b-b5d8-da95a207e391.png)

We can see from the above image, that all the Climate nodes are connected to each other via a relationship and this visualization can be brought to the front end using Neovis.js, which combines the Javascript driver for Neo4j and the vis.js visualization library. For this we need index.html file

## index.html
After having prepared the Neo4j database as explained in the above sections, it is time to run the index.html file. Only one change needs to be done and it is changing of Neo4j credentials as you can see in the below code snippet:

```
var config = {


				containerId: "viz",
				neo4j: {
					serverUrl: "bolt://localhost:7687",
					serverUser: "neo4j",
					serverPassword: "neo4j-some_password_that_you_set"
				},
				
 ```
 Once you change the credentials and run the index.html file, you will be able to access the climate change reporter

## Software documentation
To know more about the softwares used and the process of our workflow, please visit the [Wiki page](https://github.com/Hina-samreen/climatechange_2022/wiki) of our project.
