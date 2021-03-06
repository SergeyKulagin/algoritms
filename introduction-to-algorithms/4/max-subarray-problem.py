import math
import datetime

def findMaxSubArray(a):
    if len(a) == 0:
        return SubArrayInfo(None, None, None)
    return findMaxSubArrayRecStep(a, 0, len(a) - 1)

def findMaxSubArrayRecStep(a, start, end):
    if start == end:
        return SubArrayInfo(start, start, a[start])
    middle = math.floor((start + end) / 2)
    leftMaxSubArrayInfo = findMaxSubArrayRecStep(a, start, middle)
    rightMaxSubArrayInfo = findMaxSubArrayRecStep(a, middle + 1, end)
    middleMaxSubArrayInfo = findMaxSubArrayFromPoint(a, start, end, middle)
    maxSubArrayInfo = max(max(leftMaxSubArrayInfo, rightMaxSubArrayInfo), middleMaxSubArrayInfo)
    return maxSubArrayInfo

def max(subArrayInfoFirst, subArrayInfoSecond):
    if subArrayInfoFirst.sum > subArrayInfoSecond.sum:
        return subArrayInfoFirst
    else:
        return subArrayInfoSecond


def findMaxSubArrayFromPointLeft(a, point, to):
    sum = 0
    maxSubArrayInfo = SubArrayInfo(point, point, float('-inf'))
    for k in range(point, to, -1):
        sum = sum + a[k]
        if sum > maxSubArrayInfo.sum:
            maxSubArrayInfo.start = k
            maxSubArrayInfo.sum = sum
    return maxSubArrayInfo


def findMaxSubArrayFromPointRight(a, point, to):
    sum = 0
    maxSubArrayInfo = SubArrayInfo(point, point, a[point])
    for k in range(point, to, 1):
        sum = sum + a[k]
        if sum > maxSubArrayInfo.sum:
            maxSubArrayInfo.end = k
            maxSubArrayInfo.sum = sum
    return maxSubArrayInfo


def findMaxSubArrayFromPoint(a, start, end, middle):
    leftSubArray = findMaxSubArrayFromPointLeft(a, middle, start)
    rightSubArray = findMaxSubArrayFromPointRight(a, middle + 1, end + 1)
    return SubArrayInfo(leftSubArray.start, rightSubArray.end, leftSubArray.sum + rightSubArray.sum)


#===========================
# brute force

def findMaxSubArrayBruteForce(a):
    if len(a) == 0:
        return SubArrayInfo(None, None, None)
    return findMaxSubArrayBruteForceInterval(a, 0, len(a))

def findMaxSubArrayBruteForceInterval(a, start, end):
    maxSubArray = SubArrayInfo(None, None, float('-inf'))
    for i in range(start, end):
        sum = 0
        for j in range(i, end):
            sum = sum + a[j]
            if sum > maxSubArray.sum:
                maxSubArray.sum = sum
                maxSubArray.start = i
                maxSubArray.end = j
    return maxSubArray
#===========================
#delegating to brute force

def findMaxSubArrayDelegating(a, minRecursiveProblemSize):
    if len(a) == 0:
        return SubArrayInfo(None, None, None)
    return findMaxSubArrayRecStepDelegating(a, 0, len(a) - 1, minRecursiveProblemSize)

def findMaxSubArrayRecStepDelegating(a, start, end, minRecursiveProblemSize):
    if end - start <= minRecursiveProblemSize:
        return findMaxSubArrayBruteForceInterval(a, start, end)
    middle = math.floor((start + end) / 2)
    leftMaxSubArrayInfo = findMaxSubArrayRecStepDelegating(a, start, middle, minRecursiveProblemSize)
    rightMaxSubArrayInfo = findMaxSubArrayRecStepDelegating(a, middle + 1, end, minRecursiveProblemSize)
    middleMaxSubArrayInfo = findMaxSubArrayFromPoint(a, start, end, middle)
    maxSubArrayInfo = max(max(leftMaxSubArrayInfo, rightMaxSubArrayInfo), middleMaxSubArrayInfo)
    return maxSubArrayInfo

#===========================

#todo fix
def findMaxSubArrayLinear(a):
    maxSubArray = SubArrayInfo(0, 0, a[0])
    for i in range(0, len(a)):
        sum = 0
        for j in  range(i, maxSubArray.start - 1, -1):
            sum = sum + a[j]
            if sum > maxSubArray.sum:
                maxSubArray.sum = sum
                maxSubArray.start = j
                maxSubArray.end = i
    return maxSubArray


class SubArrayInfo:
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.sum = sum

    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "], sum = " + str(self.sum)


