# TypeTrainer
Project for course of Technologies of Programming and Python course in MIPT

## Содержание
 * [Об игре](#об-игре)
 * [Ход игры](#ход-игры)
 * [Техническая часть](#техническая-часть)
 * [Идеи](#идеи)            
 * [ToDo](#todo)

## Об игре
Игра-тренировка для людей, которые только осваивают десятипальцевый набор. Особенно полезна для детей, так как предлагает научиться печатать быстро и эффективно в формате игры

## Ход игры
"В вашем мире любого врага можно уничтожить, если вы знаете его имя. Древние знания ваших предков позволили вам видеть имена всех ваших врагов. Защитите ваш дом от полчищ гадких тварей, насылая на них потоки заклинаний"
Чтобы уничтожить врага, нужно последовательно ввесьи буквы его имени (заклинание), из которых состоит его имя. На low левелах можно ошибаться в записи, на высоких уровнях приходится после ошибки вводить заклинание заново.
Типы монстров:
 * обычные монстры - средняя длина имени и средняя скорость
 * монстры-матки - имя больше по длине, генерирует маленьких монстров с большими именами, пока живет
 * скоростные монстры, с коротким именем но высокой скоростью
 * боссы - длинные древние имена, сложные для произнесения (длинные, с знаками препинания, капсом). Медленные, но иногда генерируют поток заклинаний в твою сторону (не успеешь остановить - умрешь) или призвать обычного миньона

Враги будут двигать сверху вниз, скорость врагов  варьируется от типа и уровня игры. Враги будут наступать волнами, с каждой волной врагов будет все больше, на каждой 10 босс

## Техническая часть
Для всех основных типов врагов будут создаваться Prototype при запуске
 
## Идеи
Заклинания, которые будут заряжаться от быстрой скорости ввода текста или введения букв подряд без ошибок в течении долгого времени
Как варинт добавить прокачку персонажа, добавить урон у врагов и ХП у персонажа, а также зелья и заклинания для защиты/регена

## ToDo
 * Классы врагов
 * Продумать концепцию из Идей
