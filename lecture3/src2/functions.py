def square(x):
    return x * x


def main():
	for i in range(10):
	    print("{} squared is {}".format(i, square(i)))

	print("\n")

	for i in range(10):
	    print(f"{i} squared is {square(i)}")

	print("\n")

	print(__name__)

if __name__ == "__main__":
	main()