---
title: LowerLogoVersion
description: LowerLogoVersion
ms.assetid: b11b9190-9e3f-473d-b78f-b472601c60e2
keywords:
- LowerLogoVersion
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# LowerLogoVersion


**LowerLogoVersion** is a [device setup class property](https://msdn.microsoft.com/library/windows/hardware/ff542239) that affects the signature score of a driver as follows:

-   Windows assigns the best signature score to drivers that have a WHQL signature for a Windows version that is the same or later than the **LowerLogoVersion** value.

-   Windows assigns the next best signature score to a driver that was signed by a third-party using Authenticode technology and to a driver that has a WHQL signature for a Windows version earlier than the **LowerLogoVersion** value.

A **LowerLogoVersion** value is a NULL-terminated string that specifies the Windows version, as indicated in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Windows version</th>
<th align="left">LowerLogoVersion value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Windows 7</p></td>
<td align="left"><p>6.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows Server 2008</p></td>
<td align="left"><p>6.1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Vista</p></td>
<td align="left"><p>6.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows Server 2003</p></td>
<td align="left"><p>5.2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows XP</p></td>
<td align="left"><p>5.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 2000</p></td>
<td align="left"><p>5.0</p></td>
</tr>
</tbody>
</table>

 

The system default **LowerLogoVersion** value for a system-defined [device setup class](device-setup-classes.md) is "5.1." This means that drivers that have a WHQL signature for Windows Server 2003 and Windows XP have the same signature score as a driver that is signed by Microsoft for Windows Vista and later versions of Windows.

For more information about driver ranking, see [How Windows Ranks Drivers (Windows Vista and Later)](how-setup-ranks-drivers--windows-vista-and-later-.md).

 

 





