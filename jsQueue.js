class Queue {
    // Array is used to implement a Queue 
    constructor() {
        this.song = [];
    }

    // Functions to be implemented 
    enqueue(song) {
        this.items.push(song);
    } 
    dequeue()
    {
        if (this.isEmpty())
            return "Can't Dequeue";
        return this.items.shift();
    } 

    front() {
        if (this.isEmpty())
            return "No elements in Queue";
        return this.items[0]; 
    }

    isEmpty() {
        return this.items.length == 0; 
    }


    printQueue() {
        var str = "";
        for (var i = 0; i < this.items.length; i++)
            str += this.items[i] + " ";
        return str; 
    }
} 