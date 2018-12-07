---
title: OID_GEN_STATISTICS
description: As a query, NDIS and overlying drivers use the OID_GEN_STATISTICS OID to obtain statistics of an adapter or a miniport driver.
ms.assetid: ff81d6b0-806d-4ddf-9da1-a169221be61f
ms.date: 08/08/2017
keywords: 
 -OID_GEN_STATISTICS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_STATISTICS


As a query, NDIS and overlying drivers use the OID\_GEN\_STATISTICS OID to obtain statistics of an adapter or a miniport driver.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Mandatory.

The NDIS\_STATISTICS\_INFO structure is defined as follows:

```ManagedCPlusPlus
    typedef struct _NDIS_STATISTICS_INFO {
         NDIS_OBJECT_HEADER Header;
         ULONG SupportedStatistics;
         ULONG64 ifInDiscards;
         ULONG64 ifInErrors;
         ULONG64 ifHCInOctets;
         ULONG64 ifHCInUcastPkts;
         ULONG64 ifHCInMulticastPkts;
         ULONG64 ifHCInBroadcastPkts;
         ULONG64 ifHCOutOctets;
         ULONG64 ifHCOutUcastPkts;
         ULONG64 ifHCOutMulticastPkts;
         ULONG64 ifHCOutBroadcastPkts;
         ULONG64 ifOutErrors;
         ULONG64 ifOutDiscards;
         ULONG64 ifHCInUcastOctets;
         ULONG64 ifHCInMulticastOctets;
         ULONG64 ifHCInBroadcastOctets;
         ULONG64 ifHCOutUcastOctets;
         ULONG64 ifHCOutMulticastOctets;
         ULONG64 ifHCOutBroadcastOctets;
    } NDIS_STATISTICS_INFO, *PNDIS_STATISTICS_INFO;
```




This structure contains the following members:

