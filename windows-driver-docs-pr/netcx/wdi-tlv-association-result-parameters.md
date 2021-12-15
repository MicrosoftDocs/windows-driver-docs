---
title: WDI_TLV_ASSOCIATION_RESULT_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_ASSOCIATION_RESULT_PARAMETERS is a WiFiCx TLV that contains parameters for an association result.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_ASSOCIATION_RESULT_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ASSOCIATION\_RESULT\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_ASSOCIATION\_RESULT\_PARAMETERS is a TLV that contains parameters for an association result.

## TLV Type


0x2D

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                        | Description                                                                                                                                                                                                                                         |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32                                                      | Specifies the completion status of the association attempt as defined in [**WDI\_ASSOC\_STATUS**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_assoc_status).                                                                                                                       |
| UINT32                                                      | The 802.11 status code sent by the peer in response to an authentication or association request from this port.                                                                                                                                     |
| UINT8                                                       | Specifies whether the port sent an 802.11 association or an 802.11 reassociation request to the AP. This value should be set to 1 if a reassociation request was used.                                                                              |
| [**WDI\_AUTH\_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_auth_algorithm)     | The authentication algorithm that the port negotiated with the peer during association.                                                                                                                                                             |
| [**WDI\_CIPHER\_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_cipher_algorithm) | The unicast cipher algorithm that the port negotiated with the peer during association.                                                                                                                                                             |
| [**WDI\_CIPHER\_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_cipher_algorithm) | The multicast data cipher algorithm that the port negotiated with the peer during association.                                                                                                                                                      |
| [**WDI\_CIPHER\_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_cipher_algorithm) | The multicast management cipher algorithm that the port negotiated with the peer during association.                                                                                                                                                |
| UINT8                                                       | Specifies if the port has associated with a peer that supports distribution system (DS) services for ISO Layer 2 bridging on any station in the BSS network, including mobile stations and APs. This value should be set to 1 if this is supported. |
| UINT8                                                       | Specifies whether the port has performed port authorization during the association operation.                                                                                                                                                       |
| UINT8                                                       | Specifies whether 802.11 WMM QoS protocol has been negotiated for this association. This value should be set to 1 if it has been negotiated.                                                                                                        |
| [**WDI\_DS\_INFO**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_ds_info)                   | Specifies whether the port is connected to the same DS as its previous association.                                                                                                                                                                 |
| UINT32                                                      | When a (re)association fails with an 802.11 reason code of 30, this value indicates the value of the association comeback time requested by the peer.                                                                                               |
| [**WDI\_BAND\_ID**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_band_id) (UINT32)                                      | The band ID on which the association is established.                                                                                                                                                                                                |
| UINT32                                                      | The IHV association status. If the association failed, this can contain an IHV-defined status code. This is only used for debugging purpose.                                                                                                        |
| [**WDI_DISABLE_DATA_PATH_OFFLOADS_SCENARIO**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_disable_data_path_offloads_scenario) (UINT32)                                      | IHVs can set this to instruct the OS to disable datapath offloads for this connection only. This may be necessary if the IHV needs to perform encryption/decryption in software or if it encountered a hardware error that prevents it from using its supported offloads.                                                                                                                                                                                               |




## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

