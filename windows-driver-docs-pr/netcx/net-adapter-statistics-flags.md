---
title: NET_ADAPTER_STATISTICS_FLAGS enumeration
description: .
ms.assetid: 64545e16-d6b4-439b-a913-c077bbe6ee32
keywords: ["NET_ADAPTER_STATISTICS_FLAGS enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_STATISTICS_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_STATISTICS\_FLAGS enumeration


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_STATISTICS_FLAGS { 
  NET_ADAPTER_STATISTICS_NO_FLAGS               = = 0,
  NET_ADAPTER_STATISTICS_XMIT_OK                = = NDIS_STATISTICS_XMIT_OK_SUPPORTED,
  NET_ADAPTER_STATISTICS_RCV_OK                 = = NDIS_STATISTICS_RCV_OK_SUPPORTED,
  NET_ADAPTER_STATISTICS_XMIT_ERROR             = = NDIS_STATISTICS_XMIT_ERROR_SUPPORTED,
  NET_ADAPTER_STATISTICS_RCV_ERROR              = = NDIS_STATISTICS_RCV_ERROR_SUPPORTED,
  NET_ADAPTER_STATISTICS_RCV_NO_BUFFER          = = NDIS_STATISTICS_RCV_NO_BUFFER_SUPPORTED,
  NET_ADAPTER_STATISTICS_DIRECTED_BYTES_XMIT    = = NDIS_STATISTICS_DIRECTED_BYTES_XMIT_SUPPORTED,
  NET_ADAPTER_STATISTICS_DIRECTED_FRAMES_XMIT   = = NDIS_STATISTICS_DIRECTED_FRAMES_XMIT_SUPPORTED,
  NET_ADAPTER_STATISTICS_MULTICAST_BYTES_XMIT   = = NDIS_STATISTICS_MULTICAST_BYTES_XMIT_SUPPORTED,
  NET_ADAPTER_STATISTICS_MULTICAST_FRAMES_XMIT  = = NDIS_STATISTICS_MULTICAST_FRAMES_XMIT_SUPPORTED,
  NET_ADAPTER_STATISTICS_BROADCAST_BYTES_XMIT   = = NDIS_STATISTICS_BROADCAST_BYTES_XMIT_SUPPORTED,
  NET_ADAPTER_STATISTICS_BROADCAST_FRAMES_XMIT  = = NDIS_STATISTICS_BROADCAST_FRAMES_XMIT_SUPPORTED,
  NET_ADAPTER_STATISTICS_DIRECTED_BYTES_RCV     = = NDIS_STATISTICS_DIRECTED_BYTES_RCV_SUPPORTED,
  NET_ADAPTER_STATISTICS_DIRECTED_FRAMES_RCV    = = NDIS_STATISTICS_DIRECTED_FRAMES_RCV_SUPPORTED,
  NET_ADAPTER_STATISTICS_MULTICAST_BYTES_RCV    = = NDIS_STATISTICS_MULTICAST_BYTES_RCV_SUPPORTED,
  NET_ADAPTER_STATISTICS_MULTICAST_FRAMES_RCV   = = NDIS_STATISTICS_MULTICAST_FRAMES_RCV_SUPPORTED,
  NET_ADAPTER_STATISTICS_BROADCAST_BYTES_RCV    = = NDIS_STATISTICS_BROADCAST_BYTES_RCV_SUPPORTED,
  NET_ADAPTER_STATISTICS_BROADCAST_FRAMES_RCV   = = NDIS_STATISTICS_BROADCAST_FRAMES_RCV_SUPPORTED,
  NET_ADAPTER_STATISTICS_RCV_CRC_ERROR          = = NDIS_STATISTICS_RCV_CRC_ERROR_SUPPORTED,
  NET_ADAPTER_STATISTICS_TRANSMIT_QUEUE_LENGTH  = = NDIS_STATISTICS_TRANSMIT_QUEUE_LENGTH_SUPPORTED,
  NET_ADAPTER_STATISTICS_BYTES_RCV              = = NDIS_STATISTICS_BYTES_RCV_SUPPORTED,
  NET_ADAPTER_STATISTICS_BYTES_XMIT             = = NDIS_STATISTICS_BYTES_XMIT_SUPPORTED,
  NET_ADAPTER_STATISTICS_RCV_DISCARDS           = = NDIS_STATISTICS_RCV_DISCARDS_SUPPORTED,
  NET_ADAPTER_STATISTICS_GEN_STATISTICS         = = NDIS_STATISTICS_GEN_STATISTICS_SUPPORTED,
  NET_ADAPTER_STATISTICS_XMIT_DISCARDS          = = NDIS_STATISTICS_XMIT_DISCARDS_SUPPORTED
} NET_ADAPTER_STATISTICS_FLAGS;
```

Constants
---------

<a href="" id="net-adapter-statistics-no-flags"></a>**NET\_ADAPTER\_STATISTICS\_NO\_FLAGS**  

<a href="" id="net-adapter-statistics-xmit-ok"></a>**NET\_ADAPTER\_STATISTICS\_XMIT\_OK**  

<a href="" id="net-adapter-statistics-rcv-ok"></a>**NET\_ADAPTER\_STATISTICS\_RCV\_OK**  

<a href="" id="net-adapter-statistics-xmit-error"></a>**NET\_ADAPTER\_STATISTICS\_XMIT\_ERROR**  

<a href="" id="net-adapter-statistics-rcv-error"></a>**NET\_ADAPTER\_STATISTICS\_RCV\_ERROR**  

<a href="" id="net-adapter-statistics-rcv-no-buffer"></a>**NET\_ADAPTER\_STATISTICS\_RCV\_NO\_BUFFER**  

<a href="" id="net-adapter-statistics-directed-bytes-xmit"></a>**NET\_ADAPTER\_STATISTICS\_DIRECTED\_BYTES\_XMIT**  

<a href="" id="net-adapter-statistics-directed-frames-xmit"></a>**NET\_ADAPTER\_STATISTICS\_DIRECTED\_FRAMES\_XMIT**  

<a href="" id="net-adapter-statistics-multicast-bytes-xmit"></a>**NET\_ADAPTER\_STATISTICS\_MULTICAST\_BYTES\_XMIT**  

<a href="" id="net-adapter-statistics-multicast-frames-xmit"></a>**NET\_ADAPTER\_STATISTICS\_MULTICAST\_FRAMES\_XMIT**  

<a href="" id="net-adapter-statistics-broadcast-bytes-xmit"></a>**NET\_ADAPTER\_STATISTICS\_BROADCAST\_BYTES\_XMIT**  

<a href="" id="net-adapter-statistics-broadcast-frames-xmit"></a>**NET\_ADAPTER\_STATISTICS\_BROADCAST\_FRAMES\_XMIT**  

<a href="" id="net-adapter-statistics-directed-bytes-rcv"></a>**NET\_ADAPTER\_STATISTICS\_DIRECTED\_BYTES\_RCV**  

<a href="" id="net-adapter-statistics-directed-frames-rcv"></a>**NET\_ADAPTER\_STATISTICS\_DIRECTED\_FRAMES\_RCV**  

<a href="" id="net-adapter-statistics-multicast-bytes-rcv"></a>**NET\_ADAPTER\_STATISTICS\_MULTICAST\_BYTES\_RCV**  

<a href="" id="net-adapter-statistics-multicast-frames-rcv"></a>**NET\_ADAPTER\_STATISTICS\_MULTICAST\_FRAMES\_RCV**  

<a href="" id="net-adapter-statistics-broadcast-bytes-rcv"></a>**NET\_ADAPTER\_STATISTICS\_BROADCAST\_BYTES\_RCV**  

<a href="" id="net-adapter-statistics-broadcast-frames-rcv"></a>**NET\_ADAPTER\_STATISTICS\_BROADCAST\_FRAMES\_RCV**  

<a href="" id="net-adapter-statistics-rcv-crc-error"></a>**NET\_ADAPTER\_STATISTICS\_RCV\_CRC\_ERROR**  

<a href="" id="net-adapter-statistics-transmit-queue-length"></a>**NET\_ADAPTER\_STATISTICS\_TRANSMIT\_QUEUE\_LENGTH**  

<a href="" id="net-adapter-statistics-bytes-rcv"></a>**NET\_ADAPTER\_STATISTICS\_BYTES\_RCV**  

<a href="" id="net-adapter-statistics-bytes-xmit"></a>**NET\_ADAPTER\_STATISTICS\_BYTES\_XMIT**  

<a href="" id="net-adapter-statistics-rcv-discards"></a>**NET\_ADAPTER\_STATISTICS\_RCV\_DISCARDS**  

<a href="" id="net-adapter-statistics-gen-statistics"></a>**NET\_ADAPTER\_STATISTICS\_GEN\_STATISTICS**  

<a href="" id="net-adapter-statistics-xmit-discards"></a>**NET\_ADAPTER\_STATISTICS\_XMIT\_DISCARDS**  

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_ADAPTER_STATISTICS_FLAGS%20enumeration%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




