# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import cv2

# construct
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

cd = ColorDescriptor((8,12,3))

# load the 
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform
searcher = Searcher(args["index"])
results = searcher.search(features)

# display
cv2.imshow("Query", query)

# loop
for (score, resultID) in results:
	# load
	result = cv2.imread(args["result_path"]+"/"+resultID)
	cv2.imshow("Result",result)
	cv2.waitKey(0)