<a href="" id="header"></a>**Header**  
The [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure for the NDIS\_STATISTICS\_INFO structure. Set the **Type** member of the structure that **Header** specifies to NDIS\_OBJECT\_TYPE\_DEFAULT, the **Revision** member to NDIS\_STATISTICS\_INFO\_REVISION\_1, and the **Size** member to NDIS\_SIZEOF\_STATISTICS\_INFO\_REVISION\_1.

<a href="" id="supportedstatistics"></a>**SupportedStatistics**  
The set of statistics that the miniport driver supports.

**Note**  NDIS 6.0 and later drivers must support all statistics and must report them when queried for OID\_GEN\_STATISTICS.



The value is the bitwise OR of the following flags:

<a href="" id="ndis-statistics-flags-valid-directed-frames-rcv"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_DIRECTED\_FRAMES\_RCV  
The data in the **ifHCInUcastPkts** member is valid.

<a href="" id="ndis-statistics-flags-valid-multicast-frames-rcv"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_MULTICAST\_FRAMES\_RCV  
The data in the **ifHCInMulticastPkts** member is valid.

<a href="" id="ndis-statistics-flags-valid-broadcast-frames-rcv"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_BROADCAST\_FRAMES\_RCV  
The data in the **ifHCInBroadcastPkts** member is valid.

<a href="" id="ndis-statistics-flags-valid-bytes-rcv"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_BYTES\_RCV  
The data in the **ifHCInOctets** member is valid.

<a href="" id="ndis-statistics-flags-valid-rcv-discards"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_RCV\_DISCARDS  
The data in the **ifInDiscards** member is valid.

<a href="" id="ndis-statistics-flags-valid-rcv-error"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_RCV\_ERROR  
The data in the **ifInErrors** member is valid.

<a href="" id="ndis-statistics-flags-valid-directed-frames-xmit"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_DIRECTED\_FRAMES\_XMIT  
The data in the **ifHCOutUcastPkts** member is valid.

<a href="" id="ndis-statistics-flags-valid-multicast-frames-xmit"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_MULTICAST\_FRAMES\_XMIT  
The data in the **ifHCOutMulticastPkts** member is valid.

<a href="" id="ndis-statistics-flags-valid-broadcast-frames-xmit"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_BROADCAST\_FRAMES\_XMIT  
The data in the **ifHCOutBroadcastPkts** member is valid.

<a href="" id="ndis-statistics-flags-valid-bytes-xmit"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_BYTES\_XMIT  
The data in the **ifHCOutOctets** member is valid.

<a href="" id="ndis-statistics-flags-valid-xmit-error"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_XMIT\_ERROR  
The data in the **ifOutErrors** member is valid.

<a href="" id="ndis-statistics-flags-valid-xmit-discards"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_XMIT\_DISCARDS  
The data in the **ifOutDiscards** member is valid.

<a href="" id="ndis-statistics-flags-valid-directed-bytes-rcv"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_DIRECTED\_BYTES\_RCV  
The data in the **ifHCInUcastOctets** member is valid.

<a href="" id="ndis-statistics-flags-valid-multicast-bytes-rcv"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_MULTICAST\_BYTES\_RCV  
The data in the **ifHCInMulticastOctets** member is valid.

<a href="" id="ndis-statistics-flags-valid-broadcast-bytes-rcv"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_BROADCAST\_BYTES\_RCV  
The data in the **ifHCInBroadcastOctets** member is valid.

<a href="" id="ndis-statistics-flags-valid-directed-bytes-xmit"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_DIRECTED\_BYTES\_XMIT  
The data in the **ifHCOutUcastOctets** member is valid.

<a href="" id="ndis-statistics-flags-valid-multicast-bytes-xmit"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_MULTICAST\_BYTES\_XMIT  
The data in the **ifHCOutMulticastOctets** member is valid.

<a href="" id="ndis-statistics-flags-valid-broadcast-bytes-xmit"></a>NDIS\_STATISTICS\_FLAGS\_VALID\_BROADCAST\_BYTES\_XMIT  
The data in the **ifHCOutBroadcastOctets** member is valid.

<a href="" id="ifindiscards"></a>**ifInDiscards**  
The dropped-receive-buffer error count. This is the same value that [OID\_GEN\_RCV\_DISCARDS](oid-gen-rcv-discards.md) returns.

<a href="" id="ifinerrors"></a>**ifInErrors**  
The receive error count. This count is the same value that [OID\_GEN\_RCV\_ERROR](oid-gen-rcv-error.md) returns.

<a href="" id="ifhcinoctets"></a>**ifHCInOctets**  
The sum of the receive-directed byte count, receive-multicast byte count, and receive-broadcast byte count. This sum is the same value that [OID\_GEN\_BYTES\_RCV](oid-gen-bytes-rcv.md) returns.

<a href="" id="ifhcinucastpkts"></a>**ifHCInUcastPkts**  
The number of directed packets that are received without errors. This number is the same value that [OID\_GEN\_DIRECTED\_FRAMES\_RCV](oid-gen-directed-frames-rcv.md) returns.

<a href="" id="ifhcinmulticastpkts"></a>**ifHCInMulticastPkts**  
The number of multicast/functional packets that are received without errors. This number is the same value that [OID\_GEN\_MULTICAST\_FRAMES\_RCV](oid-gen-multicast-frames-rcv.md) returns.

<a href="" id="ifhcinbroadcastpkts"></a>**ifHCInBroadcastPkts**  
The number of broadcast packets that are received without errors. This number is the same value that [OID\_GEN\_BROADCAST\_FRAMES\_RCV](oid-gen-broadcast-frames-rcv.md) returns.

<a href="" id="ifhcoutoctets"></a>**ifHCOutOctets**  
The sum of the transmit-directed byte count, transmit-multicast byte count and transmit-broadcast byte count. This sum is the same value that [OID\_GEN\_BYTES\_XMIT](oid-gen-bytes-xmit.md) returns.

<a href="" id="ifhcoutucastpkts"></a>**ifHCOutUcastPkts**  
The number of directed packets that are transmitted without errors. This number is the same value that [OID\_GEN\_DIRECTED\_FRAMES\_XMIT](oid-gen-directed-frames-xmit.md) returns.

<a href="" id="ifhcoutmulticastpkts"></a>**ifHCOutMulticastPkts**  
The number of multicast/functional packets that are transmitted without errors. This number is the same value that [OID\_GEN\_MULTICAST\_FRAMES\_XMIT](oid-gen-multicast-frames-xmit.md) returns.

<a href="" id="ifhcoutbroadcastpkts"></a>**ifHCOutBroadcastPkts**  
The number of broadcast packets that are transmitted without errors. This number is the same value that [OID\_GEN\_BROADCAST\_FRAMES\_XMIT](oid-gen-broadcast-frames-xmit.md) returns.

<a href="" id="ifouterrors"></a>**ifOutErrors**  
The transmit error count. This count is the same value that [OID\_GEN\_XMIT\_ERROR](oid-gen-xmit-error.md) returns.

<a href="" id="ifoutdiscards"></a>**ifOutDiscards**  
The number of packets that is discarded by the interface. This is same as the value that is returned by querying the [OID\_GEN\_XMIT\_DISCARDS](oid-gen-xmit-discards.md) OID.

<a href="" id="ifhcinucastoctets"></a>**ifHCInUcastOctets**  
The number of bytes in directed packets that are received without errors. This count is the same value that [OID\_GEN\_DIRECTED\_BYTES\_RCV](oid-gen-directed-bytes-rcv.md) returns.

<a href="" id="ifhcinmulticastoctets"></a>**ifHCInMulticastOctets**  
The number of bytes in multicast/functional packets that are received without errors. This count is the same value that [OID\_GEN\_MULTICAST\_BYTES\_RCV](oid-gen-multicast-bytes-rcv.md) returns.

<a href="" id="ifhcinbroadcastoctets"></a>**ifHCInBroadcastOctets**  
The number of bytes in broadcast packets that are received without errors. This count is the same value that [OID\_GEN\_BROADCAST\_BYTES\_RCV](oid-gen-broadcast-bytes-rcv.md) returns.

<a href="" id="ifhcoutucastoctets"></a>**ifHCOutUcastOctets**  
The number of bytes in directed packets that are transmitted without errors. This count is the same value that [OID\_GEN\_DIRECTED\_BYTES\_XMIT](oid-gen-directed-bytes-xmit.md) returns.

<a href="" id="ifhcoutmulticastoctets"></a>**ifHCOutMulticastOctets**  
The number of bytes in multicast/functional packets that are transmitted without errors. This count is the same value that [OID\_GEN\_MULTICAST\_BYTES\_XMIT](oid-gen-multicast-bytes-xmit.md) returns.

<a href="" id="ifhcoutbroadcastoctets"></a>**ifHCOutBroadcastOctets**  
The number of bytes in broadcast packets that are transmitted without errors. This count is the same value that [OID\_GEN\_BROADCAST\_BYTES\_XMIT](oid-gen-broadcast-bytes-xmit.md) returns.

Remarks
-------

Miniport drivers must implement the statistics counters and report the correct statistics values. The statistics counters are unsigned 64-bit values. The miniport driver returns the statistics in an NDIS\_STATISTICS\_INFO structure.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588)

