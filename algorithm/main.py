from matplotlib import pyplot as plt
import convex
class Main(object):
    """docstring for main"""
    def __init__(self):
        super(Main, self).__init__()
        #self.main()
        #self.test_speed()
        self.plot_time_cost()

    def test_time(self, number):
        convex = Convex()
        points = convex.get_points(number)
        
        graham_time_start = time.time()
        stack = convex.graham(points)
        graham_time_end = time.time()
        print 'Done graham '
        dc_time_start = time.time()
        hcq = convex.divideConquer(points)
        dc_time_end = time.time()
        print 'Done dc'
        force_time_srart = time.time()
        force, ans = convex.force(points)
        force_time_end = time.time()
        print 'Done force'
        t1 = force_time_end - force_time_srart
        t2 = graham_time_end - graham_time_start
        t3 = dc_time_end - dc_time_start
        
        plt.title('Convex Hull')
        plt.subplot(221)
        plt.title('{} samples running time'.format(str(len(points))), fontsize=10)
        plt.ylabel(u'Time cost/s')
        rects = plt.bar([1, 2, 3],list([t1, t2, t3]), width=0.35, facecolor = 'lightskyblue',edgecolor = 'white', align="center", alpha=0.8)
        plt.xticks(np.array([1,2,3]) , ('Force', 'Graham scan', 'DC'), fontsize=8)
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2., 1.03 * height, '%.2f' % float(height), fontsize=4)

        #plt.xticks(x, xticks1, size='small', rotation=30)
        plt.subplot(222)
        plt.title('Force', fontsize=10)
        plt.scatter([item.x for item in points], [item.y for item in points],  marker='x', s=0.5)
        for item in ans:
            plt.plot([item.start.x, item.end.x], [item.start.y, item.end.y], linewidth=2)
        plt.subplot(223)
        plt.title('Graham Scan', fontsize=10)
        plt.scatter([item.x for item in points], [item.y for item in points], marker='x', s=0.5)
        plt.plot([stack.stack[0].x, stack.stack[-1].x], [stack.stack[0].y, stack.stack[-1].y])
        for i in range(1, len(stack.stack)):
            plt.plot([stack.stack[i - 1].x, stack.stack[i].x], [stack.stack[i - 1].y, stack.stack[i].y], linewidth=2)
        plt.subplot(224)
        plt.title('Divide and Conquer', fontsize=10)
        plt.scatter([item.x for item in points], [item.y for item in points], marker='x', s=0.5)
        plt.plot([hcq.stack[0].x, hcq.stack[-1].x], [hcq.stack[0].y, hcq.stack[-1].y])
        for i in range(1, len(stack.stack)):
            plt.plot([hcq.stack[i - 1].x, hcq.stack[i].x], [hcq.stack[i - 1].y, hcq.stack[i].y], linewidth=2)
        plt.savefig('{}-samples.png'.format(len(points)), dpi=1000)
        #plt.show()

        return force_time_end - force_time_srart, graham_time_end - \
            graham_time_start, dc_time_end - dc_time_start, points

    def main(self):
        t1, t2, t3, points = self.test_time(4000)
        pass
    
    def test_speed(self):
        convex = Convex()
        f = open('time.csv', 'w')
        f.write('Samples,GrahamScan,DC\n')
        #number_size = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 10000, 15000, 20000, 25000, 30000, 100000, 200000, 300000, 1000000]
        number_size = []
        i = 10000
        while i < 100000000:
            number_size.append(i)
            i = i + 10000
            pass

        for i in range(0, len(number_size)):
            print 'number_size{}'.format(number_size[i])
            points = convex.get_points(number_size[i])
            
            graham_time_start = time.time()
            stack = convex.graham(points)
            graham_time_end = time.time()
            print 'Done graham '
            dc_time_start = time.time()
            hcq = convex.divideConquer(points)
            dc_time_end = time.time()
            print 'Done dc'
            g_time = graham_time_end - graham_time_start
            dc_time = dc_time_end - dc_time_start
            f.write("{},{},{}\n".format(str(number_size[i]), str(g_time), str(dc_time)))

    def plot_time_cost(self):
        f = open('time.csv')
        count = 0
        time = []
        graham = []
        dc = []

        for item in f.readlines():
            if count == 0:
                count += 1 
                continue
            item = item.replace('\n', '')
            item = item.split(',')
            time.append(int(item[0]))
            graham.append(float(item[1]))
            dc.append(float(item[2]))
        label = ['GrahamScan', 'DC']
        rec = plt.title('Time cost')
        plt.plot(time, graham)
        plt.plot(time, dc)
        plt.legend(label, loc=0)
        plt.xlabel('Sample number')
        plt.ylabel('Time /s')
        plt.savefig('timecost.png', dpi=800)
        plt.show()

if __name__ == '__main__':
    main = Main()