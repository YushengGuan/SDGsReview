# -*- coding: utf-8 -*-
import PyPDF2

def read_pdf(file_path):
    # print(f"正在打开PDF文件: {file_path}")
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text


def read_pdf_no_ref(file_path):
    text_all = read_pdf(file_path)
    if 'References' in text_all:
        id = text_all.find('References')
    else:
        id = -1
    return text_all[:id]

if __name__ == '__main__':
    # 使用函数
    pdf_text = read_pdf_no_ref('article_for_test.pdf')
    print(pdf_text)