#1000
print("\n")
print("#1000")
startTime = datetime.datetime.now()
arr = [-1000, -999, -998, -997, -996, -993, -992, -988, -983, -979, -978, -976, -975, -974, -971, -970, -968, -967, -966, -965, -962, -957, -955, -954, -953, -952, -950, -947, -943, -941, -940, -938, -937, -936, -935, -933, -931, -930, -926, -925, -923, -922, -920, -919, -918, -915, -914, -910, -908, -907, -906, -902, -900, -899, -898, -894, -889, -886, -885, -884, -878, -877, -876, -873, -869, -868, -867, -863, -862, -858, -853, -852, -849, -848, -846, -843, -841, -839, -837, -836, -835, -833, -832, -831, -828, -827, -821, -820, -817, -816, -812, -811, -809, -808, -807, -803, -801, -800, -799, -796, -794, -793, -792, -786, -784, -783, -782, -781, -780, -778, -771, -769, -767, -763, -760, -759, -757, -756, -754, -753, -749, -745, -744, -742, -741, -740, -739, -738, -734, -730, -729, -727, -726, -723, -721, -720, -719, -718, -717, -716, -715, -712, -707, -703, -702, -701, -698, -693, -691, -690, -686, -685, -680, -679, -676, -675, -674, -672, -670, -669, -667, -664, -663, -656, -655, -654, -653, -652, -650, -647, -646, -645, -644, -642, -640, -639, -638, -637, -636, -633, -632, -630, -629, -628, -627, -625, -624, -621, -619, -611, -609, -607, -606, -605, -598, -597, -594, -592, -588, -587, -585, -584, -580, -578, -576, -575, -573, -572, -570, -569, -565, -564, -560, -557, -556, -554, -553, -551, -550, -544, -542, -541, -539, -537, -534, -532, -531, -530, -529, -528, -526, -525, -524, -523, -522, -521, -518, -517, -514, -513, -511, -507, -506, -505, -502, -501, -497, -496, -494, -493, -492, -491, -489, -487, -485, -484, -480, -478, -476, -474, -473, -472, -468, -467, -463, -461, -460, -459, -457, -456, -454, -450, -448, -445, -444, -441, -440, -439, -438, -437, -435, -433, -429, -428, -427, -426, -424, -423, -421, -420, -419, -418, -416, -415, -414, -412, -410, -407, -400, -399, -397, -396, -394, -386, -385, -384, -383, -382, -381, -380, -378, -377, -374, -373, -372, -370, -369, -368, -367, -364, -363, -362, -361, -359, -358, -357, -356, -354, -352, -351, -348, -346, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -327, -324, -322, -320, -319, -317, -316, -315, -314, -313, -309, -308, -306, -305, -303, -302, -301, -298, -295, -294, -290, -289, -287, -285, -284, -283, -282, -281, -279, -277, -276, -275, -271, -270, -267, -265, -262, -261, -259, -258, -256, -253, -252, -249, -248, -247, -246, -245, -243, -242, -241, -238, -237, -236, -235, -233, -232, -231, -229, -226, -224, -222, -221, -219, -217, -216, -215, -212, -210, -207, -206, -204, -201, -200, -198, -197, -196, -193, -187, -181, -180, -178, -176, -174, -171, -169, -168, -167, -166, -165, -164, -160, -155, -152, -149, -148, -144, -139, -138, -137, -136, -135, -134, -133, -131, -130, -129, -126, -125, -122, -120, -119, -116, -114, -113, -112, -111, -107, -106, -105, -103, -101, -99, -97, -95, -93, -91, -90, -82, -80, -79, -78, -77, -74, -73, -71, -69, -68, -67, -66, -65, -64, -62, -55, -53, -51, -48, -44, -40, -37, -35, -34, -33, -32, -30, -27, -22, -21, -20, -16, -15, -9, -7, -6, -5, -3, 0, 4, 5, 6, 7, 8, 10, 15, 19, 20, 22, 23, 24, 25, 27, 29, 30, 33, 34, 37, 38, 39, 40, 44, 47, 48, 49, 50, 53, 57, 58, 61, 63, 64, 66, 68, 69, 72, 73, 74, 76, 80, 81, 84, 88, 93, 95, 97, 98, 99, 100, 102, 103, 104, 105, 109, 110, 112, 115, 116, 118, 119, 121, 126, 130, 134, 135, 136, 138, 139, 140, 143, 144, 145, 146, 152, 154, 155, 157, 158, 164, 165, 166, 167, 168, 172, 174, 175, 176, 179, 181, 184, 185, 186, 188, 189, 190, 193, 197, 198, 203, 210, 215, 218, 219, 220, 221, 222, 226, 227, 228, 230, 231, 232, 233, 234, 236, 240, 241, 242, 244, 248, 249, 250, 253, 254, 255, 256, 257, 258, 260, 261, 262, 263, 266, 267, 269, 272, 273, 274, 275, 278, 279, 282, 287, 288, 289, 290, 292, 295, 297, 299, 303, 309, 311, 312, 314, 319, 320, 323, 324, 325, 326, 331, 333, 336, 337, 340, 342, 344, 345, 346, 348, 349, 350, 351, 352, 353, 354, 357, 359, 362, 364, 368, 369, 370, 371, 373, 375, 377, 378, 379, 380, 388, 389, 390, 392, 394, 395, 396, 400, 401, 402, 403, 404, 408, 411, 413, 414, 415, 417, 419, 420, 421, 425, 427, 429, 430, 431, 434, 435, 439, 441, 444, 445, 446, 447, 449, 452, 453, 454, 456, 457, 463, 465, 468, 469, 471, 472, 473, 476, 477, 478, 481, 483, 484, 485, 486, 487, 489, 491, 493, 495, 498, 499, 500, 503, 504, 505, 507, 508, 509, 514, 515, 516, 519, 521, 523, 524, 526, 528, 531, 532, 533, 534, 536, 537, 539, 541, 542, 544, 545, 546, 548, 551, 552, 553, 556, 562, 565, 566, 568, 569, 572, 573, 574, 575, 576, 577, 578, 580, 581, 582, 583, 586, 588, 590, 591, 592, 595, 598, 601, 602, 606, 608, 610, 616, 617, 619, 620, 625, 630, 631, 632, 634, 636, 641, 643, 644, 645, 651, 655, 658, 659, 660, 662, 670, 671, 672, 676, 677, 680, 681, 682, 683, 686, 690, 691, 692, 693, 695, 699, 701, 702, 704, 706, 707, 708, 710, 711, 716, 719, 722, 723, 726, 728, 732, 733, 734, 737, 738, 740, 745, 749, 753, 754, 755, 758, 760, 763, 765, 766, 769, 771, 772, 776, 778, 779, 780, 783, 784, 785, 786, 788, 789, 793, 795, 796, 797, 803, 805, 806, 810, 812, 813, 815, 816, 819, 822, 823, 824, 826, 827, 830, 831, 832, 834, 837, 838, 843, 845, 846, 848, 850, 854, 855, 856, 858, 859, 863, 866, 871, 872, 873, 874, 875, 876, 877, 883, 885, 887, 889, 891, 897, 898, 901, 903, 905, 910, 916, 917, 920, 921, 923, 925, 929, 932, 933, 934, 937, 940, 941, 942, 947, 948, 949, 952, 954, 956, 958, 959, 961, 963, 966, 968, 969, 972, 975, 976, 977, 979, 980, 984, 991, 992, 993, 994, 996, 998, 1000];
print(findMaxSubArrayBruteForce([-1000, -999, -998, -997, -996, -993, -992, -988, -983, -979, -978, -976, -975, -974, -971, -970, -968, -967, -966, -965, -962, -957, -955, -954, -953, -952, -950, -947, -943, -941, -940, -938, -937, -936, -935, -933, -931, -930, -926, -925, -923, -922, -920, -919, -918, -915, -914, -910, -908, -907, -906, -902, -900, -899, -898, -894, -889, -886, -885, -884, -878, -877, -876, -873, -869, -868, -867, -863, -862, -858, -853, -852, -849, -848, -846, -843, -841, -839, -837, -836, -835, -833, -832, -831, -828, -827, -821, -820, -817, -816, -812, -811, -809, -808, -807, -803, -801, -800, -799, -796, -794, -793, -792, -786, -784, -783, -782, -781, -780, -778, -771, -769, -767, -763, -760, -759, -757, -756, -754, -753, -749, -745, -744, -742, -741, -740, -739, -738, -734, -730, -729, -727, -726, -723, -721, -720, -719, -718, -717, -716, -715, -712, -707, -703, -702, -701, -698, -693, -691, -690, -686, -685, -680, -679, -676, -675, -674, -672, -670, -669, -667, -664, -663, -656, -655, -654, -653, -652, -650, -647, -646, -645, -644, -642, -640, -639, -638, -637, -636, -633, -632, -630, -629, -628, -627, -625, -624, -621, -619, -611, -609, -607, -606, -605, -598, -597, -594, -592, -588, -587, -585, -584, -580, -578, -576, -575, -573, -572, -570, -569, -565, -564, -560, -557, -556, -554, -553, -551, -550, -544, -542, -541, -539, -537, -534, -532, -531, -530, -529, -528, -526, -525, -524, -523, -522, -521, -518, -517, -514, -513, -511, -507, -506, -505, -502, -501, -497, -496, -494, -493, -492, -491, -489, -487, -485, -484, -480, -478, -476, -474, -473, -472, -468, -467, -463, -461, -460, -459, -457, -456, -454, -450, -448, -445, -444, -441, -440, -439, -438, -437, -435, -433, -429, -428, -427, -426, -424, -423, -421, -420, -419, -418, -416, -415, -414, -412, -410, -407, -400, -399, -397, -396, -394, -386, -385, -384, -383, -382, -381, -380, -378, -377, -374, -373, -372, -370, -369, -368, -367, -364, -363, -362, -361, -359, -358, -357, -356, -354, -352, -351, -348, -346, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -327, -324, -322, -320, -319, -317, -316, -315, -314, -313, -309, -308, -306, -305, -303, -302, -301, -298, -295, -294, -290, -289, -287, -285, -284, -283, -282, -281, -279, -277, -276, -275, -271, -270, -267, -265, -262, -261, -259, -258, -256, -253, -252, -249, -248, -247, -246, -245, -243, -242, -241, -238, -237, -236, -235, -233, -232, -231, -229, -226, -224, -222, -221, -219, -217, -216, -215, -212, -210, -207, -206, -204, -201, -200, -198, -197, -196, -193, -187, -181, -180, -178, -176, -174, -171, -169, -168, -167, -166, -165, -164, -160, -155, -152, -149, -148, -144, -139, -138, -137, -136, -135, -134, -133, -131, -130, -129, -126, -125, -122, -120, -119, -116, -114, -113, -112, -111, -107, -106, -105, -103, -101, -99, -97, -95, -93, -91, -90, -82, -80, -79, -78, -77, -74, -73, -71, -69, -68, -67, -66, -65, -64, -62, -55, -53, -51, -48, -44, -40, -37, -35, -34, -33, -32, -30, -27, -22, -21, -20, -16, -15, -9, -7, -6, -5, -3, 0, 4, 5, 6, 7, 8, 10, 15, 19, 20, 22, 23, 24, 25, 27, 29, 30, 33, 34, 37, 38, 39, 40, 44, 47, 48, 49, 50, 53, 57, 58, 61, 63, 64, 66, 68, 69, 72, 73, 74, 76, 80, 81, 84, 88, 93, 95, 97, 98, 99, 100, 102, 103, 104, 105, 109, 110, 112, 115, 116, 118, 119, 121, 126, 130, 134, 135, 136, 138, 139, 140, 143, 144, 145, 146, 152, 154, 155, 157, 158, 164, 165, 166, 167, 168, 172, 174, 175, 176, 179, 181, 184, 185, 186, 188, 189, 190, 193, 197, 198, 203, 210, 215, 218, 219, 220, 221, 222, 226, 227, 228, 230, 231, 232, 233, 234, 236, 240, 241, 242, 244, 248, 249, 250, 253, 254, 255, 256, 257, 258, 260, 261, 262, 263, 266, 267, 269, 272, 273, 274, 275, 278, 279, 282, 287, 288, 289, 290, 292, 295, 297, 299, 303, 309, 311, 312, 314, 319, 320, 323, 324, 325, 326, 331, 333, 336, 337, 340, 342, 344, 345, 346, 348, 349, 350, 351, 352, 353, 354, 357, 359, 362, 364, 368, 369, 370, 371, 373, 375, 377, 378, 379, 380, 388, 389, 390, 392, 394, 395, 396, 400, 401, 402, 403, 404, 408, 411, 413, 414, 415, 417, 419, 420, 421, 425, 427, 429, 430, 431, 434, 435, 439, 441, 444, 445, 446, 447, 449, 452, 453, 454, 456, 457, 463, 465, 468, 469, 471, 472, 473, 476, 477, 478, 481, 483, 484, 485, 486, 487, 489, 491, 493, 495, 498, 499, 500, 503, 504, 505, 507, 508, 509, 514, 515, 516, 519, 521, 523, 524, 526, 528, 531, 532, 533, 534, 536, 537, 539, 541, 542, 544, 545, 546, 548, 551, 552, 553, 556, 562, 565, 566, 568, 569, 572, 573, 574, 575, 576, 577, 578, 580, 581, 582, 583, 586, 588, 590, 591, 592, 595, 598, 601, 602, 606, 608, 610, 616, 617, 619, 620, 625, 630, 631, 632, 634, 636, 641, 643, 644, 645, 651, 655, 658, 659, 660, 662, 670, 671, 672, 676, 677, 680, 681, 682, 683, 686, 690, 691, 692, 693, 695, 699, 701, 702, 704, 706, 707, 708, 710, 711, 716, 719, 722, 723, 726, 728, 732, 733, 734, 737, 738, 740, 745, 749, 753, 754, 755, 758, 760, 763, 765, 766, 769, 771, 772, 776, 778, 779, 780, 783, 784, 785, 786, 788, 789, 793, 795, 796, 797, 803, 805, 806, 810, 812, 813, 815, 816, 819, 822, 823, 824, 826, 827, 830, 831, 832, 834, 837, 838, 843, 845, 846, 848, 850, 854, 855, 856, 858, 859, 863, 866, 871, 872, 873, 874, 875, 876, 877, 883, 885, 887, 889, 891, 897, 898, 901, 903, 905, 910, 916, 917, 920, 921, 923, 925, 929, 932, 933, 934, 937, 940, 941, 942, 947, 948, 949, 952, 954, 956, 958, 959, 961, 963, 966, 968, 969, 972, 975, 976, 977, 979, 980, 984, 991, 992, 993, 994, 996, 998, 1000]))
endTime = datetime.datetime.now()
duration = endTime - startTime
print("findMaxSubArrayBruteForce, duration: " + str(duration.microseconds))

