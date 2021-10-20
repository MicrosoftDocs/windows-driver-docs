---
title: WDI_TLV_DEVICE_SERVICE_PARAMS_GUID (dot11wificxtypes.hpp)
description: WDI_TLV_DEVICE_SERVICE_PARAMS_GUID is a WiFiCx TLV that contains a GUID that identifies the device service to which this status indication belongs.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_DEVICE_SERVICE_PARAMS_GUID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_DEVICE_SERVICE_PARAMS_GUID (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI_TLV_DEVICE_SERVICE_PARAMS_GUID is a TLV that contains a GUID that identifies the device service to which this status indication belongs. This TLV is used in the [NDIS_STATUS_WDI_INDICATION_DEVICE_SERVICE_EVENT](ndis-status-wdi-indication-device-service-event.md) status indication.

## TLV Type

0x140

## Length

The size, in bytes, of a GUID.

## Values

| Type | Description |
| --- | --- |
| GUID | The GUID that identifies the device service to which this status indication belongs (as defined by the IHV/OEM). |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

