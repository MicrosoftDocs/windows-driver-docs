---
title: NET_ADAPTER_LINK_STATE_INIT method
topic_type:
- apiref
api_name:
- NET_ADAPTER_LINK_STATE_INIT
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_LINK\_STATE\_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes a [NET\_ADAPTER\_LINK\_STATE](net-adapter-link-state.md) structure.

Syntax
------

```ManagedCPlusPlus
FORCEINLINE VOID NET_ADAPTER_LINK_STATE_INIT(
  _Out_ PNET_ADAPTER_LINK_STATE            LinkState,
  _In_  ULONG64                            LinkSpeed,
  _In_  NET_IF_MEDIA_CONNECT_STATE         MediaConnectState,
  _In_  NET_IF_MEDIA_DUPLEX_STATE          MediaDuplexState,
  _In_  NET_ADAPTER_PAUSE_FUNCTIONS        SupportedPauseFunctions,
  _In_  NET_ADAPTER_AUTO_NEGOTIATION_FLAGS SupportedPauseFunctions
);
```

Parameters
----------

*LinkState* \[out\]  
A pointer to a driver-allocated [**NET\_ADAPTER\_LINK\_STATE**](net-adapter-link-state.md) structure.

*LinkSpeed* \[in\]  
The link speed of the adapter in bits per second.

*MediaConnectState* \[in\]  
The media connect state for the miniport adapter.

*MediaDuplexState* \[in\]  
The media duplex state for the miniport adapter.

*SupportedPauseFunctions* \[in\]  
Support for the IEEE 802.3 pause frames. For more info, see [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923).

*SupportedPauseFunctions* \[in\]  
The auto-negotiation settings for the miniport adapter. For more info, see [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923).

Return value
------------

This method does not return a value.

Remarks
-------

Call **NET\_ADAPTER\_LINK\_STATE\_INIT** or [**NET\_ADAPTER\_LINK\_STATE\_INIT\_DISCONNECTED**](net-adapter-link-state-init-disconnected.md) to initialize a [**NET\_ADAPTER\_LINK\_STATE**](net-adapter-link-state.md) structure.

An initialized **NET\_ADAPTER\_LINK\_STATE** structure is an input parameter value to [**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md).

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

[**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md)

[**NET\_ADAPTER\_LINK\_STATE\_INIT\_DISCONNECTED**](net-adapter-link-state-init-disconnected.md)

[**NET\_ADAPTER\_LINK\_STATE**](net-adapter-link-state.md)

 