startTime = datetime.datetime.now()
print(findMaxSubArray([-1000, -999, -998, -997, -996, -993, -992, -988, -983, -979, -978, -976, -975, -974, -971, -970, -968, -967, -966, -965, -962, -957, -955, -954, -953, -952, -950, -947, -943, -941, -940, -938, -937, -936, -935, -933, -931, -930, -926, -925, -923, -922, -920, -919, -918, -915, -914, -910, -908, -907, -906, -902, -900, -899, -898, -894, -889, -886, -885, -884, -878, -877, -876, -873, -869, -868, -867, -863, -862, -858, -853, -852, -849, -848, -846, -843, -841, -839, -837, -836, -835, -833, -832, -831, -828, -827, -821, -820, -817, -816, -812, -811, -809, -808, -807, -803, -801, -800, -799, -796, -794, -793, -792, -786, -784, -783, -782, -781, -780, -778, -771, -769, -767, -763, -760, -759, -757, -756, -754, -753, -749, -745, -744, -742, -741, -740, -739, -738, -734, -730, -729, -727, -726, -723, -721, -720, -719, -718, -717, -716, -715, -712, -707, -703, -702, -701, -698, -693, -691, -690, -686, -685, -680, -679, -676, -675, -674, -672, -670, -669, -667, -664, -663, -656, -655, -654, -653, -652, -650, -647, -646, -645, -644, -642, -640, -639, -638, -637, -636, -633, -632, -630, -629, -628, -627, -625, -624, -621, -619, -611, -609, -607, -606, -605, -598, -597, -594, -592, -588, -587, -585, -584, -580, -578, -576, -575, -573, -572, -570, -569, -565, -564, -560, -557, -556, -554, -553, -551, -550, -544, -542, -541, -539, -537, -534, -532, -531, -530, -529, -528, -526, -525, -524, -523, -522, -521, -518, -517, -514, -513, -511, -507, -506, -505, -502, -501, -497, -496, -494, -493, -492, -491, -489, -487, -485, -484, -480, -478, -476, -474, -473, -472, -468, -467, -463, -461, -460, -459, -457, -456, -454, -450, -448, -445, -444, -441, -440, -439, -438, -437, -435, -433, -429, -428, -427, -426, -424, -423, -421, -420, -419, -418, -416, -415, -414, -412, -410, -407, -400, -399, -397, -396, -394, -386, -385, -384, -383, -382, -381, -380, -378, -377, -374, -373, -372, -370, -369, -368, -367, -364, -363, -362, -361, -359, -358, -357, -356, -354, -352, -351, -348, -346, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -327, -324, -322, -320, -319, -317, -316, -315, -314, -313, -309, -308, -306, -305, -303, -302, -301, -298, -295, -294, -290, -289, -287, -285, -284, -283, -282, -281, -279, -277, -276, -275, -271, -270, -267, -265, -262, -261, -259, -258, -256, -253, -252, -249, -248, -247, -246, -245, -243, -242, -241, -238, -237, -236, -235, -233, -232, -231, -229, -226, -224, -222, -221, -219, -217, -216, -215, -212, -210, -207, -206, -204, -201, -200, -198, -197, -196, -193, -187, -181, -180, -178, -176, -174, -171, -169, -168, -167, -166, -165, -164, -160, -155, -152, -149, -148, -144, -139, -138, -137, -136, -135, -134, -133, -131, -130, -129, -126, -125, -122, -120, -119, -116, -114, -113, -112, -111, -107, -106, -105, -103, -101, -99, -97, -95, -93, -91, -90, -82, -80, -79, -78, -77, -74, -73, -71, -69, -68, -67, -66, -65, -64, -62, -55, -53, -51, -48, -44, -40, -37, -35, -34, -33, -32, -30, -27, -22, -21, -20, -16, -15, -9, -7, -6, -5, -3, 0, 4, 5, 6, 7, 8, 10, 15, 19, 20, 22, 23, 24, 25, 27, 29, 30, 33, 34, 37, 38, 39, 40, 44, 47, 48, 49, 50, 53, 57, 58, 61, 63, 64, 66, 68, 69, 72, 73, 74, 76, 80, 81, 84, 88, 93, 95, 97, 98, 99, 100, 102, 103, 104, 105, 109, 110, 112, 115, 116, 118, 119, 121, 126, 130, 134, 135, 136, 138, 139, 140, 143, 144, 145, 146, 152, 154, 155, 157, 158, 164, 165, 166, 167, 168, 172, 174, 175, 176, 179, 181, 184, 185, 186, 188, 189, 190, 193, 197, 198, 203, 210, 215, 218, 219, 220, 221, 222, 226, 227, 228, 230, 231, 232, 233, 234, 236, 240, 241, 242, 244, 248, 249, 250, 253, 254, 255, 256, 257, 258, 260, 261, 262, 263, 266, 267, 269, 272, 273, 274, 275, 278, 279, 282, 287, 288, 289, 290, 292, 295, 297, 299, 303, 309, 311, 312, 314, 319, 320, 323, 324, 325, 326, 331, 333, 336, 337, 340, 342, 344, 345, 346, 348, 349, 350, 351, 352, 353, 354, 357, 359, 362, 364, 368, 369, 370, 371, 373, 375, 377, 378, 379, 380, 388, 389, 390, 392, 394, 395, 396, 400, 401, 402, 403, 404, 408, 411, 413, 414, 415, 417, 419, 420, 421, 425, 427, 429, 430, 431, 434, 435, 439, 441, 444, 445, 446, 447, 449, 452, 453, 454, 456, 457, 463, 465, 468, 469, 471, 472, 473, 476, 477, 478, 481, 483, 484, 485, 486, 487, 489, 491, 493, 495, 498, 499, 500, 503, 504, 505, 507, 508, 509, 514, 515, 516, 519, 521, 523, 524, 526, 528, 531, 532, 533, 534, 536, 537, 539, 541, 542, 544, 545, 546, 548, 551, 552, 553, 556, 562, 565, 566, 568, 569, 572, 573, 574, 575, 576, 577, 578, 580, 581, 582, 583, 586, 588, 590, 591, 592, 595, 598, 601, 602, 606, 608, 610, 616, 617, 619, 620, 625, 630, 631, 632, 634, 636, 641, 643, 644, 645, 651, 655, 658, 659, 660, 662, 670, 671, 672, 676, 677, 680, 681, 682, 683, 686, 690, 691, 692, 693, 695, 699, 701, 702, 704, 706, 707, 708, 710, 711, 716, 719, 722, 723, 726, 728, 732, 733, 734, 737, 738, 740, 745, 749, 753, 754, 755, 758, 760, 763, 765, 766, 769, 771, 772, 776, 778, 779, 780, 783, 784, 785, 786, 788, 789, 793, 795, 796, 797, 803, 805, 806, 810, 812, 813, 815, 816, 819, 822, 823, 824, 826, 827, 830, 831, 832, 834, 837, 838, 843, 845, 846, 848, 850, 854, 855, 856, 858, 859, 863, 866, 871, 872, 873, 874, 875, 876, 877, 883, 885, 887, 889, 891, 897, 898, 901, 903, 905, 910, 916, 917, 920, 921, 923, 925, 929, 932, 933, 934, 937, 940, 941, 942, 947, 948, 949, 952, 954, 956, 958, 959, 961, 963, 966, 968, 969, 972, 975, 976, 977, 979, 980, 984, 991, 992, 993, 994, 996, 998, 1000]))
endTime = datetime.datetime.now()
duration = endTime - startTime
print("findMaxSubArray, duration: " + str(duration.microseconds))


