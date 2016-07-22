---
title: Enabling Event Categories for a Text Log
description: Enabling Event Categories for a Text Log
ms.assetid: 555f698b-69e2-469b-b958-185cb35eeb5a
keywords: ["event categories WDK SetupAPI logging", "text logs WDK SetupAPI , event categories", "LogMask"]
---

# Enabling Event Categories for a Text Log


SetupAPI writes a log entry in a text log only if the event category for the log entry is enabled for the text log and the [event level](setting-the-event-level-for-a-text-log.md) for the text log is equal to or greater than the event level for the log entry.

The following table lists the event categories that SetupAPI supports, the manifest constants that represent the event categories, and the values of the manifest constants.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event category operation</th>
<th align="left">Event category manifest constant</th>
<th align="left">Event category value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Device installation</p></td>
<td align="left"><p>TXTLOG_DEVINST</p></td>
<td align="left"><p>0x00000001</p></td>
</tr>
<tr class="even">
<td align="left"><p>Manage INF files</p></td>
<td align="left"><p>TXTLOG_INF</p></td>
<td align="left"><p>0x00000002</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Manage file queues</p></td>
<td align="left"><p>TXTLOG_FILEQ</p></td>
<td align="left"><p>0x00000004</p></td>
</tr>
<tr class="even">
<td align="left"><p>Copy files</p></td>
<td align="left"><p>TXTLOG_COPYFILES</p></td>
<td align="left"><p>0x00000008</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Manage registry settings</p></td>
<td align="left"><p>TXTLOG_REGISTRY</p></td>
<td align="left"><p>0x00000010</p></td>
</tr>
<tr class="even">
<td align="left"><p>Verify digital signatures</p></td>
<td align="left"><p>TXTLOG_SIGVERIF</p></td>
<td align="left"><p>0x00000020</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Manage device and driver properties</p></td>
<td align="left"><p>TXTLOG_PROPERTIES</p></td>
<td align="left"><p>0x00000040</p></td>
</tr>
<tr class="even">
<td align="left"><p>Backup data</p></td>
<td align="left"><p>TXTLOG_BACKUP</p></td>
<td align="left"><p>0x00000080</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Manage user interface dialog boxes</p></td>
<td align="left"><p>TXTLOG_UI</p></td>
<td align="left"><p>0x00000100</p></td>
</tr>
<tr class="even">
<td align="left"><p>New device manager</p></td>
<td align="left"><p>TXTLOG_NEWDEV</p></td>
<td align="left"><p>0x01000000</p></td>
</tr>
<tr class="odd">
<td align="left"><p>User-mode PnP manager</p></td>
<td align="left"><p>TXTLOG_UMPNPMGR</p></td>
<td align="left"><p>0x02000000</p></td>
</tr>
<tr class="even">
<td align="left"><p>Manage the driver store</p></td>
<td align="left"><p>TXTLOG_DRIVER_STORE</p></td>
<td align="left"><p>0x04000000</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Class installer or co-installer operation</p></td>
<td align="left"><p>TXTLOG_INSTALLER</p></td>
<td align="left"><p>0x40000000</p></td>
</tr>
<tr class="even">
<td align="left"><p>Vendor-supplied operation</p></td>
<td align="left"><p>TXTLOG_VENDOR</p></td>
<td align="left"><p>0x80000000</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="to-enable-event-categories-for-the-setupapi-logs--create--or-modify--the-following-reg-dword-registry-value-"></a>To enable event categories for the SetupAPI logs, create (or modify) the following REG\_DWORD registry value:  
**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Setup\\LogMask**

The **LogMask** registry value applies to the device installation text log and the application installation text log.

If the **LogMask** registry value does not exist, SetupAPI enables all event categories for the text logs. If the **LogMask** registry value is zero, SetupAPI disables all event categories for the text logs.

The **LogMask** registry value is formatted as 0X*VVVVVVVV, where VVVVVVVV* is a 32-bitfield. To enable all categories, set **LogMask** to 0XFFFFFFFF. To enable only specific categories, perform a bitwise OR of the corresponding event category constants. For example:

-   To enable only log entries that are written by device installation operations, set **LogMask** to the value of TXTLOG\_DEVINST (0X00000001)

-   To enable only log entries that are written by device installation operations and driver store operations, set **LogMask** to (TTXTLOG\_DRIVER\_STORE | TEXTLOG\_DEVINST) (0x04000001).

-   To enable only log entries that are written by custom installation operations, set **LogMask** to TXTLOG\_VENDOR (0x80000000).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Enabling%20Event%20Categories%20for%20a%20Text%20Log%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




