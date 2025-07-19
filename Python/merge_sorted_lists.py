#!/usr/bin/env python3
"""
Function merges 2 sorted lists to produce a single sorted list
"""

def merge_sorted_lists(A, B):
    return sorted(A + B)

    merged_list = []
    i, j = 0, 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged_list.append(A[i])
            i += 1
        else:
            merged_list.append(B[j])
            j += 1

    merged_list.extend(A[i:])
    merged_list.extend(B[j:])

    return merged_list

if __name__ == '__main__':
    A = [1, 2, 3]
    B = [4, 5, 6]

    print(merge_sorted_lists(A, B))
