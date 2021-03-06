# Open Story License
#
# Story: stringer
# Writer: Kalab J. Oster(TM)
# Copyright Holders: Kalab J. Oster(TM)
# copyright (C) 2017 Kalab J. Oster(TM)
#
# Permission is granted by the Copyright Holders for humans or other intelligent agents to read, write, edit, publish and critique the Story
# if the humans or intelligent agents keep this Open Story License with the Story,
# and if the Story you tell remains free,
# and if another writer writes or edits the Story then the writer's name needs to be appended to the end of the Writer list of this Open Story License.

'''
Tests for permutations.
'''
import stringer.utils.permutate_utils as perm

def test_permutations_short_string():

    perm_list1 = perm.generate("aaa")
    perm_list2 = perm.generate("cake")
    perm_list3 = perm.generate("banana")

    assert ['aaa', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa'] == perm_list1
    assert ['cake', 'caek', 'ckae', 'ckea', 'ceak', 'ceka', 'acke', 'acek', 'akce', 'akec', 'aeck', 'aekc', 'kcae',
            'kcea', 'kace', 'kaec', 'keca', 'keac', 'ecak', 'ecka', 'eack', 'eakc', 'ekca', 'ekac'] == perm_list2
    assert "anaban" == perm_list3[714]