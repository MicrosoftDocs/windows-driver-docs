---
mode: 'agent'
model: Claude Sonnet 4.5
tools: [microsoft_docs_search, runCommands, edit, runTasks]
description: 'Automated agent prompt that performs content freshness passes on Windows Driver documentation files. It reads a CSV file containing file paths, opens each file, and systematically reviews and updates content for accuracy, relevance, and completeness according to Microsoft Learn freshness guidelines.'
---

Prompt:

Your goal is to perform a content freshness pass on Windows Driver Kit (WDK) documentation files listed in a CSV file.

## Setup

1. Locate the first attachment whose filename ends with ".csv" and parse it as CSV (comma delimiter; first row = header; support quoted fields and embedded newlines).
   - The CSV should contain a column named "Url". Use this column to determine the list of files and file paths to review.
   - Expected file paths should be in the format: `windows-driver-docs-pr/kernel/defining-i-o-control-codes.md`
   - Skip any header row and empty rows

2. Verify environment access:
   - Run `git status` to confirm Git is available
   - If Git is not available, report the problem and stop

## Freshness Review Process

For each file in the spreadsheet, perform the following checks and updates. Report each step's actions and findings.

1. Article Accuracy and Completeness
- Review the entire article for technical accuracy, relevance, and completeness within its scope
- Verify that all information is current and reflects the latest Windows driver development practices
- Check that examples and code snippets are accurate and follow current best practices

2. Screenshots and Images
- Review all screenshots to ensure they reflect the current customer-facing UI
- Verify images are still relevant and accurate
- Check that all images have proper alt text (accessibility requirement)
- See: [Alt text requirements for images](https://review.learn.microsoft.com/help/contribute/alt-text)

3. Links
- Check that all links (internal and external) go to current, accurate, and relevant content
- Update or remove broken links
- Convert fully qualified learn.microsoft.com URLs to site-relative links (e.g., `/windows-hardware/drivers/...`)
- Verify relative links resolve correctly

4. Product and Feature Names
- Check for outdated release references (e.g., old Windows version names)
- Verify product and feature names are current
- Update deprecated terminology

5. HTML to Markdown Conversion
- Convert any remaining HTML to Markdown where appropriate
- Ensure proper Markdown formatting throughout

6. Metadata Updates
- Update the `ms.date` field to today's date (MM/DD/YYYY format)
- If you make changes to the file beyond updating `ms.date`, ensure `ai-usage: ai-assisted` is included in the YAML frontmatter
- Verify all required metadata is present and accurate

7. When done, issue a reminder to the content owner to run the Learn Authoring Assistant and/or Acrolinx on all the files.

## Guidelines

- Make substantive improvements, not just superficial changes
- Preserve the author's voice and technical accuracy
- Don't remove valid existing content
- Be thorough but efficient - focus on meaningful updates
- If a file doesn't exist at the specified path, report it and continue to the next file
- Keep changes focused on freshness - this is not a complete rewrite

## Reference

For more information, see [Content freshness definitions and maintenance checklist](https://review.learn.microsoft.com/help/contribute/freshness).
