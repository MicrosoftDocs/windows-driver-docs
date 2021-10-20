---
title: WDI_TLV_NEXT_DIALOG_TOKEN (dot11wificxtypes.hpp)
description: WDI_TLV_NEXT_DIALOG_TOKEN is a WiFiCx TLV that contains the dialog token to be used in the next Action frame.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_NEXT_DIALOG_TOKEN Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_NEXT\_DIALOG\_TOKEN (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_NEXT\_DIALOG\_TOKEN is a TLV that contains the dialog token to be used in the next Action frame.

## TLV Type


0xE1

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                           |
|-------|-------------------------------------------------------|
| UINT8 | The dialog token to be used in the next Action frame. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

## See also


[OID\_WDI\_GET\_NEXT\_ACTION\_FRAME\_DIALOG\_TOKEN](./oid-wdi-get-next-action-frame-dialog-token.md)

 