[OID\_GEN\_BROADCAST\_BYTES\_RCV](oid-gen-broadcast-bytes-rcv.md)

[OID\_GEN\_BROADCAST\_BYTES\_XMIT](oid-gen-broadcast-bytes-xmit.md)

[OID\_GEN\_BROADCAST\_FRAMES\_RCV](oid-gen-broadcast-frames-rcv.md)

[OID\_GEN\_BROADCAST\_FRAMES\_XMIT](oid-gen-broadcast-frames-xmit.md)

[OID\_GEN\_BYTES\_RCV](oid-gen-bytes-rcv.md)

[OID\_GEN\_BYTES\_XMIT](oid-gen-bytes-xmit.md)

[OID\_GEN\_DIRECTED\_BYTES\_RCV](oid-gen-directed-bytes-rcv.md)

[OID\_GEN\_DIRECTED\_BYTES\_XMIT](oid-gen-directed-bytes-xmit.md)

[OID\_GEN\_DIRECTED\_FRAMES\_RCV](oid-gen-directed-frames-rcv.md)

[OID\_GEN\_DIRECTED\_FRAMES\_XMIT](oid-gen-directed-frames-xmit.md)

[OID\_GEN\_MULTICAST\_FRAMES\_RCV](oid-gen-multicast-frames-rcv.md)

[OID\_GEN\_MULTICAST\_FRAMES\_XMIT](oid-gen-multicast-frames-xmit.md)

[OID\_GEN\_MULTICAST\_BYTES\_RCV](oid-gen-multicast-bytes-rcv.md)

[OID\_GEN\_MULTICAST\_BYTES\_XMIT](oid-gen-multicast-bytes-xmit.md)

[OID\_GEN\_RCV\_DISCARDS](oid-gen-rcv-discards.md)

[OID\_GEN\_RCV\_ERROR](oid-gen-rcv-error.md)

[OID\_GEN\_XMIT\_DISCARDS](oid-gen-xmit-discards.md)

[OID\_GEN\_XMIT\_ERROR](oid-gen-xmit-error.md)








