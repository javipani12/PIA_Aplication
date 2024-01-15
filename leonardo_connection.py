from leonardo_api import Leonardo


class My_Leonardo():
    def __init__(self, auth_token):
        self.leonardo = Leonardo(auth_token= auth_token)

    def get_user_info(self):
        return self.leonardo.get_user_info()
    
    def image_generation(self, prompt):
        response = self.leonardo.post_generations(
            prompt= prompt,
            num_images= 1,
            model_id= 'e316348f-7773-490e-adcd-46757c738eb7',
            width= 1024,
            height= 1024,
            guidance_scale= 7
        )

        image_id = response['sdGenerationJob']['generationId']
        response_image = self.leonardo.wait_for_image_generation(image_id)        
        print(response_image)
        image_route = response_image['url']

        return image_route
