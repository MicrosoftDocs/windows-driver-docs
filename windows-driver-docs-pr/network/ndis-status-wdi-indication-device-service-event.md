---
title: NDIS_STATUS_WDI_INDICATION_DEVICE_SERVICE_EVENT
description: The NDIS_STATUS_WDI_INDICATION_DEVICE_SERVICE_EVENT status indication is used by a miniport driver to pass on unsolicited information about a device to a user mode client.
ms.assetid: 6A9EA354-86F0-4C3F-974E-4FC164239D6A
ms.date: 06/14/2018
keywords:
 - NDIS_STATUS_WDI_INDICATION_DEVICE_SERVICE_EVENT Network Drivers Starting with Windows Vista
---

# NDIS_STATUS_WDI_INDICATION_DEVICE_SERVICE_EVENT

The NDIS_STATUS_WDI_INDICATION_DEVICE_SERVICE_EVENT status indication is used by an IHV miniport driver to pass on unsolicited information about a device to a user mode client.

Device service indications must be sent by the miniport driver only when in the *D0* power state, and it must not cause the device to wake from *Dx*. WDI will drop this indication without forwarding it up the stack if it receives it when in *Dx*.

This indication is currently handled only on the default port (station).

The miniport driver should send a separate notification for every device service GUID and opcode pair whenever necessary.

## Payload data

| Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- |
| [WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB](wdi-tlv-device-service-params-data-blob.md) |   | X | The information received from the IHV miniport driver. |
| [WDI_TLV_DEVICE_SERVICE_PARAMS_GUID](wdi-tlv-device-service-params-guid.md) |   |   | The GUID that identifies the device service to which this indication belongs (as defined by the IHV/OEM). |
| [WDI_TLV_DEVICE_SERVICE_PARAMS_OPCODE](wdi-tlv-device-service-params-opcode.md) |   |   | The opcode specific to the device service. |

## Requirements

|   |   |
| --- | --- |
| Minimum supported client | Windows 10, version 1809 |
| Minimum supported server | Windows Server 2016 |
| Header | Dot11wdi.h |
