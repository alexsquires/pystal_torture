from pymatgen.core import Structure
import random

"Simple functions for manipulating and doping a pymatgen structure"


def count_sites(structure, species=None, labels=None):
    """
     Given structure object and either specie string or label string,  it counts and returns the 
     number of sites with that species or label (or  both) in the structure

     Args:
         - structure (Structure): pymatgen structure object
         - species   ({str}): site species to count
         - labels     ({str}): site labels to count

     Returns:
         - (int): number of sites occupied by species or label (or both) in structure
    """

    if labels and species:
        return len(
            [
                i
                for i, site in enumerate(structure)
                if ((site.label in labels) and (site.species_string in species))
            ]
        )
    elif species and not labels:
        return len(
            [i for i, site in enumerate(structure) if site.species_string in species]
        )
    elif labels and not species:
        return len([i for i, site in enumerate(structure) if site.label in labels])
    else:
        raise ValueError("Need to supply either specie, or label to count_sites")


def index_sites(structure, species=None, labels=None):
    """
    Return a list of the site indices in a structure that are occupied by specie or label (or both)

     Args:
         - structure (Structure): pymatgen structure object
         - species   ({str}): site species to count
         - label     ({str}): site label to count

     Returns:
         - ([int]): list with site indices occupied by species or label (or both) in structure

    """
    if labels and species:
        return [
            i
            for i, site in enumerate(structure)
            if ((site.label in labels) and (site.species_string in species))
        ]
    elif species and not labels:
        return [i for i, site in enumerate(structure) if site.species_string in species]
    elif labels and not species:
        return [i for i, site in enumerate(structure) if site.label in labels]
    else:
        raise ValueError("Need to supply either specie, or label to index_sites")

def dope_structure(
    structure, conc, species_to_rem, species_to_insert, label_to_remove=None
):
    """
    Dope a pymatgen structure object to a particular concentration (within the bounds of integer sites).
    Removes conc * no(species_to_remove) from structure and inserts species to insert in 
    their place. Does so at random (excepting when label_to_remove is passed)

    Args:
       - structure (Structure): pymatgen structure object
       - conc (real): fractional % of sites to remove
       - species_to_rem (str): the species to remove from structure
       - species_to_insert ([str,str]): a list of species to equally distribute over sites that are removed
       - label_to_remove (str): label of sites to select for removal.

    """
    if {species_to_rem}.issubset(structure.symbol_set):
        no_sites = count_sites(
            structure, species=species_to_rem, labels=label_to_remove
        )
        site_indices = index_sites(
            structure, species=species_to_rem, labels=label_to_remove
        )
        no_dopants = int(round(conc * no_sites) / len(species_to_insert))
        random.shuffle(site_indices)
        for species in species_to_insert:
            for dopant in range(no_dopants):
                structure[site_indices.pop()] = species
        return structure.get_sorted_structure()
    else:
        raise ValueError("dope_structure: species_to_rem is not in structure")


def dope_structure_by_no(
    structure, no_dopants, species_to_rem, species_to_insert, label_to_remove=None
):
    """
    Dope a pymatgen structure object by swapping 'no_dopants' of 'species_to_rem' from the original structure.
    Removes no_dopants(species_to_remove) from structure and inserts species to insert in 
    their place. Does so at random (excepting when label_to_remove is passed)

    Args:
       - structure (Structure): pymatgen structure object
       - no_dopants (int): no of each type of dopant to insert
       - species_to_remove (str): the species to remove from structure
       - species_to_insert ([str,str]): a list of species to equally distribute over sites that are removed
       - label_to_remove (str): label of sites to select for removal.

    """
    if {species_to_rem}.issubset(structure.symbol_set):
        no_sites = count_sites(
            structure, species=species_to_rem, labels=label_to_remove
        )
        site_indices = index_sites(
            structure, species=species_to_rem, labels=label_to_remove
        )
        random.shuffle(site_indices)

        for species in species_to_insert:
            for dopant in range(no_dopants):
                structure[site_indices.pop()] = species
        structure = sort_structure(
            structure=structure, order=[species for species in structure.symbol_set]
        )

        return structure
    else:
        raise ValueError("dope_struture_by_no: species_to_rem is not in structure")
