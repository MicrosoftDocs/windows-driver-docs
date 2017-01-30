---
title: NET_ADAPTER_PHYSICAL_ADDRESS structure
description: Call NET\_ADAPTER\_PHYSICAL\_ADDRESS\_INIT to initialize this structure.
ms.assetid: 19d6a263-9741-47ce-beeb-20c59b9d1f54
keywords: ["NET_ADAPTER_PHYSICAL_ADDRESS structure Network Drivers Starting with Windows Vista", "PNET_ADAPTER_PHYSICAL_ADDRESS structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_PHYSICAL_ADDRESS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_PHYSICAL\_ADDRESS structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Call [NET\_ADAPTER\_PHYSICAL\_ADDRESS\_INIT](net-adapter-physical-address-init.md) to initialize this structure.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_ADAPTER_PHYSICAL_ADDRESS {
  USHORT Length;
  UCHAR  PermanentAddress;
  UCHAR  CurrentAddress;
} NET_ADAPTER_PHYSICAL_ADDRESS, *PNET_ADAPTER_PHYSICAL_ADDRESS;
```

Members
-------

**Length**  

**PermanentAddress**  

**CurrentAddress**  

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
<td align="left">Netadapter.h</td>
</tr>
</tbody>
</table>

 

 





