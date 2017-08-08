---
title: OID\_WAN\_CO\_GET\_STATS\_INFO
author: windows-driver-content
description: The OID\_WAN\_CO\_GET\_STATS\_INFO OID requests the miniport driver to return statistics information that is specific to a virtual connection (VC).
ms.assetid: 53ab1c04-7bb2-401d-ad54-72f3c1587dc0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WAN_CO_GET_STATS_INFO Network Drivers Starting with Windows Vista
---

# OID\_WAN\_CO\_GET\_STATS\_INFO


The OID\_WAN\_CO\_GET\_STATS\_INFO OID requests the miniport driver to return statistics information that is specific to a virtual connection (VC). A WAN miniport driver is expected to keep statistics and to return these statistics for this OID in an NDIS\_WAN\_CO\_GET\_STATS\_INFO structure, defined as follows:

```ManagedCPlusPlus
    typedef struct _NDIS_WAN_CO_GET_STATS_INFO {
         OUT ULONG BytesSent;
         OUT ULONG BytesRcvd;
         OUT ULONG FramesSent;
         OUT ULONG FramesRcvd;
         OUT ULONG CRCErrors;
         OUT ULONG TimeoutErrors;
         OUT ULONG AlignmentErrors;
         OUT ULONG SerialOverrunErrors;
         OUT ULONG FramingErrors;
         OUT ULONG BufferOverrunErrors;
         OUT ULONG BytesTransmittedUncompressed;
         OUT ULONG BytesReceivedUncompressed;
         OUT ULONG BytesTransmittedCompressed;
         OUT ULONG BytesReceivedCompressed;
    } NDIS_WAN_CO_GET_STATS_INFO,   *PNDIS_WAN_CO_GET_STATS_INFO;
  
```

## <a href="" id="ddk-oid-wan-co-get-stats-info-nr"></a>


The members of this structure contain the following information:

<a href="" id="bytessent"></a>**BytesSent**  
Specifies the number of bytes transmitted.

<a href="" id="bytesrcvd"></a>**BytesRcvd**  
Specifies the number of bytes received.

<a href="" id="framessent"></a>**FramesSent**  
Specifies the number of frames (WAN packets) sent.

<a href="" id="framesrcvd"></a>**FramesRcvd**  
Specifies the number of frames received.

<a href="" id="crcerrors"></a>**CRCErrors**  
Specifies the number of CRC errors encountered for this VC. CRC errors are caused by the failure of a cyclic redundancy check. A CRC error indicates that one or more bytes in the frame received were found garbled on arrival.

<a href="" id="timeouterrors"></a>**TimeoutErrors**  
Specifies the number of time-out errors encountered for this VC. Time-out errors occur when an expected byte is not received in time.

<a href="" id="alignmenterrors"></a>**AlignmentErrors**  
Specifies the number of alignment errors encountered for this VC. Alignment errors occur when a byte received is different from the byte expected. This typically happens when a byte is lost or when a time-out error occurs.

<a href="" id="serialoverrunerrors"></a>**SerialOverrunErrors**  
Specifies the number of serial overruns encountered for this VC. Serial overruns occur when the WAN NIC cannot handle the rate at which data is received.

<a href="" id="framingerrors"></a>**FramingErrors**  
Specifies the number of framing errors encountered for this VC. A framing error occurs when an asynchronous byte is received with an invalid start or stop bit.

<a href="" id="bufferoverrunerrors"></a>**BufferOverrunErrors**  
Specifies the number of buffer overruns encountered for this VC. Buffer overruns occur when the WAN miniport driver cannot handle the rate at which data is received.

<a href="" id="bytestransmitteduncompressed"></a>**BytesTransmittedUncompressed**  
Specifies the number of bytes of uncompressed data transmitted. A miniport driver returns a nonzero value only if it supports compression.

<a href="" id="bytesreceiveduncompressed"></a>**BytesReceivedUncompressed**  
Specifies the number of bytes of uncompressed data received. A miniport driver returns a nonzero value only if it supports compression.

<a href="" id="bytestransmittedcompressed"></a>**BytesTransmittedCompressed**  
Specifies the number of bytes of compressed data transmitted. A miniport driver returns a nonzero value only if it supports compression.

<a href="" id="bytesreceivedcompressed"></a>**BytesReceivedCompressed**  
Specifies the number of bytes of compressed data received. A miniport driver returns a nonzero value only if it supports compression.

Remarks
-------

If the underlying driver or its NIC does not support compression, the driver returns zero for the **Bytes..Uncompressed/Compressed** members.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS 5.1 drivers in Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WAN_CO_GET_STATS_INFO%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


