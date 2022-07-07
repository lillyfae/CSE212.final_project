#Linked list 

    The purpose of a linked list is to be able to store information in a way that order matters. A linked list has a head, tail, and 
    nodes in between. To keep the list in order, we will point the node to the node directly before it and directly behind it, except in
    the cases of the head and tail that will only point to one node each. The big O notation for this data structure is O(n) because to 
    find a specific node, we loop through the linked list. 

    We can solve problems that require storing different information in memory, where you want to keep moving down the line of the 
    information, but you'd have to point in the direction it needs to go. Common errors that could occur for this data structure are not 
    removing or inserting a node correctly.



#Video
    https://www.youtube.com/watch?v=WwfhLC16bis&ab_channel=CSDojo


#Example:

    Let's say I have 3 children living at home. Names are:

    `Jameson,Calissa, and Kaden.`

    I want to keep these kids in order of oldest to youngest so I make a node called Jameson. Next is Calissa, so the data for the head of this linked list would be called Jameson and his node would point to Calissa by doing something like Jameson.next = Calissa. Then Calissa would point back to Jameson and forward to Kaden.

    Now, let's say I had another child named Brylee. I need to add her in last so now Kaden will point forward to her and Brylee will point back to Kaden. 

    `Jameson, Calissa, Kaden, and Brylee`

    Oh wow! Now I just adopted a little girl named Karah. She is older than Brylee and younger than Kaden, so she'll need to be pointing to both of them and Kaden will now point forward to Karah and Brylee will point back to Kaden. 

    Jameson, Calissa, Kaden, Karah, and Brylee`


    Let's look at this as if it were a linked list:




