---
title: IPM Hard Disk Drive Idle Timeout
description: IPM Hard Disk Drive Idle Timeout
ms.assetid: 1dcc261a-803c-4c0e-a68e-29b00f46cd32
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPM Hard Disk Drive Idle Timeout


Although the hard disk drive (HDD) is not the primary power consumer in the typical mobile PC, power savings can be realized by spinning down the HDD media. The HDD idle timeout allows Windows to automatically spin down the HDD media after a period of disk read and write inactivity.

The power savings that are realized when the HDD media is spun down varies by the make and model of the HDD. We encourage system manufacturers to work with HDD vendors to determine the optimal HDD idle timeout value for specific devices.

By default, Windows Vista specifies moderately long HDD idle timeout values. System manufacturers should consider specifying shorter values when trying to achieve aggressive battery conservation on mobile PCs. The following table summarizes details of the HDD idle settings.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Detail</strong></p></td>
<td align="left"><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Friendly name</p></td>
<td align="left"><p>Turn off hard disk after</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Description</p></td>
<td align="left"><p>Specifies how long the hard drive is inactive before the disk turns off</p></td>
</tr>
<tr class="even">
<td align="left"><p>PowerCfg Alias</p></td>
<td align="left"><p>DISKIDLE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Group policy path</p></td>
<td align="left"><p>Administrative Templates\System\Power Management\Hard Disk Settings\Turn Off the Hard Disk</p></td>
</tr>
<tr class="even">
<td align="left"><p>GUID</p></td>
<td align="left"><p>6738e2c4-e8a5-4a42-b16a-e040e769756e</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Defined in</p></td>
<td align="left"><p>Ntpoapi.h</p></td>
</tr>
<tr class="even">
<td align="left"><p>Balanced defaults</p></td>
<td align="left"><p>60 minutes (AC) 30 minutes (DC)</p></td>
</tr>
</tbody>
</table>

 

For more information see [Mobile Battery Life Solutions - A Guide for Mobile Platform Professionals.](http://go.microsoft.com/fwlink/p/?linkid=144534)

 

 




