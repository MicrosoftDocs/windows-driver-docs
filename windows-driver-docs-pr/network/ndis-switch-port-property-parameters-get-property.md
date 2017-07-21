---
title: NDIS_SWITCH_PORT_PROPERTY_PARAMETERS_GET_PROPERTY macro
author: windows-driver-content
description: Hyper-V extensible switch extensions use the NDIS_SWITCH_PORT_PROPERTY_PARAMETERS_GET_PROPERTY macro to access the port property buffer inside an NDIS_SWITCH_PORT_PROPERTY_PARAMETERS structure.
ms.assetid: 51E84480-1858-4B7A-BB4E-A2EA72149271
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_SWITCH_PORT_PROPERTY_PARAMETERS_GET_PROPERTY macro Network Drivers Starting with Windows Vista
---

# NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS\_GET\_PROPERTY macro


Hyper-V extensible switch extensions use the **NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS\_GET\_PROPERTY** macro to access the port property buffer inside an [**NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598238) structure.

Syntax
------

```ManagedCPlusPlus
PVOID NDIS_SWITCH_PORT_PROPERTY_PARAMETERS_GET_PROPERTY(
   PNDIS_SWITCH_PORT_PROPERTY_PARAMETERS _PortParameters_
);
```

Parameters
----------

*\_PortParameters\_*   
A pointer to an [**NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598238) structure.

Return value
------------

The **NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS\_GET\_PROPERTY** macro returns a pointer to the port property buffer inside an [**NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598238) structure.

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
[**NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598238)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_SWITCH_PORT_PROPERTY_PARAMETERS_GET_PROPERTY%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


