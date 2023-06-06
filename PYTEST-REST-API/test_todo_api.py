#allow us to interact w http directly from python
import requests

ENDPOINT = "https://todo.pixegami.io/"

#will return a response object
'''response = requests.get(ENDPOINT)

print(response)

#print("Hello")

#http response contains quite a bit of info, response body: json data
data = response.json()
print(data)

#status code useful for testing
#returned as integer which we can use to verify if API is working
status_code = response.status_code
print(status_code) '''

#Test for pytest, a function
#check that call is successful
def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    #if true, passes, if false, throws exception and test fails
    assert response.status_code == 200
    pass

def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert  create_task_response.status_code == 200

    data =  create_task_response.json()
    #print(data)

    #task object in response payload
    task_id = data["task"]["task_id"]

    #call get endpoint
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    #print(get_task_data)

    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

    #test if can update item
def test_can_update_task():

        #create a task
        payload = new_task_payload()
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200
        task_id = create_task_response.json()["task"]["task_id"]

        #update the task
        new_payload = {
            "user-id" : payload["user_id"],
            #task_id is generated by the server each time 
            "task_id" : task_id,
            "content" : "completed",
            "is_done" : True,
        }

        update_task_response = update_task(new_payload)
        assert update_task_response.status_code == 200

        #get and validate the changes
        get_task_response = get_task(task_id)
        assert get_task_response.status_code == 200
        get_task_data = get_task_response.json()
        assert get_task_data["content"] == new_payload["content"]
        assert get_task_data["is_done"] == new_payload["is_done"] 
        pass

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def new_task_payload():
  return  {
        "content": "drink water",
        "user_id": "jclima",
        "task_id": "123",
        "is_done": False,
    }   