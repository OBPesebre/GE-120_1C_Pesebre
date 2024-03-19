"""

1. Procedural programming does not abide with the "DRY" or Do not write everything method as the codes are based on every procedures needed. Thus, one step or procedure equates
to one line. In terms of functional programming, the programmers make use of several functions in order to have an easier way of maintaining the code. Through functional programming, the programmer can lessen the amount of lines
needed to finish one task. 

2. Git allows programmers through push and pull. In programming, it is essential for us, programmers, to show our work to people and accept feedback. With that in mind, one
can push his/her file to Git in order for his/her collaborators to view them. When pushing a file, he/she can attach a commit message that can give more details to his/her
work. On one end, the collaborators can pull the file to see the programmer's work so that they can edit. Furthermore, they can push it back with messages for the sender to
be notified. Another advantage of Git is that all collaborators can work with one file at the same time. In short, Git is assistive in collaboration of programmers towards
the development and improvement of certain programs. An example is when a group is working with a large project, such as accomplishing traverse computations in Python.
One member can do the computations for the original latitude and departure. The other one can compute for the REC, LEC, and Bearing of the side error. 
The other can adjust the latitude and departure. Thus, all of them can provide comments to each other's works.

3. While loop and for loop are used for iterations. While loop is significant when the programmer is unaware of how many iterations needed for the code. Meanwhile, for loop
is utilized when the programmer knows the exact number of iterations needed. A while loop can be made use of when asking for an input of distances and angles per line in a traverse 
since the programmer is not aware of how many lines does the user have. For loop, on the other hand, can be used when the programmer inserts a limitation to the number of lines
that will be computed. For example, the task is to perform a traverse of a 4-sided parking lot, the programmer can utilize for loops since the exact amount of lines is determined.

4. In programming, it is expected that there are multiple requirements needed to finish the job. 
Hence, it is better for us to have a plan before starting to code as it can help as map out the things that we need to perform. One way of doing that is through the Divide
and Conquer paradigm. Through this framework, we will divide the things that we need into categories. From those categories, we can further dissect them into different parameters.
Thus, in the end, when these are combined, they are able to accomplish the task needed. For example, we need to create a program that makes it easier for geodetic engineers 
to finish computations needed for lotplan through sideshots. The main categories that one can make are traverse processes, sideshots processes, and area computation. Under the processes of traverse, it 
includes the computation of the latitude and departure of the provided lines, LEC, bearing of the side error, and REC. Furthermore, the adjustment of bearings and distances. 
Lastly, the adjustment of coordinates. Moving forward, the sideshots processes entail the computation of latitude and departure, the adjustment of latitude and departure,
and the adjustment of bearings and distances. One can also include the computation for the tie line. For the area computations, one can create codes for DMD-DPA computations. Adding
these things result to the final goal of lotplan computations

5. An example of it is three-wire levelling computation. When being done manually, a good way to start is by setting up your table of values. In this case, we can have a 
better view of our data and incomplete information. From the table, we can see a pattern for computation. We can start by computing the mean readings of foresight and 
backsight readings. Next is by adding the height of the instrument to the known elevation to the backsight reading. Thus, subtracting mean foresight reading from it to
obtain the elevation of the next line. Another step is to compute for the distances of each turning point to BM1. Next, to compute for the error and allowable error. Lastly, is to
adjust the elevations if the performed levelling satisfied the geodetic control order. In terms of programming, the first thing to do is to Divide and Conquer. Divide it 
into different categories and conquer it with pseudocode. Pseudocode is essential in understanding the specific programming functions, input, and other elements needed to finish
the task. Thus, with the mentioned processes in manual computations, my pseucode will involve functions encompassing if, else if, else, input, float. It will also have 
mathematical operations, such as addition, subtraction, multiplication, and division.

"""