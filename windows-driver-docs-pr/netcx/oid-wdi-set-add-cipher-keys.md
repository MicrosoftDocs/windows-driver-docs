---
title: OID_WDI_SET_ADD_CIPHER_KEYS (dot11wificxintf.h)
description: The OID_WDI_SET_ADD_CIPHER_KEYS command adds or overwrites cipher keys in the key table of a port. This is a set-only property.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_ADD_CIPHER_KEYS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_ADD\_CIPHER\_KEYS (dot11wificxintf.h)


OID\_WDI\_SET\_ADD\_CIPHER\_KEYS adds or overwrites cipher keys in the key table of a port. This is a set-only property.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

Cipher keys that are marked as Static should not be cleared on a roam. They can only be cleared on a [OID\_WDI\_TASK\_DOT11\_RESET](oid-wdi-task-dot11-reset.md) or if they are overwritten with a new OID\_WDI\_SET\_ADD\_CIPHER\_KEYS.

## Set property parameters


| TLV                                                                          | Multiple TLV instances allowed | Optional | Description                                                              |
|------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------------------|
| [**WDI\_TLV\_SET\_CIPHER\_KEY\_INFO**](./wdi-tlv-set-cipher-key-info.md) | X                              |          | The cipher keys to be added or overwritten in the key table of the port. |

 

## Set property results


No additional data. The data in the header is sufficient.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

## See also


[OID\_WDI\_SET\_DELETE\_CIPHER\_KEYS](oid-wdi-set-delete-cipher-keys.md)

 

