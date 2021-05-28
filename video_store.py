import requests
import datetime

class VideoStore:

    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_customer=None, selected_video=None):
        self.url = url
        self.selected_customer = selected_customer
        self.selected_video = selected_video
    
    # Option 1: add a video
    def add_video(self,title,release_date,total_inventory):

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()  
    
    # Option 2: edit a video 
    def update_video(self,video_id,title=None,release_date=None,total_inventory=None):

        if not title: 
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]   

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
        }
        response = requests.put(
            self.url+f"/videos/{video_id}",
            json=query_params
            )
        print("response:", response)
        self.selected_video = response.json()
        return response.json()
    
    # Option 3: delete a video 
    def delete_video(self, id):
        response = requests.delete(self.url+f"/videos/{id}")
        return response.json()

    # Option 4: get information about all videos
    def list_all_videos(self):
        response = requests.get(self.url+"/videos") 
        return response.json()
    
    # Option 5: get information about one video
    def get_video(self, id):
        response = requests.get(self.url+f"/videos/{id}")
        self.video = response.json()
        return response.json()

    # Option 11: check out a video to a customer
    def checkout_video_to_customer(self, customer_id, video_id,):
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-out", json=request_body)
        return response

    # Option 12: check in a video from a customer
    def checkin_video_from_customer(self, customer_id, video_id):
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-in", json=request_body)
        return response