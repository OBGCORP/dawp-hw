# Hocam bu ödev için baya bir araştırma yapmam gerekti.
# Tam olarak istediğiniz şey bu mu bilmiyorum ama böyle bir program çıkarabildim.

# Çalışması için gerekli olan owlready2 kütüphanesini kurmayı unutmayınız.
# 28. satıra .owl uzantılı OWL ontology'nizin dosya adresini veriniz.
# Aynı zamanda bu programın çalışması için bilgisayarınızda Java bulunması gerekiyor, eğer yoksa kurmayı unutmayınız.

# Java için -> https://www.oracle.com/java/technologies/downloads/?er=221886#jdk23-windows
# owlready2 için -> pip install owlready2

import sys
from owlready2 import get_ontology, default_world, sync_reasoner

def find_paradoxes_in_ontology(ontology_path):

    print(f"Loading OWL ontology: {ontology_path}...")
    onto = get_ontology(ontology_path).load()

    print("Running the reasoner. This may take a while...")
    with onto:
        sync_reasoner()

    print("Checking for unsatisfiable classes...")

    inconsistent = list(default_world.inconsistent_classes())

    return inconsistent


def main():
    ontology_path = "pizza.owl"
    paradoxical_classes = find_paradoxes_in_ontology(ontology_path)

    if paradoxical_classes:
        print("Found unsatisfiable (paradoxical) classes:")
        for cls in paradoxical_classes:
            print(f" - {cls}")
    else:
        print("No unsatisfiable classes found!")


if __name__ == "__main__":
    main()