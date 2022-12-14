
def calendar_array(dates, data):
    i, j = zip(*[d.isocalendar()[1:] for d in dates])
    i = np.array(i) - min(i)
    j = np.array(j) - 1
    ni = max(i) + 1

    calendar = np.nan * np.zeros((ni, 7))
    calendar[i, j] = data
    return i, j, calendar


def calendar_heatmap(ax, dates, data, overall_max, show_color_bar = True):
    i, j, calendar = calendar_array(dates, data)
    im = ax.imshow(calendar, interpolation='none', cmap='summer',
                   vmin = 0, vmax = overall_max)
    label_days(ax, dates, i, j, calendar)
    label_months(ax, dates, i, j, calendar)
    
    if show_color_bar:
        ax.figure.colorbar(im)
    
    ax.spines['bottom'].set_color('lightgreen')
    ax.spines['top'].set_color('lightgreen') 
    ax.spines['right'].set_color('lightgreen')
#     ax.spines['right'].set_linewidth(3)
    ax.spines['left'].set_color('lightgreen')
#     ax.spines['left'].set_lw(3)
    ax.xaxis.label.set_color('lightgreen')
    ax.yaxis.label.set_color('lightgreen')
    ax.tick_params(colors='lightgreen', which='both')

def label_days(ax, dates, i, j, calendar):
#     ni, nj = calendar.shape
#     day_of_month = np.nan * np.zeros((ni, 7))
#     day_of_month[i, j] = [d.day for d in dates]

#     for (i, j), day in np.ndenumerate(day_of_month):
#         if np.isfinite(day):
#             ax.text(j, i, int(day), ha='center', va='center')

    ax.set(xticks=np.arange(7), 
           xticklabels=['M', 'T', 'W', 'R', 'F', 'S', 'S'])
    
    ax.xaxis.tick_top()

def label_months(ax, dates, i, j, calendar):
    month_labels = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                             'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    months = np.array([d.month for d in dates])
    uniq_months = sorted(set(months))
    yticks = [i[months == m].mean() for m in uniq_months]
    labels = [month_labels[m - 1] for m in uniq_months]
    ax.set(yticks=yticks)
    ax.set_yticklabels(labels, rotation=90)