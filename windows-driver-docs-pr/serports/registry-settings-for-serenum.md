---
title: Registry Settings for Serenum
description: Registry Settings for Serenum
ms.assetid: c8a8f1b7-ea58-49ed-98e0-40297ec9a769
keywords:
- Serenum driver WDK , registry settings
- registry WDK serial devices
- serial devices WDK , registry settings
- serial devices WDK , Serenum driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registry Settings for Serenum





This topic describes the entry values that Serenum uses for an RS-232 port in Microsoft Windows 2000 and later.

The following registry entry values are under the Plug and Play hardware device registry key for an RS-232 port:

<a href="" id="portname--reg-sz-"></a>**PortName** (REG\_SZ)  
Specifies the name of the port. Serenum reads this value and returns the port name in response to an [**IOCTL\_SERENUM\_GET\_PORT\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff546533) request.

<a href="" id="identifier--reg-sz-"></a>**Identifier** (REG\_SZ)  
Specifies the name of the port. Serenum reads this value. Support for the **Identifier** entry value is provided only for compatibility with some legacy PCMCIA devices. The use of the **Identifier** entry value is obsolete and should not be implemented with drivers in Windows 2000 and later. Serenum returns the port name in response to an IOCTL\_SERENUM\_GET\_PORT\_NAME request.

<a href="" id="skipenumerations--reg-dword-"></a>**SkipEnumerations** (REG\_DWORD)  
In Windows XP and later, this entry value controls when Serenum enumerates a port in response to an [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff551670) request for **BusRelations**. This entry value is not supported by Windows 2000.

Each time the system builds a serial port device stack, Serenum sets the *enumeration mode* that it uses to enumerate a port. During the initialization of a port's device stack, Serenum's [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine reads the port's **SkipEnumerations** entry value and sets the enumeration mode as described in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Enumeration mode</th>
<th>SkipEnumerations value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Enumerate normally.</p></td>
<td><p>0x00000000</p>
<p>(or the value entry is not present)</p></td>
<td><p>Serenum enumerates a serial port in response to all <strong>BusRelations</strong> requests (whether initiated by a system boot or by the user through Device Manager or Add Hardware Wizard).</p></td>
</tr>
<tr class="even">
<td><p>Skip a specified number of enumerations.</p></td>
<td><p>A value from 0x00000001 to 0xFFFFFFE</p></td>
<td><p>Serenum skips the specified number of enumerations and subsequently enumerates normally as long as the port remains enabled.</p></td>
</tr>
<tr class="odd">
<td><p>Skip all enumerations.</p></td>
<td><p>0xFFFFFFFF</p></td>
<td><p>Serenum never enumerates a port. A device attached to the port must be manually installed.</p></td>
</tr>
</tbody>
</table>

 

For example, if a serial port's **SkipEnumerations** entry value is set to three when the system builds a port device stack, Serenum will skip the first three **BusRelations** requests it receives for the port. Serenum will subsequently enumerate the port in a normal manner as long as the port remains enabled.

 

 




