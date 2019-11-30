try:
    a=int(input())
except ValueError as e:
    print("ValueError",e)
except EOFError as e:
    print("EOFError",e)
except KeyboardInterrupt as e:
    print("KeyboardInterrupt",e)
