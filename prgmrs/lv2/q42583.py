def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_count = len(truck_weights)
    on_bridge = [0] * bridge_length
    after_bridge = []
    sum_bridge = 0
    head, tail = 0, 0

    while len(after_bridge) != truck_count:
        if len(truck_weights) != 0:
            tail = truck_weights[0]

        else:
            tail = 0

        if sum_bridge + tail > weight or tail == 0:
            while on_bridge[0] == 0:
                on_bridge.pop(0)
                on_bridge.append(0)
                answer += 1

        answer += 1
        head = on_bridge.pop(0)
        
        if head != 0:
            after_bridge.append(head)
            sum_bridge -= head
        
        if sum_bridge + tail <= weight and tail != 0:
            on_bridge.append(truck_weights.pop(0))
            sum_bridge += tail

        else:
            on_bridge.append(0)
        
        # print(after_bridge, on_bridge, truck_weights, answer)

    return answer

# bridge_length_list = [2, 100, 100]
# weight_list = [10, 100, 100]
# truck_weights_list = [
#     [7,4,5,6],
#     [10],
#     [10,10,10,10,10,10,10,10,10,10]	
# ]
# for i in range(3):
#     print(solution(bridge_length_list[i], weight_list[i], truck_weights_list[i]))