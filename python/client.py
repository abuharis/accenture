from requests import put, get, post

ret = get('http://localhost:5000/todos/todo1' )

print ("GET(): {}".format(ret.status_code, ret.text))




#ret = post('http://localhost:5000/todos', data={'task':'cooltask'} )

#print ("POST(()) :{}".format(ret.status_code, ret.text))


ret = put('http://localhost:5000/todos/todo10',data={'task':'something cool'})
print("PUT(()):{}".format(ret.status_code, ret.json()))


ret = delete('http://localhost:5000/todos/todo1' )

print ("DELETE(): {}".format(ret.status_code, ret.text))

