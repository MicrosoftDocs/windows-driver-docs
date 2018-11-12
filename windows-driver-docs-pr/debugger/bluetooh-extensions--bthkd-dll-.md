---
title: Bluetooth Extensions (Bthkd.dll)
description: The Bluetooth debugger extensions display information about the current Bluetooth environment on the target system.
ms.assetid: F6C5295D-F1F9-4180-BE57-A7D47AC8690C
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Bluetooth Extensions (Bthkd.dll)


The Bluetooth debugger extensions display information about the current Bluetooth environment on the target system.

**Note**  As you work with the Bluetooth debugging extensions, you may come across undocumented behavior or APIs. We strongly recommend against taking dependencies on undocumented behavior or APIs as it's subject to change in future releases.

 

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
<td align="left"><p><strong><a href="-bthkd-bthdevinfo.md" data-raw-source="[!bthkd.bthdevinfo](-bthkd-bthdevinfo.md)">!bthkd.bthdevinfo</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-bthdevinfo.md" data-raw-source="[!bthkd.bthdevinfo](-bthkd-bthdevinfo.md)">!bthkd.bthdevinfo</a></strong> command displays the information about a given BTHENUM created device PDO.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="-bthkd-bthenuminfo.md" data-raw-source="[!bthkd.bthenuminfo](-bthkd-bthenuminfo.md)">!bthkd.bthenuminfo</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-bthenuminfo.md" data-raw-source="[!bthkd.bthenuminfo](-bthkd-bthenuminfo.md)">!bthkd.bthenuminfo</a></strong> command displays information about the BTHENUM FDO.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="-bthkd-bthinfo-.md" data-raw-source="[!bthkd.bthinfo](-bthkd-bthinfo-.md)">!bthkd.bthinfo</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-bthinfo-.md" data-raw-source="[!bthkd.bthinfo](-bthkd-bthinfo-.md)">!bthkd.bthinfo</a></strong> command displays details about the BTHPORT FDO. This command is a good starting point for Bluetooth investigations as it displays address information that can be used to access many of the other Bluetooth debug extension commands.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="-bthkd-bthhelp.md" data-raw-source="[!bthkd.bthhelp](-bthkd-bthhelp.md)">!bthkd.bthhelp</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-bthhelp.md" data-raw-source="[!bthkd.bthhelp](-bthkd-bthhelp.md)">!bthkd.bthhelp</a></strong> command displays help for the Bluetooth debug extension commands.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="-bthkd-bthtree.md" data-raw-source="[!bthkd.bthtree](-bthkd-bthtree.md)">!bthkd.bthtree</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-bthtree.md" data-raw-source="[!bthkd.bthtree](-bthkd-bthtree.md)">!bthkd.bthtree</a></strong> command displays the complete Bluetooth device tree.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="-bthkd-bthusbtransfer.md" data-raw-source="[!bthkd.bthusbtransfer](-bthkd-bthusbtransfer.md)">!bthkd.bthusbtransfer</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-bthusbtransfer.md" data-raw-source="[!bthkd.bthusbtransfer](-bthkd-bthusbtransfer.md)">!bthkd.bthusbtransfer</a></strong> command displays the Bluetooth usb transfer context including Irp, Bip and transfer buffer information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="-bthkd-dibflags.md" data-raw-source="[!bthkd.dibflags](-bthkd-dibflags.md)">!bthkd.dibflags</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-dibflags.md" data-raw-source="[!bthkd.dibflags](-bthkd-dibflags.md)">!bthkd.dibflags</a></strong> command displays DEVICE_INFO_BLOCK.DibFlags dumps flags set in _DEVICE_INFO_BLOCK.DibFlags.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="-bthkd-hcicmd.md" data-raw-source="[!bthkd.hcicmd](-bthkd-hcicmd.md)">!bthkd.hcicmd</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-hcicmd.md" data-raw-source="[!bthkd.hcicmd](-bthkd-hcicmd.md)">!bthkd.hcicmd</a></strong> command displays a list of the currently pending commands.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="-bthkd-hciinterface.md" data-raw-source="[!bthkd.hciinterface](-bthkd-hciinterface.md)">!bthkd.hciinterface</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-hciinterface.md" data-raw-source="[!bthkd.hciinterface](-bthkd-hciinterface.md)">!bthkd.hciinterface</a></strong> command displays the bthport!_HCI_INTERFACE structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="-bthkd-l2capinterface-.md" data-raw-source="[!bthkd.l2capinterface](-bthkd-l2capinterface-.md)">!bthkd.l2capinterface</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-l2capinterface-.md" data-raw-source="[!bthkd.l2capinterface](-bthkd-l2capinterface-.md)">!bthkd.l2capinterface</a></strong> command displays information about the L2CAP interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="-bthkd-rfcomminfo.md" data-raw-source="[!bthkd.rfcomminfo](-bthkd-rfcomminfo.md)">!bthkd.rfcomminfo</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-rfcomminfo.md" data-raw-source="[!bthkd.rfcomminfo](-bthkd-rfcomminfo.md)">!bthkd.rfcomminfo</a></strong> command displays information about the RFCOMM FDO and the TDI Device Object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="-bthkd-rfcommconnection.md" data-raw-source="[!bthkd.rfcommconnection](-bthkd-rfcommconnection.md)">!bthkd.rfcommconnection</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-rfcommconnection.md" data-raw-source="[!bthkd.rfcommconnection](-bthkd-rfcommconnection.md)">!bthkd.rfcommconnection</a></strong> command displays information about a given RFCOMM connection object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="-bthkd-rfcommchannel.md" data-raw-source="[!bthkd.rfcommchannel](-bthkd-rfcommchannel.md)">!bthkd.rfcommchannel</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-rfcommchannel.md" data-raw-source="[!bthkd.rfcommchannel](-bthkd-rfcommchannel.md)">!bthkd.rfcommchannel</a></strong> command displays information about a given RFCOMM channel CB.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="-bthkd-sdpinterface.md" data-raw-source="[!bthkd.sdpinterface](-bthkd-sdpinterface.md)">!bthkd.sdpinterface</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-sdpinterface.md" data-raw-source="[!bthkd.sdpinterface](-bthkd-sdpinterface.md)">!bthkd.sdpinterface</a></strong> command displays information about the SDP interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="-bthkd-scointerface-.md" data-raw-source="[!bthkd.scointerface](-bthkd-scointerface-.md)">!bthkd.scointerface</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-scointerface-.md" data-raw-source="[!bthkd.scointerface](-bthkd-scointerface-.md)">!bthkd.scointerface</a></strong> command displays information about the SCO interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="-bthkd-sdpnode.md" data-raw-source="[!bthkd.sdpnode](-bthkd-sdpnode.md)">!bthkd.sdpnode</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-sdpnode.md" data-raw-source="[!bthkd.sdpnode](-bthkd-sdpnode.md)">!bthkd.sdpnode</a></strong> command displays information about a node in an sdp tree.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="-bthkd-sdpstream.md" data-raw-source="[!bthkd.sdpstream](-bthkd-sdpstream.md)">!bthkd.sdpstream</a></strong></p></td>
<td align="left"><p>The <strong><a href="-bthkd-sdpstream.md" data-raw-source="[!bthkd.sdpstream](-bthkd-sdpstream.md)">!bthkd.sdpstream</a></strong> command displays the contents of a SDP stream.</p></td>
</tr>
</tbody>
</table>

 

 

 





