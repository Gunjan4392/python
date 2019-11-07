# Declare file path
file_path = "/usr/local/share/datasets/airports.csv"

# Read in the airports data
airports = spark.read.csv(file_path, header=True)

# Show the data
airports.show()

# Create the DataFrame flights where flights is a table which can be seen by spark.catalog.listTables()
flights = spark.table("flights")

# Add a new column, duration_hrs
flights = flights.withColumn("duration_hrs",flights.air_time/60)
