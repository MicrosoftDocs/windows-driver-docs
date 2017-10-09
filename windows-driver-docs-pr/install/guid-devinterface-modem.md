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

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_MODEM%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





