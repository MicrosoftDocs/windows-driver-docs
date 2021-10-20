---
title: OID_WDI_SET_FLUSH_BSS_ENTRY (dot11wificxintf.h)
description: The OID_WDI_SET_FLUSH_BSS_ENTRY command is sent to the device to flush the list of BSS entries maintained by the adapter.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_FLUSH_BSS_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_FLUSH\_BSS\_ENTRY (dot11wificxintf.h)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_SET\_FLUSH\_BSS\_ENTRY is sent to the device to flush the list of BSS entries maintained by the adapter. This command can only be sent on the station port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

## Set property parameters


No additional parameters. The data in the header is sufficient.
## Set property results


No additional data. The data in the header is sufficient.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

 




