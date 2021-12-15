---
title: OID_WDI_GET_AUTO_POWER_SAVE (dot11wificxintf.h)
description: The OID_WDI_GET_AUTO_POWER_SAVE command gets the power save state of the port.
ms.date: 07/31/2021
keywords:
 - OID_WDI_GET_AUTO_POWER_SAVE Network Drivers Starting with Windows Vista
---

# OID\_WDI\_GET\_AUTO\_POWER\_SAVE (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_GET\_AUTO\_POWER\_SAVE gets the power save state of the port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Not applicable           | 1                               |

 

There is a trade-off between power saving and latency. When auto power save mode is set to be enabled with the [OID\_WDI\_SET\_CONNECTION\_QUALITY](oid-wdi-set-connection-quality.md) command, the firmware tries to interact with the connected access point to go to power save mode as much as appropriate to save power. The firmware is also responsible for detecting if the connected access point confirms to the 802.11 specification and follows the power save mode protocol. If the access point does not conform (does not support power save mode correctly), the firmware should not go into power save mode, even when Auto Power Save is set to enabled. When Auto Power Save is set to disabled, the firmware focuses on low latency of sending and receiving packets. Examples of this are when streaming mode is on, and when the system is using AC power so low latency is preferred to saving power.

## Get property parameters


No additional parameters. The data in the header is sufficient.
## Get property results


| TLV                                                                          | Multiple TLV instances allowed | Optional | Description                  |
|------------------------------------------------------------------------------|--------------------------------|----------|------------------------------|
| [**WDI\_TLV\_GET\_AUTO\_POWER\_SAVE**](./wdi-tlv-get-auto-power-save.md) |                                |          | Auto power save information. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

