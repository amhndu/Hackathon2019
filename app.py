import api
import redact
import sys

if __name__ == "__main__":
    print('arg:' , sys.argv[1])
    result = api.processResponse(api.sendRequest(sys.argv[1]))
    print('result: ', result)
    print('redact:', redact.redact(sys.argv[1], result))
