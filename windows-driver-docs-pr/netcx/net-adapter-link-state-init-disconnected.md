---
title: NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED method
topic_type:
- apiref
api_name:
- NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes a [**NET_ADAPTER_LINK_STATE**](net-adapter-link-state.md) structure for an adapter that is disconnected from the network.

Syntax
------

```cpp
FORCEINLINE VOID NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED(
  _Out_ PNET_ADAPTER_LINK_STATE LinkState
);
```

Parameters
----------

*LinkState* [out]  
A pointer to a driver-allocated [**NET_ADAPTER_LINK_STATE**](net-adapter-link-state.md) structure.

Return value
------------

This method does not return a value.

Remarks
-------

Call [**NET_ADAPTER_LINK_STATE_INIT**](net-adapter-link-state-init.md) or **NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED** to initialize a [**NET_ADAPTER_LINK_STATE**](net-adapter-link-state.md) structure.

An initialized **NET_ADAPTER_LINK_STATE** structure is an input parameter value to [**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md).

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
<td align="left"><p>&lt;=DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)

[**NET_ADAPTER_LINK_STATE_INIT**](net-adapter-link-state-init.md)

[**NET_ADAPTER_LINK_STATE**](net-adapter-link-state.md)

[**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md)


 

 






