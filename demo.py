import statistics as stats
import math


def Mean(args) -> list:
    return f"{round(sum(args)/len(args),3)}"

def HarmonicMean(args) -> list:
    s = 0
    for i in range(0,len(args)):
        a = 1/(args[i])
        s += a
    return f"{round(len(args)/s,3)}"

def GeometricMean(args) -> list:
    p = 1
    for i in range(0,len(args)):
        a = args[i]
        p *= a
    return f"{round(p**(1/len(args)),3)}"

def Mode(args) -> list:
    return f"{round(stats.mode(args),3)}"

def Range(args) -> list:
    return f"{max(args)-min(args)}"

def Product(args) -> list:
    p = 1
    for i in range(0,len(args)):
        p *= args[i]
    return f"{p}"

def SquareSum(args) -> list:
    s = 0
    for i in range(0,len(args)):
        sq = args[i]**2
        s += sq
    return f"{s}"

def StandardDeviation(args) -> list:
    mean = round(sum(args)/len(args),3)
    rep = []
    for i in range(0,len(args)):
        a = (args[i]-mean)**2
        rep.append(a)
    total = sum(rep)
    return (round(math.sqrt(total/(len(args)-1)),3))

def Median(args) -> list:
    if len(args)%2 == 0:
        mid1 = int(len(args)/2)
        mid2 = mid1-1
        return (args[mid1]+args[mid2])/2
    else:
        mid = int(len(args)/2)
        return args[mid]

def MeanDeviation(args) -> list:
    mean = round(sum(args)/len(args),3)
    rep = []
    for i in range(0,len(args)):
        a = abs(args[i]-mean)
        rep.append(a)
    total = sum(rep)
    return round(total/len(args),3)

def Variance(args) -> list:
    mean = round(sum(args)/len(args),3)
    rep = []
    for i in range(0,len(args)):
        a = (args[i]-mean)**2
        rep.append(a)
    total = sum(rep)
    return round(total/(len(args)-1),3)

def RMS(args) -> list:
    rep = []
    for i in range(0,len(args)):
        a = args[i]**2
        rep.append(a)
    total = sum(rep)
    return round(math.sqrt(total/len(args)),3)

def LR(args,kwargs) -> list:
    if len(args) == len(kwargs):
        y = sum(kwargs)
        x = sum(args)
        xy = 0
        x2 = 0
        for i in range(0,len(args)):
            a = args[i]**2
            b = args[i]*kwargs[i]
            xy += b
            x2 += a
        N1 = y*x2-x*xy
        D1 = len(args)*x2-x**2
        intercept = round(N1/D1,3)
        N2 = len(args)*xy-x*y
        D2 = len(args)*x2-x**2
        slope = round(N2/D2,3)
        return f"Intercept: {intercept}\nSlope: {slope}\ny = {slope}x + {intercept}"
    else:
        return "Length of the both parameters should be euqal"

def StandardError(args) -> list:
    dev = StandardDeviation(args)
    return round(dev/math.sqrt(len(args)),3)

def RelativeFrequency(args) -> list:
    rel = []
    freq = {}
    for item in args:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    f = list(freq.values())
    for i in range(0,len(f)):
        r = f[i]/len(args)
        rel.append(r)
    return f"{freq}\n{rel}"

def CorrelationCoefficient(args,kwargs) -> list:
    if len(args) == len(kwargs):
        y = sum(kwargs)
        x = sum(args)
        xy = 0
        x2 = 0
        y2 = 0
        for i in range(0,len(args)):
            a = args[i]**2
            b = args[i]*kwargs[i]
            c = kwargs[i]**2
            x2 += a
            xy += b
            y2 += c
        N = len(args)*xy-x*y
        D = math.sqrt((len(args)*x2-x**2)*(len(args)*y2-y**2))
        return f"{round(N/D,3)}"
    else:
        return "Length of the both parameters should be euqal"

def CoefficientDetermination(args,kwargs) -> list:
    if len(args) == len(kwargs):
        x = sum(args)
        y = sum(kwargs)
        x2 = 0
        y2 = 0
        xy = 0
        for i in range(0,len(args)):
            a = args[i]**2
            b = args[i]*kwargs[i]
            c = kwargs[i]**2
            x2 += a
            y2 += c
            xy += b
        N = len(args)*xy-x*y
        D = math.sqrt((len(args)*x2-x**2)*(len(args)*y2-y**2))
        return f"{round(N/D,3)}"
    else:
        return "Length of the both parameters should be euqal"
