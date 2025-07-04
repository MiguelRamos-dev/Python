"""Escribe una función que reciba dos palabras (String) y retorne
    * verdadero o falso (Bool) según sean o no anagramas.
    * - Un Anagrama consiste en formar una palabra reordenando TODAS
    *   las letras de otra palabra inicial.
    * - NO hace falta comprobar que ambas palabras existan.
    * - Dos palabras exactamente iguales no son anagrama."""
def anagram(word1: str, word2: str):
    #igualar los formatos
    clean_word1 = word1.lower().replace(" ", "")
    clean_word2 = word2.lower().replace(" ", "")
     
    #comprobar si son iguales
    if clean_word1 == clean_word2:
        print("las palabras son iguales")
        
    if sorted(clean_word1) == sorted(clean_word2):
        print("Es un anagrama")
    else:
        print("no es un anagrama")
        
    
    
    
    

anagram("claRa", "Cradl")
anagram("Roma", "AmoR")
