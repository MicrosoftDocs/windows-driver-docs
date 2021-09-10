---
title: WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB (dot11wificxtypes.hpp)
description: WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB is a WiFiCx TLV that contains information about a device service received from the IHV driver.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB (dot11wificxtypes.hpp)

WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB is a TLV that contains information about a device service received from the IHV driver. This TLV is used in the [NDIS_STATUS_WDI_INDICATION_DEVICE_SERVICE_EVENT](ndis-status-wdi-indication-device-service-event.md) status indication.

## TLV Type

0x141

## Length

The size, in bytes, of the array of UINT8 elements.

## Values

| Type | Description |
| --- | --- |
| UINT8[] | The information received from the IHV driver. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

