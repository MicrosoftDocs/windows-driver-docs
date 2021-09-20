---
title: OID_WDI_GET_SUPPORTED_DEVICE_SERVICES
description: OID_WDI_GET_SUPPORTED_DEVICE_SERVICES queries the IHV driver for all of its supported device services.
ms.date: 07/31/2021
keywords:
 - OID_WDI_GET_SUPPORTED_DEVICE_SERVICES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_WDI_GET_SUPPORTED_DEVICE_SERVICES


OID_WDI_GET_SUPPORTED_DEVICE_SERVICES queries the IHV driver for all of its supported device services (with each device service identified by a GUID). If no device services are supported, LE should fail the command with **STATUS_NOT_SUPPORTED**.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

WLAN will provide a pipeline for any user mode component (UMDF driver or UM service) to communicate with the IHV WLAN driver. Among other things, this pipeline can be used for engaging SAR scenarios by being the platform to send information between the OEM sensors and the IHV firmware. The definition/format of the data to be sent to the IHV/LE driver and what the commands must do is not specified by UE. All contracts with the IHV must be defined by the OEM, and the device service WDI commands (and the corresponding user mode WLAN APIs) will just serve as a generic pipeline.

## Get property parameters


No additional parameters. The data in the header is sufficient.
## Get property results


| TLV                                                                     | Multiple TLV instances allowed | Optional | Description     |
|-------------------------------------------------------------------------|--------------------------------|----------|-----------------|
| [**WDI_TLV_DEVICE_SERVICE_GUID_LIST**](./wdi-tlv-device-service-guid-list.md) |                                |          | The list of device services that the underlying IHV driver exposes to UM components. |

 

## Requirements


|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

