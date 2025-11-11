#!/usr/bin/env python3
"""
Script to update all headings containing :::no-loc syntax by wrapping them with <a> elements
"""

import re
import os

def generate_id_from_text(text):
    """Generate an ID from the no-loc text content"""
    # Match JS logic: text.toLowerCase().replace(/_/g, '-').replace(/\W/g, '-')
    if text.startswith('/'):
        text = text[1:]
    if not text:
        return ''
    id_text = text.lower()
    # Replace underscores with hyphens
    id_text = id_text.replace('_', '-')
    # Replace all non-word characters (\W matches anything that's not [a-zA-Z0-9_]) with hyphens
    id_text = re.sub(r'\W', '', id_text)
    return id_text

def update_heading(match):
    """Convert a heading with :::no-loc to include <a> element"""
    heading_level = match.group(1)
    full_no_loc = match.group(2)
    
    # Extract the text content from :::no-loc text="...":::
    text_match = re.search(r':::no-loc text="([^"]+)":::', full_no_loc)
    if not text_match:
        # Return unchanged if we can't parse it
        return match.group(0)
    
    text_content = text_match.group(1)
    id_value = generate_id_from_text(text_content)
    
    # Build the new heading with <a> element
    new_heading = f'{heading_level} <a id="{id_value}">{full_no_loc}</a>'
    return new_heading

def process_file(filepath):
    """Process a single markdown file"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match headings with :::no-loc
    # Matches: ## :::no-loc text="...":::
    # Also matches when there's additional markup: ### :::no-loc text="/":::**:::no-loc text="scan":::**
    pattern = r'^(#{2,4})\s+(:::no-loc.*?:::(?:\*\*:::no-loc.*?:::\*\*)?)$'
    
    # Count matches before
    matches_before = len(re.findall(pattern, content, re.MULTILINE))
    
    # Replace all matching headings
    updated_content = re.sub(pattern, update_heading, content, flags=re.MULTILINE)
    
    # Count matches after (should be 0)
    matches_after = len(re.findall(pattern, updated_content, re.MULTILINE))
    
    # Only write if changes were made
    if content != updated_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"  ✓ Updated {matches_before} headings")
        return matches_before
    else:
        print(f"  - No changes needed")
        return 0

def main():
    """Main function"""
    base_dir = r'd:\cpx\content\windows-driver-docs-pr\windows-driver-docs-pr'
    
    # List of files to process
    files_to_process = [
        # r'devtest\pairtool-command-syntax.md',
        r'taef\te-exe-command-line-parameters.md',
        # r'devtest\-static-driver-verifier-commands--msbuild-.md',
        # r'devtest\devgen-command-syntax.md',
        # r'devtest\devgen-examples.md',
        # r'devtest\inf2cat.md',
        # r'devtest\pairtool-examples.md',
        # r'devtest\pnputil-command-syntax.md',
        # r'devtest\pnputil-examples.md',
    ]
    
    total_updates = 0
    for rel_path in files_to_process:
        full_path = os.path.join(base_dir, rel_path)
        if os.path.exists(full_path):
            updates = process_file(full_path)
            total_updates += updates
        else:
            print(f"File not found: {full_path}")
    
    print(f"\n✓ Total: Updated {total_updates} headings across {len(files_to_process)} files")

if __name__ == '__main__':
    main()
