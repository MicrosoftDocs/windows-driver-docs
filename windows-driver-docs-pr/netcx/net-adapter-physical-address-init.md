---
title: NET_ADAPTER_PHYSICAL_ADDRESS_INIT method
description: Initializes the NET\_ADAPTER\_PHYSICAL\_ADDRESS structure.
ms.assetid: 5b170ab3-a360-4824-952c-08dd1f99c297
keywords: ["NET_ADAPTER_PHYSICAL_ADDRESS_INIT method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_PHYSICAL_ADDRESS_INIT
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_PHYSICAL\_ADDRESS\_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the [**NET\_ADAPTER\_PHYSICAL\_ADDRESS**](net-adapter-physical-address.md) structure.

Syntax
------

```ManagedCPlusPlus
VOID NET_ADAPTER_PHYSICAL_ADDRESS_INIT(
  _Out_ PNET_ADAPTER_PHYSICAL_ADDRESS PhysicalAddress,
  _In_  USHORT                        Length,
  _In_  PCUCHAR                       PermanentAddressBuffer,
  _In_  PCUCHAR                       CurrentAddressBuffer
);
```

Parameters
----------

*PhysicalAddress* \[out\]  
A pointer to the driver-allocated [**NET\_ADAPTER\_PHYSICAL\_ADDRESS**](net-adapter-physical-address.md) structure.

*Length* \[in\]  

*PermanentAddressBuffer* \[in\]  

*CurrentAddressBuffer* \[in\]  

Return value
------------

This method does not return a value.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





