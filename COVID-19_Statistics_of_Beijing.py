### Beijing Novel CoronaVirus statistics ###
''' Data before Feburary is recorded on its date of symptoms.
    Data in and after Feburary is recorded on its comfirmed/reported date.
    Note: A 2.24 comfirmed head was reported on 6.2 and was cured on an unknow date, recorderd on 6.2;
          On 2.13, 1 died from other disease;
          On 4.26, add 1 addition died case.
'''

%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime


## Prepare X axis - Date ##
start_date = datetime.datetime(2020, 1, 9)
end_date = datetime.datetime(2020, 8, 25)
dates = []
date = start_date
while date<=end_date:
    dates.append(date.strftime('%Y-%m-%d'))
    date = date + datetime.timedelta(days=1)

    
## Prepare Y axis - Toll ##
def accumulate(addition_list):
    accumulated_list = [addition_list[0]]
    for i in range(1,len(addition_list)):
        accumulated_list.append(accumulated_list[-1] + addition_list[i])
    return accumulated_list


newly_confirmed = [1,2,1,
    1,3,5,1,4,3,11,
    6,8,7,19,13,22,12,
    5,29,10,19,8,1,
        0,
        21,16,25,21,23,18,11,
        11,5,10,14,6,3,5,
        1,6,6,2,1,3,0,
        0,2,0,10,0,1,2,
    1,0,3,1,4,4,2,
    0,1,6,0,1,1,5,
    4,9,3,21,6,14,13,
    10,32,5,6,4,3,4,
    1,3,0,
        2,1,2,1,
        1,0,1,0,0,1,0,
        0,0,1,3,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,
    0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,
        0,0,0,0,0,
        0,0,0,0,0,1,6,
        36,36,27,31,21,25,22,
        22,9,13,7,13,11,17,
        14,7,7,3,
    1,2,1,2,
    1,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,2,1,1,0,0,
        0,
        0,0,1,0,1,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0]

newly_cured = [0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,1,1,
    0,0,2,0,1,0,
        4,
        3,11,1,7,2,1,3,
        7,4,8,12,11,18,8,
        9,8,23,8,16,9,11,
        9,17,20,13,9,14,5,
    6,6,6,3,1,5,5,
    7,5,6,8,8,7,4,
    5,10,5,6,5,8,6,
    2,1,0,2,3,3,2,
    1,4,2,
        6,10,4,3,
        2,5,7,9,5,5,5,
        5,7,4,8,6,0,1,
        4,2,2,4,2,1,0,
        0,11,2,4,5,
    0,4,
    2,1,1,2,3,3,2,
    3,3,2,1,0,2,1,
    1,0,0,1,0,0,2,
    0,0,0,0,0,0,0,
    0,
        0,1,1,0,0,
        0,0,1,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,1,0,
        0,0,1,1,
    2,3,2,1,
    1,4,13,32,12,12,11,
    14,21,14,23,10,13,13,
    16,12,17,8,14,12,11,
    3,14,1,5,10,4,
        2,
        0,1,1,0,1,0,0,
        0,0,0,0,2,1,0,
        0,1,0,0,0,0,0,
        0,0,2]

newly_death = [0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,1,0,0,0,0,
        0,
        0,0,0,0,0,1,0,
        0,1,0,0,1,1,0,
        0,0,0,0,0,0,0,
        0,0,0,1,2,1,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,
        0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,
    0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,
        0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,
    0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,
        0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0]
total_confirmed = accumulate(newly_confirmed)
total_cured = accumulate(newly_cured)
total_death = accumulate(newly_death)
current_confirmed =[total_confirmed[i] - total_cured[i] - total_death[i] for i in range(len(total_confirmed))]


## Plot Figures ##
def formatter(x, pos):  # used in format the x axis label
    x = int(x)
    if x>=0 and x<len(dates):
        return dates[x]
    else:
        return None

plt.figure(figsize=(16,12))
plt.title("Beijing Novel CoronaVirus statistics (per Beijing Municipal Health Commission)")
plt.xlabel('Date')
plt.ylabel('Toll') 

# Set the display of major/minor x axis tick labels
# plt.xticks(range(0,len(dates)), dates, rotation=30, ha='right') 
ax = plt.gca() # get current axe
ax.xaxis.set_major_locator(plt.MultipleLocator(7))  # major locator with interval 7
# ax.xaxis.set_minor_locator(plt.MultipleLocator(1))  # minor locator with interval 1
ax.xaxis.set_minor_formatter(plt.FuncFormatter(formatter))
plt.xticks(rotation=30, ha='right')
# plt.setp(ax.xaxis.get_minorticklabels(), rotation=30, ha='right')
# plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha='right')

# plot curves
plt.plot(dates, total_confirmed, color="blue", linestyle="-", marker='o', label='total confirmed')
plt.plot(dates, total_cured, color="green", linestyle="-", label='total cured')
plt.plot(dates, total_death, color="gray", linestyle="-", label='total death')
plt.plot(dates, current_confirmed, color="red", linestyle="-", label='current confirmed')
plt.plot(dates, newly_confirmed, color="blue", linestyle='--', label='newly confirmed')
plt.plot(dates, newly_cured, color="green", linestyle='--', label='newly cured')
plt.plot(dates, [0 for i in range(len(dates))], color="black", linestyle='-')

# mark the lastest number
plt.plot(dates[-1], total_confirmed[-1], color="blue", marker='o')
plt.annotate(total_confirmed[-1], xy=(dates[-1],total_confirmed[-1]))
plt.plot(dates[-1], current_confirmed[-1], color="red", marker='o')
plt.annotate(current_confirmed[-1], xy=(dates[-1],current_confirmed[-1]))
plt.plot(dates[-1], total_cured[-1], color="green", marker='o')
plt.annotate(total_cured[-1], xy=(dates[-1],total_cured[-1]))
plt.plot(dates[-1], total_death[-1], color="gray", marker='o')
plt.annotate(total_death[-1], xy=(dates[-1],total_death[-1]))

# mark the highest number
def mark_summit(seq, color):
    max_value = max(seq)
    max_value_index = seq.index(max_value)
    plt.plot(max_value_index, max_value, color=color, marker="o")
    plt.annotate(max_value, xy=(max_value_index, max_value), textcoords='offset points', xytext=(-10,5))

mark_summit(current_confirmed, "red")
mark_summit(newly_confirmed, "blue")
mark_summit(newly_cured, "green")

plt.legend(loc='upper left', frameon=True)
# plt.grid(which='major', axis='x')  # show the align grid on figure
plt.grid(which='major', axis='y')  # show the align grid on figure
# for a, b in zip(dates, total_confirmed):  # show number on points of plot
#     plt.text(a, b, b, horizontalalignment='right', verticalalignment='bottom', fontsize=13)

# rainbow background by month
plt.axvspan(0, 22, facecolor='red', alpha=0.1)
plt.axvspan(22, 51, facecolor='orange', alpha=0.1)
plt.axvspan(51, 82, facecolor='yellow', alpha=0.1)
plt.axvspan(82, 112, facecolor='green', alpha=0.1)
plt.axvspan(112, 143, facecolor='cyan', alpha=0.1)
plt.axvspan(143, 173, facecolor='blue', alpha=0.1)
plt.axvspan(173, 204, facecolor='purple', alpha=0.1)
plt.axvspan(204, len(dates), facecolor='black', alpha=0.1)
    
# plt.savefig('BJ19nCoV.png')
plt.show()