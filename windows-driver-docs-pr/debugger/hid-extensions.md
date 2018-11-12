---
title: HID Extensions
description: This section describes the Human Interface Device (HID) debugger extension commands.
ms.assetid: 796DB87B-1E04-40FA-90F9-699EE7032B3C
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
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
<td align="left"><p><strong><a href="-hidkd-help.md" data-raw-source="[!hidkd.help](-hidkd-help.md)">!hidkd.help</a></strong></p></td>
<td align="left"><p>The <strong><a href="-hidkd-help.md" data-raw-source="[!hidkd.help](-hidkd-help.md)">!hidkd.help</a></strong> command displays help for the HID debugger extension commands.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="-hidkd-hidfdo.md" data-raw-source="[!hidkd.hidfdo](-hidkd-hidfdo.md)">!hidkd.hidfdo</a></strong></p></td>
<td align="left"><p>The <strong><a href="-hidkd-hidfdo.md" data-raw-source="[!hidkd.hidfdo](-hidkd-hidfdo.md)">!hidkd.hidfdo</a></strong> command displays HID information associated with a functional device object (FDO).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="-hidkd-hidpdo.md" data-raw-source="[!hidkd.hidpdo](-hidkd-hidpdo.md)">!hidkd.hidpdo</a></strong></p></td>
<td align="left"><p>The <strong><a href="-hidkd-hidpdo.md" data-raw-source="[!hidkd.hidpdo](-hidkd-hidpdo.md)">!hidkd.hidpdo</a></strong> command displays HID information associated with a physical device object (PDO).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="-hidkd-hidtree.md" data-raw-source="[!hidkd.hidtree](-hidkd-hidtree.md)">!hidkd.hidtree</a></strong></p></td>
<td align="left"><p>The <strong><a href="-hidkd-hidtree.md" data-raw-source="[!hidkd.hidtree](-hidkd-hidtree.md)">!hidkd.hidtree</a></strong> command displays a list of all device nodes that have a HID function driver along with their child nodes. The child nodes have a physical device object (PDO) that was created by the parent node&#39;s HID function driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="-hidkd-hidppd.md" data-raw-source="[!hidkd.hidppd](-hidkd-hidppd.md)">!hidkd.hidppd</a></strong></p></td>
<td align="left"><p>The <strong><a href="-hidkd-hidppd.md" data-raw-source="[!hidkd.hidppd](-hidkd-hidppd.md)">!hidkd.hidppd</a></strong> command displays HID preparsed data.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="-hidkd-hidrd.md" data-raw-source="[!hidkd.hidrd](-hidkd-hidrd.md)">!hidkd.hidrd</a></strong></p></td>
<td align="left"><p>The <strong><a href="-hidkd-hidrd.md" data-raw-source="[!hidkd.hidrd](-hidkd-hidrd.md)">!hidkd.hidrd</a></strong> command displays a HID report descriptor in both raw and parsed format.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[RCDRKD Extensions](rcdrkd-extensions.md)

[Specialized Extension Commands](specialized-extensions.md)

 

 






