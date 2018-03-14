---
title: NDIS_SWITCH_PROPERTY_CUSTOM_GET_BUFFER macro
author: windows-driver-content
description: Hyper-V extensible switch extensions use the NDIS_SWITCH_PROPERTY_CUSTOM_GET_BUFFER macro to access the custom extensible switch property buffer inside an NDIS_SWITCH_PROPERTY_CUSTOM structure.
ms.assetid: 40D17048-0014-4FFE-8FEA-73E94CC7AD32
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_SWITCH_PROPERTY_CUSTOM_GET_BUFFER macro Network Drivers Starting with Windows Vista
---

# NDIS\_SWITCH\_PROPERTY\_CUSTOM\_GET\_BUFFER macro


Hyper-V extensible switch extensions use the **NDIS\_SWITCH\_PROPERTY\_CUSTOM\_GET\_BUFFER** macro to access the custom extensible switch property buffer inside an [**NDIS\_SWITCH\_PROPERTY\_CUSTOM**](https://msdn.microsoft.com/library/windows/hardware/hh598247) structure.

Syntax
------

```ManagedCPlusPlus
PVOID NDIS_SWITCH_PROPERTY_CUSTOM_GET_BUFFER(
   PNDIS_SWITCH_PROPERTY_CUSTOM _SwitchPropertyCustom_
);
```

Parameters
----------

*\_SwitchPropertyCustom\_*   
A pointer to an [**NDIS\_SWITCH\_PROPERTY\_CUSTOM**](https://msdn.microsoft.com/library/windows/hardware/hh598247) structure.

Return value
------------

The **NDIS\_SWITCH\_PROPERTY\_CUSTOM\_GET\_BUFFER** returns a pointer to the custom extensible switch property buffer inside an [**NDIS\_SWITCH\_PROPERTY\_CUSTOM**](https://msdn.microsoft.com/library/windows/hardware/hh598247) structure.

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
[**NDIS\_SWITCH\_PROPERTY\_CUSTOM**](https://msdn.microsoft.com/library/windows/hardware/hh598247)

 

 




