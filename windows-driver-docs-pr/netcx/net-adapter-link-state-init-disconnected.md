---
title: NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED method
description: Initializes a NET\_ADAPTER\_LINK\_STATE structure for an adapter that is disconnected from the network.
ms.assetid: 4666d7b9-bedf-4c37-8cbb-d0e1fef29d31
keywords: ["NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_LINK\_STATE\_INIT\_DISCONNECTED method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes a [**NET\_ADAPTER\_LINK\_STATE**](net-adapter-link-state.md) structure for an adapter that is disconnected from the network.

Syntax
------

```ManagedCPlusPlus
FORCEINLINE VOID NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED(
  _Out_ PNET_ADAPTER_LINK_STATE LinkState
);
```

Parameters
----------

*LinkState* \[out\]  
A pointer to a driver-allocated [**NET\_ADAPTER\_LINK\_STATE**](net-adapter-link-state.md) structure.

Return value
------------

This method does not return a value.

Remarks
-------

**NET\_ADAPTER\_LINK\_STATE\_INIT\_DISCONNECTED**

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

## See also


[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)

[**NET\_ADAPTER\_LINK\_STATE\_INIT**](net-adapter-link-state-init.md)

 

 






