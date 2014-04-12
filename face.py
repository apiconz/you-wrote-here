import facebook
graph = facebook.GraphAPI("CAACEdEose0cBACslRV8vdQvCturrjPL0yJirVDqANxgrJ3RdCdQvLIzT33YgZAH3pEwqC8B3tuzvmYnHap2i74kvRPVu8X5VOmfm4MbWyHuJjssZCLO7uVAyfBMYZCJJJk6xZC3JbqZBK2qGHXKFdn3jFE8vXRdiCRGnpAe8BIJI24h8YJU7lsaZAWFV0s1vsZD")
profile = graph.get_object("me")
#friends = graph.get_connections("me", "friends")
graph.put_object("me", "feed", message="Estoy escribiendo en mi muro desde una rutina en Python y con el Facebook SDK!")