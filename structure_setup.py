import os

def create_structure():
    # Base directory is the current working directory where the script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # List of known maps to process. 
    # We can either hardcode them or discover them. 
    # Based on the previous list_dir, we have these:
    maps = [
        "ancient", "anubis", "dust2", "inferno", 
        "mirage", "nuke", "overpass", "vertigo"
    ]
    
    grenade_types = ["smokes", "molotovs", "nades", "flashes"]
    sides = ["t", "ct"]
    
    print(f"Processing in {base_dir}...")

    for map_name in maps:
        map_path = os.path.join(base_dir, map_name)
        
        # Check if map directory exists
        if not os.path.isdir(map_path):
            print(f"Warning: Map directory '{map_name}' not found. Skipping.")
            continue
            
        print(f"Processing {map_name}...")
        
        for g_type in grenade_types:
            type_path = os.path.join(map_path, g_type)
            if not os.path.exists(type_path):
                print(f"  Creating {g_type}")
                os.makedirs(type_path)
            
            for side in sides:
                side_path = os.path.join(type_path, side)
                if not os.path.exists(side_path):
                    print(f"    Creating {g_type}/{side}")
                    os.makedirs(side_path)

if __name__ == "__main__":
    create_structure()
