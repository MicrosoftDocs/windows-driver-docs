---
title: OID_WDI_DEVICE_SERVICE_COMMAND (dot11wificxintf.h)
description: The OID_WDI_DEVICE_SERVICE_COMMAND command is used to set or get parameters for an IHV defined service identified by a GUID.
ms.date: 07/31/2021
keywords:
 - OID_WDI_DEVICE_SERVICE_COMMAND Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_WDI_DEVICE_SERVICE_COMMAND (dot11wificxintf.h)

OID_WDI_DEVICE_SERVICE_COMMAND is used to set or get parameters for an IHV defined service identified by a GUID. 

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 
The GUID is based on the contract between a user mode component and IHV driver. WDI serves as a generic pipe and will help pass down the parameters set from user mode component down to LE and returns any data from the IHV to the user mode component. The device service GUID can be specific to an area. For example, for SAR, a GUID and opcodes can be defined for each function under this service.

## Command parameter


| TLV                                                  | Multiple TLV instances allowed | Optional | Description                                        |
|------------------------------------------------------|--------------------------------|----------|----------------------------------------------------|
| [**WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB**](wdi-tlv-device-service-params-data-blob.md) |                                | X        | The information to be sent to the IHV driver. |
| [**WDI_TLV_DEVICE_SERVICE_PARAMS_GUID**](./wdi-tlv-device-service-params-guid.md) |                                |         | The GUID which identifies the device service that this command belongs to (as defined by the IHV/OEM). |
| [**WDI_TLV_DEVICE_SERVICE_PARAMS_OPCODE**](./wdi-tlv-device-service-params-opcode.md) |                                | X        | The opcode specific to the device service. |

 

## Response result


| TLV                                                  | Multiple TLV instances allowed | Optional | Description                                                                                                                 |
|------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------|
| [**WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB**](wdi-tlv-device-service-params-data-blob.md) |                                | X        | The information received from the IHV driver. The data (Value) in this TLV is forwarded as is to the user mode component. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|


 

