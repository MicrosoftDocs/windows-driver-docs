---
title: LowerLogoVersion
description: LowerLogoVersion
ms.assetid: b11b9190-9e3f-473d-b78f-b472601c60e2
keywords: ["LowerLogoVersion"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20LowerLogoVersion%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




