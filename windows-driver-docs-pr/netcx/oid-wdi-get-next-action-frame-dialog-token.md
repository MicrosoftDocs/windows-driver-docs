---
title: OID_WDI_GET_NEXT_ACTION_FRAME_DIALOG_TOKEN (dot11wificxintf.h)
description: The OID_WDI_GET_NEXT_ACTION_FRAME_DIALOG_TOKEN command requests the DialogToken to be used in the next Action frame.
ms.date: 07/31/2021
keywords:
 - OID_WDI_GET_NEXT_ACTION_FRAME_DIALOG_TOKEN Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_GET\_NEXT\_ACTION\_FRAME\_DIALOG\_TOKEN (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_GET\_NEXT\_ACTION\_FRAME\_DIALOG\_TOKEN requests the DialogToken to be used in the next Action frame.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

## Get property parameters


No additional parameters. The data in the header is sufficient.
## Get property results


| TLV                                                                     | Multiple TLV instances allowed | Optional | Description     |
|-------------------------------------------------------------------------|--------------------------------|----------|-----------------|
| [**WDI\_TLV\_NEXT\_DIALOG\_TOKEN**](./wdi-tlv-next-dialog-token.md) |                                |          | A dialog token. |

 

## Requirements


|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

