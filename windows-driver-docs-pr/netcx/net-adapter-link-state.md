---
title: NET_ADAPTER_LINK_STATE structure
topic_type:
- apiref
api_name:
- NET_ADAPTER_LINK_STATE
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_LINK_STATE structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Describes the link state of the adapter.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_ADAPTER_LINK_STATE {
  ULONG                                Size;
  ULONG64                              TxLinkSpeed;
  ULONG64                              RxLinkSpeed;
  NET_IF_MEDIA_CONNECT_STATE           MediaConnectState;
  NET_IF_MEDIA_DUPLEX_STATE            MediaDuplexState;
  NET_ADAPTER_PAUSE_FUNCTIONS          SupportedPauseFunctions;
  NET_ADAPTER_AUTO_NEGOTIATION_FLAGS   AutoNegotiationFlags;
} NET_ADAPTER_LINK_STATE, *PNET_ADAPTER_LINK_STATE;
```

Members
-------

**Size**  
Size of the **NET_ADAPTER_LINK_STATE** structure.

**TxLinkSpeed**  
The current transmit link speed of the adapter in bits per second.

**RxLinkSpeed**  
The current receive link speed of the adapter in bits per second.

**MediaConnectState**  
The media connect state for the network adapter.

**MediaDuplexState**  
The media duplex state for the network adapter.

**SupportedPauseFunctions**  
Support for the IEEE 802.3 pause frames. For more info, see [**NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923).

**AutoNegotiationFlags**  
The auto-negotiation settings for the network adapter. For more info, see [**NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923).

Remarks
-------

Call [**NET_ADAPTER_LINK_STATE_INIT**](net-adapter-link-state-init.md) or [**NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED**](net-adapter-link-state-init-disconnected.md) to initialize this structure.

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

## See also

[**NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)

[**NET_ADAPTER_LINK_STATE_INIT**](net-adapter-link-state-init.md)

[**NET_ADAPTER_LINK_STATE_INIT_DISCONNECTED**](net-adapter-link-state-init-disconnected.md)

[**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md)

 

 






