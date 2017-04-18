---
title: Top-Level Collections Opened by Windows for System Use
author: windows-driver-content
description: Top-Level Collections Opened by Windows for System Use
ms.assetid: e489ce46-379e-4ba9-a0e3-5848b1f4a17b
keywords: ["top-level collections WDK HID"]
---

# Top-Level Collections Opened by Windows for System Use


## <a href="" id="ddk-top-level-collections-opened-by-windows-for-system-use-kg"></a>


Windows opens the following [top-level collections](top-level-collections.md) for system use:

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Device Type</th>
<th>Usage Page</th>
<th>Usage ID</th>
<th>Windows Client</th>
<th>Access Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Pointer</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
<td><p>Win32 subsystem</p></td>
<td><p>Exclusive</p></td>
</tr>
<tr class="even">
<td><p>Mouse</p></td>
<td><p>0x01</p></td>
<td><p>0x02</p></td>
<td><p>Win32 subsystem</p></td>
<td><p>Exclusive</p></td>
</tr>
<tr class="odd">
<td><p>Joystick</p></td>
<td><p>0x01</p></td>
<td><p>0x04</p></td>
<td><p>DirectInput</p></td>
<td><p>Shared</p></td>
</tr>
<tr class="even">
<td><p>Game pad</p></td>
<td><p>0x01</p></td>
<td><p>0x05</p></td>
<td><p>DirectInput</p></td>
<td><p>Shared</p></td>
</tr>
<tr class="odd">
<td><p>Keyboard</p></td>
<td><p>0x01</p></td>
<td><p>0x06</p></td>
<td><p>Win32 subsystem</p></td>
<td><p>Exclusive</p></td>
</tr>
<tr class="even">
<td><p>Keypad</p></td>
<td><p>0x01</p></td>
<td><p>0x07</p></td>
<td><p>Win32 subsystem</p></td>
<td><p>Exclusive</p></td>
</tr>
<tr class="odd">
<td><p>System Control</p></td>
<td><p>0x01</p></td>
<td><p>0x80</p></td>
<td><p>Win32 subsystem</p></td>
<td><p>Shared</p></td>
</tr>
<tr class="even">
<td><p>Consumer Audio Control</p></td>
<td><p>0x0C</p></td>
<td><p>0x01</p></td>
<td><p>hidserv.exe in Windows 2000 and hidserv.dll (one of the SVC host services) in Microsoft Windows XP</p></td>
<td><p>Shared</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Top-Level%20Collections%20Opened%20by%20Windows%20for%20System%20Use%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


