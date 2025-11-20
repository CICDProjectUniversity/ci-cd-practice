import unittest
from app import add, subtract, multiply

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        """Тест функции сложения"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract(self):
        """Тест функции вычитания"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(10, 10), 0)
    
    def test_multiply(self):
        """Тест функции умножения"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(-2, 3), -6)

if __name__ == '__main__':
    unittest.main()
```

4. Commit message: `Добавлены тесты`
5. Нажми **Commit new file**

## Шаг 5: Создание requirements.txt

1. **Add file** → **Create new file**
2. Имя файла: `requirements.txt`
3. Содержимое:
```
pytest==7.4.3
