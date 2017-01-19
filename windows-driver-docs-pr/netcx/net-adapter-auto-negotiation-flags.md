---
title: NET\_ADAPTER\_AUTO\_NEGOTIATION\_FLAGS enumeration
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


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_ADAPTER_AUTO_NEGOTIATION_FLAGS%20enumeration%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




