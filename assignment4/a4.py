show_views_file = sc.textFile("input/join2_gennum?.txt")
#show_views_file.take(2)

def split_show_views(line):
    line = line.split(",")
    show = line[0]
    views = int(line[1])
    return(show,views)

show_views = show_views_file.map(split_show_views)

show_channel_file = sc.textFile("input/join2_genchan?.txt")

def split_show_channel(line):
    line = line.split(",")
    show = line[0]
    channel = line[1]
    return(show,channel)

show_channel = show_channel_file.map(split_show_channel)

joined_dataset=show_channel.join(show_views)
#joined_dataset.take(3)

def extract_channel_views(show_views_channel):
    channelViews = show_views_channel[1]
    return channelViews

channel_views = joined_dataset.map(extract_channel_views)

from operator import add
result = channel_views.reduceByKey(add).collect()

