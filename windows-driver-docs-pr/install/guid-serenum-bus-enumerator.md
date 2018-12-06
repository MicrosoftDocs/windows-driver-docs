---
title: GUID_SERENUM_BUS_ENUMERATOR
description: GUID_SERENUM_BUS_ENUMERATOR
ms.assetid: 85d72641-e86c-4611-9509-aea4a3344950
keywords: ["GUID_SERENUM_BUS_ENUMERATOR Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_SERENUM_BUS_ENUMERATOR
api_location:
- Ntddser.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_SERENUM_BUS_ENUMERATOR


GUID_SERENUM_BUS_ENUMERATOR is an obsolete identifier for the [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) for Plug and Play (PnP) serial ports. Starting with Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR**](guid-devinterface-serenum-bus-enumerator.md) class identifier for new instances of this class.

Remarks
-------

The WDK includes the serial enumerator sample ([*serenum*](https://msdn.microsoft.com/library/windows/hardware/ff546505)). The serial enumerator uses GUID_SERENUM_BUS_ENUMERATOR to register instances of this device interface class. The serenum sample is included in the *src\\kernel* directory of the WDK.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Obsolete. Starting with Windows 2000, use GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddser.h (include Ntddser.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR**](guid-devinterface-serenum-bus-enumerator.md)

 

 