startTime = datetime.datetime.now()
print(findMaxSubArrayDelegating([-1000, -999, -998, -997, -996, -993, -992, -988, -983, -979, -978, -976, -975, -974, -971, -970, -968, -967, -966, -965, -962, -957, -955, -954, -953, -952, -950, -947, -943, -941, -940, -938, -937, -936, -935, -933, -931, -930, -926, -925, -923, -922, -920, -919, -918, -915, -914, -910, -908, -907, -906, -902, -900, -899, -898, -894, -889, -886, -885, -884, -878, -877, -876, -873, -869, -868, -867, -863, -862, -858, -853, -852, -849, -848, -846, -843, -841, -839, -837, -836, -835, -833, -832, -831, -828, -827, -821, -820, -817, -816, -812, -811, -809, -808, -807, -803, -801, -800, -799, -796, -794, -793, -792, -786, -784, -783, -782, -781, -780, -778, -771, -769, -767, -763, -760, -759, -757, -756, -754, -753, -749, -745, -744, -742, -741, -740, -739, -738, -734, -730, -729, -727, -726, -723, -721, -720, -719, -718, -717, -716, -715, -712, -707, -703, -702, -701, -698, -693, -691, -690, -686, -685, -680, -679, -676, -675, -674, -672, -670, -669, -667, -664, -663, -656, -655, -654, -653, -652, -650, -647, -646, -645, -644, -642, -640, -639, -638, -637, -636, -633, -632, -630, -629, -628, -627, -625, -624, -621, -619, -611, -609, -607, -606, -605, -598, -597, -594, -592, -588, -587, -585, -584, -580, -578, -576, -575, -573, -572, -570, -569, -565, -564, -560, -557, -556, -554, -553, -551, -550, -544, -542, -541, -539, -537, -534, -532, -531, -530, -529, -528, -526, -525, -524, -523, -522, -521, -518, -517, -514, -513, -511, -507, -506, -505, -502, -501, -497, -496, -494, -493, -492, -491, -489, -487, -485, -484, -480, -478, -476, -474, -473, -472, -468, -467, -463, -461, -460, -459, -457, -456, -454, -450, -448, -445, -444, -441, -440, -439, -438, -437, -435, -433, -429, -428, -427, -426, -424, -423, -421, -420, -419, -418, -416, -415, -414, -412, -410, -407, -400, -399, -397, -396, -394, -386, -385, -384, -383, -382, -381, -380, -378, -377, -374, -373, -372, -370, -369, -368, -367, -364, -363, -362, -361, -359, -358, -357, -356, -354, -352, -351, -348, -346, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -327, -324, -322, -320, -319, -317, -316, -315, -314, -313, -309, -308, -306, -305, -303, -302, -301, -298, -295, -294, -290, -289, -287, -285, -284, -283, -282, -281, -279, -277, -276, -275, -271, -270, -267, -265, -262, -261, -259, -258, -256, -253, -252, -249, -248, -247, -246, -245, -243, -242, -241, -238, -237, -236, -235, -233, -232, -231, -229, -226, -224, -222, -221, -219, -217, -216, -215, -212, -210, -207, -206, -204, -201, -200, -198, -197, -196, -193, -187, -181, -180, -178, -176, -174, -171, -169, -168, -167, -166, -165, -164, -160, -155, -152, -149, -148, -144, -139, -138, -137, -136, -135, -134, -133, -131, -130, -129, -126, -125, -122, -120, -119, -116, -114, -113, -112, -111, -107, -106, -105, -103, -101, -99, -97, -95, -93, -91, -90, -82, -80, -79, -78, -77, -74, -73, -71, -69, -68, -67, -66, -65, -64, -62, -55, -53, -51, -48, -44, -40, -37, -35, -34, -33, -32, -30, -27, -22, -21, -20, -16, -15, -9, -7, -6, -5, -3, 0, 4, 5, 6, 7, 8, 10, 15, 19, 20, 22, 23, 24, 25, 27, 29, 30, 33, 34, 37, 38, 39, 40, 44, 47, 48, 49, 50, 53, 57, 58, 61, 63, 64, 66, 68, 69, 72, 73, 74, 76, 80, 81, 84, 88, 93, 95, 97, 98, 99, 100, 102, 103, 104, 105, 109, 110, 112, 115, 116, 118, 119, 121, 126, 130, 134, 135, 136, 138, 139, 140, 143, 144, 145, 146, 152, 154, 155, 157, 158, 164, 165, 166, 167, 168, 172, 174, 175, 176, 179, 181, 184, 185, 186, 188, 189, 190, 193, 197, 198, 203, 210, 215, 218, 219, 220, 221, 222, 226, 227, 228, 230, 231, 232, 233, 234, 236, 240, 241, 242, 244, 248, 249, 250, 253, 254, 255, 256, 257, 258, 260, 261, 262, 263, 266, 267, 269, 272, 273, 274, 275, 278, 279, 282, 287, 288, 289, 290, 292, 295, 297, 299, 303, 309, 311, 312, 314, 319, 320, 323, 324, 325, 326, 331, 333, 336, 337, 340, 342, 344, 345, 346, 348, 349, 350, 351, 352, 353, 354, 357, 359, 362, 364, 368, 369, 370, 371, 373, 375, 377, 378, 379, 380, 388, 389, 390, 392, 394, 395, 396, 400, 401, 402, 403, 404, 408, 411, 413, 414, 415, 417, 419, 420, 421, 425, 427, 429, 430, 431, 434, 435, 439, 441, 444, 445, 446, 447, 449, 452, 453, 454, 456, 457, 463, 465, 468, 469, 471, 472, 473, 476, 477, 478, 481, 483, 484, 485, 486, 487, 489, 491, 493, 495, 498, 499, 500, 503, 504, 505, 507, 508, 509, 514, 515, 516, 519, 521, 523, 524, 526, 528, 531, 532, 533, 534, 536, 537, 539, 541, 542, 544, 545, 546, 548, 551, 552, 553, 556, 562, 565, 566, 568, 569, 572, 573, 574, 575, 576, 577, 578, 580, 581, 582, 583, 586, 588, 590, 591, 592, 595, 598, 601, 602, 606, 608, 610, 616, 617, 619, 620, 625, 630, 631, 632, 634, 636, 641, 643, 644, 645, 651, 655, 658, 659, 660, 662, 670, 671, 672, 676, 677, 680, 681, 682, 683, 686, 690, 691, 692, 693, 695, 699, 701, 702, 704, 706, 707, 708, 710, 711, 716, 719, 722, 723, 726, 728, 732, 733, 734, 737, 738, 740, 745, 749, 753, 754, 755, 758, 760, 763, 765, 766, 769, 771, 772, 776, 778, 779, 780, 783, 784, 785, 786, 788, 789, 793, 795, 796, 797, 803, 805, 806, 810, 812, 813, 815, 816, 819, 822, 823, 824, 826, 827, 830, 831, 832, 834, 837, 838, 843, 845, 846, 848, 850, 854, 855, 856, 858, 859, 863, 866, 871, 872, 873, 874, 875, 876, 877, 883, 885, 887, 889, 891, 897, 898, 901, 903, 905, 910, 916, 917, 920, 921, 923, 925, 929, 932, 933, 934, 937, 940, 941, 942, 947, 948, 949, 952, 954, 956, 958, 959, 961, 963, 966, 968, 969, 972, 975, 976, 977, 979, 980, 984, 991, 992, 993, 994, 996, 998, 1000], 79))
endTime = datetime.datetime.now()
duration = endTime - startTime
print("findMaxSubArrayDelegating, duration: " + str(duration.microseconds))

