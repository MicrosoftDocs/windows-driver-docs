---
title: NDIS_SWITCH_PORT_DESTINATION_AT_ARRAY_INDEX macro
author: windows-driver-content
description: Hyper-V extensible switch extensions use the NDIS_SWITCH_PORT_DESTINATION_AT_ARRAY_INDEX macro to access an NDIS_SWITCH_PORT_DESTINATION element inside an NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY structure.
ms.assetid: 2FD94E64-1E15-426D-822A-B6F5FC035C92
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_SWITCH_PORT_DESTINATION_AT_ARRAY_INDEX macro Network Drivers Starting with Windows Vista
---

# NDIS\_SWITCH\_PORT\_DESTINATION\_AT\_ARRAY\_INDEX macro


Hyper-V extensible switch extensions use the **NDIS\_SWITCH\_PORT\_DESTINATION\_AT\_ARRAY\_INDEX** macro to access an [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) element inside an [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure.

Syntax
------

```ManagedCPlusPlus
PNDIS_SWITCH_PORT_DESTINATION NDIS_SWITCH_PORT_DESTINATION_AT_ARRAY_INDEX(
   PNDIS_SWITCH_FORWARDING_DESTINATION_ARRAY _DestArray_,
   USHORT                                    _Index_
);
```

Parameters
----------

*\_DestArray\_*   
A pointer to an [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure.

*\_Index\_*   
A USHORT value that specifies the zero-based index of the [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) element inside the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210).

**Note**  This value must be less than the value of the **NumElements** member of the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210) structure.

 

Return value
------------

The **NDIS\_SWITCH\_PORT\_DESTINATION\_AT\_ARRAY\_INDEX** macro returns a pointer to the specified [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) element inside the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224)

[**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598210)

 

 




