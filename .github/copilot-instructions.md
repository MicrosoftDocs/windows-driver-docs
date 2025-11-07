# Windows Driver Documentation - Copilot Instructions

## Repository Overview

This repository contains the source files for the Windows Driver Kit (WDK) conceptual and guidance documentation. The content is published to [learn.microsoft.com/windows-hardware/drivers](/windows-hardware/drivers).

### Purpose
- Provides comprehensive conceptual documentation and guidance for Windows device driver development
- Covers driver architecture, design patterns, programming techniques, and best practices
- Serves as the authoritative source for driver development concepts across all driver technologies
- Complements the DDI reference documentation found in the [windows-driver-docs-ddi repository](https://github.com/MicrosoftDocs/windows-driver-docs-ddi)

## Repository Structure

```
windows-driver-docs-pr/
├── {technology}/              # Technology area directories
│   ├── *.md                   # Conceptual documentation files
│   ├── toc.yml                # Table of contents for the technology
│   ├── index.md               # Technology area overview/landing page
│   └── images/                # Images specific to this technology
├── docfx.json                 # Build configuration
├── toc.yml                    # Root table of contents
├── index.yml                  # Root landing page
├── breadcrumbs/               # Breadcrumb navigation
└── includes/                  # Reusable content snippets
```

### Folder Organization
Technology area directories represent major driver categories and development topics:
- **Audio** (`audio/`) - Audio driver concepts and design patterns
- **Display** (`display/`) - Display and graphics driver guidance
- **Kernel** (`kernel/`) - Kernel-mode driver fundamentals and techniques
- **Network** (`netcx/`, `network/`) - Network driver development
- **Storage** (`storage/`) - Storage driver concepts
- **USB** (`usbcon/`) - USB driver development
- **WDF** (`wdf/`) - Windows Driver Framework concepts
- **Install** (`install/`) - Driver installation and INF files
- **Debugger** (`debugger/`, `debuggercmds/`) - Debugging documentation
- And many other specialized driver areas

Each technology directory typically contains conceptual articles, how-to guides, design patterns, and technology-specific guidance.

## File Naming Conventions

Unlike the DDI reference documentation, conceptual documentation files use descriptive, topic-based naming:

- Use lowercase with hyphens for multi-word names: `defining-i-o-control-codes.md`
- Use descriptive names that reflect the content: `introduction-to-wdm.md`, `writing-dpc-routines.md`
- Landing pages are typically named `index.md`
- Table of contents files are named `toc.yml`

## Content Structure

Each documentation file contains:

### YAML Frontmatter (Required)
Every file must start with YAML frontmatter containing metadata:

```yaml
---
title: {Article title}
description: {Brief description of the article}
keywords: ["{keyword1}", "{keyword2}", "{keyword3}"]
ms.date: {Date in MM/DD/YYYY format}
ms.topic: {concept-article|design-pattern|overview|reference|how-to}
---
```

#### Required AI Usage Metadata

**IMPORTANT**: When Copilot creates or modifies content, ensure that `ai-usage: ai-assisted` is included as a metadata attribute in the YAML frontmatter. If this attribute is not present, add it.

### Common Metadata Patterns

#### Topic Types (ms.topic):
- `concept-article` - Explanatory/conceptual content
- `design-pattern` - Design patterns and architectural guidance
- `overview` - High-level overviews and introductions
- `reference` - Reference information (not API reference, but tables, lists, etc.)
- `how-to` - Step-by-step procedures

#### Other Common Metadata:
- `targetos: Windows` - Specifies target operating system
- `ms.custom` - Custom tags for special handling
- `ms.update-cycle` - Update frequency for content that changes regularly

### Content Sections

Conceptual documentation is more flexible than API reference, but should follow these general patterns:

#### Standard Structure:
1. **Title** - H1 heading matching the title in frontmatter
2. **Introduction** - Brief overview of the topic and its purpose
3. **Main content** - Organized with H2 and H3 headings as appropriate
4. **Code examples** - When applicable, showing practical implementations
5. **Related topics** - Links to related articles

#### Common Section Types:
- Overview and introduction sections
- Architecture and design explanations
- Step-by-step procedures and how-tos
- Best practices and guidelines
- Examples and sample code
- Troubleshooting information
- Related topics and see-also sections

## Link Formatting Guidelines

### Site-Relative Links (Required)
**IMPORTANT**: Use site-relative links instead of fully qualified URLs for learn.microsoft.com content.

✅ **Correct:**
```markdown
[Windows Hardware Developer](/windows-hardware)
[Driver Development](/windows-hardware/drivers)
[API Reference](/windows-hardware/drivers/ddi)
```

❌ **Incorrect:**
```markdown  
[Windows Hardware Developer](https://learn.microsoft.com/windows-hardware)
[Driver Development](https://learn.microsoft.com/windows-hardware/drivers)
[API Reference](https://learn.microsoft.com/windows-hardware/drivers/ddi)
```

### Cross-References
- Link to other conceptual articles using relative paths: `[Introduction to WDM](introduction-to-wdm.md)`
- Link to DDI reference using full site-relative paths: `[IoCallDriver](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)`
- Use **bold** formatting for API names in text: `**IoCallDriver**`

### External Links
External links (non-learn.microsoft.com) should use full URLs:
```markdown
[Windows SDK](https://developer.microsoft.com/windows/downloads/windows-sdk/)
```

## Writing Guidelines

### Style and Tone
- Use clear, concise technical language
- Write in second person when addressing the reader ("you" form) for procedural content
- Use third person for conceptual/explanatory content
- Use active voice when possible
- Be consistent with terminology across related articles

### Content Quality
- Provide context and explain the "why" in addition to the "what" and "how"
- Include practical examples and scenarios when helpful
- Cross-reference related conceptual articles and DDI reference topics
- Verify technical accuracy of all information
- Follow Microsoft Writing Style Guide for technical documentation
- Use consistent terminology with existing documentation

### Code Examples
When including code examples:
- Use proper C/C++ syntax highlighting with ` ```cpp ` code blocks
- Include necessary header files and context
- Provide explanatory comments in the code
- Show practical, realistic scenarios
- Keep examples focused and relevant to the topic

```cpp
// Example code block
#include <ntddk.h>

NTSTATUS
DriverEntry(
    _In_ PDRIVER_OBJECT DriverObject,
    _In_ PUNICODE_STRING RegistryPath
    )
{
    // Set up dispatch routines
    DriverObject->MajorFunction[IRP_MJ_CREATE] = DispatchCreate;
    DriverObject->MajorFunction[IRP_MJ_CLOSE] = DispatchClose;
    
    return STATUS_SUCCESS;
}
```

### Common Patterns
- **Conceptual articles**: Explain architecture, concepts, and design principles
- **How-to guides**: Provide step-by-step instructions for specific tasks
- **Design patterns**: Show best practices and recommended approaches
- **Reference tables**: Organize information about constants, flags, behaviors
- **Overviews**: Introduce technology areas with context and navigation

## Build and Validation

The repository uses DocFX for building documentation. Key configuration is in `docfx.json`.

### Local Validation
- Ensure YAML frontmatter is valid
- Verify all internal links resolve correctly
- Check that images display properly
- Validate that required metadata is present
- Review for consistency with Microsoft Writing Style Guide

### Content Review Checklist
- [ ] YAML frontmatter complete and valid
- [ ] AI usage metadata included if AI was used
- [ ] Site-relative links used for learn.microsoft.com content
- [ ] Title and description accurately reflect content
- [ ] Appropriate `ms.topic` value selected
- [ ] Technical accuracy verified
- [ ] Cross-references added to related articles
- [ ] Examples provided where helpful
- [ ] Images include alt text
- [ ] Consistent with Microsoft Writing Style Guide
- [ ] Content is clear and well-organized

## Technology Areas

The repository covers all major driver development areas including:
- **Audio** - Audio device drivers (WDM audio, ACX)
- **Display** - Display and graphics drivers (WDDM, DirectX)
- **Kernel** - Kernel-mode driver fundamentals (WDM, I/O, power, PnP)
- **Network** - Network drivers (NetAdapterCx, NDIS)
- **Storage** - Storage drivers (Storport, file systems)
- **USB** - USB drivers and devices
- **HID** - Human Interface Devices
- **Bluetooth** - Bluetooth drivers
- **Sensors** - Sensor drivers
- **Print** - Print drivers
- **WDF** - Windows Driver Framework (KMDF, UMDF)
- **Install** - Driver installation, INF files, and device installation
- **Debugger** - Debugging tools and techniques
- **DevTest** - Driver testing and verification
- **Dashboard** - Hardware Dev Center and driver submission
- And many more specialized driver areas

Each technology area has its own directory with focused content for that domain.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines, including:
- Pull request process
- Code review requirements  
- Microsoft Contributor License Agreement (CLA)
- Style guide adherence
