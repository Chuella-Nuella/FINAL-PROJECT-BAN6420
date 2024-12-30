class User:
    def _init_(self, user_collection):
        self.user_collection = user_collection

    def create_user_data(self, user_data):
        self.user_collection.insert_one(user_data)  # Insert the user data into MongoDB

    def fetch_all_user(self):
        return self.user_collection.find()  # Fetch all user data from MongoDB

    def update_user_data(self, user_id, update_data):
        self.user_collection.update_one({"_id": user_id}, {"$set": update_data})  # Update user data

    def delete_user_data(self, user_id):
        self.user_collection.delete_one({"_id": user_id})  # Delete user data