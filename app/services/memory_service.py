class MemoryService:

    def get_user_memory(self, user_id: str):

        fake_db = {
            "123": [
                "Usuário gosta de viajar",
                "Usuário gosta de trilha", 
                "Se chama Diego, tem 37 anos."
            ]
        }

        return fake_db.get(user_id, [])