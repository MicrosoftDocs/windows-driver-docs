---
title: GPD File Entry Format
description: GPD File Entry Format
keywords:
- GPD file entries WDK Unidrv , formats
- formats WDK GPD files
ms.date: 01/27/2023
---

# GPD File Entry Format

[!include[Print Support Apps](../includes/print-support-apps.md)]

All GPD file entries conform to the following format:

\***EntryName: EntryValue** {*GPD\_FileEntry, GPD\_FileEntry, ...*}

*EntryName* is always a predefined keyword that Unidrv's GPD parser recognizes, preceded by an asterisk.

*EntryValue* must be one of the [GPD value types](gpd-value-types.md).

Each *GPD\_FileEntry* is another GPD file entry, conforming to the format shown above. Each of these subentries must be valid for the specified *EntryName* of the entry containing it.

Some *EntryName* keywords do not accept braces or enclosed subentries.

Each GPD entry is terminated by end-of-line or a right brace ( **}** ).

An example of a simple GPD file entry, which does not accept subentries, is the following attribute entry:

```GPD
*MaxCopies: 99
```

This entry specifies that the maximum number of copies the printer can handle is 99.

Following is a more complex example, describing a printer that can print pages in either of two page orientations (portrait or landscape). The example also specifies the commands the driver must send to select each orientation.

```GPD
*Feature: Orientation
{
    *Name: "Orientation"
    *DefaultOption: Portrait
    *Option: Portrait
    {
        *Name: "Portrait"
        *Command: CmdSelect
        {
            *Order: DOC_SETUP.7
            *Cmd: "<1B>&l0O"
        }
    }
    *Option: LANDSCAPE_CC90
    {
        *Name: "Landscape"
        *Command: CmdSelect
        {
            *Order: DOC_SETUP.7
            *Cmd: "<1B>&l1O"
        }
    }
}
```
