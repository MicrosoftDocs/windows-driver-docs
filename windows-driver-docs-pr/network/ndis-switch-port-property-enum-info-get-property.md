---
title: NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO_GET_PROPERTY macro
author: windows-driver-content
description: Hyper-V extensible switch extensions use the NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO_GET_PROPERTY macro to access the port property buffer that is specified by an NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO structure.
ms.assetid: 76E08A71-E030-4814-AE4D-D55974968F3A
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO_GET_PROPERTY macro Network Drivers Starting with Windows Vista
---

# NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO\_GET\_PROPERTY macro


Hyper-V extensible switch extensions use the **NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO\_GET\_PROPERTY** macro to access the port property buffer that is specified by an [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598233) structure.

Syntax
------

```ManagedCPlusPlus
PVOID NDIS_SWITCH_PORT_PROPERTY_ENUM_INFO_GET_PROPERTY(
   PVOID __PortEnumInfo__
);
```

Parameters
----------

*\_\_PortEnumInfo\_\_*   
A pointer to an [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598233) structure.

Return value
------------

The **NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO\_GET\_PROPERTY** macro returns a pointer to the port property buffer.

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

 

 




