---
title: WDI_TLV_ASSOCIATION_RESPONSE_PARAMETERS (dot11wificxtypes.h)
description: WDI_TLV_ASSOCIATION_RESPONSE_PARAMETERS is a WiFiCx TLV that contains association response parameters for OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_ASSOCIATION_RESPONSE_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ASSOCIATION\_RESPONSE\_PARAMETERS (dot11wificxtypes.h)


WDI\_TLV\_ASSOCIATION\_RESPONSE\_PARAMETERS is a TLV that contains association response parameters for [OID\_WDI\_TASK\_SEND\_AP\_ASSOCIATION\_RESPONSE](./oid-wdi-task-send-ap-association-response.md).

## TLV Type


0x97

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


|Type|Description|
|--- |--- |
|UINT8|Specifies whether or not to accept the association request. Valid values are 0 (do not accept) and 1 (accept).|
|UINT16|Specifies the reason code. If accept request is set to 0, this field provides a reason code to send back to the peer adapter.|

 

## Requirements


|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

