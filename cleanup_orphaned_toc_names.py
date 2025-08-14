#!/usr/bin/env python3
import os
import yaml
from collections import defaultdict

def find_toc_files(directory):
    """Find all toc.yml files in the directory tree"""
    toc_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'toc.yml':
                toc_files.append(os.path.join(root, file))
    return toc_files

def has_href_children(item):
    """Check if an item or any of its children have an href"""
    if isinstance(item, dict):
        # Check if this item has an href
        if 'href' in item:
            return True
        # Check children
        if 'items' in item:
            for child in item['items']:
                if has_href_children(child):
                    return True
    return False

def remove_orphaned_names(items):
    """Remove items that have name but no href and no children with hrefs"""
    if not isinstance(items, list):
        return items
    
    cleaned_items = []
    removed_count = 0
    
    for item in items:
        if isinstance(item, dict):
            # If item has children, recursively clean them first
            if 'items' in item:
                cleaned_children, child_removed = remove_orphaned_names(item['items'])
                item['items'] = cleaned_children
                removed_count += child_removed
                
                # If after cleaning, the item has no children left and no href, remove it
                if len(item['items']) == 0 and 'href' not in item:
                    print(f"  Removing empty parent: {item.get('name', 'unnamed')}")
                    removed_count += 1
                    continue
            
            # Check if this is a leaf node with name but no href
            if 'name' in item and 'href' not in item and 'items' not in item:
                print(f"  Removing orphaned name: {item['name']}")
                removed_count += 1
                continue
            
            # Check if this has name but no href and no children with hrefs
            elif 'name' in item and 'href' not in item and 'items' in item:
                if not has_href_children(item):
                    print(f"  Removing branch with no hrefs: {item['name']}")
                    removed_count += 1
                    continue
            
            cleaned_items.append(item)
        else:
            cleaned_items.append(item)
    
    return cleaned_items, removed_count

def analyze_and_clean_toc_file(file_path):
    """Analyze and clean a single TOC file"""
    print(f"\nAnalyzing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse YAML
        data = yaml.safe_load(content)
        
        if not data:
            print("  No data found in TOC")
            return 0
        
        # Handle both array format and object with items format
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict) and 'items' in data:
            items = data['items']
        else:
            print("  Unexpected TOC format")
            return 0
        
        original_count = count_total_items(items)
        print(f"  Original item count: {original_count}")
        
        # Clean the items
        cleaned_items, removed_count = remove_orphaned_names(items)
        
        final_count = count_total_items(cleaned_items)
        print(f"  Final item count: {final_count}")
        print(f"  Removed {removed_count} orphaned name entries")
        
        if removed_count > 0:
            # Write back the cleaned file
            if isinstance(data, list):
                result_data = cleaned_items
            else:
                data['items'] = cleaned_items
                result_data = data
            
            with open(file_path, 'w', encoding='utf-8') as f:
                yaml.dump(result_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
            print(f"  ✓ Updated {file_path}")
        
        return removed_count
        
    except Exception as e:
        print(f"  Error processing {file_path}: {e}")
        return 0

def count_total_items(items):
    """Count total items in a nested structure"""
    if not isinstance(items, list):
        return 0
    
    count = 0
    for item in items:
        if isinstance(item, dict):
            count += 1
            if 'items' in item:
                count += count_total_items(item['items'])
    return count

def main():
    base_dir = "windows-driver-docs-pr"
    
    if not os.path.exists(base_dir):
        print(f"Directory {base_dir} not found!")
        return
    
    print("Finding all TOC files...")
    toc_files = find_toc_files(base_dir)
    print(f"Found {len(toc_files)} TOC files")
    
    total_removed = 0
    
    for toc_file in toc_files:
        removed = analyze_and_clean_toc_file(toc_file)
        total_removed += removed
    
    print(f"\n=== SUMMARY ===")
    print(f"Total TOC files processed: {len(toc_files)}")
    print(f"Total orphaned name entries removed: {total_removed}")
    print(f"Expected range: 249-252 (matching previous href removals)")
    
    if 249 <= total_removed <= 252:
        print("✓ Removal count matches expected range!")
    else:
        print(f"⚠ Removal count ({total_removed}) is outside expected range (249-252)")

if __name__ == "__main__":
    main()
