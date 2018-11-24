---
title: GUID_DEVINTERFACE_MODEM
description: GUID_DEVINTERFACE_MODEM
ms.assetid: 80f5c063-8b22-422f-8102-4ac1e62241c8
keywords: ["GUID_DEVINTERFACE_MODEM Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_MODEM
api_location:
- Ntddmodm.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_MODEM


The GUID_DEVINTERFACE_MODEM [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [modem devices](https://msdn.microsoft.com/library/windows/hardware/ff542573).

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
<td align="left"><p>GUID_DEVINTERFACE_MODEM</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{2C7089AA-2E0E-11D1-B114-00C04FC2AAE4}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for modem devices register instances of this device interface class to notify the operating system and applications of the presence of modem devices.

GUID_DEVINTERFACE_MODEM in *Ntddmodm.h* will be defined correctly only if the correct versions of the INITGUID and DEFINE_GUID macros are defined before the inclusion of *Ntddmodm.h*. The DEFINE_GUID macro is defined in the *Guiddef.h*. To make sure that INITGUID, DEFINE_GUID, and GUID_DEVINTERFACE_MODEM are correctly defined, include the following code in a header file:

```cpp
#ifndef INITGUID
#define INITGUID
#include <guiddef.h>
#undef INITGUID
#else 
#include <guiddef.h>
#endif

#include <ntddmodm.h>
...
```

For information about modem devices, see [Modem Devices Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff542476).

For an example of using this device interface class, see the [FakeModem - Unimodem controller-less modem sample driver](http://go.microsoft.com/fwlink/p/?linkid=256110) sample that is provided in the WDK.

[**GUID_CLASS_MODEM**](guid-class-modem.md) is an obsolete identifier for this device interface class; for new instances of this class, use GUID_DEVINTERFACE_MODEM instead.

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
<td align="left"><p>Available in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddmodm.h (include Ntddmodm.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_CLASS_MODEM**](guid-class-modem.md)

 

 






