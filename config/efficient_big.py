from models.attention import EfficientAttentionModel


# Data generation
shuffle_entities = True
shuffle_questions = True
concat_ctx_and_question = False
concat_question_before = False
sort_batch_count = 20
vocab_size = 29958
n_entities = 550
batch_size = 32

# Architecture
embedding_size = 512
n_hidden_que = 512
n_hidden_con = 512
n_out_hidden = 512
depth_rnn = 1
grad_clipping = 10
model = EfficientAttentionModel(
    vocab_size=vocab_size,
    embedding_size=embedding_size,
    n_hidden_que=n_hidden_que,
    n_hidden_con=n_hidden_con,
    n_out_hidden=n_out_hidden,
    n_entities=n_entities,
    depth_rnn=depth_rnn,
    grad_clipping=grad_clipping)

# Trianing
algo = 'adam'
learning_rate = 0.0003

# Monitoring
train_freq_print = 100
valid_freq_print = 1000
dump_every_batches = 10000