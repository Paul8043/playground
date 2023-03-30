# Issue: value of __name__

print(f"__name__ is {__name__}")

if __name__ == '__main__':
    print("running as main")

# Behavior when run as main:
# for VS-Code:    __name__ is "__main__"
# for cq-editor:  __name__ is "temp"
# Behavior when imported be runner.py:
# for VS-Code:    __name__ is "whoami"
# for cq-editor:  __name__ is "whoami"
