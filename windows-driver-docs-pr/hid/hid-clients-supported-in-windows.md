---
title: HID Clients Supported in Windows
author: windows-driver-content
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: E6584286-6BF1-40C7-83C1-D07077B13F3E
description: 
---

# HID Clients Supported in Windows


Windows supports the following top-level collections:

<table style="width:100%;">
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<thead>
<tr class="header">
<th>Usage Page</th>
<th>Usage</th>
<th>Windows 7</th>
<th>Windows 8</th>
<th>Windows 10</th>
<th>Notes</th>
<th>Access Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0x0001</td>
<td>0x0001 - 0x0002</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Mouse class driver and mapper driver</td>
<td>Exclusive</td>
</tr>
<tr class="even">
<td>0x0001</td>
<td>0x0004 - 0x0005</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Game Controllers</td>
<td>Shared</td>
</tr>
<tr class="odd">
<td>0x0001</td>
<td>0x0006 - 0x0007</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Keyboard / Keypad class driver and mapper driver</td>
<td>Exclusive</td>
</tr>
<tr class="even">
<td>0x0001</td>
<td>0x000C</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Flight Mode Switch</td>
<td>Shared</td>
</tr>
<tr class="odd">
<td>0x0001</td>
<td>0x0080</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>System Controls (Power)</td>
<td>Shared</td>
</tr>
<tr class="even">
<td>0x000C</td>
<td>0x0001</td>
<td>Yes</td>
<td>Yes</td>
<td><p>Yes</p>
<p>(For both Windows 10 and Windows 10 Mobile)</p></td>
<td>Consumer Controls</td>
<td><p>Shared</p>
<p>(For both Windows 10 and Windows 10 Mobile)</p></td>
</tr>
<tr class="odd">
<td>0x000D</td>
<td>0x0001</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>External Pen Device</td>
<td>Exclusive</td>
</tr>
<tr class="even">
<td>0x000D</td>
<td>0x0002</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Integrated Pen Device</td>
<td>Exclusive</td>
</tr>
<tr class="odd">
<td>0x000D</td>
<td>0x0004</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Touchscreen</td>
<td>Exclusive</td>
</tr>
<tr class="even">
<td>0x000D</td>
<td>0x0005</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Precision Touchpad (PTP)</td>
<td>Exclusive</td>
</tr>
<tr class="odd">
<td>0x0020</td>
<td>Multiple</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Sensors</td>
<td>Shared</td>
</tr>
<tr class="even">
<td>0x0084</td>
<td>0x004</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>HID UPS Battery</td>
<td>Shared</td>
</tr>
<tr class="odd">
<td>0x008C</td>
<td>0x0002</td>
<td>No</td>
<td><p>Yes</p>
<p>(Windows 8.1 and later)</p></td>
<td>Yes</td>
<td>Barcode Scanner (hidscanner.dll)</td>
<td>Shared</td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20HID%20Clients%20Supported%20in%20Windows%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


