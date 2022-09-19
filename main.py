import basicobj
import count

def main():
    counter = count.Counter()

    obj1 = basicobj.BasicObj(counter)
    obj2 = basicobj.BasicObj(counter)
    print(obj1.GetID())
    print(obj2.GetID())

if __name__ == "__main__":
    main()