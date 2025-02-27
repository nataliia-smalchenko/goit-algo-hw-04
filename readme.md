# Порівняння алгоритмів сортування

## Результати тестування

Нижче наведені результати виконання алгоритмів сортування для різних списків. Вказаний час виконання в мілісекундах для 10 000 ітерацій.

```
List: [5, 3, 8, 4, 2, 1, 7]
Insertion sort: 0.7234692920173984 10000
Merge iterative sort: 7.371398332994431 10000
Merge recursive sort: 4.620675374986604 10000
Timsort: 0.17211308400146663 10000

List: [1, 2, 4, 5, 7, 8, 9]
Insertion sort: 0.7200276670046151 10000
Merge iterative sort: 7.299064374994487 10000
Merge recursive sort: 4.675493500020821 10000
Timsort: 0.17106229197815992 10000

List: [9, 7, 5, 4, 3, 2, 1]
Insertion sort: 0.7574854999838863 10000
Merge iterative sort: 7.338956624997081 10000
Merge recursive sort: 4.679946541989921 10000
Timsort: 0.20807416600291617 10000

List: [1, 1, 1, 1, 1, 1, 1]
Insertion sort: 0.7331771659955848 10000
Merge iterative sort: 7.332113082986325 10000
Merge recursive sort: 4.62070662502083 10000
Timsort: 0.1721600420132745 10000

List: [93, 56, 32, 15, 14, 5, 5, 9, 17, 33, 26, 71, 33, 19, 34, 85, 53, 66, 82, 95, 61, 41, 3, 55, 26, 34, 75, 63, 8, 45, 73, 28, 38, 60, 77, 39, 93, 91, 30, 21, 72, 93, 10, 26, 55, 17, 48, 50, 96, 96, 59, 18, 83, 94, 8, 19, 73, 56, 99, 73, 15, 95, 15, 73, 16, 82, 31, 89, 17, 23, 38, 51, 7, 14, 87, 45, 4, 76, 63, 29, 20, 80, 74, 60, 12, 88, 93, 78, 30, 56, 59, 85, 75, 88, 73, 83, 41, 58, 36, 64, 66, 67, 51, 14, 99, 27, 69, 81, 16, 76, 53, 34, 24, 58, 78, 75, 50, 43, 12, 81, 80, 8, 22, 67, 10, 27, 79, 8, 60, 84, 3, 25, 95, 93, 85, 43, 72, 6, 19, 59, 31, 85, 95, 33, 59, 57, 15, 80, 2, 40, 84, 37, 46, 73, 27, 45, 67, 50, 6, 66, 19, 93, 57, 27, 35, 63, 64, 37, 96, 86, 44, 15, 6, 48, 60, 83, 57, 40, 58, 16, 13, 36, 62, 54, 35, 13, 33, 40, 24, 37, 46, 71, 55, 62, 53, 43, 20, 45, 96, 96, 43, 62, 13, 2, 60, 58, 78, 64, 5, 20, 11, 65, 22, 24, 51, 89, 36, 31, 36, 91, 21, 77, 92, 18, 32, 4, 10, 7, 59, 16, 35, 53, 52, 67, 57, 1, 47, 77, 36, 63, 97, 45, 100, 55, 85, 99, 9, 97, 54, 82, 1, 99, 76, 34, 6, 88, 56, 71, 89, 39, 63, 10, 65, 30, 91, 61, 68, 19, 85, 82, 18, 75, 92, 98, 53, 43, 90, 69, 78, 91, 89, 54, 66, 6, 76, 88, 44, 14, 50, 56, 64, 3, 57, 23, 80, 38, 37, 90, 23, 22]
Insertion sort: 32.39374470800976 10000
Merge iterative sort: 529.5925474160176 10000
Merge recursive sort: 389.4910268749809 10000
Timsort: 1.8309489579987712 10000
```

## Висновки

Результати експерименту чітко демонструють **перевагу алгоритму Timsort** над іншими розглянутими алгоритмами сортування (сортування вставками та сортування злиттям) у всіх тестових сценаріях.

- **На малих списках (7 елементів):**
  - Timsort показав приблизно **5-кратне прискорення** порівняно з сортуванням вставками.
  - Значно перевершив обидва варіанти сортування злиттям.
- **На великих списках:**
  - Розрив у продуктивності лише збільшився.
  - Timsort став **16 разів швидшим** за сортування вставками.
  - Продемонстрував помітне покращення порівняно з сортуванням злиттям.
  - Це підтверджує ефективність Timsort для сортування великих обсягів даних.
- **Алгоритмічна складність:**
  - Хоча сортування вставками має гіршу алгоритмічну складність (O(n^2)) порівняно з сортуванням злиттям (O(n log n)), реальна кількість операцій впливає на продуктивність.
  - Timsort же поєднує в собі найкращі якості обох цих алгоритмів.
- **Висновок:**
  - Експеримент підтверджує, що **Timsort є найбільш ефективним алгоритмом сортування для реальних сценаріїв**.
