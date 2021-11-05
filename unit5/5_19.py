# 创建临时文件和文件夹

from tempfile import TemporaryFile
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


def temp_file_test():
    with TemporaryFile('w+t') as f:
        # Read/write to the file
        f.write('Hello World\n')
        f.write('Testing\n')

        # Seek back to beginning and read the data
        f.seek(0)
        data = f.read()
        print(data)

    # Temporary file is destroyed


def create_watermark(content):
    """水印信息"""
    # 默认大小为21cm*29.7cm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    pdfmetrics.registerFont(TTFont('song', 'STSONG.ttf'))
    file_name = "mark.pdf"
    c = canvas.Canvas(file_name, pagesize=(21 * cm, 29.7 * cm))
    # 移动坐标原点(坐标系左下为(0,0))
    c.translate(5 * cm, 10 * cm)

    # 设置字体

    c.setFont("song", 20)
    # 指定描边的颜色
    c.setStrokeColorRGB(0, 1, 0)
    # 指定填充颜色
    c.setFillColorRGB(0, 1, 0)
    # 画一个矩形
    # c.rect(cm, cm, 7*cm, 17*cm, fill=1)
    # 旋转45度,坐标系被旋转
    c.rotate(30)
    # 指定填充颜色
    c.setFillColorRGB(0, 0, 0, 0.1)
    # 设置透明度,1为不透明
    # c.setFillAlpha(0.1)
    # 画几个文本,注意坐标系旋转的影响
    c.drawString(3 * cm, 0 * cm, content)

    c.translate(0 * cm, 5 * cm)
    c.drawString(3 * cm, 0 * cm, content)
    c.setFillAlpha(0.6)
    # 关闭并保存pdf文件
    c.save()
    return file_name


def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    """把水印添加到pdf中"""
    pdf_output = PdfFileWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(input_stream, strict=False)

    # 获取PDF文件的页数
    pageNum = pdf_input.getNumPages()

    # 读入水印pdf文件
    pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.getPage(i)
        page.mergePage(pdf_watermark.getPage(0))
        page.compressContentStreams()  # 压缩内容
        pdf_output.addPage(page)
    pdf_output.write(open(pdf_file_out, 'wb'))


def temp_pdf_test():
    pass


if __name__ == '__main__':
    print('Leyton Yu')
    pdf_file_in = r'D:\下载\温州大学_16计算机_傅航飞_1 .pdf'
    pdf_file_out = 'watermark.pdf'
    pdf_file_mark = create_watermark('青塔人才')

    # add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)
