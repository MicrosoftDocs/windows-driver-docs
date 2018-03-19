---
title: NDIS_SWITCH_PORT_AT_ARRAY_INDEX macro
author: windows-driver-content
description: Hyper-V extensible switch extensions use the NDIS_SWITCH_PORT_AT_ARRAY_INDEX macro to access an NDIS_SWITCH_PORT_PARAMETERS element inside an NDIS_SWITCH_PORT_ARRAY structure.
ms.assetid: C632350C-CD13-4564-B8E5-4FE90B674510
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_SWITCH_PORT_AT_ARRAY_INDEX macro Network Drivers Starting with Windows Vista
---

# NDIS\_SWITCH\_PORT\_AT\_ARRAY\_INDEX macro


Hyper-V extensible switch extensions use the **NDIS\_SWITCH\_PORT\_AT\_ARRAY\_INDEX** macro to access an [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) element inside an [**NDIS\_SWITCH\_PORT\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598221) structure.

Syntax
------

```ManagedCPlusPlus
PNDIS_SWITCH_PORT_PARAMETERS NDIS_SWITCH_PORT_AT_ARRAY_INDEX(
   PNDIS_SWITCH_PORT_ARRAY _PortArray_,
   USHORT                  _Index_
);
```

Parameters
----------

*\_PortArray\_*   
A pointer to an [**NDIS\_SWITCH\_PORT\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598221) structure.

*\_Index\_*   
A USHORT value that specifies the zero-based index of the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) element inside the [**NDIS\_SWITCH\_PORT\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598221).

**Note**  This value must be less than the value of the **NumElements** member of the [**NDIS\_SWITCH\_PORT\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598221) structure.

 

Return value
------------

The **NDIS\_SWITCH\_PORT\_AT\_ARRAY\_INDEX** macro returns a pointer to the specified [**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229) element inside the [**NDIS\_SWITCH\_PORT\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598221).

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
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_SWITCH\_PORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598229)

[**NDIS\_SWITCH\_PORT\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598221)

 

 




