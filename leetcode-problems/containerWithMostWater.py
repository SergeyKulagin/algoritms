from typing import List

from util.util import rand_array
import time


class Solution:
    # linear speed
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left_idx = 0
        right_idx = len(heights) - 1
        while left_idx < right_idx:
            x_len = right_idx - left_idx
            left_y = heights[left_idx]
            right_y = heights[right_idx]
            y_len = min(left_y, right_y)
            area = x_len * y_len
            max_area = area if area > max_area else max_area
            if left_y < right_y:
                left_idx += 1
            elif right_y < left_y:
                right_idx -= 1
            else:  # both equal
                if left_idx + 1 < right_idx - 1:
                    if heights[left_idx + 1] <= heights[right_idx - 1]:
                        # if both equal choose left (just by convention)
                        left_idx += 1
                    else:
                        right_idx -= 1
                else:
                    left_idx += 1

        return max_area

    # quadratic speed
    def maxAreaSlowButCorrect(self, heights: List[int]) -> int:
        idx = 0
        max_area = 0
        max_height = 0
        left_heights = []
        while idx < len(heights):
            height = heights[idx]
            j = 0
            while j < len(left_heights):
                x_len = idx - left_heights[j][0]
                area = min(height, left_heights[j][1]) * x_len
                max_area = area if area > max_area else max_area
                j += 1
            if height > max_height:
                # tuple - index (to calculated x length) and height
                left_heights.append((idx, height))
                max_height = height
            idx += 1
        return max_area

    def maxAreaPrint(self, heights: List[int]) -> int:
        print(heights)
        expected_area = self.maxAreaSlowButCorrect(heights)
        current_area = self.maxArea(heights)
        assert expected_area == current_area, f"Not expected, expected = {expected_area}, current = {current_area}"
        #print(f"max_area={current_area}");


# test cases
s = Solution()

