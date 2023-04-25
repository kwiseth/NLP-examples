# Ling 165 Lab 1 kwiseth Feb and Mar... and April 2013
# probs.py
# Methods to calculate expected frequency
# based on probabilities using three different
# smoothing algorithms.
# Was toying with the idea of using default values
# in method signatures (since the we're passing the
# dictionaries to the methods), but since we're only
# looking for 10 values, this is likely okay.

def get_mle (bigram, train_dict, train_tokens_ct, test_tokens_ct):
    if bigram in train_dict:
        train_ct = train_dict[bigram]
        mle_prob = float(train_ct)/float(train_tokens_ct)
        exp_f_mle = float(mle_prob) * float(test_tokens_ct)
    else:
        exp_f_mle = 0
    return exp_f_mle


def get_one (bigram, train_dict, vocab, test_tokens_ct):
    if bigram in train_dict:
        train_ct = train_dict[bigram]
    else:
        train_ct = 0
    one_prob = float(train_ct + 1)/float(len(train_dict) + len(vocab)**2)
    exp_f_one = float(one_prob) * float(test_tokens_ct)
    return exp_f_one



def get_sgt (bigram, train_dict, train_tokens_ct, train_hapax, vocab, adj_freq_dict, test_tokens_ct):
    poss_bgm_B = len(vocab)**2

    if bigram in train_dict:
        sgt_prob = adj_freq_dict[bigram]/train_tokens_ct
    else:
        sgt_prob = train_hapax/(poss_bgm_B-len(train_dict))*train_tokens_ct

    exp_f_sgt = sgt_prob * test_tokens_ct
    return exp_f_sgt
