---
title: OID_WAN_CO_GET_LINK_INFO
description: The OID_WAN_CO_GET_LINK_INFO OID requests the miniport driver to return PPP framing information about the current state of a virtual connection (VC). This information is returned in an NDIS_WAN_CO_GET_LINK_INFO structure, defined as follows.
ms.assetid: 26582bc4-c32f-4243-a208-9230c62f4d16
ms.date: 08/08/2017
keywords: 
 -OID_WAN_CO_GET_LINK_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WAN\_CO\_GET\_LINK\_INFO


The OID\_WAN\_CO\_GET\_LINK\_INFO OID requests the miniport driver to return PPP framing information about the current state of a virtual connection (VC). This information is returned in an NDIS\_WAN\_CO\_GET\_LINK\_INFO structure, defined as follows.

```ManagedCPlusPlus
    typedef struct _NDIS_WAN_CO_GET_LINK_INFO {
         OUT ULONG MaxSendFrameSize;
         OUT ULONG MaxRecvFrameSize;
         OUT ULONG SendFramingBits;
         OUT ULONG RecvFramingBits;
         OUT ULONG SendCompressionBits;
         OUT ULONG RecvCompressionBits;
         OUT ULONG SendACCM;
         OUT ULONG RecvACCM;
    } NDIS_WAN_CO_GET_LINK_INFO,   *PNDIS_WAN_CO_GET_LINK_INFO;
```




The members of this structure contain the following information:

<a href="" id="maxsendframesize"></a>**MaxSendFrameSize**  
Specifies the maximum buffer size, in bytes, that the miniport driver can accept for transmission on this VC. The miniport driver's *MiniportCoSendPackets* function can reject any incoming send packet that is larger than this size.

<a href="" id="maxrecvframesize"></a>**MaxRecvFrameSize**  
Specifies the largest packet that will be received from the network. The miniport driver can drop any packets that are larger.

<a href="" id="sendframingbits"></a>**SendFramingBits**  
Specifies send-framing bits indicating the type of framing that should be sent. If the miniport driver detects incompatibilities between **SendFramingBits** and **RecvFramingBits**, it returns NDIS\_STATUS\_INVALID\_DATA.

The proper NLPID and framing format should be used based on the framing bits wherever applicable.

<a href="" id="recvframingbits"></a>**RecvFramingBits**  
Specifies receive-framing bits indicating the type of framing that should be received.

<a href="" id="sendcompressionbits"></a>**SendCompressionBits**  
Reserved.

<a href="" id="recvcompressionbits"></a>**RecvCompressionBits**  
Reserved.

<a href="" id="sendaccm"></a>**SendACCM**  
For asynchronous media types, logical bits 0-31 indicate the respective byte to be byte stuffed. That is, if bit 0 is set to 1, then ASCII character 0x00 should be byte stuffed, and so forth.

<a href="" id="recvaccm"></a>**RecvACCM**  
As described for **SendACCM**.

Remarks
-------

Possible values for **SendFramingBits** and **RecvFramingBits** include any the driver returned in response to the OID\_WAN\_CO\_GET\_LINK\_INFO query.

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

## See also


[OID\_WAN\_CO\_GET\_LINK\_INFO](oid-wan-co-get-link-info.md)








