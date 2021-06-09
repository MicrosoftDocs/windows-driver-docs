---
title: Event Constants
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
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Event Constants


The sensor platform defines the following constants for driver events.

### Sensor Event Types

The sensor platform defines the following sensor event types identifiers.

|Name|Description|
|--|--|
|SENSOR_EVENT_DATA_UPDATED|Indicates that new data is available.|
|SENSOR_EVENT_PROPERTY_CHANGED|Indicates that a property value changed.|
|SENSOR_EVENT_STATE_CHANGED|Indicates a change of operational state, for example, from SENSOR_STATE_INITIALIZING to SENSOR_STATE_READY.|

 

### Sensor Event PROPERTYKEYs

The sensor platform defines the following **PROPERTYKEY**s to identify the parameters for sensor events.

|Name|Description|
|--|--|
|SENSOR_EVENT_PARAMETER_EVENT_ID|Indicates that the <strong>GUID</strong> value in [IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues) is an event type ID, such as SENSOR_EVENT_DATA_UPDATED.|
|SENSOR_EVENT_PARAMETER_STATE|Indicates that the unsigned integer value in [IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues) is a sensor state, such as SENSOR_STATE_READY. To raise a state changed event, call [<strong>ISensorClassExtension::PostStateChange</strong>](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-poststatechange). You do not have to explicitly specify SENSOR_EVENT_PARAMETER_STATE to raise the event.|

 

## Requirements

**Minimum supported client**: Windows 7

**Minimum supported server**: None supported

**Version**: Available in Windows 7

**Header**: Sensors.h




## See also


[About Sensor Driver Events](about-sensor-driver-events.md)

[Filtering data](filtering-data.md)

[The Sensors Geolocation Driver Sample](../gnss/sensors-geolocation-driver-sample.md)

[**SensorState**](/windows-hardware/drivers/ddi/sensorsclassextension/ne-sensorsclassextension-__midl___midl_itf_windowssensorclassextension_0000_0000_0001)

