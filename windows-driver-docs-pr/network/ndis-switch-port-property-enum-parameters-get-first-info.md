---
title: NDIS_SWITCH_PORT_PROPERTY_ENUM_PARAMETERS_GET_FIRST_INFO macro
author: windows-driver-content
description: Hyper-V extensible switch extensions use the NDIS_SWITCH_PORT_PROPERTY_ENUM_PARAMETERS_GET_FIRST_INFO macro to access the first NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO element that is specified by an NDIS_SWITCH_PORT_PROPERTY_ENUM_PARAMETERS structure.
ms.assetid: 43DDB75F-7CD6-421E-9AC6-C9C96A2348D4
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_SWITCH_PORT_PROPERTY_ENUM_PARAMETERS_GET_FIRST_INFO macro Network Drivers Starting with Windows Vista
---

# NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_PARAMETERS\_GET\_FIRST\_INFO macro


Hyper-V extensible switch extensions use the **NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_PARAMETERS\_GET\_FIRST\_INFO** macro to access the first [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598233) element that is specified by an [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598236) structure.

Syntax
------

```ManagedCPlusPlus
PNDIS_SWITCH_PORT_PROPERTY_ENUM_INFO NDIS_SWITCH_PORT_PROPERTY_ENUM_PARAMETERS_GET_FIRST_INFO(
   PNDIS_SWITCH_PORT_PROPERTY_ENUM_PARAMETERS _PortEnumParams_
);
```

Parameters
----------

*\_PortEnumParams\_*   
A pointer to an [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598236) structure.

Return value
------------

The **NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_PARAMETERS\_GET\_FIRST\_INFO** macro returns a pointer to the first [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598233) element that is specified by an [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598236) structure.

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
[**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598233)

[**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598236)

 

 




