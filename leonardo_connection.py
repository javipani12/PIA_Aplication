from leonardo_api import Leonardo

class My_Leonardo():
    def __init__(self, auth_token):
        self.leonardo = Leonardo(auth_token= auth_token)

    def get_user_info(self):
        return self.leonardo.get_user_info()
    
    def image_generation(self, image):
        response = self.leonardo.post_generations(
            prompt= image.prompt,
            num_images= image.num_images,
            model_id= image.model_id,
            width= image.width,
            height= image.height,
            guidance_scale= image.guidance_scale
        )
        
        response_json = self.leonardo.wait_for_image_generation(generation_id= response['sdGenerationJob']['generationId'])
        images = []

        for element in range(0, len(response_json)):
            images.append(response_json[element]['url'])

        return images
    
    