# other tests
s.maxAreaPrint([1, 8, 6, 2, 5, 4, 8, 3, 7])
s.maxAreaPrint([1, 5, 1, 5])
s.maxAreaPrint([1, 5, 10, 10, 10, 20])
s.maxAreaPrint([1])
s.maxAreaPrint([])
s.maxAreaPrint([1, 8, 6, 2, 5, 4, 8, 3, 7])
s.maxAreaPrint([100, 75, 100, 36, 99, 15, 15, 58, 87, 67])
s.maxAreaPrint([52, 14, 27, 94, 97, 12, 13, 42, 96, 42])
s.maxAreaPrint([15, 72, 14, 74, 98, 23, 43, 71, 44, 95])
s.maxAreaPrint([52, 67, 41, 52, 62, 88, 72, 29, 13, 92])
s.maxAreaPrint([80, 53, 63, 63, 60, 7, 15, 51, 21, 35])
s.maxAreaPrint([22, 36, 89, 43, 99, 81, 0, 57, 83, 3])
s.maxAreaPrint([57, 50, 23, 28, 61, 10, 63, 3, 86, 63])
s.maxAreaPrint([94, 57, 3, 93, 21, 54, 16, 71, 58, 73])
s.maxAreaPrint([23, 54, 28, 3, 26, 70, 79, 82, 63, 88])
s.maxAreaPrint([71, 56, 23, 23, 99, 43, 94, 82, 50, 30])
s.maxAreaPrint([14, 48, 65, 5, 54, 85, 18, 100, 72, 44])
s.maxAreaPrint([75, 72, 33, 48, 90, 28, 43, 68, 43, 41])
s.maxAreaPrint([72, 81, 23, 87, 45, 13, 69, 31, 7, 1])
s.maxAreaPrint([73, 34, 49, 87, 72, 9, 68, 72, 51, 34])
s.maxAreaPrint([14, 91, 12, 32, 42, 43, 52, 76, 4, 95])
s.maxAreaPrint([96, 17, 39, 88, 79, 2, 2, 52, 24, 60])
s.maxAreaPrint([35, 37, 40, 10, 83, 63, 86, 85, 4, 66])
s.maxAreaPrint([64, 81, 1, 34, 11, 79, 25, 30, 17, 50])
s.maxAreaPrint([89, 67, 82, 9, 99, 42, 29, 42, 77, 27])
s.maxAreaPrint([65, 96, 67, 49, 86, 94, 50, 61, 73, 41])
s.maxAreaPrint([8, 36, 33, 100, 45, 17, 37, 19, 53, 5])
s.maxAreaPrint([11, 66, 43, 41, 88, 63, 37, 4, 37, 49])
s.maxAreaPrint([5, 92, 59, 15, 7, 1, 35, 7, 29, 16])
s.maxAreaPrint([9, 51, 55, 29, 1, 59, 96, 65, 67, 41])
s.maxAreaPrint([31, 54, 21, 6, 5, 45, 36, 99, 17, 99])
s.maxAreaPrint([58, 100, 12, 38, 68, 45, 50, 82, 87, 41])
s.maxAreaPrint([72, 71, 42, 76, 41, 78, 93, 81, 25, 71])
s.maxAreaPrint([94, 78, 59, 50, 73, 93, 90, 83, 56, 20])
s.maxAreaPrint([51, 59, 51, 92, 91, 44, 9, 9, 21, 53])
s.maxAreaPrint([12, 86, 64, 15, 15, 87, 37, 45, 61, 9])
s.maxAreaPrint([75, 80, 51, 25, 42, 88, 94, 84, 19, 37])
s.maxAreaPrint([42, 84, 17, 48, 23, 100, 42, 83, 86, 6])
s.maxAreaPrint([45, 67, 2, 34, 99, 72, 50, 26, 64, 65])
s.maxAreaPrint([0, 93, 24, 21, 32, 15, 25, 79, 72, 31])
s.maxAreaPrint([65, 62, 92, 24, 43, 28, 51, 52, 35, 96])
s.maxAreaPrint([92, 12, 99, 9, 94, 41, 53, 27, 68, 53])
s.maxAreaPrint([22, 51, 59, 76, 83, 41, 27, 28, 51, 96])
s.maxAreaPrint([43, 50, 53, 56, 88, 98, 33, 49, 59, 51])
s.maxAreaPrint([87, 45, 42, 40, 34, 56, 45, 12, 69, 27])
s.maxAreaPrint([14, 10, 91, 2, 25, 7, 20, 18, 100, 67])
s.maxAreaPrint([98, 41, 17, 61, 27, 99, 57, 76, 78, 54])
s.maxAreaPrint([7, 60, 12, 70, 9, 90, 7, 83, 48, 63])
s.maxAreaPrint([16, 0, 18, 45, 56, 57, 76, 34, 67, 72])
s.maxAreaPrint([35, 94, 58, 86, 21, 95, 68, 42, 97, 43])
s.maxAreaPrint([20, 18, 53, 17, 22, 90, 12, 77, 76, 32])
s.maxAreaPrint([90, 43, 66, 31, 78, 84, 3, 49, 78, 35])
s.maxAreaPrint([25, 90, 52, 64, 2, 97, 60, 23, 66, 63])
s.maxAreaPrint([48, 79, 82, 30, 44, 86, 46, 13, 46, 20])
s.maxAreaPrint([31, 28, 1, 79, 60, 68, 48, 12, 61, 22])
s.maxAreaPrint([44, 100, 63, 71, 39, 91, 77, 67, 77, 51])
s.maxAreaPrint([28, 40, 29, 32, 44, 65, 19, 97, 47, 58])
s.maxAreaPrint([17, 2, 27, 27, 77, 72, 60, 30, 25, 76])
s.maxAreaPrint([63, 41, 63, 79, 92, 60, 20, 13, 56, 81])
s.maxAreaPrint([87, 5, 57, 92, 40, 1, 58, 56, 94, 27])
s.maxAreaPrint([39, 12, 61, 79, 71, 91, 9, 61, 85, 41])
s.maxAreaPrint([61, 35, 75, 65, 78, 8, 31, 17, 67, 39])
s.maxAreaPrint([20, 84, 85, 62, 29, 83, 79, 51, 36, 38])
s.maxAreaPrint([36, 36, 28, 61, 59, 30, 31, 55, 64, 69])
s.maxAreaPrint([30, 74, 1, 51, 23, 16, 43, 94, 77, 79])
s.maxAreaPrint([49, 77, 38, 87, 40, 99, 77, 42, 24, 77])
s.maxAreaPrint([72, 27, 72, 88, 29, 57, 1, 58, 89, 34])
s.maxAreaPrint([55, 42, 29, 82, 33, 58, 15, 44, 16, 58])
s.maxAreaPrint([42, 42, 92, 49, 94, 8, 12, 41, 5, 2])
s.maxAreaPrint([6, 49, 34, 55, 48, 76, 13, 50, 51, 78])
s.maxAreaPrint([26, 29, 89, 38, 37, 62, 25, 75, 38, 9])
s.maxAreaPrint([63, 22, 87, 81, 67, 67, 57, 6, 94, 86])
s.maxAreaPrint([39, 22, 11, 12, 15, 12, 70, 9, 63, 18])
s.maxAreaPrint([66, 85, 39, 57, 8, 34, 3, 56, 65, 35])
s.maxAreaPrint([58, 39, 2, 32, 95, 76, 52, 6, 76, 1])
s.maxAreaPrint([70, 4, 78, 18, 63, 41, 53, 53, 62, 81])
s.maxAreaPrint([77, 60, 7, 89, 56, 35, 83, 46, 65, 5])
s.maxAreaPrint([3, 1, 9, 53, 87, 53, 8, 55, 73, 92])
s.maxAreaPrint([92, 42, 65, 72, 94, 53, 17, 48, 44, 50])
s.maxAreaPrint([63, 62, 5, 39, 68, 25, 98, 2, 62, 57])
s.maxAreaPrint([25, 70, 15, 13, 75, 31, 41, 87, 45, 69])
s.maxAreaPrint([20, 100, 63, 93, 63, 90, 31, 87, 98, 51])
s.maxAreaPrint([63, 9, 34, 40, 51, 89, 44, 91, 82, 44])
s.maxAreaPrint([48, 78, 38, 29, 6, 86, 53, 60, 46, 8])
s.maxAreaPrint([64, 2, 84, 64, 68, 11, 62, 65, 81, 76])
s.maxAreaPrint([7, 36, 70, 29, 45, 13, 12, 66, 73, 69])
s.maxAreaPrint([2, 82, 15, 44, 72, 13, 47, 100, 5, 38])
s.maxAreaPrint([28, 6, 45, 64, 52, 97, 11, 13, 66, 91])
s.maxAreaPrint([25, 62, 95, 24, 57, 34, 47, 1, 52, 47])
s.maxAreaPrint([97, 93, 46, 6, 24, 13, 55, 16, 17, 20])
s.maxAreaPrint([41, 13, 53, 82, 56, 71, 86, 86, 98, 65])
s.maxAreaPrint([37, 13, 80, 65, 69, 43, 67, 44, 99, 67])
s.maxAreaPrint([8, 69, 52, 12, 88, 68, 36, 15, 35, 12])
s.maxAreaPrint([56, 96, 97, 19, 91, 54, 54, 48, 33, 0])
s.maxAreaPrint([19, 25, 60, 70, 65, 21, 79, 70, 56, 42])
s.maxAreaPrint([98, 94, 16, 76, 48, 14, 98, 71, 47, 67])
s.maxAreaPrint([57, 92, 56, 44, 0, 93, 61, 29, 54, 31])
s.maxAreaPrint([3, 2, 69, 10, 32, 28, 92, 19, 55, 57])
s.maxAreaPrint([37, 7, 8, 38, 18, 3, 25, 55, 71, 71])
s.maxAreaPrint([90, 1, 30, 98, 18, 60, 80, 98, 59, 13])
s.maxAreaPrint([6, 36, 49, 65, 93, 77, 100, 52, 79, 96])
s.maxAreaPrint([58, 49, 96, 64, 47, 13, 75, 64, 48, 24])
s.maxAreaPrint([4, 7, 74, 30, 68, 12, 98, 27, 69, 43])
s.maxAreaPrint([31, 47, 49, 59, 40, 0, 29, 100, 54, 37])
s.maxAreaPrint([98, 92, 15, 91, 58, 35, 42, 13, 31, 26])
s.maxAreaPrint([0, 22, 13, 93, 51, 86, 43, 82, 12, 1])
s.maxAreaPrint([371, 164, 897, 366, 830, 311, 231, 958, 174, 225])
s.maxAreaPrint([128, 285, 697, 873, 898, 572, 474, 289, 986, 896])
s.maxAreaPrint([86, 236, 506, 795, 717, 46, 357, 822, 820, 773])
s.maxAreaPrint([209, 25, 223, 174, 422, 394, 380, 132, 859, 256])
s.maxAreaPrint([353, 739, 778, 445, 840, 153, 216, 558, 181, 362])
s.maxAreaPrint([321, 765, 387, 701, 31, 753, 981, 884, 937, 850])
s.maxAreaPrint([306, 562, 554, 909, 666, 540, 196, 10, 64, 346])
s.maxAreaPrint([655, 906, 995, 508, 827, 573, 75, 871, 60, 452])
s.maxAreaPrint([548, 831, 764, 78, 763, 636, 538, 81, 672, 863])
s.maxAreaPrint([383, 323, 541, 160, 562, 222, 666, 480, 488, 674])
s.maxAreaPrint([93, 595, 369, 799, 518, 891, 658, 196, 906, 104])
s.maxAreaPrint([623, 647, 435, 326, 895, 779, 903, 328, 821, 812])
s.maxAreaPrint([822, 866, 970, 61, 726, 201, 714, 600, 961, 574])
s.maxAreaPrint([180, 486, 708, 375, 235, 863, 306, 676, 180, 315])
s.maxAreaPrint([336, 536, 190, 423, 98, 19, 129, 236, 351, 578])
s.maxAreaPrint([953, 659, 9, 315, 404, 545, 387, 468, 269, 38])
s.maxAreaPrint([293, 117, 273, 763, 621, 817, 462, 760, 589, 751])
s.maxAreaPrint([693, 333, 127, 316, 772, 888, 576, 831, 438, 553])
s.maxAreaPrint([239, 800, 124, 419, 199, 91, 258, 796, 498, 962])
s.maxAreaPrint([283, 43, 283, 728, 232, 966, 281, 707, 62, 250])
s.maxAreaPrint([701, 608, 357, 488, 527, 576, 498, 101, 150, 370])
s.maxAreaPrint([434, 12, 727, 621, 223, 464, 428, 272, 829, 162])
s.maxAreaPrint([796, 777, 824, 788, 567, 978, 511, 298, 718, 771])
s.maxAreaPrint([479, 877, 571, 871, 772, 160, 496, 267, 872, 140])
s.maxAreaPrint([597, 696, 990, 825, 431, 278, 701, 702, 745, 637])
s.maxAreaPrint([615, 354, 429, 911, 339, 996, 86, 415, 870, 815])
s.maxAreaPrint([348, 819, 557, 977, 83, 106, 655, 322, 477, 624])
s.maxAreaPrint([511, 917, 992, 276, 862, 444, 986, 606, 53, 514])
s.maxAreaPrint([86, 565, 826, 144, 317, 475, 784, 716, 49, 419])
s.maxAreaPrint([362, 946, 324, 972, 552, 958, 188, 614, 155, 205])
s.maxAreaPrint([28, 773, 987, 446, 283, 499, 635, 398, 491, 549])
s.maxAreaPrint([12, 678, 662, 198, 156, 817, 237, 640, 556, 392])
s.maxAreaPrint([58, 592, 212, 296, 418, 625, 55, 272, 420, 102])
s.maxAreaPrint([327, 934, 453, 648, 752, 76, 718, 624, 9, 785])
s.maxAreaPrint([684, 322, 673, 104, 287, 761, 730, 365, 150, 971])
s.maxAreaPrint([799, 405, 800, 306, 895, 683, 808, 292, 731, 726])
s.maxAreaPrint([243, 828, 277, 85, 339, 30, 382, 47, 405, 749])
s.maxAreaPrint([686, 52, 171, 154, 330, 818, 451, 426, 308, 31])
s.maxAreaPrint([229, 639, 214, 159, 6, 434, 74, 564, 603, 727])
s.maxAreaPrint([955, 878, 723, 922, 499, 919, 185, 16, 810, 828])
s.maxAreaPrint([933, 310, 535, 68, 571, 476, 796, 892, 45, 961])
s.maxAreaPrint([182, 69, 160, 910, 197, 517, 911, 5, 1000, 439])
s.maxAreaPrint([902, 763, 469, 938, 866, 860, 433, 226, 113, 53])
s.maxAreaPrint([270, 981, 169, 874, 882, 742, 719, 334, 238, 407])
s.maxAreaPrint([38, 370, 40, 837, 197, 475, 228, 723, 758, 577])
s.maxAreaPrint([471, 990, 570, 847, 393, 520, 382, 742, 811, 889])
s.maxAreaPrint([510, 755, 405, 851, 104, 337, 708, 982, 287, 940])
s.maxAreaPrint([975, 292, 437, 906, 877, 947, 433, 653, 628, 570])
s.maxAreaPrint([731, 108, 962, 661, 375, 260, 826, 702, 402, 914])
s.maxAreaPrint([112, 19, 391, 505, 289, 666, 464, 929, 544, 972])
s.maxAreaPrint([807, 177, 559, 146, 542, 566, 265, 194, 848, 753])
s.maxAreaPrint([453, 889, 600, 39, 283, 870, 155, 369, 343, 378])
s.maxAreaPrint([826, 739, 121, 333, 282, 486, 813, 547, 746, 423])
s.maxAreaPrint([823, 990, 915, 237, 322, 867, 702, 889, 989, 924])
s.maxAreaPrint([514, 579, 402, 765, 803, 430, 121, 784, 138, 254])
s.maxAreaPrint([573, 476, 758, 601, 965, 931, 16, 981, 948, 335])
s.maxAreaPrint([384, 854, 368, 687, 10, 178, 7, 319, 461, 557])
s.maxAreaPrint([481, 616, 484, 806, 745, 603, 444, 204, 539, 431])
s.maxAreaPrint([117, 154, 383, 965, 915, 822, 232, 404, 778, 168])
s.maxAreaPrint([529, 729, 957, 321, 125, 619, 263, 126, 213, 774])
s.maxAreaPrint([213, 279, 650, 232, 177, 978, 645, 351, 410, 939])
s.maxAreaPrint([728, 451, 446, 183, 702, 678, 350, 164, 526, 948])
s.maxAreaPrint([276, 904, 744, 952, 876, 509, 406, 25, 766, 800])
s.maxAreaPrint([507, 105, 577, 12, 27, 742, 777, 323, 920, 545])
s.maxAreaPrint([245, 24, 130, 712, 137, 764, 481, 514, 541, 493])
s.maxAreaPrint([416, 893, 171, 240, 422, 260, 636, 698, 981, 106])
s.maxAreaPrint([436, 695, 947, 8, 283, 647, 825, 598, 890, 504])
s.maxAreaPrint([599, 378, 633, 183, 205, 525, 76, 478, 583, 813])
s.maxAreaPrint([434, 133, 106, 759, 27, 715, 93, 161, 247, 568])
s.maxAreaPrint([378, 646, 400, 427, 27, 21, 235, 949, 508, 532])
s.maxAreaPrint([234, 442, 774, 768, 263, 22, 886, 517, 522, 52])
s.maxAreaPrint([737, 885, 853, 965, 860, 225, 204, 72, 896, 139])
s.maxAreaPrint([817, 599, 36, 162, 846, 314, 931, 139, 827, 576])
s.maxAreaPrint([392, 129, 752, 596, 785, 198, 633, 147, 258, 469])
s.maxAreaPrint([532, 234, 347, 731, 673, 117, 875, 276, 978, 104])
s.maxAreaPrint([753, 246, 923, 705, 988, 303, 124, 339, 380, 323])
s.maxAreaPrint([644, 754, 730, 147, 752, 406, 511, 931, 727, 486])
s.maxAreaPrint([339, 570, 777, 753, 29, 744, 318, 59, 453, 945])
s.maxAreaPrint([502, 766, 993, 650, 618, 888, 283, 713, 318, 503])
s.maxAreaPrint([684, 786, 527, 784, 404, 499, 668, 653, 722, 494])
s.maxAreaPrint([899, 550, 803, 771, 885, 643, 220, 673, 204, 765])
s.maxAreaPrint([204, 356, 34, 823, 377, 53, 638, 803, 799, 986])
s.maxAreaPrint([21, 212, 216, 342, 261, 804, 384, 646, 253, 41])
s.maxAreaPrint([261, 653, 454, 954, 204, 551, 450, 440, 752, 615])
s.maxAreaPrint([971, 544, 586, 316, 966, 354, 811, 217, 232, 436])
s.maxAreaPrint([455, 696, 609, 666, 743, 568, 573, 915, 905, 67])
s.maxAreaPrint([269, 826, 691, 669, 280, 570, 386, 129, 477, 805])
s.maxAreaPrint([797, 375, 321, 572, 986, 776, 682, 414, 65, 523])
s.maxAreaPrint([112, 99, 104, 385, 292, 166, 552, 55, 127, 76])
s.maxAreaPrint([120, 857, 310, 761, 888, 899, 69, 175, 511, 564])
s.maxAreaPrint([71, 37, 418, 22, 843, 128, 17, 353, 58, 986])
s.maxAreaPrint([737, 557, 533, 480, 517, 514, 522, 236, 376, 898])
s.maxAreaPrint([518, 449, 607, 297, 936, 813, 517, 217, 416, 849])
s.maxAreaPrint([951, 964, 783, 546, 120, 492, 814, 648, 823, 860])
s.maxAreaPrint([601, 821, 235, 857, 368, 937, 379, 433, 433, 483])
s.maxAreaPrint([606, 626, 319, 62, 415, 982, 749, 355, 915, 742])
s.maxAreaPrint([644, 972, 675, 19, 945, 409, 44, 797, 762, 967])
s.maxAreaPrint([788, 730, 151, 627, 332, 351, 225, 564, 97, 655])
s.maxAreaPrint([92, 150, 765, 709, 75, 874, 753, 508, 682, 212])
s.maxAreaPrint([899, 959, 630, 668, 249, 238, 313, 5, 138, 365])

# test_num = 100
# i = 0
# while i < test_num:
#     print(rand_array(10, 0, 1000))
#     i += 1
#
#print(list(range(40000)))


#big input tests
# start = time.time();
# big_input_count = 15000
# big_sorted_asc = list(range(big_input_count))
# print(s.maxArea(big_sorted_asc))
# print(f"Time spend (linear-asc) {time.time() - start}")
#
# start = time.time();
# print(s.maxAreaSlow(big_sorted_asc))
# print(f"Time spend (quadratic) {time.time() - start}")
#
# start = time.time();
# big_sorted_desc = list(range(big_input_count))
# big_sorted_desc.reverse()
# print(s.maxArea(big_sorted_desc))
# print(f"Time spend (linear-desc) {time.time() - start}")
#
# start = time.time();
# print(s.maxAreaSlow(big_sorted_desc))
# print(f"Time spend (quadratic-desc) {time.time() - start}")