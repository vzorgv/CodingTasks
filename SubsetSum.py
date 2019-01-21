import numpy as np


def subset_sum(sequence, target):
    T = np.zeros((len(sequence) + 1, target + 1), dtype=int)
    T[:, 0] = 1
    for i, num in enumerate(sequence, start=1):
        for j in range(1, target + 1):
            if j >= num:
                T[i, j] = T[i - 1, j - num] or T[i - 1, j]
            else:
                T[i, j] = T[i - 1, j]
    return T


def subset_sum_solution(sequence, target):
    T = subset_sum(sequence, target)
    n = len(sequence)
    solution = []
    if T[n, target]:
        while n > 0 and target > 0:
            if not T[n-1, target]:
                solution.append(sequence[n-1])
                target -= sequence[n-1]
            n -= 1
    return solution


seq = [764, 525, 956, 903, 149, 85, 936, 745, 217, 50, 968, 110, 200, 752, 150, 927, 171, 194, 607, 915, 373, 590, 828,
       113, 554, 897, 170, 649, 327, 821, 974, 238, 647, 242, 739, 511, 615, 192, 25, 406, 302, 914, 741, 503, 819, 634,
       779, 105, 214, 812, 394, 990, 963, 560, 406, 39, 599, 641, 302, 583, 750, 635, 529, 407, 198, 868, 498, 337, 245,
       596, 972, 951, 767, 917, 532, 80, 592, 318, 725, 178, 861, 943, 266, 190, 93, 107, 627, 257, 719, 632, 731, 88,
       644, 629, 899, 971, 26, 230, 784, 265, 764, 709, 360, 894, 692, 659, 278, 685, 318, 65, 406, 986, 496, 170, 476,
       118, 818, 98, 622, 619, 460, 350, 945, 42, 416, 942, 568, 91, 779, 611, 757, 386, 358, 917, 311, 111, 149, 165,
       923, 558, 636, 749, 952, 165, 472, 687, 723, 734, 26, 89, 598, 108, 788, 234, 444, 270, 875, 239, 553, 144, 165,
       453, 986, 442, 65, 972, 675, 343, 949, 568, 362, 377, 554, 247, 242, 139, 324, 611, 24, 201, 861, 143, 48, 548,
       140, 382, 872, 226, 44, 964, 804, 867, 263, 180, 296, 568, 245, 129, 949, 491, 144, 477, 832, 98, 295, 980, 494,
       441, 153, 225, 922, 740, 110, 19, 104, 639, 993, 238, 57, 742, 558, 119, 77, 470, 220, 56, 72, 260, 574, 957,
       543, 276, 175, 160, 612, 707, 344, 217, 135, 183, 497, 836, 836, 68, 179, 478, 936, 629, 344, 377, 681, 732, 945,
       272, 873, 914, 906, 362, 9, 958, 639, 63, 269, 703, 515, 818, 448, 463, 414, 60, 920, 654, 585, 80, 151, 9, 269,
       416, 825, 190, 16, 363, 618, 266, 261, 966, 821, 25, 597, 713, 994, 860, 473, 856, 297, 820, 228, 952, 668, 582,
       775, 477, 748, 90, 625, 143, 660, 650, 271, 912, 962, 867, 646, 853, 964, 860, 70, 132, 626, 75, 930, 107, 831,
       288, 593, 86, 368, 817, 126, 983, 349, 191, 535, 433, 462, 741, 937, 555, 252, 499, 809, 497, 568, 769, 71, 653,
       183, 46, 848, 752, 157, 801, 877, 75, 789, 149, 156, 109, 394, 202, 958, 362, 183, 500, 771, 368, 389, 811, 553,
       337, 839, 199, 485, 123, 35, 85, 837, 861, 905, 497, 359, 608, 432, 727, 769, 171, 189, 893, 770, 887, 537, 666,
       247, 489, 404, 653, 296, 874, 850, 549, 266, 538, 552, 996, 174, 112, 852, 396, 131, 849, 185, 684, 513, 530,
       618, 899, 117, 278, 992, 379, 485, 962, 739, 862, 817, 687, 710, 511, 232, 64, 227, 900, 833, 31, 498, 539, 354,
       679, 850, 352, 198, 372, 611, 847, 956, 369, 80, 491, 465, 276, 794, 96, 431, 709, 52, 695, 230, 886, 4, 269, 8,
       520, 950, 110, 631, 250, 591, 501, 990, 303, 540, 575, 153, 745, 800, 382, 201, 873, 105, 247, 373, 488, 234,
       978, 361, 939, 148, 424, 910, 921, 211, 23, 456, 337, 763, 795, 385, 275, 673, 30]
target = 3000

print(subset_sum_solution(seq, target))