#500
print("\n")
print("#500")
startTime = datetime.datetime.now()
print(findMaxSubArrayBruteForce([-1000, -999, -983, -981, -978, -976, -973, -971, -967, -963, -957, -955, -947, -944, -943, -939, -937, -928, -925, -924, -912, -910, -907, -905, -904, -900, -899, -895, -891, -890, -885, -883, -880, -877, -872, -869, -868, -860, -859, -857, -855, -854, -851, -849, -841, -837, -835, -822, -821, -816, -814, -810, -809, -805, -804, -800, -795, -784, -776, -773, -763, -754, -752, -751, -745, -738, -736, -732, -730, -728, -726, -721, -720, -719, -717, -716, -715, -706, -704, -695, -694, -693, -688, -685, -684, -679, -677, -675, -671, -670, -668, -665, -663, -654, -646, -644, -640, -632, -619, -616, -611, -610, -608, -604, -593, -592, -588, -587, -585, -580, -574, -573, -571, -567, -565, -563, -561, -556, -555, -550, -547, -543, -539, -535, -529, -516, -515, -513, -512, -508, -504, -499, -498, -491, -489, -486, -476, -470, -468, -467, -454, -453, -452, -449, -446, -437, -433, -430, -420, -417, -414, -413, -412, -410, -409, -405, -404, -389, -387, -386, -378, -377, -370, -368, -364, -360, -355, -353, -349, -345, -343, -339, -336, -332, -329, -328, -324, -323, -315, -312, -296, -292, -288, -287, -286, -281, -279, -277, -273, -268, -267, -256, -254, -247, -246, -242, -237, -236, -232, -226, -225, -217, -213, -208, -201, -191, -188, -182, -181, -180, -179, -178, -175, -174, -172, -168, -156, -153, -130, -125, -116, -115, -105, -100, -97, -81, -78, -77, -76, -69, -67, -64, -57, -56, -55, -51, -49, -48, -46, -45, -43, -41, -37, -25, -21, -20, -19, -17, -12, -9, -4, 1, 3, 8, 10, 11, 13, 19, 24, 28, 31, 33, 46, 49, 54, 57, 59, 61, 67, 68, 72, 75, 76, 79, 84, 85, 87, 90, 92, 97, 107, 110, 114, 117, 118, 119, 120, 127, 129, 130, 133, 136, 137, 138, 149, 152, 155, 163, 170, 171, 174, 177, 180, 184, 186, 192, 193, 199, 203, 208, 221, 230, 234, 238, 250, 251, 253, 255, 258, 259, 268, 270, 274, 275, 276, 281, 282, 283, 290, 293, 295, 298, 299, 303, 309, 313, 322, 323, 324, 328, 342, 343, 346, 353, 354, 355, 365, 366, 371, 376, 377, 379, 386, 391, 396, 400, 411, 414, 415, 433, 438, 441, 449, 451, 462, 465, 468, 472, 477, 484, 486, 502, 509, 510, 513, 515, 516, 521, 522, 525, 527, 550, 558, 565, 577, 581, 587, 588, 596, 599, 600, 603, 604, 605, 609, 614, 616, 617, 624, 627, 630, 635, 642, 648, 654, 655, 663, 666, 670, 671, 673, 674, 677, 678, 680, 681, 691, 699, 702, 707, 709, 711, 721, 726, 729, 730, 736, 738, 745, 754, 759, 762, 764, 765, 769, 772, 777, 780, 787, 789, 798, 805, 808, 809, 820, 821, 823, 824, 832, 834, 835, 836, 837, 838, 844, 845, 847, 848, 850, 854, 863, 867, 868, 875, 876, 880, 892, 898, 902, 903, 906, 908, 910, 915, 919, 927, 929, 935, 937, 938, 941, 942, 944, 945, 946, 960, 962, 969, 970, 973, 975, 979, 982, 983, 984, 985, 992, 996, 998, 1000]))
endTime = datetime.datetime.now()
duration = endTime - startTime
print("findMaxSubArrayBruteForce, duration: " + str(duration.microseconds))
startTime = datetime.datetime.now()
print(findMaxSubArray([-1000, -999, -983, -981, -978, -976, -973, -971, -967, -963, -957, -955, -947, -944, -943, -939, -937, -928, -925, -924, -912, -910, -907, -905, -904, -900, -899, -895, -891, -890, -885, -883, -880, -877, -872, -869, -868, -860, -859, -857, -855, -854, -851, -849, -841, -837, -835, -822, -821, -816, -814, -810, -809, -805, -804, -800, -795, -784, -776, -773, -763, -754, -752, -751, -745, -738, -736, -732, -730, -728, -726, -721, -720, -719, -717, -716, -715, -706, -704, -695, -694, -693, -688, -685, -684, -679, -677, -675, -671, -670, -668, -665, -663, -654, -646, -644, -640, -632, -619, -616, -611, -610, -608, -604, -593, -592, -588, -587, -585, -580, -574, -573, -571, -567, -565, -563, -561, -556, -555, -550, -547, -543, -539, -535, -529, -516, -515, -513, -512, -508, -504, -499, -498, -491, -489, -486, -476, -470, -468, -467, -454, -453, -452, -449, -446, -437, -433, -430, -420, -417, -414, -413, -412, -410, -409, -405, -404, -389, -387, -386, -378, -377, -370, -368, -364, -360, -355, -353, -349, -345, -343, -339, -336, -332, -329, -328, -324, -323, -315, -312, -296, -292, -288, -287, -286, -281, -279, -277, -273, -268, -267, -256, -254, -247, -246, -242, -237, -236, -232, -226, -225, -217, -213, -208, -201, -191, -188, -182, -181, -180, -179, -178, -175, -174, -172, -168, -156, -153, -130, -125, -116, -115, -105, -100, -97, -81, -78, -77, -76, -69, -67, -64, -57, -56, -55, -51, -49, -48, -46, -45, -43, -41, -37, -25, -21, -20, -19, -17, -12, -9, -4, 1, 3, 8, 10, 11, 13, 19, 24, 28, 31, 33, 46, 49, 54, 57, 59, 61, 67, 68, 72, 75, 76, 79, 84, 85, 87, 90, 92, 97, 107, 110, 114, 117, 118, 119, 120, 127, 129, 130, 133, 136, 137, 138, 149, 152, 155, 163, 170, 171, 174, 177, 180, 184, 186, 192, 193, 199, 203, 208, 221, 230, 234, 238, 250, 251, 253, 255, 258, 259, 268, 270, 274, 275, 276, 281, 282, 283, 290, 293, 295, 298, 299, 303, 309, 313, 322, 323, 324, 328, 342, 343, 346, 353, 354, 355, 365, 366, 371, 376, 377, 379, 386, 391, 396, 400, 411, 414, 415, 433, 438, 441, 449, 451, 462, 465, 468, 472, 477, 484, 486, 502, 509, 510, 513, 515, 516, 521, 522, 525, 527, 550, 558, 565, 577, 581, 587, 588, 596, 599, 600, 603, 604, 605, 609, 614, 616, 617, 624, 627, 630, 635, 642, 648, 654, 655, 663, 666, 670, 671, 673, 674, 677, 678, 680, 681, 691, 699, 702, 707, 709, 711, 721, 726, 729, 730, 736, 738, 745, 754, 759, 762, 764, 765, 769, 772, 777, 780, 787, 789, 798, 805, 808, 809, 820, 821, 823, 824, 832, 834, 835, 836, 837, 838, 844, 845, 847, 848, 850, 854, 863, 867, 868, 875, 876, 880, 892, 898, 902, 903, 906, 908, 910, 915, 919, 927, 929, 935, 937, 938, 941, 942, 944, 945, 946, 960, 962, 969, 970, 973, 975, 979, 982, 983, 984, 985, 992, 996, 998, 1000]))
endTime = datetime.datetime.now()
duration = endTime - startTime
print(duration.microseconds)
print("findMaxSubArray, duration: " + str(duration.microseconds))


