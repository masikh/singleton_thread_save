import threading
import time
mutex = threading.Lock()


def singleton(_class):
    _instance = {}

    def wrap(*args, **kwargs):
        with mutex:
            if _class not in _instance:
                _instance[_class] = _class(*args, **kwargs)
        return _instance[_class]
    return wrap

#
# Example usage
#

@singleton
class Test(object):
    def _init_(self, name):
        self.name = name

def run(now, i, name):
    print('thread {i} {name} running'.format(i=i, name=name))
    while int(time.time() - 1) < now:
        time.sleep(0.00001)
    t = Test(name)
    print(i, name, t.name)


if __name__ == '__main__':
    names = ['aap', 'noot', 'mies', 'teun', 'vuur', 'gijs', 'wim', 'weide', 'does', 'kip']
    threads = {}
    now = int(time.time())
    for i in range(0, 10):
        threads[i] = threading.Thread(target=run, args=(now, i, names[i],))
        threads[i].start()
       
