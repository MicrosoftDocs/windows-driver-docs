---
title: NDIS_STATUS_WDI_INDICATION_FT_ASSOC_PARAMS_NEEDED (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_FT_ASSOC_PARAMS_NEEDED to request parameters for 802.11r roaming.ObjectPort .
ms.date: 07/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_FT_ASSOC_PARAMS_NEEDED Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_FT\_ASSOC\_PARAMS\_NEEDED (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_FT\_ASSOC\_PARAMS\_NEEDED to request parameters for 802.11r roaming.

| Object |
|--------|
| Port   |

 

During [OID\_WDI\_TASK\_ROAM](oid-wdi-task-roam.md), WDI provides the parameters to send the 802.11 Authentication Request (PmkR0Name, R0KH-ID, SNonce, MDIE). Upon receiving the Authentication response, the LE requests additional needed parameters for the reassociation request, such as PMKR1Name and R1KH-ID. The LE also sends the parameters received in the Authentication Response (ANonce, SNonce, and R1KHID).

For a connection where Initial Mobility Domain is successfully done, the LE should only perform 11r roams (Fast roams). The LE can use the candidate list provided by the operating system, or use their own for the roams. If the LE uses its own candidate list, it must use the parameters (MDE, FTE, and PMKR0Name) provided in any one of the candidates suggested by the operating system to do a 11r roam. 11r is disabled whenever the connection is in FIPS mode. 11r fast roaming is currently only supported for FT over 1x authentication type.

## Payload data


| Type                                                                  | Multiple TLV instances allowed | Optional | Description                            |
|-----------------------------------------------------------------------|--------------------------------|----------|----------------------------------------|
| [**WDI\_TLV\_BSSID**](./wdi-tlv-bssid.md)                         |                                |          | The BSSID of the AP.                   |
| [**WDI\_TLV\_FT\_AUTH\_REQUEST**](./wdi-tlv-ft-auth-request.md)   |                                |          | The authentication request byte blob.  |
| [**WDI\_TLV\_FT\_AUTH\_RESPONSE**](./wdi-tlv-ft-auth-response.md) |                                |          | The authentication response byte blob. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

## See also


[OID\_WDI\_TASK\_ROAM](oid-wdi-task-roam.md)

 

