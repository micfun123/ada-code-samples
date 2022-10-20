# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


def read_csv():
    """Read and display the records from a CSV file"""
    file_object = open("movies.csv", mode="r")
    for record in file_object:
       movie_data = record.split(",")
       title = movie_data[0]
       rating = movie_data[4]
       print(f"Movie name: {title}, Rating: {rating}")
    file_object.close()


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    read_csv()
