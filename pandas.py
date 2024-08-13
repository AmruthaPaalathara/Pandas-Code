class m_pandas:

    def __init__(self,file_name):
        self.file = file_name
        self.data = []

        with open (self.file) as file:
            read_file = file.readlines()
            self.data = read_file

    def m_head(self,num_rows = 5): #to print the first 5 rows.
            lines = self.data[:num_rows + 1] #printing the first 5 rows of the file.
            row_lines = []
            for line in lines:
                stripped_lines = line.strip() #removes whitespaces
                split_lines = stripped_lines.split(",") #splitting with ",".
                row_lines.append(split_lines) #appending the splitted line to the list.
            
            return row_lines
        
    def m_tail(self,tail_rows = 5):
            lines = self.data[len(self.data) - tail_rows:]
            row_lines = []
            for line in lines:
                stripped_lines = line.strip()
                split_lines = stripped_lines.split(",")
                row_lines.append(split_lines)

            return row_lines
        
    def m_columns(self):
            data = self.data
            read_first_line = data[0:1]
            for line in read_first_line:
                column_list =[]
                strip_split_line = line.strip().split(",")
                column_list.append(strip_split_line)
        
            return column_list
        
    def m_to_numpy(self):
            data = self.data
            to_numpy_line = data[1:]
            to_numpy_list = []
            for line in to_numpy_line:
                strip_split_rows = line.strip().split()
                to_numpy_list.append(strip_split_rows)

            return to_numpy_list
    
    def m_describe(self):
        data= self.data
        _describe = data[1:]
        count = 0
        sum = 0

        for no_items in _describe:
            strip_items = no_items.strip()
            count = count + 1
        return print("Count: ",count)
        

        for item in _describe:
             