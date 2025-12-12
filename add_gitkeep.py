import os

def add_gitkeep_to_empty_dirs(start_path):
    fn_count = 0
    for root, dirs, files in os.walk(start_path):
        # If a directory has no subdirectories and no files, it is empty.
        # However, we also want to catch directories that might only contain empty dirs recursively,
        # but the standard approach is: if leaf dir is empty, add .gitkeep and it's no longer empty.
        
        # Checking if 'dirs' is empty helps identification of leaf, but checking 'files' is crucial.
        if not dirs and not files:
            gitkeep_path = os.path.join(root, '.gitkeep')
            print(f"Adding .gitkeep to: {root}")
            with open(gitkeep_path, 'w') as f:
                pass # Create empty file
            fn_count += 1
            
    print(f"Added .gitkeep to {fn_count} directories.")

if __name__ == "__main__":
    # Run in the directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Scanning {current_dir}...")
    add_gitkeep_to_empty_dirs(current_dir)
