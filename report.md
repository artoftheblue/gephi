# Exploring Word Chains

## Introduction

The problem at question has piqued my interest quite a while ago, and it deals with my interest in word games, specifically Scrabble. 

It gives you a massive advantage to know what letter strings could be transformed into one another if a single letter is changed because it allows you to look at a variety of new options at once which might be difficult to see otherwise. Similarly, it could allow swapping one of the letter from your letter rack with a tile that is already at play.

The most useful application of this tool is to find connection between $7$-letter words and $8$ letter words. However, the graphs that emerge if trying to visualize this are very clunky, so I have opted to only consider connection between the words of average length, that is $5$. This allows me to describe patterns that occur in graphs of all sizes.

Overall, these visualizations allow you to have a peek into what words are at play with each other and notice patterns that could be useful for competitive play later. Additionally, the program written in this project could be used to solve word chain exercises that are prevalent in Olympiad English books.

## Data Sources

The main source is the scrabble SOWPODS database that contains all the words that are currently in use in CSW23 wordlist in competitive Scrabble. This is the most comprehensive wordlist freely available. Thus, it allows getting the most interesting graphs possible.

Words are vertices, whereas two vertices are connected by an edge if they differ by a single letter. The edge weight is the highest point value of the letter as per the standard Scrabble letter point distribution.

Since the operation of swapping one letter is reversible, the graph is non-oriented.

> *See `WordChainSolver.py` file for additional context, as well as the Word Chain Finder tool.*

## Centrality Indexes

> *Trying to plug in a table into the report is an absolute nightmare, so refer to the `.gephi` file*

### Degree Centrality

Degree Centrality denotes what words are connected to most other words. There are three major groups of vertices that have the highest degree centrality, and all of them are separate close-knit groups that have an `-ES` ending. This totally matches my expectations given that most of $5$-letter words in English have that ending.

### Weighted Degree Centrality

Weighted Degree Centrality highlights the same groups, but gives more attention to the high-value, rare connections with uncommon letters.

### Betweenness Centrality

Betweenness Centrality gives the vertices that allow to form the highest number of longest chains possible.

### Closeness Centrality 

Closeness Centrality is relatively inconclusive because it takes absolutely forever to calculate. 

## Bundle and Pivotal

> *Refer to the `bundle & pivotal.py` file, as well as the `.gephi` file*

## Clusters

> *Refer to the `.gephi` file* 

## Dijkstra's Algorithm

Trivial since the most connected vertex is one-edge away from all others that are connected to it, and other nodes are unreachable.

## Minimal Spanning Tree

> *Refer to the `.gephi` file* 

Trivial since most nodes are disconnected. Just remove one extra edge to eliminate loops.

## Conclusion

The goal is definitely achieved. There is now a tool that I can use to explore how the words are connected to each other in a way that is not intuitive to people. It is not only very fun and addicting, but also has a benefit to understanding common linguistic patterns that exist in the language of choice. 

The main result is actually the word chain finder script in python, whereas the colourful graphs help to show its results as well as track some general statistics.

Gephi is an amazing tool to work with graphs, with one exception: there is no undo button (HOW?). The homework itself is pretty general and some subproblems are useless because the chosen restrictions are too general and may lead to trivial graphs.