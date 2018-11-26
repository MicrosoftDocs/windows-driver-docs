---
title: Comments and Ignored Blocks
description: Comments and Ignored Blocks
ms.assetid: 8b3a0195-b2c8-491d-abcd-bfaebefbc77d
keywords:
- GPD file entries WDK Unidrv , ignored blocks
- ignored blocks WDK GPD files
- GPD file entries WDK Unidrv , comments
- comments WDK GPD files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Comments and Ignored Blocks





GPD files can contain comments. The format for a comment is as follows:

**\*%** *CommentString*

where *CommentString* is any string of characters ending with a line terminator. Each line of a multiline comment must begin with the **\*%** character sequence. The **\*%** sequence must be preceded by white space or a line break.

The following are examples of valid comments:

```cpp
*% This section of the GPD file
*% contains macro definitions.
*Macros: HP4L
{
    *% These macros define command prefixes for the paper size feature.
    LetterCmdPrefix: "<1B>&l2a8c1E<1B>*p0x0Y"  *% Prefix for letter option.
    A4CmdPrefix: "<1B>&l26a8c1E<1B>*p0x0Y"     *% Prefix for A4 option.
    Env10CmdPrefix: "<1B>&l81a8c1E<1B>*p0x0Y"  *% Prefix for Env10 option.
}
```

To request the GPD parser to ignore a group of GPD entries, you can create an ignored block that contains the entries to be ignored. The format for an ignored block is as follows:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>*IgnoreBlock</strong> { <em>IgnoredEntries</em> }</p></td>
</tr>
</tbody>
</table>

 

where *IgnoredEntries* is a set of GPD file entries, containing an equal number of left and right braces.

In the following example, the GPD parser ignores the GPD entries describing the LANDSCAPE\_CC90 option.

```cpp
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
*IgnoreBlock
{
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
}
```

 

 




