---
title: OID_WAN_CO_SET_LINK_INFO
description: The OID_WAN_CO_SET_LINK_INFO OID requests the miniport driver to set PPP framing information for a specific virtual connection (VC). A protocol uses an NDIS_WAN_CO_SET_LINK_INFO structure, defined as follows, to indicate this PPP framing information.
ms.assetid: 4487289a-01f6-4ae1-b660-3011d66acb29
ms.date: 08/08/2017
keywords: 
 -OID_WAN_CO_SET_LINK_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WAN\_CO\_SET\_LINK\_INFO


The OID\_WAN\_CO\_SET\_LINK\_INFO OID requests the miniport driver to set PPP framing information for a specific virtual connection (VC). A protocol uses an NDIS\_WAN\_CO\_SET\_LINK\_INFO structure, defined as follows, to indicate this PPP framing information.

```ManagedCPlusPlus
    typedef struct _NDIS_WAN_CO_SET_LINK_INFO {
         IN ULONG MaxSendFrameSize;
         IN ULONG MaxRecvFrameSize;
         IN ULONG SendFramingBits;
         IN ULONG RecvFramingBits;
         IN ULONG SendCompressionBits;
         IN ULONG RecvCompressionBits;
         IN ULONG SendACCM;
         IN ULONG RecvACCM;
    } NDIS_WAN_CO_SET_LINK_INFO,   *PNDIS_WAN_CO_SET_LINK_INFO;
```




The members of this structure contain the following information:

<a href="" id="maxsendframesize"></a>**MaxSendFrameSize**  
Specifies the largest buffer, in bytes, the protocol will send for this VC. This value must be less than or equal to that returned by the miniport driver for the [OID\_WAN\_CO\_GET\_LINK\_INFO](oid-wan-co-get-link-info.md) query.

The miniport driver's *MiniportCoSendPackets* function can reject any send packets submitted for this link that are larger than this value.

<a href="" id="maxrecvframesize"></a>**MaxRecvFrameSize**  
Specifies the largest network packet that the protocol will receive subsequently. This value must be less than or equal to that returned by the miniport driver for the OID\_WAN\_CO\_GET\_LINK\_INFO query. The miniport driver can drop any received packets for this VC that are larger.

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
For asynchronous media types, logical bits 0-31 indicate the respective byte to be byte stuffed. That is, if bit 0 is set to one then ASCII character 0x00 should be byte stuffed, and so forth.

<a href="" id="recvaccm"></a>**RecvACCM**  
As described for **SendACCM**.

Remarks
-------

Possible values for **SendFramingBits** and **RecvFramingBits** include any the underlying driver returned in response to the [OID\_WAN\_CO\_GET\_INFO](oid-wan-co-get-info.md) query.

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


[OID\_WAN\_CO\_GET\_INFO](oid-wan-co-get-info.md)

[OID\_WAN\_CO\_GET\_LINK\_INFO](oid-wan-co-get-link-info.md)








