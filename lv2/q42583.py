def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_count = len(truck_weights)
    on_bridge = [0] * bridge_length
    after_bridge = []

    while True:
        answer += 1
        passed = on_bridge.pop(0)
        fast_foward = 0
        now_truck = 0
        next_truck = 0

        if passed > 0:
            after_bridge.append(passed)

            if len(after_bridge) >= truck_count:
                break
        
        if len(truck_weights) != 0:
            now_truck = truck_weights[0]
        
            if sum(on_bridge) + now_truck <= weight:
                on_bridge.append(truck_weights.pop(0))
        
        if len(truck_weights) != 0:
            next_truck = truck_weights[0]

        if sum(on_bridge) + next_truck > weight or next_truck == 0:
            while on_bridge[0] == 0:
                on_bridge.pop(0)
                fast_foward += 1

            # print(on_bridge, fast_foward)
            on_bridge = on_bridge + [0] * fast_foward
            answer += fast_foward
            # print(on_bridge)

        print(on_bridge, truck_weights, answer)

    return answer

bridge_length_list = [2, 100, 100]
weight_list = [10, 100, 100]
truck_weights_list = [
    [7,4,5,6],
    [10],
    [10,10,10,10,10,10,10,10,10,10]	
]
for i in range(3):
    print(solution(bridge_length_list[i], weight_list[i], truck_weights_list[i]))