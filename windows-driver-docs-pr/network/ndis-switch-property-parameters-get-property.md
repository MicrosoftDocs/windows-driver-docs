---
title: NDIS_SWITCH_PROPERTY_PARAMETERS_GET_PROPERTY macro
author: windows-driver-content
description: Hyper-V extensible switch extensions use the NDIS_SWITCH_PROPERTY_PARAMETERS_GET_PROPERTY macro to access the extensible switch property buffer inside an NDIS_SWITCH_PROPERTY_PARAMETERS structure.
ms.assetid: EED459C4-F01E-4C39-9936-93F597751414
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_SWITCH_PROPERTY_PARAMETERS_GET_PROPERTY macro Network Drivers Starting with Windows Vista
---

# NDIS\_SWITCH\_PROPERTY\_PARAMETERS\_GET\_PROPERTY macro


Hyper-V extensible switch extensions use the **NDIS\_SWITCH\_PROPERTY\_PARAMETERS\_GET\_PROPERTY** macro to access the extensible switch property buffer inside an [**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598255) structure.

Syntax
------

```ManagedCPlusPlus
PVOID NDIS_SWITCH_PROPERTY_PARAMETERS_GET_PROPERTY(
   PNDIS_SWITCH_PROPERTY_PARAMETERS _SwitchParameters_
);
```

Parameters
----------

*\_SwitchParameters\_*   
A pointer to an [**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598255) structure.

Return value
------------

The **NDIS\_SWITCH\_PROPERTY\_PARAMETERS\_GET\_PROPERTY** macro returns a pointer to the extensible switch property buffer inside an [**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598255) structure.

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
[**NDIS\_SWITCH\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598255)

 

 




