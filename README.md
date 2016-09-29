# day_repr
noteddddd my learn 

-2016-
      -9-
          -29-
		  	*python*
				1. global 全局变量 在 python函数 中 声明 才是全局
				
				gao = True																gao = True
				def show_a():															def show_a():
					print gao																print gao

				def show_b():															def show_b():
					global gao																gao = False
					gao = False																print gao
					print gao

				def main():																def main():
					show_a()																show_a()
					show_b()																show_b()
					show_a()																show_a()
				
				ouput>>> True															output>>>True
						 False																	 False
						 False																	 True
	
		  		2.threading 使用 Thread() example 2016.9.29-threading
			
			*sublime*
				1. sublime-快捷键
			
			
