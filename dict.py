msg=input(">")
w=msg.split(' ')
output=""
dict={"t":"tommy",
      "sir":"sirsendu"}

#nested_dict={'first':{'a':1},'second':{'b':2}}
for word in w:

    output+=dict.get(word,word)+" "
    #print(dict.get(word))

print(output)
#print(dict.values())
#print(dict.keys())




print('--------------------------------')
print('working with another dictionary ')
print('--------------------------------')


nested_dict={'first':{'a':1},'second':{'b':2}}
print('Dictionary is')
print(nested_dict)
print('values in dictionary are')
for x, y in nested_dict.items():
    print(y)
    for z, w in y.items():

       y.update({z: float(w)})
    nested_dict.update({x: y})
print('updated dictionary is as below')
print(nested_dict)
#dict.update({dict.keys(): dict.values()+'r'})



print('-------------------------------')
print('working with another dictionary')
print('-------------------------------')

dict1={'a':1,'b':2,'c':3,'d':4}
#dict1_even_odd={k:('even' if v%2==0 else 'odd') for (k,v) in dict.items()}
print(dict1)
for ke,val in dict1.items():
    if val%2 ==0:
        val='even'
        dict1.update({ke: val})
    else:
        val='odd'
        dict1.update({ke :val})

print('modified dictionary is')
print(dict1)

print('-------------------------------')
print('working with another dictionary')
print('-------------------------------')

s3_event={
  'Records': [
    {
      'eventVersion': '2.1',
      'eventSource': 'aws:s3',
      'awsRegion': 'us-east-1',
      'eventTime': '2019-08-29T09:33:24.736Z',
      'eventName': 'ObjectCreated:Put',
      'userIdentity': {
        'principalId': 'AWS:AIDA3AW5VFDLLWBDB3TQB'
      },
      'requestParameters': {
        'sourceIPAddress': '54.167.54.94'
      },
      'responseElements': {
        'x-amz-request-id': 'xxxxxxx',
        'x-amz-id-2': 'xxxxxxxxxxxxxx'
      },
      's3': {
        's3SchemaVersion': '1.0',
        'configurationId': '02732f98-e85b-4ac3-8407-b32119d6f300',
        'bucket': {
          'name': 'sqlserverbucket',
          'ownerIdentity': {
            'principalId': 'A180M1JIQI0IZ1'
          },
          'arn': 'arn:aws:s3:::sqlserverbucket'
        },
        'object': {
          'key': 'custrec.json',
          'size': 759,
          'eTag': 'a5f397824aab9c7e546dd5e524574fff',
          'sequencer': '005D679BE4AD361BD6'
        }
      }
    },
    {
      'eventVersion': '2.1',
      'eventSource': 'aws:s3',
      'awsRegion': 'us-east-1',
      'eventTime': '2019-08-29T09:33:24.736Z',
      'eventName': 'ObjectCreated:Put',
      'userIdentity': {
        'principalId': 'AWS:AIDA3AW5VFDLLWBDB3TQB'
      },
      'requestParameters': {
        'sourceIPAddress': '54.167.54.94'
      },
      'responseElements': {
        'x-amz-request-id': 'xxxxxxx',
        'x-amz-id-2': 'xxxxxxxxxxxxxx'
      },
      's3': {
        's3SchemaVersion': '1.0',
        'configurationId': '02732f98-e85b-4ac3-8407-b32119d6f300',
        'bucket': {
          'name': 'sqlserverbucket1',
          'ownerIdentity': {
            'principalId': 'A180M1JIQI0IZ1'
          },
          'arn': 'arn:aws:s3:::sqlserverbucket'
        },
        'object': {
          'key': 'custrec1.json',
          'size': 759,
          'eTag': 'a5f397824aab9c7e546dd5e524574fff',
          'sequencer': '005D679BE4AD361BD6'
        }
      }
    }
  ]

}

print(s3_event)

for x in range(1):
    print(x)
    bucket=s3_event['Records'][x]['s3']['bucket']['name']
    print('s3 bucket name is:')
    print(bucket)
    file_name=s3_event['Records'][x]['s3']['object']['key']
    print('file name is:')
    print(file_name)
