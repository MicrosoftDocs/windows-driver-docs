#!/usr/bin/env python3
"""
Fix redirect URLs in .openpublishing.redirection.json
- Process entries from line 22404 onwards (newly added redirects)
- If source_path and redirect_url have identical last 2 path segments, redirect to parent directory instead
"""

import json
import os

def get_last_two_segments(path):
    """Extract the last two path segments (directory/filename without .md)"""
    # Remove .md extension if present
    path = path.replace('.md', '')
    # Split path and get last two segments
    segments = path.strip('/').split('/')
    if len(segments) >= 2:
        return '/'.join(segments[-2:])
    return path

def get_parent_directory_url(redirect_url):
    """Convert a redirect URL to point to its parent directory"""
    # Remove trailing filename and keep parent directory
    segments = redirect_url.strip('/').split('/')
    if len(segments) > 1:
        return '/' + '/'.join(segments[:-1]) + '/'
    return redirect_url

def main():
    redirect_file = ".openpublishing.redirection.json"
    
    print("Loading redirection file...")
    with open(redirect_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    redirections = data.get('redirections', [])
    total_entries = len(redirections)
    
    print(f"Total redirect entries: {total_entries}")
    
    # Find the starting index (line 22404 corresponds to array index)
    # The JSON structure shows each entry spans multiple lines, so we need to find
    # the first entry that was added in our recent batch
    
    # Look for entries that match our pattern (newly added ones should have consistent format)
    start_index = None
    for i, entry in enumerate(redirections):
        if (isinstance(entry, dict) and 
            'source_path' in entry and 
            'redirect_url' in entry and
            entry.get('source_path', '').startswith('windows-driver-docs-pr/') and
            entry.get('redirect_url', '').startswith('/windows-hardware/drivers/')):
            # Check if this looks like one of our newly added entries
            source_path = entry['source_path']
            redirect_url = entry['redirect_url']
            
            # Our newly added entries will have the pattern where source and redirect match
            source_segments = get_last_two_segments(source_path)
            redirect_segments = get_last_two_segments(redirect_url)
            
            if source_segments == redirect_segments:
                if start_index is None:
                    start_index = i
                break
    
    if start_index is None:
        print("Could not find the starting point for newly added redirects.")
        print("Looking for entries added by our curation script...")
        
        # Alternative approach: look for specific files we know were added
        known_files = [
            "windows-driver-docs-pr/driver-changes-for-windows-11-version-21h2.md",
            "windows-driver-docs-pr/acpi/supporting-an-operation-region.md",
            "windows-driver-docs-pr/audio/directsound-hardware-acceleration-in-wdm-audio.md"
        ]
        
        for i, entry in enumerate(redirections):
            if isinstance(entry, dict) and entry.get('source_path') in known_files:
                start_index = i
                break
    
    if start_index is None:
        print("❌ Could not find newly added redirect entries.")
        return
    
    print(f"Found newly added redirects starting at index {start_index}")
    print(f"Processing {total_entries - start_index} entries...")
    
    fixed_count = 0
    
    # Process entries from start_index to end
    for i in range(start_index, total_entries):
        entry = redirections[i]
        
        if not isinstance(entry, dict) or 'source_path' not in entry or 'redirect_url' not in entry:
            continue
            
        source_path = entry['source_path']
        redirect_url = entry['redirect_url']
        
        # Skip if not our format
        if not source_path.startswith('windows-driver-docs-pr/'):
            continue
        if not redirect_url.startswith('/windows-hardware/drivers/'):
            continue
            
        # Get last two path segments
        source_segments = get_last_two_segments(source_path)
        redirect_segments = get_last_two_segments(redirect_url)
        
        # If they match, we need to fix the redirect URL
        if source_segments == redirect_segments:
            old_url = redirect_url
            new_url = get_parent_directory_url(redirect_url)
            
            # Update the entry
            redirections[i]['redirect_url'] = new_url
            fixed_count += 1
            
            print(f"✓ Fixed: {source_path}")
            print(f"  From: {old_url}")
            print(f"  To:   {new_url}")
    
    print(f"\n=== SUMMARY ===")
    print(f"Entries processed: {total_entries - start_index}")
    print(f"Entries fixed: {fixed_count}")
    
    if fixed_count > 0:
        # Write back the updated file
        print(f"\nWriting updated redirection file...")
        with open(redirect_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"✅ Successfully updated {redirect_file}")
    else:
        print("No changes needed.")

if __name__ == "__main__":
    main()
