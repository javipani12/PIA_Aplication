# Library which allow us to connect with Leonardo AI for image
# generations.
from leonardo_api import Leonardo


class My_Leonardo():
    '''
    All methods created in this class have been obtained from 
    this website: https://pypi.org/project/leonardo-api/
    '''

    def __init__(self, auth_token):
        '''
        Here it is created an object with leonardo ai connection
        using the token given by Leonardo AI.
        '''
        self.leonardo = Leonardo(auth_token=auth_token)

    def get_user_info(self):
        """
        Function to get the Leonardo user information

        :return: (Dict) All the information about the user
        """
        return self.leonardo.get_user_info()

    def image_generation(self, prompt):
        """
        This function is used to generate an image on Leonardo based on a prompt

        :param prompt: (String) The text to generate the image
        :return: (String) URL of the generated image
        """
        print("Generating the image with Leonardo...")
        try:
            response = self.leonardo.post_generations(
                prompt=prompt,
                num_images=1,
                model_id='e316348f-7773-490e-adcd-46757c738eb7',
                width=1024,
                height=1024,
                guidance_scale=7
            )
            image_id = response['sdGenerationJob']['generationId']
            response_image = self.leonardo.wait_for_image_generation(image_id)
            image_route = response_image['url']
            print("Image generated successfully...")
        except Exception as ex:
            print("An error occurred", ex)
            exit()
        return image_route
