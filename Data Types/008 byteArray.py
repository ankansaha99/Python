list=[3,4,6,34]

storage = bytes(list) #0-256

print("\nWhatb should be it ",storage)

print(type (storage))

#ow hae, byte er value change kora jay na
#like jodi storage[1]=5 dei tahole error dibe, bujhcho janpakhi

#Accha Akhon byte Array te ashi

arr=[1,2,3,4,5,6,7]

store=bytearray(arr)

#akhon kintu byte array er majhe value change kora jabe jeta byte a kora jeto na
#like
arr[0]=11

print(arr) #Na bujhte mara khao