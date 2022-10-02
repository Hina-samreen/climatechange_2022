## climatechange_2022
Climate change reporter 2022

A website where all the climate change related articles are placed and rendered in the form of graph. Useful for climate enthusiasts.![Screenshot 2022-10-02 at 17 26 30](https://user-images.githubusercontent.com/66202956/193462111-e8e67ae0-1bbc-4047-a2d6-bc8e0166b033.png)

## Features
- Display of Climate change related nodes
- Display of Climate change related articles with the nodes using a relationship
- User can search for his preferred climate label related articles
- User can view the relationship details by clicking on the arrow
- He/She can navigate to the article using the URL displayed in the details window
- User can filter articles using calendar acooring to years

## How to use start this website?
Firstly the Neo4j has to be prepared as follows:
- Start with a blank Neo4j instance(you can either use [Neo4j browser](https://neo4j.com/docs/operations-manual/current/installation/neo4j-browser/#:~:text=Neo4j%20Browser%20is%20a%20tool,Neo4j%20Server%20and%20Neo4j%20Desktop.) or spin up a blank [Neo4j Sandbox](https://neo4j.com/sandbox/)and then load the Climate change dataset and run the cypher queries as below:

```
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Hina-samreen/climatechange_2022/main/relations_message_version3_withyear.csv'AS row  
MERGE (src:Climate {name: row.subjects})  
MERGE (tgt:Climate {name: row.objects})  
MERGE (src)-[r:has{relation:row.relationships,date:row.dates,year:row.Year,title:row.titles}]->(tgt) 

```

We have precalculated community detection algorithm to assign community ids for each Character. So we can load that next using the below cypher query:

```
LOAD CSV WITH HEADERS FROM 'https://github.com/Hina-samreen/climatechange_2022/blob/main/names_message_version3.csv' AS row  
MATCH (c:Climate {name: row.name})  
SET c.community = toInteger(row.community) 

```
Our graph consists of Climate nodes that are connected by an has relationship. We can visualize the whole graph in Neo4j Browser by running the following cypher:
```
MATCH p = (:Climate)-[:has]->(:Climate)
RETURN p
```
![Screenshot 2022-10-02 at 19 49 01](https://user-images.githubusercontent.com/66202956/193468473-cfdfb56e-f6c1-4a3b-b5d8-da95a207e391.png)

