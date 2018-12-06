---
title: WDI_TLV_DEVICE_SERVICE_PARAMS_GUID
description: WDI_TLV_DEVICE_SERVICE_PARAMS_GUID is a TLV that contains a GUID that identifies the device service to which this status indication belongs.
ms.assetid: BBD64E6F-A2E2-4601-A231-4FCB4574EFC7
ms.date: 06/15/2018
keywords:
 - WDI_TLV_DEVICE_SERVICE_PARAMS_GUID Network Drivers Starting with Windows Vista
---

# WDI_TLV_DEVICE_SERVICE_PARAMS_GUID

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

|   |   |
| --- | --- |
| Minimum supported client | Windows 10, version 1809 |
| Minimum supported server | Windows Server 2016 |
| Header | Wditypes.hpp |
