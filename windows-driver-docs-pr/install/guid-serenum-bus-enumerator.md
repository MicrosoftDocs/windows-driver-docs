---
title: GUID_SERENUM_BUS_ENUMERATOR
description: GUID_SERENUM_BUS_ENUMERATOR
keywords: ["GUID_SERENUM_BUS_ENUMERATOR Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_SERENUM_BUS_ENUMERATOR
api_location:
- Ntddser.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# GUID_SERENUM_BUS_ENUMERATOR


GUID_SERENUM_BUS_ENUMERATOR is an obsolete identifier for the [device interface class](./overview-of-device-interface-classes.md) for Plug and Play (PnP) serial ports. Starting with Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR**](guid-devinterface-serenum-bus-enumerator.md) class identifier for new instances of this class.

## Remarks

The WDK includes the serial enumerator sample ([*serenum*](/previous-versions/ff546505(v=vs.85))). The serial enumerator uses GUID_SERENUM_BUS_ENUMERATOR to register instances of this device interface class. The serenum sample is included in the *src\\kernel* directory of the WDK.

## Requirements

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

 

