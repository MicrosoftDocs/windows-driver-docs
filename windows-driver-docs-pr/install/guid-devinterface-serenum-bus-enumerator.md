---
title: GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR
description: GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR
ms.assetid: 163b58b1-9f88-4857-9899-32be5e9ffc3c
keywords: ["GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR
api_location:
- Ntddser.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR


The GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for Plug and Play (PnP) [serial ports](https://msdn.microsoft.com/library/windows/hardware/ff547451).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Identifier</p></td>
<td align="left"><p>GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{4D36E978-E325-11CE-BFC1-08002BE10318}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied enumerator for serial port devices registers instances of GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR to notify the operating system and applications of the presence of serial port devices.

The WDK includes the serial enumerator sample [serenum](https://msdn.microsoft.com/library/windows/hardware/ff546505). The serenum sample uses the obsolete identifier [**GUID_SERENUM_BUS_ENUMERATOR**](guid-serenum-bus-enumerator.md) to register instances of this device interface class. The serenum sample is located in the *src\\kernel* directory of the WDK.

For information about serial devices and drivers, see [Serial Devices and Drivers](https://msdn.microsoft.com/library/windows/hardware/ff547451).

For information about the device interface class for serial port devices, see [**GUID_DEVINTERFACE_COMPORT**](guid-devinterface-comport.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ntddser.h (include Ntddser.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_COMPORT**](guid-devinterface-comport.md)

[**GUID_SERENUM_BUS_ENUMERATOR**](guid-serenum-bus-enumerator.md)

 

 






