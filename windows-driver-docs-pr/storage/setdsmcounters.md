---
title: SetDSMCounters function
description: The SetDSMCounters method is used to set the timer counters for a particular DSM.
ms.assetid: 6ea2ae07-d50e-48af-92da-7a5083a75bc7
keywords: ["SetDSMCounters function Storage Devices"]
topic_type:
- apiref
api_name:
- SetDSMCounters
api_location:
- MPIOwmi.h
api_type:
- HeaderDef
---

# SetDSMCounters function


The SetDSMCounters method is used to set the timer counters for a particular DSM.

Syntax
------

```ManagedCPlusPlus
void SetDSMCounters(
   [in, Description("DSM Context"):amended] uint64              DSMcontext,
   [in, Description("DSM Timer Counters"):amended] DSM_COUNTERS DsmCounters
);
```

Parameters
----------

*DSMcontext*   
A 64-bitfield that provides the DSM context.

*DsmCounters*   
A DSM\_COUNTERS structure.

Return value
------------

None

Remarks
-------

This WMI method belongs to the MPIO\_WMI\_METHODS WMI class.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">MPIOwmi.h (include MPIOwmi.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SetDSMCounters%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




