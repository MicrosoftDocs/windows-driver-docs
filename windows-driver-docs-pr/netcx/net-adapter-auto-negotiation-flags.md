---
title: NET_ADAPTER_AUTO_NEGOTIATION_FLAGS enumeration
description: .
ms.assetid: e879294b-f70c-4dd2-9367-111facddf776
keywords: ["NET_ADAPTER_AUTO_NEGOTIATION_FLAGS enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_AUTO_NEGOTIATION_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_AUTO\_NEGOTIATION\_FLAGS enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_AUTO_NEGOTIATION_FLAGS { 
  NET_ADAPTER_AUTO_NEGOTIATION_NO_FLAGS                   = = 0,
  NET_ADAPTER_LINK_STATE_XMIT_LINK_SPEED_AUTO_NEGOTIATED  = = NDIS_LINK_STATE_XMIT_LINK_SPEED_AUTO_NEGOTIATED,
  NET_ADAPTER_LINK_STATE_RCV_LINK_SPEED_AUTO_NEGOTIATED   = = NDIS_LINK_STATE_RCV_LINK_SPEED_AUTO_NEGOTIATED,
  NET_ADAPTER_LINK_STATE_DUPLEX_AUTO_NEGOTIATED           = = NDIS_LINK_STATE_DUPLEX_AUTO_NEGOTIATED,
  NET_ADAPTER_LINK_STATE_PAUSE_FUNCTIONS_AUTO_NEGOTIATED  = = NDIS_LINK_STATE_PAUSE_FUNCTIONS_AUTO_NEGOTIATED
} NET_ADAPTER_AUTO_NEGOTIATION_FLAGS;
```

Constants
---------

<a href="" id="net-adapter-auto-negotiation-no-flags"></a>**NET\_ADAPTER\_AUTO\_NEGOTIATION\_NO\_FLAGS**  

<a href="" id="net-adapter-link-state-xmit-link-speed-auto-negotiated"></a>**NET\_ADAPTER\_LINK\_STATE\_XMIT\_LINK\_SPEED\_AUTO\_NEGOTIATED**  

<a href="" id="net-adapter-link-state-rcv-link-speed-auto-negotiated"></a>**NET\_ADAPTER\_LINK\_STATE\_RCV\_LINK\_SPEED\_AUTO\_NEGOTIATED**  

<a href="" id="net-adapter-link-state-duplex-auto-negotiated"></a>**NET\_ADAPTER\_LINK\_STATE\_DUPLEX\_AUTO\_NEGOTIATED**  

<a href="" id="net-adapter-link-state-pause-functions-auto-negotiated"></a>**NET\_ADAPTER\_LINK\_STATE\_PAUSE\_FUNCTIONS\_AUTO\_NEGOTIATED**  

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

 

 





