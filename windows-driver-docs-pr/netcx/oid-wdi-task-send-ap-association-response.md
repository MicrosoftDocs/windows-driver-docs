---
title: OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE (dot11wificxintf.h)
description: The OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE command requests that the IHV component sends an Association Response to a peer device that has recently sent an association request.
ms.date: 07/31/2021
keywords:
 - OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_SEND\_AP\_ASSOCIATION\_RESPONSE (dot11wificxintf.h)


OID\_WDI\_TASK\_SEND\_AP\_ASSOCIATION\_RESPONSE requests that the IHV component sends an Association Response to a peer device that has recently sent an association request.

| Object | Abort capable                                           | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. The port must be in a clean state after the abort. | 3                                     | 1                               |

 

If the send fails for any reason, an empty [NDIS\_STATUS\_WDI\_INDICATION\_SEND\_AP\_ASSOCIATION\_RESPONSE\_COMPLETE](ndis-status-wdi-indication-send-ap-association-response-complete.md) is expected, with the correct status included in the populated header.

## Task parameters


| TLV                                                                                                      | Multiple TLV instances allowed | Optional | Description                                                                                                      |
|----------------------------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_ASSOCIATION\_RESPONSE\_PARAMETERS**](./wdi-tlv-association-response-parameters.md)      |                                |          | Association response parameters.                                                                                 |
| [**WDI\_TLV\_VENDOR\_SPECIFIC\_IE**](./wdi-tlv-vendor-specific-ie.md)                                |                                | X        | Additional IEs that the port must append to Association Response IE set before sending response to peer adapter. |
| [**WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_INFO**](./wdi-tlv-incoming-association-request-info.md) |                                |          | Information about the incoming association request.                                                              |
| [**WDI\_TLV\_WFD\_ASSOCIATION\_STATUS**](./wdi-tlv-wfd-association-status.md)                        |                                | X        | The Status value to set when the association request is denied.                                                  |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_SEND\_AP\_ASSOCIATION\_RESPONSE\_COMPLETE](ndis-status-wdi-indication-send-ap-association-response-complete.md)

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

