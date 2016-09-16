---
title: Command Entry Format
author: windows-driver-content
description: Command Entry Format
MS-HAID:
- 'nt5gpd\_5d956627-52d5-4a87-ad19-081a2dad7620.xml'
- 'print.command\_entry\_format'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f2b14c12-3c34-45b2-9ead-8cd57d657e9e
keywords: ["printer commands WDK Unidrv , entry format", "formats WDK printer commands"]
---

# Command Entry Format


## <a href="" id="ddk-command-entry-format-gg"></a>


To specify a printer command entry in a GPD file, use the following format:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>*Command</strong>: <em>CommandName</em> {<em>CommandAttributes</em>}</p></td>
</tr>
</tbody>
</table>

 

where *CommandName* is one of the predefined [command names](command-names.md), and *CommandAttributes* is a set of [command attributes](command-attributes.md).

For example, a GPD file might contain the following specification of the CmdStartPage command, which initializes a page for printing.

```
*Command: CmdStartPage
{
    *Order: PAGE_SETUP.100
    *Cmd: "<0D>"
}
```

If, for a particular *CommandName* value, you only need to specify the \*Cmd attribute, you can use a shortened version of the command entry format, as follows:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>*Command</strong>: <em>CommandName</em>: <em>CommandString</em></p></td>
</tr>
</tbody>
</table>

 

where *CommandString* is a text string representing a printer command escape sequence. For more information about specifying escape sequences, see [Command String Format](command-string-format.md).

For example, a GPD file might contain the following specification of the CmdBoldOn command, which turns on bold text:

```
*Command: CmdBoldOn: "<1B>(s3B"
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Command%20Entry%20Format%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


