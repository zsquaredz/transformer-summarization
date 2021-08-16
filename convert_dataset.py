# this script is used to convert existing dataset to the required dataset format for this repo
# the default format of the required format need to be converted to: Each line of the document has two parts: source and target separated by tab symbol

def convert_txt_to_tsv(file_article, file_summary, file_output):
    with open(file_article, 'r', encoding='utf-8') as f_article, open(file_summary, 'r', encoding='utf-8') as f_summary,\
    open(file_output, 'w', encoding='utf-8') as f_out:
        line_article = f_article.readline()
        line_summary = f_summary.readline()
        while line_article and line_summary:
            f_out.write(line_article.strip()+'\t'+line_summary.strip())
            line_article = f_article.readline()
            line_summary = f_summary.readline()

if __name__ == '__main__':
    print('starting to convert')
    convert_txt_to_tsv('/disk/ocean/zheng/A_distance/data/cnndm_xsum/train.source',
                       '/disk/ocean/zheng/A_distance/data/cnndm_xsum/train.target',
                       'dataset/cnndm_xsum/train.tsv')
    print('training done')
    convert_txt_to_tsv('/disk/ocean/zheng/A_distance/data/cnndm_xsum/val.source',
                       '/disk/ocean/zheng/A_distance/data/cnndm_xsum/val.target',
                       'dataset/cnndm_xsum/val.tsv')
    print('val done')
    convert_txt_to_tsv('/disk/ocean/zheng/A_distance/data/cnndm_xsum/test.source',
                       '/disk/ocean/zheng/A_distance/data/cnndm_xsum/test.target',
                       'dataset/cnndm_xsum/test.tsv')
    print('test done')