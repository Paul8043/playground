# Issue: value of __name__

def main():
    print("run as main")
    return

def echo():
    print(f"__name__={__name__}")
    return

echo()

if __name__ == '__main__':
    main()

# Behavior when run as main:
# for VS-Code:    __name__ is "__main__"
# for cq-editor:  __name__ is "temp"
# Behavior when imported be runner.py:
# for VS-Code:    __name__ is "anyscript"
# for cq-editor:  __name__ is "anyscript"
