import dendropy 
import os.path

def sequence_reader(filepath):

    assert os.path.exists(filepath)
    
    sequence_set = dendropy.DNACharacterMatrix.get(
        path = filepath
        schema="phylip")
    
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    
    return(sequence_set)