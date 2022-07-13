class Joke():
	# 일부 값은 None으로 유니온 해도 될까?
	id:str | None
	value:str | None
	icon_url:str | None
	url:str | None
	updated_at:str | None
	created_at:str | None
	categories:str | None
	def __init__(self, response_dict:dict):
		for arg in ['id','value','categories','icon_url','updated_at','created_at','url']:
			if arg in response_dict:
				self.__setitem__(arg,response_dict[arg])
				pass
			else:
				self.__setitem__(arg,None)

	def __setitem__ (self,k,v):
		setattr(self,k,v)