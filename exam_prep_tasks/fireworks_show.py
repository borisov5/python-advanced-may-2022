from collections import deque


def are_fireworks_enough(fireworks):
    return all(x >= 3 for x in fireworks.values())


def mix_fireworks(firework_effects, explosive_powers):
    firework_effects_queue = deque([x for x in firework_effects if x > 0])
    explosive_powers_stack = [x for x in explosive_powers if x > 0]

    fireworks = {
        'palm': 0,
        'willow': 0,
        'crossette': 0,
    }

    while firework_effects_queue \
            and explosive_powers_stack \
            and not are_fireworks_enough(fireworks):
        firework_effect = firework_effects_queue.popleft()  # firework_effects_queue[0]
        explosive_power = explosive_powers_stack.pop()  # explosive_powers_stack[-1]

        current_sum = firework_effect + explosive_power

        if current_sum % 3 == 0 and current_sum % 5 == 0:
            fireworks['crossette'] += 1
        elif current_sum % 3 == 0:
            fireworks['palm'] += 1
        elif current_sum % 5 == 0:
            fireworks['willow'] += 1
        else:
            #  firework_effect - 1 > 0 => firework_effect > 1
            if firework_effect > 1:
                firework_effects_queue.append(firework_effect - 1)
            explosive_powers_stack.append(explosive_power)

    return (fireworks, firework_effects_queue, explosive_powers_stack)


def print_fireworks(fireworks, firework_effects, explosive_powers):
    if firework_effects:
        print(f'Firework Effects left: {", ".join(str(x) for x in firework_effects)}')
    if explosive_powers:
        print(f'Explosive Power left: {", ".join(str(x) for x in explosive_powers)}')
    print(f'''Palm Fireworks: {fireworks['palm']}
Willow Fireworks: {fireworks['willow']}
Crossette Fireworks: {fireworks['crossette']}
''')


def print_success(fireworks, firework_effects, explosive_powers):
    print(f'Congrats! You made the perfect firework show!')
    print_fireworks(fireworks, firework_effects, explosive_powers)


def print_fail(fireworks, firework_effects, explosive_powers):
    print('Sorry. You can\'t make the perfect firework show.')
    print_fireworks(fireworks, firework_effects, explosive_powers)

# избираме опашка(дек) защото можем да махаме елемент в началото и да добавяме в края
fe = [int(x) for x in input().split(', ')]
# избираме стек защото взимаме елементи само от края
ep = [int(x) for x in input().split(', ')]

(fireworks, remaining_firework_effects, remaining_explosive_powers) = mix_fireworks(fe, ep)

if are_fireworks_enough(fireworks):
    print_success(fireworks, remaining_firework_effects, remaining_explosive_powers)
else:
    print_fail(fireworks, remaining_firework_effects, remaining_explosive_powers)
