---
title: Comments and Ignored Blocks
author: windows-driver-content
description: Comments and Ignored Blocks
MS-HAID:
- 'nt5gpd\_87925af2-dd68-44ec-9595-a0a2176d88ce.xml'
- 'print.comments\_and\_ignored\_blocks'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8b3a0195-b2c8-491d-abcd-bfaebefbc77d
keywords: ["GPD file entries WDK Unidrv , ignored blocks", "ignored blocks WDK GPD files", "GPD file entries WDK Unidrv , comments", "comments WDK GPD files"]
---

# Comments and Ignored Blocks


## <a href="" id="ddk-comments-and-ignored-blocks-gg"></a>


GPD files can contain comments. The format for a comment is as follows:

**\*%** *CommentString*

where *CommentString* is any string of characters ending with a line terminator. Each line of a multiline comment must begin with the **\*%** character sequence. The **\*%** sequence must be preceded by white space or a line break.

The following are examples of valid comments:

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Comments%20and%20Ignored%20Blocks%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


