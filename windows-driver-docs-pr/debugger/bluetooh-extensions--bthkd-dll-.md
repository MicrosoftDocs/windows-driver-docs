---
title: Bluetooth Extensions (Bthkd.dll)
description: The Bluetooth debugger extensions display information about the current Bluetooth environment on the target system.
ms.assetid: F6C5295D-F1F9-4180-BE57-A7D47AC8690C
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p><strong>[!bthkd.bthdevinfo](-bthkd-bthdevinfo.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.bthdevinfo](-bthkd-bthdevinfo.md)</strong> command displays the information about a given BTHENUM created device PDO.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!bthkd.bthenuminfo](-bthkd-bthenuminfo.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.bthenuminfo](-bthkd-bthenuminfo.md)</strong> command displays information about the BTHENUM FDO.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!bthkd.bthinfo](-bthkd-bthinfo-.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.bthinfo](-bthkd-bthinfo-.md)</strong> command displays details about the BTHPORT FDO. This command is a good starting point for Bluetooth investigations as it displays address information that can be used to access many of the other Bluetooth debug extension commands.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!bthkd.bthhelp](-bthkd-bthhelp.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.bthhelp](-bthkd-bthhelp.md)</strong> command displays help for the Bluetooth debug extension commands.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!bthkd.bthtree](-bthkd-bthtree.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.bthtree](-bthkd-bthtree.md)</strong> command displays the complete Bluetooth device tree.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!bthkd.bthusbtransfer](-bthkd-bthusbtransfer.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.bthusbtransfer](-bthkd-bthusbtransfer.md)</strong> command displays the Bluetooth usb transfer context including Irp, Bip and transfer buffer information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!bthkd.dibflags](-bthkd-dibflags.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.dibflags](-bthkd-dibflags.md)</strong> command displays DEVICE_INFO_BLOCK.DibFlags dumps flags set in _DEVICE_INFO_BLOCK.DibFlags.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!bthkd.hcicmd](-bthkd-hcicmd.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.hcicmd](-bthkd-hcicmd.md)</strong> command displays a list of the currently pending commands.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!bthkd.hciinterface](-bthkd-hciinterface.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.hciinterface](-bthkd-hciinterface.md)</strong> command displays the bthport!_HCI_INTERFACE structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!bthkd.l2capinterface](-bthkd-l2capinterface-.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.l2capinterface](-bthkd-l2capinterface-.md)</strong> command displays information about the L2CAP interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!bthkd.rfcomminfo](-bthkd-rfcomminfo.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.rfcomminfo](-bthkd-rfcomminfo.md)</strong> command displays information about the RFCOMM FDO and the TDI Device Object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!bthkd.rfcommconnection](-bthkd-rfcommconnection.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.rfcommconnection](-bthkd-rfcommconnection.md)</strong> command displays information about a given RFCOMM connection object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!bthkd.rfcommchannel](-bthkd-rfcommchannel.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.rfcommchannel](-bthkd-rfcommchannel.md)</strong> command displays information about a given RFCOMM channel CB.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!bthkd.sdpinterface](-bthkd-sdpinterface.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.sdpinterface](-bthkd-sdpinterface.md)</strong> command displays information about the SDP interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!bthkd.scointerface](-bthkd-scointerface-.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.scointerface](-bthkd-scointerface-.md)</strong> command displays information about the SCO interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[!bthkd.sdpnode](-bthkd-sdpnode.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.sdpnode](-bthkd-sdpnode.md)</strong> command displays information about a node in an sdp tree.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[!bthkd.sdpstream](-bthkd-sdpstream.md)</strong></p></td>
<td align="left"><p>The <strong>[!bthkd.sdpstream](-bthkd-sdpstream.md)</strong> command displays the contents of a SDP stream.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Bluetooth%20Extensions%20%28Bthkd.dll%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




