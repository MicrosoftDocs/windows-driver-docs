---
title: NetAdapterSetCurrentLinkState method
topic_type:
- apiref
api_name:
- NetAdapterSetCurrentLinkState
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NetAdapterSetCurrentLinkState method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Set the current link state of the of the network adapter.

Syntax
------

```ManagedCPlusPlus
VOID NetAdapterSetCurrentLinkState(
  _In_ NETADAPTER              Adapter,
  _In_ PNET_ADAPTER_LINK_STATE CurrentLinkState
);
```

Parameters
----------

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*CurrentLinkState* \[in\]  
A pointer to an allocated and initialized [**NET\_ADAPTER\_LINK\_STATE**](net-adapter-link-state.md) structure that describes the current link state of the adapter.

Return value
------------

This method does not return a value.

Remarks
-------

The client driver calls **NetAdapterSetCurrentLinkState** from its [*EVT\_NET\_ADAPTER\_SET\_CAPABILITIES*](evt-net-adapter-set-capabilities.md) implementation, or from a callback function that NetAdapterCx calls after *EVT\_NET\_ADAPTER\_SET\_CAPABILITIES*.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Universal</td>
</tr>
<tr class="even">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NET\_ADAPTER\_LINK\_STATE\_INIT**](net-adapter-link-state-init.md)

[**NET\_ADAPTER\_LINK\_STATE\_INIT\_DISCONNECTED**](net-adapter-link-state-init-disconnected.md)

 

 






