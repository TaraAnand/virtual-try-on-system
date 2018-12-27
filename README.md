# VirtualTryOnSystem
Technica 2018 Research Track Team Project

This project was developed as part of the Virtual Try-On System Research Track for the Technica 2018 Hackathon. The Virtual Try-On System Project is working to develop virtual animations to model clothing on figures. Images can be used to create 3D visualizations of an individual's body and different clothing of various sizes and textures can be modeled on the figure so someone can see how a clothing would realistically fit on them. 

The cloth-movement simulations are created from .obj files, which each represent a different frame of clothing motion. These object files are often quite large, and for our project, we were interested in investigating ways to decrease the data transmission time (since simulations are done on the cloud) by compressing/decompressing algorithms designed specifically to the mesh data. The methods of compression that we implemented are discussed below.

## Elimination of Redundant Information 
The .obj files contain 3 types of information: texture, vertex coordinates (x, y, z), and vertex connections to create the triangles that compose the faces of the mesh. For a given clothing garment, the texture and vertex connection information is the same for all .obj files representing its different frames. Instead of saving including this information in every .obj file, we create a new file containing only this information, and then strip everything but the vertex coordinate information from each .obj file before compression, and revert to the original format upon decompression. This decreases the collective directory size by about 75%.
  
## Huffman Encoding 
We then implemented a Huffman encoding on the remaining file data based on [Bhrigu Srivastava's Implementation](http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/). This decreases the collective directory size by an additional 50% for a total compression rate of about 88%. 

## Rounding 

## Hashing 

## Similar Frame Reduction 


