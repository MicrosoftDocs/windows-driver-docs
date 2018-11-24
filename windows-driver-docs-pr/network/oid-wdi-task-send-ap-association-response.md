---
title: OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE
description: OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE requests that the IHV component sends an Association Response to a peer device that has recently sent an association request.
ms.assetid: 8d19b009-db81-4b5e-ac63-5e6c5ad9727d
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




