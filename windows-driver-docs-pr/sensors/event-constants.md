---
title: Event constants
description: The sensor platform defines the following constants for driver events.
keywords:
- Event Constants
- Sensor Devices
topic_type:
- apiref
api_name:
- Event Constants
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 12/01/2022
---

# Event constants

The sensor platform defines the following constants for driver events.

## Sensor event types

The sensor platform defines the following sensor event types identifiers.

| Name | Description |
|---|---|
| SENSOR_EVENT_DATA_UPDATED | Indicates that new data is available. |
| SENSOR_EVENT_PROPERTY_CHANGED | Indicates that a property value changed. |
| SENSOR_EVENT_STATE_CHANGED | Indicates a change of operational state, for example, from SENSOR_STATE_INITIALIZING to SENSOR_STATE_READY. |

## Sensor event PROPERTYKEYs

The sensor platform defines the following **PROPERTYKEY**s to identify the parameters for sensor events.

|Name|Description|
|--|--|
|SENSOR_EVENT_PARAMETER_EVENT_ID|Indicates that the **GUID** value in [IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues) is an event type ID, such as SENSOR_EVENT_DATA_UPDATED.|
|SENSOR_EVENT_PARAMETER_STATE|Indicates that the unsigned integer value in [IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues) is a sensor state, such as SENSOR_STATE_READY. To raise a state changed event, call **[ISensorClassExtension::PostStateChange](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-poststatechange)**. You do not have to explicitly specify SENSOR_EVENT_PARAMETER_STATE to raise the event.|

## Requirements

| &nbsp; | &nbsp; |
|---|---|
| **Minimum supported client** | Windows 7 |
| **Minimum supported server** | None supported |
| **Header** | Sensors.h |

## See also

- [About Sensor Driver Events](about-sensor-driver-events.md)
- [Filtering data](filtering-data.md)
- [The Sensors Geolocation Driver Sample](../gnss/sensors-geolocation-driver-sample.md)
- **[SensorState](/windows-hardware/drivers/ddi/sensorsclassextension/ne-sensorsclassextension-__midl___midl_itf_windowssensorclassextension_0000_0000_0001)**
