class Image:
    def __init__(self, prompt, num_images, model_id, width, height, guidance_scale):
        self.prompt = prompt
        self.num_images = num_images
        self.model_id = model_id
        self.width = width
        self.height = height
        self.guidance_scale = guidance_scale

    @property
    def prompt(self):
        return self.prompt
    
    def prompt(self, new_prompt):
        self.prompt = new_prompt

    @property
    def num_images(self):
        return self.num_images
    
    def num_images(self, new_num_images):
        self.num_images = new_num_images

    @property
    def model_id(self):
        return self.model_id
    
    def model_id(self, new_model_id):
        self.model_id = new_model_id

    @property
    def width(self):
        return self.width
    
    def width(self, new_width):
        self.width = new_width

    @property
    def height(self):
        return self.height
    
    def height(self, new_height):
        self.height = new_height

    @property
    def guidance_scale(self):
        return self.pguidance_scalerompt
    
    def guidance_scale(self, new_guidance_scale):
        self.guidance_scale = new_guidance_scale