import transformers

MAX_LEN = 512
train_batch_file = 8
valid_batch_size = 4
epoches = 10
#accumulation = 2
BERT_PATH = "../input/bert_base_uncased/"
MODEL_PATH = "model.bin"
TRAINING_FILE = "../input/imdb Dataset.csv"
tokenizer = transformers.BertTokenizer.form_pretrained(
    BERT_PATH,
    do_lower_case = True
)

