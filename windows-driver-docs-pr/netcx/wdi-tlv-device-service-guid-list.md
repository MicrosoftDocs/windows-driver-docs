---
title: WDI_TLV_DEVICE_SERVICE_GUID_LIST (dot11wificxtypes.h)
description: WDI_TLV_DEVICE_SERVICE_GUID_LIST is a WiFiCx TLV that contains information about a device service received from the IHV driver.
ms.date: 09/30/2021
keywords:
 - WDI_TLV_DEVICE_SERVICE_GUID_LIST Network Drivers Starting with Windows Vista
---

# WDI_TLV_DEVICE_SERVICE_GUID_LIST (dot11wificxtypes.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI_TLV_DEVICE_SERVICE_GUID_LIST is a TLV that contains a list of device services that an underlying IHV driver exposes to UM components. This TLV is used in [OID_WDI_GET_SUPPORTED_DEVICE_SERVICES](oid-wdi-get-supported-device-services.md).

## TLV Type

0x142

## Length

The size, in bytes, of the array of GUID elements.

## Values

| Type | Description |
| --- | --- |
| GUID[] | An array of device services. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|


