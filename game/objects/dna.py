from .fraction import fraction
from random import choice


class DNA:
    pass


class DNA:
    """
    All species' features are fractions.
    DNA can be generated at random
    or can be inherited from parent
    with small mutations.
    """
    mutate_ratio: fraction
    hp: fraction
    speed: fraction
    size: fraction
    breed_period: fraction
    lifetime: fraction
    foo: fraction

    def __init__(self, parent: DNA = None):
        """
        Creates brand new dna or uses parent's mutated one 
        to create it's own.
        """
        if parent:
            self._get_features_from_parent(**parent.mutate())
        else:
            self = self.random_dna()
        
        self.color = self._unique_color()
    
    def mutate(self):
        """
        Takes parent's mutate ratio and creates new DNA 
        with features differing by this ratio.
        """
        child_dna = {}
        for feature, value in self.__dict__.items():
            if feature != 'color':
                mutation = self._get_mutation(value)
                child_dna[feature] = fraction(mutation)
        
        return child_dna
    
    def _get_features_from_parent(self, **features):
        """
        Sets all features received from 
        parent's mutate method.
        """
        for feature, value in features.items():
            self.__setattr__(feature, value)
    
    def _get_mutation(self, value):
        """
        Generates polarized mutation ratio
        """
        polarization = choice([-1, 1])
        mutation = self.mutate_ratio * polarization
        return value + mutation * value
    
    def _unique_color(self):
        """
        Create unique 24-bit hex "color hash" from all features.
        """
        bits_num = 24
        features_num = len(self.__dict__)
        bits_per_feature = int(bits_num / features_num)
        filled_bits_num = bits_per_feature * features_num
        final_binary = ''
        for value in self.__dict__.values():
            fill_chunk = 1.0 / bits_per_feature
            chunks_num = int(value / fill_chunk)
            chunks_num_bin = str(bin(chunks_num)).lstrip('0b')
            chunks_num_bin = '0' * (bits_per_feature - len(chunks_num_bin)) + chunks_num_bin
            final_binary = final_binary + chunks_num_bin
        
        final_binary = '0b' + '0' * (bits_num - filled_bits_num) + final_binary
        unique_color = str(hex(int(final_binary, 2)))
        unique_color = unique_color[2:]
        zeros_to_add = 6 - len(unique_color)
        unique_color = '0x' + '0' * zeros_to_add + unique_color
        return unique_color

    def random_dna(self):
        """
        Takes all annotations from class
        and if it's declared type is fraction
        - then generates random fraction.
        """
        annotations = self.__class__.__annotations__
        for feature, feature_type in annotations.items():
            if feature_type == fraction:
                self.__setattr__(feature, fraction.random())
        return self
    
    def __str__(self):
        return '\n'.join(
            [f'{feature}: {fraction}' 
            for feature, fraction in self.__dict__.items()]
        )
