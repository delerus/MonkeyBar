import pandas as pd


def ingredienser_i_beholdning(drinknavn):

    df_varebeholdning = pd.read_csv("_data/varebeholdning.csv")

    df_oppskrifter = pd.read_csv("_data/oppskrifter.txt",header=None)

    df_oppskrift = df_oppskrifter[df_oppskrifter[0] == drinknavn]

    
    if len(df_oppskrift) == 0:
        print("Ingen oppskrifter funnet")
    elif len(df_oppskrift) > 1:
        print("Flere oppskrifter ble funnet")
    else:
        ingredienser = df_oppskrift.values[0,1:]
        print("Dette er ingrediensene som trengs:")
        print(ingredienser)
        print("\n")


        for ingrediens in ingredienser:
            vare_i_beholdning = df_varebeholdning[df_varebeholdning["type"] == ingrediens]
            if len(vare_i_beholdning) > 0:
                    print(vare_i_beholdning)
                    print("")
                
        for ingrediens in ingredienser:
            vare_i_beholdning = df_varebeholdning[df_varebeholdning["type"] == ingrediens]
            if len(vare_i_beholdning) == 0:
                print(f"{ingrediens} er ikke i beholdning")


            
            
