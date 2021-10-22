---
title: WDI_TLV_P2P_PROVISION_SERVICE_ATTRIBUTES (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_PROVISION_SERVICE_ATTRIBUTES is a WiFiCx TLV that contains Wi-Fi Direct Provision Service attributes.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_PROVISION_SERVICE_ATTRIBUTES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_PROVISION\_SERVICE\_ATTRIBUTES (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_PROVISION\_SERVICE\_ATTRIBUTES is a TLV that contains Wi-Fi Direct Provision Service attributes.

## TLV Type


0xC6

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                        |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8                                             | Wi-Fi Direct Status Code, as defined by the Wi-Fi Direct specification.                                                                            |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | Local MAC Address for future Wi-Fi Direct connection.                                                                                              |
| UINT8                                             | Connection Capability bitmask.                                                                                                                     |
| UINT32                                            | Feature Capability bitmask.                                                                                                                        |
| UINT32                                            | Advertisement ID for the Service Instance.                                                                                                         |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | Service address for the Service instance.                                                                                                          |
| UINT32                                            | Session ID that uniquely identifies the Session to the Service.                                                                                    |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | Session address that uniquely identifies the Session to the Service.                                                                               |
| UINT16                                            | GO Configuration Timeout in milliseconds.                                                                                                          |
| UINT16                                            | Client Configuration Timeout in milliseconds.                                                                                                      |
| UINT8                                             | A flag indicating if a Persistent Group will be used for the connection. The flag is set to 1 if a Persistent Group will be used.                  |
| UINT8                                             | A flag indicating if this frame is part of a follow-on provision discovery. The flag is set to 1 if it is part of a follow-on provision discovery. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

