---
title: WDI_TLV_DEVICE_SERVICE_PARAMS_OPCODE (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_DEVICE_SERVICE_PARAMS_OPCODE is a WiFiCx TLV that contains the opcode specific to the device service.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_DEVICE_SERVICE_PARAMS_OPCODE Network Drivers Starting with Windows Vista
---

# WDI_TLV_DEVICE_SERVICE_PARAMS_OPCODE (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI_TLV_DEVICE_SERVICE_PARAMS_OPCODE is a TLV that contains the opcode specific to the device service. This TLV is used in the [NDIS_STATUS_WDI_INDICATION_DEVICE_SERVICE_EVENT](ndis-status-wdi-indication-device-service-event.md) status indication.

## TLV Type

0x13F

## Length

The size, in bytes, of a UINT8.

## Values

| Type | Description |
| --- | --- |
| TLV\<UINT8\> | The opcode specific to the device service. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


