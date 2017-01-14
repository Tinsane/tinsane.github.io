import re


def main():
    fnum = 20
    with open('dumps.txt', 'r') as f:
        lines = f.readlines()
    with open('template.txt', 'r') as f:
        template = f.read()
    dump = ''
    content = ''
    for line in lines:
        if line.startswith('Frame') and line:
            with open('dump%d.html' % fnum, 'w') as f:
                f.write(template % (dump, content))
            fnum += 1
            dump = ''
            content = ''
        if re.match(r'[\da-f]{4}', line):
            dump += line.split('   ')[0]
            dump += '\n'
        else:
            content += line
    with open('dump%d.html' % fnum, 'w') as f:
        f.write(template % (dump, content))
    fnum += 1
    dump = ''
    content = ''
    print(fnum)


if __name__ == '__main__':
    main()
