---
title: OID_WDI_SET_DELETE_CIPHER_KEYS (dot11wificxintf.h)
description: The OID_WDI_SET_DELETE_CIPHER_KEYS command deletes cipher keys from the device's cipher key table.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_DELETE_CIPHER_KEYS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_DELETE\_CIPHER\_KEYS (dot11wificxintf.h)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_SET\_DELETE\_CIPHER\_KEYS deletes cipher keys from the device's cipher key table.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                                | Multiple TLV instances allowed | Optional | Description                                                |
|------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------|
| [**WDI\_TLV\_DELETE\_CIPHER\_KEY\_INFO**](./wdi-tlv-delete-cipher-key-info.md) | X                              |          | The cipher keys to be deleted from the device's key table. |

 

## Set property results


No additional data. The data in the header is sufficient.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

## See also


[OID\_WDI\_SET\_ADD\_CIPHER\_KEYS](oid-wdi-set-add-cipher-keys.md)

 

