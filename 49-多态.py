# 多态：关注的是同一个方法，但是会出现不同的表现形式，提示：在python里面不需要关心类型


class Text(object):
    def show(self):
        print("显示文字")


class Image(object):
    def show(self):
        print("显示图片")


class Video(object):
    def show(self):
        print("显示视频")


# 实现显示数据的功能
def show_data(data):
    data.show()


image = Image()
video = Video()
show_data(video)

