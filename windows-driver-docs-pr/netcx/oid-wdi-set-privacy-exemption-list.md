---
title: OID_WDI_SET_PRIVACY_EXEMPTION_LIST (dot11wificxintf.h)
description: The OID_WDI_SET_PRIVACY_EXEMPTION_LIST command is used by the host to provide the list of exemptions for packet description. The adapter applies these exemptions to packets it receives that match the IEEE EtherType value specified for the exemption.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_PRIVACY_EXEMPTION_LIST Network Drivers Starting with Windows Vista
---

# OID\_WDI\_SET\_PRIVACY\_EXEMPTION\_LIST (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_SET\_PRIVACY\_EXEMPTION\_LIST is used by the host to provide the list of exemptions for packet description. The adapter applies these exemptions to packets it receives that match the IEEE EtherType value specified for the exemption.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                                 | Multiple TLV instances allowed | Optional | Description                        |
|-------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------|
| [**WDI\_TLV\_PRIVACY\_EXEMPTION\_ENTRY**](./wdi-tlv-privacy-exemption-entry.md) | X                              | X        | List of privacy exemption entries. |

 

## Set property results


No additional data. The data in the header is sufficient.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

