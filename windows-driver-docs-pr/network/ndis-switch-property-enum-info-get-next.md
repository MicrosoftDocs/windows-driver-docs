---
title: NDIS_SWITCH_PROPERTY_ENUM_INFO_GET_NEXT macro
author: windows-driver-content
description: Hyper-V extensible switch extensions use the NDIS_SWITCH_PROPERTY_ENUM_INFO_GET_NEXT macro to access the next NDIS_SWITCH_PROPERTY_ENUM_INFO element that follows an NDIS_SWITCH_PROPERTY_ENUM_INFO structure in the array that is specified by an NDIS_SWITCH_PROPERTY_ENUM_PARAMETERS structure.
ms.assetid: 81A8B9AE-E401-4A8A-A84E-93F745B34954
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_SWITCH_PROPERTY_ENUM_INFO_GET_NEXT macro Network Drivers Starting with Windows Vista
---

# NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO\_GET\_NEXT macro


Hyper-V extensible switch extensions use the **NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO\_GET\_NEXT** macro to access the next [**NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598250) element that follows an **NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO** structure in the array that is specified by an [**NDIS\_SWITCH\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598253) structure.

Syntax
------

```ManagedCPlusPlus
PNDIS_SWITCH_PROPERTY_ENUM_INFO NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO_GET_NEXT(
   PNDIS_SWITCH_PROPERTY_ENUM_INFO _SwitchEnumInfo_
);
```

Parameters
----------

*\_SwitchEnumInfo\_*   
A pointer to an [**NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598250) structure.

Return value
------------

The **NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO\_GET\_NEXT** macro returns a pointer to the next [**NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598250) element in the array. If the *\_SwitchEnumInfo\_* parameter is the last element in the array, the macro returns **NULL**.

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
[**NDIS\_SWITCH\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598250)

[**NDIS\_SWITCH\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598253)

 

 




