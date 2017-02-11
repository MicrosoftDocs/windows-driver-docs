---
title: NET_ADAPTER_CONFIG_INIT method
topic_type:
- apiref
api_name:
- NET_ADAPTER_CONFIG_INIT
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_CONFIG\_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the [NET\_ADAPTER\_CONFIG](net-adapter-config.md) structure.

Syntax
------

```ManagedCPlusPlus
FORCEINLINE VOID NET_ADAPTER_CONFIG_INIT(
  _Out_ PNET_ADAPTER_CONFIG              AdapterConfig,
  _In_  PFN_NET_ADAPTER_SET_CAPABILITIES EvtAdapterSetCapabilities,
  _In_  PFN_NET_ADAPTER_CREATE_TXQUEUE   EvtAdapterCreateTxQueue,
  _In_  PFN_NET_ADAPTER_CREATE_RXQUEUE   EvtAdapterCreateRxQueue,
);
```

Parameters
----------

*AdapterConfig* \[out\]  
A pointer to the driver-allocated [**NET\_ADAPTER\_CONFIG**](net-adapter-config.md) structure.

*EvtAdapterSetCapabilities* \[in\]  
A pointer to the client's implementation of the [*EVT\_NET\_ADAPTER\_SET\_CAPABILITIES*](evt-net-adapter-set-capabilities.md) event callback.

*EvtAdapterCreateTxQueue* \[in\]  
A pointer to the client's implementation of the [*EVT\_NET\_ADAPTER\_CREATE\_TXQUEUE*](evt-net-adapter-create-txqueue.md) event callback.

*EvtAdapterCreateRxQueue* \[in\]  
A pointer to the client's implementation of the [*EVT\_NET\_ADAPTER\_CREATE\_RXQUEUE*](evt-net-adapter-create-rxqueue.md) event callback.

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

 

 





