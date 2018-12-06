---
title: OID_WAN_CO_GET_STATS_INFO
description: The OID_WAN_CO_GET_STATS_INFO OID requests the miniport driver to return statistics information that is specific to a virtual connection (VC).
ms.assetid: 53ab1c04-7bb2-401d-ad54-72f3c1587dc0
ms.date: 08/08/2017
keywords: 
 -OID_WAN_CO_GET_STATS_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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