print("\n")
print("#80")
#80 here is when recursive approach starts perfom better then brute force approach
startTime = datetime.datetime.now()
print(findMaxSubArrayBruteForce([-987, -980, -961, -912, -876, -858, -823, -789, -744, -739, -731, -720, -673, -665, -644, -530, -510, -479, -474, -451, -408, -405, -395, -383, -363, -356, -328, -322, -282, -270, -244, -226, -216, -211, -210, -198, -164, -116, -83, -77, -55, -30, 1, 43, 70, 84, 146, 165, 236, 250, 266, 271, 281, 297, 320, 358, 360, 381, 464, 470, 506, 512, 517, 519, 523, 539, 609, 631, 634, 751, 759, 783, 787, 807, 816, 836, 840, 875, 882, 903]))
endTime = datetime.datetime.now()
duration = endTime - startTime
print("findMaxSubArrayBruteForce, duration: " + str(duration.microseconds))

startTime = datetime.datetime.now()
print(findMaxSubArray([-987, -980, -961, -912, -876, -858, -823, -789, -744, -739, -731, -720, -673, -665, -644, -530, -510, -479, -474, -451, -408, -405, -395, -383, -363, -356, -328, -322, -282, -270, -244, -226, -216, -211, -210, -198, -164, -116, -83, -77, -55, -30, 1, 43, 70, 84, 146, 165, 236, 250, 266, 271, 281, 297, 320, 358, 360, 381, 464, 470, 506, 512, 517, 519, 523, 539, 609, 631, 634, 751, 759, 783, 787, 807, 816, 836, 840, 875, 882, 903]))
endTime = datetime.datetime.now()
duration = endTime - startTime
print("findMaxSubArray, duration: " + str(duration.microseconds))

