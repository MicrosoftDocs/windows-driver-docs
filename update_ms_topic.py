import os
import csv
import re

# Configuration
CSV_FILE = r"F:\python_projects\ai-topic-classification\windows-driver-docs-classification.csv"
WORKSPACE_ROOT = r"F:\git\windows-driver-docs-pr"

def update_ms_topic_in_file(file_path, classification):
    """
    Update the ms.topic metadata in a markdown file.
    Either adds ms.topic if it doesn't exist, or replaces existing ms.topic: article
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if file starts with frontmatter (---)
        if not content.startswith('---'):
            print(f"  Warning: {file_path} doesn't start with frontmatter")
            return False
        
        # Find the end of the frontmatter
        lines = content.split('\n')
        frontmatter_end = -1
        for i, line in enumerate(lines[1:], 1):  # Skip first --- line
            if line.strip() == '---':
                frontmatter_end = i
                break
        
        if frontmatter_end == -1:
            print(f"  Warning: {file_path} doesn't have valid frontmatter")
            return False
        
        # Extract frontmatter and content
        frontmatter_lines = lines[1:frontmatter_end]  # Lines between --- markers
        content_lines = lines[frontmatter_end + 1:]   # Lines after closing ---
        
        # Check if ms.topic already exists
        ms_topic_line_index = -1
        for i, line in enumerate(frontmatter_lines):
            if line.strip().startswith('ms.topic:'):
                ms_topic_line_index = i
                break
        
        # Update or add ms.topic line
        new_ms_topic_line = f"ms.topic: {classification}"
        
        if ms_topic_line_index >= 0:
            # Replace existing ms.topic line
            old_value = frontmatter_lines[ms_topic_line_index].strip()
            frontmatter_lines[ms_topic_line_index] = new_ms_topic_line
            print(f"  Updated: {old_value} -> {new_ms_topic_line}")
        else:
            # Add new ms.topic line at the end of frontmatter
            frontmatter_lines.append(new_ms_topic_line)
            print(f"  Added: {new_ms_topic_line}")
        
        # Reconstruct the file content
        new_content = '---\n' + '\n'.join(frontmatter_lines) + '\n---\n' + '\n'.join(content_lines)
        
        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"  Error processing {file_path}: {e}")
        return False

def main():
    print("Starting ms.topic update process...")
    
    # Check if CSV file exists
    if not os.path.exists(CSV_FILE):
        print(f"Error: CSV file not found at {CSV_FILE}")
        return
    
    files_processed = 0
    files_updated = 0
    files_failed = 0
    
    # Read CSV file and process each row
    with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip header row
        print(f"CSV Header: {header}")
        print("-" * 80)
        
        for row in reader:
            if len(row) < 2:
                print(f"Skipping invalid row: {row}")
                continue
                
            file_path = row[0].strip()
            classification = row[1].strip()
            
            files_processed += 1
            
            # Convert to relative path if needed and ensure it's in workspace
            if file_path.startswith(WORKSPACE_ROOT):
                relative_path = os.path.relpath(file_path, WORKSPACE_ROOT)
                print(f"Processing: {relative_path}")
            else:
                print(f"Processing: {file_path}")
            
            # Check if file exists
            if not os.path.exists(file_path):
                print(f"  Error: File not found - {file_path}")
                files_failed += 1
                continue
            
            # Update the file
            if update_ms_topic_in_file(file_path, classification):
                files_updated += 1
            else:
                files_failed += 1
            
            print()  # Empty line for readability
    
    print("-" * 80)
    print(f"Summary:")
    print(f"  Files processed: {files_processed}")
    print(f"  Files updated successfully: {files_updated}")
    print(f"  Files failed: {files_failed}")
    print("ms.topic update process completed!")

if __name__ == "__main__":
    main()
