---
title: NET_ADAPTER_AUTO_NEGOTIATION_FLAGS enumeration
topic_type:
- apiref
api_name:
- NET_ADAPTER_AUTO_NEGOTIATION_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_AUTO_NEGOTIATION_FLAGS enumeration

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Specifies the auto-negotiation settings for the miniport adapter.

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_AUTO_NEGOTIATION_FLAGS { 
  NET_ADAPTER_AUTO_NEGOTIATION_NO_FLAGS                   = = 0,
  NET_ADAPTER_LINK_STATE_XMIT_LINK_SPEED_AUTO_NEGOTIATED  = NDIS_LINK_STATE_XMIT_LINK_SPEED_AUTO_NEGOTIATED,
  NET_ADAPTER_LINK_STATE_RCV_LINK_SPEED_AUTO_NEGOTIATED   = NDIS_LINK_STATE_RCV_LINK_SPEED_AUTO_NEGOTIATED,
  NET_ADAPTER_LINK_STATE_DUPLEX_AUTO_NEGOTIATED           = NDIS_LINK_STATE_DUPLEX_AUTO_NEGOTIATED,
  NET_ADAPTER_LINK_STATE_PAUSE_FUNCTIONS_AUTO_NEGOTIATED  = NDIS_LINK_STATE_PAUSE_FUNCTIONS_AUTO_NEGOTIATED
} NET_ADAPTER_AUTO_NEGOTIATION_FLAGS;
```

Constants
---------

**NET_ADAPTER_AUTO_NEGOTIATION_NO_FLAGS**  
No flags are set.

**NET_ADAPTER_LINK_STATE_XMIT_LINK_SPEED_AUTO_NEGOTIATED**  
The adapter has auto-negotiated the transmit link speed with the link partner.

**NET_ADAPTER_LINK_STATE_RCV_LINK_SPEED_AUTO_NEGOTIATED**  
The adapter has auto-negotiated the receive link speed with the link partner.

**NET_ADAPTER_LINK_STATE_DUPLEX_AUTO_NEGOTIATED**  
The adapter has auto-negotiated the duplex state with the link partner.

**NET_ADAPTER_LINK_STATE_PAUSE_FUNCTIONS_AUTO_NEGOTIATED**  
The adapter has auto-negotiated the pause functions with the link partner.

Remarks
---
The **NET_ADAPTER_AUTO_NEGOTIATION_FLAGS** enumeration is used to specify auto-negotiation settings in the [**NET_ADAPTER_LINK_STATE**](net-adapter-link-state.md) structure.

An initialized [**NET_ADAPTER_LINK_STATE**](net-adapter-link-state.md) structure is an input to [**NetAdapterSetCurrentLinkState**](netadaptersetcurrentlinkstate.md).

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

See Also
-----
[**NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)


