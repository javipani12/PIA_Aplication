import user_interaction as ui
import leonardo_connection as lc
import credentials as cs
from image import Image
import json
#ui.test()
my_leonardo = lc.My_Leonardo(cs.Credentials.LEONARDO)
user_info = my_leonardo.get_user_info()
user_id = user_info["user_details"][0]["user"]["id"]
print(user_id)

'''my_image = Image("A blonde girl with brilliant long hair, blue eyes. The face must be the more beautiful that have never existed."+
                 "She is wearing a top with jeans. Her body estructure is like a top model.",
                 num_images= 4,
                 model_id= user_id,
                 width= 1024,
                 height= 768,
                 guidance_scale= 7)

lista_imagenes = my_leonardo.image_generation(my_image)'''