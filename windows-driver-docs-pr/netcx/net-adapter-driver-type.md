---
title: NET_ADAPTER_DRIVER_TYPE enumeration
description: The NET\_ADAPTER\_DRIVER\_TYPE enumeration identifies the type of network adapter driver.
ms.assetid: 05a9d0b1-7764-41d6-bd2c-6f1f1224b9fe
keywords: ["NET_ADAPTER_DRIVER_TYPE enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_DRIVER_TYPE
api_location:
- netadapterdriver.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_DRIVER\_TYPE enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NET\_ADAPTER\_DRIVER\_TYPE** enumeration identifies the type of network adapter driver.

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_DRIVER_TYPE { 
  NET_ADAPTER_DRIVER_TYPE_INVALID   = 0,
  NET_ADAPTER_DRIVER_TYPE_MINIPORT  = 1
} NET_ADAPTER_DRIVER_TYPE;
```

Constants
---------

**NET\_ADAPTER\_DRIVER\_TYPE\_INVALID**  

**NET\_ADAPTER\_DRIVER\_TYPE\_MINIPORT**  

Remarks
-------

The **NET\_ADAPTER\_DRIVER\_TYPE** enumeration is used as a parameter to [**NetAdapterDriverWdmGetHandle**](netadapterdriverwdmgethandle.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapterdriver.h</td>
</tr>
</tbody>
</table>

 

 





