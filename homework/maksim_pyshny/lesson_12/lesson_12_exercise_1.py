class Flowers:
    has_pestle = True
    has_stamen = True

    def __init__(self, name, flower_color, petal_color, petal_count, has_stem):
        self.name = name
        self.flower_color = flower_color
        self.petal_color = petal_color
        self.petal_count = petal_count
        self.has_stem = has_stem


class StemmedFlower(Flowers):
    def __init__(self, name, flower_color, petal_color, petal_count, has_stem, freshness, stem_length, price, lifetime):
        super().__init__(name, flower_color, petal_color, petal_count, has_stem)
        self.freshness = freshness
        self.stem_length = stem_length
        self.price = price
        self.lifetime = lifetime


class Rose(StemmedFlower):
    def __init__(self, name, flower_color, petal_color, petal_count, has_stem, freshness, stem_length, price, lifetime):
        super().__init__(name, flower_color, petal_color, petal_count, has_stem, freshness, stem_length, price,
                         lifetime)


class Peonies(StemmedFlower):
    def __init__(self, name, flower_color, petal_color, petal_count, has_stem, freshness, stem_length, price, lifetime):
        super().__init__(name, flower_color, petal_color, petal_count, has_stem, freshness, stem_length, price,
                         lifetime)


class Chamomile(StemmedFlower):
    def __init__(self, name, flower_color, petal_color, petal_count, has_stem, freshness, stem_length, price, lifetime):
        super().__init__(name, flower_color, petal_color, petal_count, has_stem, freshness, stem_length, price,
                         lifetime)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def cost_bouquet(self):
        total_cost = sum(flower.price for flower in self.flowers)
        print(f'Стоимость букета: {total_cost}')

    def life_time(self):
        life_time_bouquet = sum(flower.lifetime for flower in self.flowers) / len(self.flowers)
        print(f'Среднее время жизни букета: {life_time_bouquet}')

    def sort_bouquet(self, key):
        if key in ['flower_color', 'stem_length', 'price']:
            self.flowers.sort(key=lambda flower: getattr(flower, key))

    def search_flower(self, **kwargs):
        results = self.flowers
        for key, value in kwargs.items():
            results = [flower for flower in results if getattr(flower, key) == value]
        return results


# Создаем цветы
white_rose = Rose('Роза', 'Белый', 'Белый', 20, True,
                  'Fresh', 50, 1000, 4)
red_rose = Rose('Роза', 'Красный', 'Красный', 20,
                True, 'Fresh', 40, 2000, 5)
pink_peonies = Peonies('Пиона', 'Розовая', 'Розовый', 30, True,
                       'Fresh', 45, 1500, 6)
lilac_peonies = Peonies('Пиона', 'Сиреневая', 'Сиреневая', 40, True,
                        'Fresh', 40, 1500, 6)
white_chamomile = Chamomile('Ромашка', 'Белый', 'Белый', 40, True,
                            'Fresh', 20, 500, 7)

# Добавляем цветы в букет
buket_1 = Bouquet()
buket_1.add_flower(white_rose)
buket_1.add_flower(red_rose)
buket_1.add_flower(pink_peonies)
buket_1.add_flower(lilac_peonies)
buket_1.add_flower(white_chamomile)
