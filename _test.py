from mivmodules import utils

eval_go = utils.Utils()


print(eval_go.generate_password_sync(length=10, digits=False))