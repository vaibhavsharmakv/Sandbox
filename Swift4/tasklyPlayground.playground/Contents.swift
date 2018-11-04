import UIKit


// title, image, , notes, date/time entered, date/time due, priority(high, meduim, low)
//  When entering the date/time due, the user should have the ability to leave it blank (unspecified), select a specific date/time, or indicate that it is to be done immediately. Hint: consult the textbook for a mechanism that allows a variable to take on three different types of values.

class DueDate{
    
    var date:String?=nil
    var unspecified:String? = nil
    var priority:String? = nil
    
    func setDate(setDate:String? = nil,setUnspecified:String?=nil,setPriority:String?=nil ) -> (String?,String?, String?) {
        
        if setDate != nil {
            date = setDate!
            unspecified = nil
            priority = nil
        }
        if setUnspecified != nil {
            date = nil
            unspecified = setUnspecified!
            priority = nil
            
        }
        if setPriority != nil {
            date = nil
            unspecified = nil
            priority = setPriority!
            
        }
        
        return ("A","B","C")
    }
    
    func getDate()->(String?){
        if date == nil {
            if unspecified == nil {
                return (priority)
            }
            else{
                return(unspecified)
            }
        }
        else{
            return date
        }
        
        
    }
    
}

class task {
    
    var titleO : String = ""
    var dateO : Int = 0
    var notesO : String? = ""
    
    func addTask(title:String, date: Int,notes:String? ){
        titleO = title
        dateO = date
        notesO = notes
    
    }
    func printTasl() -> (String, Int, String?) {
        return(titleO, dateO, notesO)
    }
    
}





