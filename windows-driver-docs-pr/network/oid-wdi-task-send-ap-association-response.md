---
title: OID\_WDI\_TASK\_SEND\_AP\_ASSOCIATION\_RESPONSE
description: OID\_WDI\_TASK\_SEND\_AP\_ASSOCIATION\_RESPONSE requests that the IHV component sends an Association Response to a peer device that has recently sent an association request.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8d19b009-db81-4b5e-ac63-5e6c5ad9727d
keywords: ["OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE
api_location:
- dot11wdi.h
api_type:
- HeaderDef
---

# OID\_WDI\_TASK\_SEND\_AP\_ASSOCIATION\_RESPONSE


OID\_WDI\_TASK\_SEND\_AP\_ASSOCIATION\_RESPONSE requests that the IHV component sends an Association Response to a peer device that has recently sent an association request.

| Object | Abort capable                                           | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. The port must be in a clean state after the abort. | 3                                     | 1                               |

 

If the send fails for any reason, an empty [NDIS\_STATUS\_WDI\_INDICATION\_SEND\_AP\_ASSOCIATION\_RESPONSE\_COMPLETE](ndis-status-wdi-indication-send-ap-association-response-complete.md) is expected, with the correct status included in the populated header.

## Task parameters


| TLV                                                                                                      | Multiple TLV instances allowed | Optional | Description                                                                                                      |
|----------------------------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_ASSOCIATION\_RESPONSE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn926137)      |                                |          | Association response parameters.                                                                                 |
| [**WDI\_TLV\_VENDOR\_SPECIFIC\_IE**](https://msdn.microsoft.com/library/windows/hardware/dn898076)                                |                                | X        | Additional IEs that the port must append to Association Response IE set before sending response to peer adapter. |
| [**WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn926315) |                                |          | Information about the incoming association request.                                                              |
| [**WDI\_TLV\_WFD\_ASSOCIATION\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/mt269148)                        |                                | X        | The Status value to set when the association request is denied.                                                  |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_SEND\_AP\_ASSOCIATION\_RESPONSE\_COMPLETE](ndis-status-wdi-indication-send-ap-association-response-complete.md)
Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




