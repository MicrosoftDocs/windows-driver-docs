---
title: HID Extensions
description: This section describes the Human Interface Device (HID) debugger extension commands.
ms.assetid: 796DB87B-1E04-40FA-90F9-699EE7032B3C
---

# HID Extensions


This section describes the Human Interface Device (HID) debugger extension commands.

The HID debugger extension commands are implemented in Hidkd.dll. To load the HID commands, enter **.load hidkd.dll** in the debugger.

## <span id="Getting_started_with_the_HID_extensions_"></span><span id="getting_started_with_the_hid_extensions_"></span><span id="GETTING_STARTED_WITH_THE_HID_EXTENSIONS_"></span>Getting started with the HID extensions


To start debugging a HID issue, enter the [**!hidtree**](-hidkd-hidtree.md) command. The **!hidtree** command displays a list of commands and addresses that you can use to investigate device objects, preparsed HID data, and HID report descriptors.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>[!hidkd.help](-hidkd-help.md)</strong></p></td>
<td align="left"><p>The <strong>[!hidkd.help](-hidkd-help.md)</strong> command displays help for the HID debugger extension commands.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!hidkd.hidfdo](-hidkd-hidfdo.md)</strong></p></td>
<td align="left"><p>The <strong>[!hidkd.hidfdo](-hidkd-hidfdo.md)</strong> command displays HID information associated with a functional device object (FDO).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!hidkd.hidpdo](-hidkd-hidpdo.md)</strong></p></td>
<td align="left"><p>The <strong>[!hidkd.hidpdo](-hidkd-hidpdo.md)</strong> command displays HID information associated with a physical device object (PDO).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!hidkd.hidtree](-hidkd-hidtree.md)</strong></p></td>
<td align="left"><p>The <strong>[!hidkd.hidtree](-hidkd-hidtree.md)</strong> command displays a list of all device nodes that have a HID function driver along with their child nodes. The child nodes have a physical device object (PDO) that was created by the parent node's HID function driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!hidkd.hidppd](-hidkd-hidppd.md)</strong></p></td>
<td align="left"><p>The <strong>[!hidkd.hidppd](-hidkd-hidppd.md)</strong> command displays HID preparsed data.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!hidkd.hidrd](-hidkd-hidrd.md)</strong></p></td>
<td align="left"><p>The <strong>[!hidkd.hidrd](-hidkd-hidrd.md)</strong> command displays a HID report descriptor in both raw and parsed format.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[RCDRKD Extensions](rcdrkd-extensions.md)

[Specialized Extension Commands](specialized-extensions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20HID%20Extensions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





