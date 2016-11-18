---
title: GPD File Entry Format
author: windows-driver-content
description: GPD File Entry Format
MS-HAID:
- 'nt5gpd\_5fca696f-7c4e-4816-8579-5b58c18fd0c0.xml'
- 'print.gpd\_file\_entry\_format'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 44057b4d-5ea1-426f-ae87-047b650cbf65
keywords: ["GPD file entries WDK Unidrv , formats", "formats WDK GPD files"]
---

# GPD File Entry Format


## <a href="" id="ddk-gpd-file-entry-format-gg"></a>


All GPD file entries conform to the following format:

**\*** *EntryName***:** *EntryValue* **{***GPD\_FileEntry, GPD\_FileEntry, ...***}**

*EntryName* is always a predefined keyword that Unidrv's GPD parser recognizes, preceded by an asterisk.

*EntryValue* must be one of the [GPD value types](gpd-value-types.md).

Each *GPD\_FileEntry* is another GPD file entry, conforming to the format shown above. Each of these subentries must be valid for the specified *EntryName* of the entry containing it.

Some *EntryName* keywords do not accept braces or enclosed subentries.

Each GPD entry is terminated by end-of-line or a right brace ( **}** ).

An example of a simple GPD file entry, which does not accept subentries, is the following attribute entry:

```
*MaxCopies: 99
```

This entry specifies that the maximum number of copies the printer can handle is 99.

Following is a more complex example, describing a printer that can print pages in either of two page orientations (portrait or landscape). The example also specifies the commands the driver must send to select each orientation.

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GPD%20File%20Entry%20Format%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


