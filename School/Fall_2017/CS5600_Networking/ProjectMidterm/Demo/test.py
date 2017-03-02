import os
import math
import filecmp

solution = "test_img.jpg"
img0 = "test_img0.jpg"
img1 = "test_img1.jpg"

# solution = "textsample1.txt"
# img0 = "textsample.txt"
#img1 = "test_img1.jpg"

def sendSegment(identifier, start, end, target):
    pass

def downloadSegment(identifier, start, end, solution):
    with open(solution, 'r+b') as dest:
        with open(identifier, 'rb') as source:
            point0 = start
            steps = int(math.floor((end-start)/1024))

            print "Start: " + str(start)
            print "End: " + str(end)
            print "Length: " + str(end - start)
            print "Steps: " + str(steps)

            for i in range(steps):
                source.seek(point0, 0)
                chunk = source.read(1024)
                dest.seek(point0, 0)
                dest.write(chunk)
                point0 = point0 + 1024

            source.seek(point0, 0)
            chunk = source.read(end-point0)
            dest.seek(point0, 0)
            dest.write(chunk)

def main():
    size = os.path.getsize(img0)
    # with open(solution, "r+b") as f:
    #     f.seek(size-1)
    #     f.write("\0")

    open(solution, 'wb').close()
    #downloadSegment(img0, 0, size, solution)
    #downloadSegment(img0, int(math.floor(size/2)), size, solution)
    #downloadSegment(img0, 0, int(math.floor(size/2)), solution)
    downloadSegment(img0, 0, int(math.floor(size/3)), solution)
    downloadSegment(img0, int(math.floor(size/3)), 2 * int(math.floor(size/3)), solution)
    downloadSegment(img0, 2 * int(math.floor(size/3)), size, solution)
    #dest.close()
    print filecmp.cmp(img0, solution)
    print size
    print os.path.getsize(solution)

if __name__ == "__main__":
    main()
