class Joke():
	# 일부 값은 None으로 유니온 해도 될까?
	id:str 
	value:str 
	icon_url:str 
	url:str 
	updated_at:str 
	created_at:str
	categories:str 
	def __init__(self, response_dict:dict):
		for arg in ['id','value','categories','icon_url','updated_at','created_at','url']:
			if arg in response_dict:
				self.__setitem__(arg,response_dict[arg])
				pass
			else:
				self.__setitem__(arg,None)

	def __setitem__ (self,k,v):
		setattr(self,k,v)

# None 이 아닌걸 여기서 단언해도 되는지? 물론 실제로는 id 같은건 무조건 있겠지만야도..
# 코드 레벨에서 거르지 않는게 에러라고 생각된다.
class KorJoke():
	id:int
	value:str
	ref_id:str
	score:int
	def __init__(self, response_dict:dict):
		for arg in ['id','value','ref_id','score']:
			if arg in response_dict:
				self.__setitem__(arg,response_dict[arg])
				pass
			else:
				self.__setitem__(arg,None)

	def __setitem__ (self,k,v):
		setattr(self,k,v)
	