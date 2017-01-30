---
title: NET_ADAPTER_LINK_STATE structure
description: Describes the link state of the adapter.
ms.assetid: c7feb12d-37e1-47d5-bd5b-54eded600c28
keywords: ["NET_ADAPTER_LINK_STATE structure Network Drivers Starting with Windows Vista", "PNET_ADAPTER_LINK_STATE structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_LINK_STATE
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_LINK\_STATE structure


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
Size of the **NET\_ADAPTER\_LINK\_STATE** structure.

**TxLinkSpeed**  
The current transmit link speed of the adapter in bits per second.

**RxLinkSpeed**  
The current receive link speed of the adapter in bits per second.

**MediaConnectState**  
The media connect state for the miniport adapter.

**MediaDuplexState**  
The media duplex state for the miniport adapter.

**SupportedPauseFunctions**  
Support for the IEEE 802.3 pause frames. For more info, see [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923).

**AutoNegotiationFlags**  
The auto-negotiation settings for the miniport adapter. For more info, see [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923).

Remarks
-------

Call [**NET\_ADAPTER\_LINK\_STATE\_INIT**](net-adapter-link-state-init.md) or [**NET\_ADAPTER\_LINK\_STATE\_INIT\_DISCONNECTED**](net-adapter-link-state-init-disconnected.md) to initialize this structure.

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


[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)

[**NET\_ADAPTER\_LINK\_STATE\_INIT**](net-adapter-link-state-init.md)

[**NET\_ADAPTER\_LINK\_STATE\_INIT\_DISCONNECTED**](net-adapter-link-state-init-disconnected.md)

[**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md)

 

 






