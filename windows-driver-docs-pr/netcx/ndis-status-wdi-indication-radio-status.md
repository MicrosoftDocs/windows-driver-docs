---
title: NDIS_STATUS_WDI_INDICATION_RADIO_STATUS (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_RADIO_STATUS to indicate changes in the adapter's radio state.
ms.date: 07/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_RADIO_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_RADIO\_STATUS (dot11wificxintf.h)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_RADIO\_STATUS to indicate changes in the adapter's radio state. This unsolicited indication is sent when a software radio change is triggered by the host, and when a hardware radio state change is detected by the adapter.

| Object |
|--------|
| Adapter   |

 

## Payload data


| Type                                                                  | Multiple TLV instances allowed | Optional | Description                                              |
|-----------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------|
| [**WDI\_TLV\_RADIO\_STATE**](./wdi-tlv-radio-state-parameters.md) |                                |          | The current state of the radio in hardware and software. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|


## See also


[OID_WDI_TASK_SET_RADIO_STATE](oid-wdi-task-set-radio-state.md)

 

