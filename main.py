from random import randint


class BobineColor:
    def __init__(self, name):
        self.name = name


class BobineLaize:
    def __init__(self, width):
        self.width = width


class Bobine:
    def __init__(self, laize, color):
        self.laize = laize
        self.color = color


class BobineStock:
    def __init__(self, bobine, vente, stock_terme):
        self.bobine = bobine
        self.vente = vente
        self.stock_terme = stock_terme

    def __str__(self):
        return 'BobineStock({}, vente={}, stock_terme={})'.format(self.bobine, self.vente, self.stock_terme)

bobine_color_red = BobineColor('red')
bobine_laize = BobineLaize(140)
bobine = Bobine(laize=bobine_laize, color=bobine_color_red)
bobine_stock_1 = BobineStock(bobine, vente=10000, stock_terme=15)
print(bobine_stock_1)




POP = 1000
NOMBRE_PLAN_PRODUCTION = 10
NOMBRE_BOB_PAR_PROD = 31
REFENTE = [150, 140, 140, 140, 140, 150]

r140_u = {"color": "r", "laize": 140, "vente": 10000, "stock_terme": 15}
r140_n = {"color": "r", "laize": 140, "vente": 5000, "stock_terme": -5}
r150_i = {"color": "r", "laize": 150, "vente": 600, "stock_terme": 2}
r150_n = {"color": "r", "laize": 150, "vente": 400, "stock_terme": 20}
b140_n = {"color": "b", "laize": 140, "vente": 2000, "stock_terme": -80}
b140_u = {"color": "b", "laize": 140, "vente": 4000, "stock_terme": -200}
b150_u = {"color": "b", "laize": 150, "vente": 50, "stock_terme": 0}
b150_i = {"color": "b", "laize": 150, "vente": 400, "stock_terme": 50}
e140_i = {"color": "e", "laize": 140, "vente": 500, "stock_terme": 10}
e140_n = {"color": "e", "laize": 140, "vente": 400, "stock_terme": 200}
e150_c = {"color": "e", "laize": 150, "vente": 200, "stock_terme": 50}
e150_n = {"color": "e", "laize": 150, "vente": 420, "stock_terme": -5}
n140_c = {"color": "n", "laize": 140, "vente": 45, "stock_terme": 4}
n140_n = {"color": "n", "laize": 140, "vente": 140, "stock_terme": 15}
n150_c = {"color": "n", "laize": 150, "vente": 45, "stock_terme": 58}
n150_n = {"color": "n", "laize": 150, "vente": 45, "stock_terme": -12}

init_list_bob = [r140_u, r140_n, r150_i, r150_n, b140_n, b140_u, b150_u, b150_i, e140_i, e140_n, e150_c, e150_n, n140_c, n140_n, n150_c, n150_n]


def insert(bob, plan_prod):
    index_laize = 0
    for laize in REFENTE:
        if not plan_prod[index_laize] and laize == bob["laize"]:
            if randint(0, 1) == 1:
                plan_prod[index_laize] = bob
        index_laize += 1


def len_plan_prod(plan_prod):
    count = 0
    for i in plan_prod:
        if i:
            count += 1
    return count


def create_prod():
    prod = [None, None, None, None, None, None]
    color = None

    while len_plan_prod(prod) < len(prod):
        if not color:
            bob = init_list_bob[randint(0, len(init_list_bob)-1)]
            color = bob["color"]
        else:
            while 1:
                bob = init_list_bob[randint(0, len(init_list_bob)-1)]
                if color == bob["color"]:
                    break
        insert(bob, prod)
    return prod


def update_stock(new_list_bob, bob):
    for current_bob in new_list_bob:
        if current_bob == bob:
            current_bob["stock_terme"] += NOMBRE_BOB_PAR_PROD
    return new_list_bob


def new_list_bob(plan_prod):
    import copy
    new_list_bob = copy.deepcopy(init_list_bob)
    for prod in plan_prod:
        for bob in prod:
            update_stock(new_list_bob, bob)
    return new_list_bob


def get_fitness(plan_prod):
    return sum(t["stock_terme"]/t["vente"] for t in new_list_bob(plan_prod))


def create_plan_prod():
    plan_prod = []
    while len(plan_prod) < NOMBRE_PLAN_PRODUCTION:
        plan_prod.append(create_prod())
    fitness = get_fitness(plan_prod)
    return fitness, plan_prod


generation = []
while len(generation) < POP:
    generation.append(create_plan_prod())
print(generation)

