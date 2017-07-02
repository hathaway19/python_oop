# Object Call
class Call(object):
    # Initialize all info about this call
    def __init__(self, caller_id, name, number, time, reason):
        self.id = caller_id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    # Displays all info of the call
    def display_call_info(self):
        print "Unique id:", self.id
        print "Caller name:", self.name
        print "Caller phone number:", self.number
        print "Time since call:", self.time
        print "Reason for call:", self.reason
        print ""
        return self

class CallCenter(Call):
    # Initialize variables to hold the call queue and the size of the queue
    def __init__(self, call_list, queue_size):
        self.call_list = call_list
        self.queue_size = queue_size
    # Adds a new call to the end of the queue
    def add_call(self, caller_id, name, number, time, reason):
        print "Adding call to queue"
        self.queue_size += 1 #Queue size increases
        new_call = Call(caller_id, name, number, time, reason) #Set variables of new call from ones passed in
        self.call_list.insert(0,new_call) #Adding call to beginning of queue
        return self
    # Removes the call that's been here the longest (end of array, call_list)
    def remove_call_in_order(self):
        print "Removing call from beginning of queue"
        self.call_list.pop()
        self.queue_size -= 1 #Queue size decreases
        return self
    # Remove call out of order with queue based on caller number
    def remove_call_with_number(self, number):
        match_found = False
        for call in self.call_list:
            if call.number == number: #matching number found, delete it
                match_found = True
                print "Removing call with number:", number
                self.queue_size -= 1 #Queue size decreases
                self.call_list.remove(call) #Removes call with matching number
        if not match_found:
            print "no caller with number", number, "found..."
        return self
    # Resorts list based on time callers have been here (biggest last in array since that gets removed first)
    def sort_list_with_time(self):
        print self.call_list
        # sort call list in reverse
        new_call_list = sorted(self.call_list, key = lambda call: call.time, reverse=True)
        self.call_list = new_call_list # override old call list
        return self
    # Displays all the calls currently in the queue
    def info(self):
        for call in self.call_list:
            print ""
            print "name of caller:", call.name
            print "phone number:", call.number
            print "length of queue:", self.queue_size
            print call.time
            print ""
        return self

the_callCenter = CallCenter([],0)
the_callCenter.add_call(1,"Jim","206",15,"dont like you").add_call(2,"John","205",10,"dont like you").sort_list_with_time().remove_call_in_order().info()