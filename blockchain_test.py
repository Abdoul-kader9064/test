import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        contenu = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(contenu.encode()).hexdigest()

# Création du bloc génésis
genesis = Block(0, "Bloc Genesis", "0")
blockchain = [genesis]

# Ajout de deux blocs
block1 = Block(1, "Alice -> Bob : 5 ETH", blockchain[-1].hash)
blockchain.append(block1)

block2 = Block(2, "Bob -> Charlie : 3 ETH", blockchain[-1].hash)
blockchain.append(block2)

# Affichage de la chaîne
for b in blockchain:
    print(f"Bloc {b.index} | Hash : {b.hash[:16]}... | Précédent : {b.previous_hash[:16]}...")

# Tentative de modification du bloc 1
print("\n--- Tentative de modification du bloc 1 ---")
block1.data = "Alice -> Bob : 1000 ETH"
block1.hash = block1.compute_hash()
print(f"Nouveau hash du bloc 1 : {block1.hash[:16]}...")
print(f"previous_hash du bloc 2 : {block2.previous_hash[:16]}...")
print("Le bloc 2 est maintenant invalide : son previous_hash ne correspond plus.")