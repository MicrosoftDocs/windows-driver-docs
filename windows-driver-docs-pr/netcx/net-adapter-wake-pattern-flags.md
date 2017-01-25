---
title: NET_ADAPTER_WAKE_PATTERN_FLAGS enumeration
description: .
ms.assetid: 211fde06-ee4d-412a-84ac-8979f6de2d25
keywords: ["NET_ADAPTER_WAKE_PATTERN_FLAGS enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_WAKE_PATTERN_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_WAKE\_PATTERN\_FLAGS enumeration


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_WAKE_PATTERN_FLAGS { 
  NET_ADAPTER_WAKE_BITMAP_PATTERN            = = NDIS_PM_WOL_BITMAP_PATTERN_ENABLED,
  NET_ADAPTER_WAKE_MAGIC_PACKET              = = NDIS_PM_WOL_MAGIC_PACKET_ENABLED,
  NET_ADAPTER_WAKE_IPV4_TCP_SYN              = = NDIS_PM_WOL_IPV4_TCP_SYN_ENABLED,
  NET_ADAPTER_WAKE_IPV6_TCP_SYN              = = NDIS_PM_WOL_IPV6_TCP_SYN_ENABLED,
  NET_ADAPTER_WAKE_IPV4_DEST_ADDR_WILDCARD   = = NDIS_PM_WOL_IPV4_DEST_ADDR_WILDCARD_ENABLED,
  NET_ADAPTER_WAKE_IPV6_DEST_ADDR_WILDCARD   = = NDIS_PM_WOL_IPV6_DEST_ADDR_WILDCARD_ENABLED,
  NET_ADAPTER_WAKE_EAPOL_REQUEST_ID_MESSAGE  = = NDIS_PM_WOL_EAPOL_REQUEST_ID_MESSAGE_ENABLED
} NET_ADAPTER_WAKE_PATTERN_FLAGS;
```

Constants
---------

<a href="" id="net-adapter-wake-bitmap-pattern"></a>**NET\_ADAPTER\_WAKE\_BITMAP\_PATTERN**  

<a href="" id="net-adapter-wake-magic-packet"></a>**NET\_ADAPTER\_WAKE\_MAGIC\_PACKET**  

<a href="" id="net-adapter-wake-ipv4-tcp-syn"></a>**NET\_ADAPTER\_WAKE\_IPV4\_TCP\_SYN**  

<a href="" id="net-adapter-wake-ipv6-tcp-syn"></a>**NET\_ADAPTER\_WAKE\_IPV6\_TCP\_SYN**  

<a href="" id="net-adapter-wake-ipv4-dest-addr-wildcard"></a>**NET\_ADAPTER\_WAKE\_IPV4\_DEST\_ADDR\_WILDCARD**  

<a href="" id="net-adapter-wake-ipv6-dest-addr-wildcard"></a>**NET\_ADAPTER\_WAKE\_IPV6\_DEST\_ADDR\_WILDCARD**  

<a href="" id="net-adapter-wake-eapol-request-id-message"></a>**NET\_ADAPTER\_WAKE\_EAPOL\_REQUEST\_ID\_MESSAGE**  

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_ADAPTER_WAKE_PATTERN_FLAGS%20enumeration%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




