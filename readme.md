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

List: [великий список із 200 елементів]
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
