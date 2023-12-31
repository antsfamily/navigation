import pyaibox as pb


srclinks = ['"https://iridescent.ink/"', '"https://iridescent.ink/torchbox"', '"https://iridescent.ink/pyaibox"', '"https://iridescent.ink/HowToMakeDocs"']
dstlinks = ['"https://www.iridescent.ink"', '"https://torchbox.iridescent.ink"', '"https://pyaibox.iridescent.ink"', '"https://mkdocs.iridescent.ink"']

htmlfiles = pb.listxfile('./_site/', exts='.html', recursive=True)

for htmlfile in htmlfiles:
    txtstr = pb.readtxt(htmlfile, mode='all')
    for srclink, dstlink in zip(srclinks, dstlinks):
        txtstr = txtstr.replace(srclink, dstlink)
        print(htmlfile)

    pb.writetxt(htmlfile, txtstr)