print("\n")
print("#50")
startTime = datetime.datetime.now()
print(findMaxSubArrayBruteForce([-962, -949, -919, -882, -857, -853, -851, -844, -828, -815, -783, -755, -733, -697, -694, -685, -592, -546, -461, -458, -420, -323, -156, -140, -113, -61, -38, 50, 55, 106, 179, 204, 244, 261, 267, 281, 417, 497, 498, 579, 732, 741, 806, 828, 829, 867, 892, 919, 921, 948
]))
endTime = datetime.datetime.now()
duration = endTime - startTime
print("findMaxSubArrayBruteForce, duration: " + str(duration.microseconds))

startTime = datetime.datetime.now()
print(findMaxSubArray([-962, -949, -919, -882, -857, -853, -851, -844, -828, -815, -783, -755, -733, -697, -694, -685, -592, -546, -461, -458, -420, -323, -156, -140, -113, -61, -38, 50, 55, 106, 179, 204, 244, 261, 267, 281, 417, 497, 498, 579, 732, 741, 806, 828, 829, 867, 892, 919, 921, 948
]))
endTime = datetime.datetime.now()
duration = endTime - startTime
print("findMaxSubArray, duration: " + str(duration.microseconds))


print(findMaxSubArrayLinear([-962, -949, -919, -882, -857, -853, -851, -844, -828, -815, -783, -755, -733, -697, -694, -685, -592, -546, -461, -458, -420, -323, -156, -140, -113, -61, -38, 50, 55, 106, 179, 204, 244, 261, 267, 281, 417, 497, 498, 579, 732, 741, 806, 828, 829, 867, 892, 919, 921, 948
]))