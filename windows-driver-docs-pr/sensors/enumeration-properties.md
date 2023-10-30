---
title: Enumeration properties
description: This article describes the static sensor properties that are available from the PnP Driver Store.
ms.date: 03/02/2023
ms.topic: reference
---

# Enumeration properties

This article describes the static sensor properties that are available from the PnP Driver Store.

The following table shows static sensor properties. The Class Extension (CX) writes these properties for each sensor when [SensorsCxSensorCreate](/windows-hardware/drivers/ddi/sensorscx/nf-sensorscx-sensorscxsensorcreate) is called. Client applications can use these properties to search for sensors on the Windows device.

For more information about the data types shown in the **Type** column, see [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant).

| Property key | Type | Required/Optional | Description |
|---|---|---|---|
| DEVPKEY_Sensor_Type | **VT_CLSID** | Required | A GUID that identifies the type of sensor. For more information about sensor types, see [Sensor type GUIDs](./about-sensor-constants.md). |
| DEVPKEY_Sensor_Category | **VT_CLSID** | Required | The sensor category. This key is for backwards compatibility with Desktop v1 stack, where it's a requirement. |
| DEVPKEY_Sensor_ConnectionType | **VT_UI4** | Optional</br></br>Required for Ambient Light Sensor and Accelerometer | The sensor connection type. Sensor connection types can be integrated, attached, or external.</br></br>For more information, see the **[SensorConnectionType](/windows-hardware/drivers/ddi/sensorsclassextension/ne-sensorsclassextension-__midl___midl_itf_windowssensorclassextension_0000_0000_0002)** enumeration. |
| DEVPKEY_Sensor_IsPrimary | **VT_BOOL** | Optional | An indication that this is the primary sensor. This key has a default value of false, if not set. |
| DEVPKEY_Sensor_Name | **VT_LPWSTR** | Required for custom sensors. | The name of the sensor. |
| DEVPKEY_Sensor_Manufacturer | **VT_LPWSTR** | Required | The manufacturer for the sensor. |
| DEVPKEY_Sensor_Model | **VT_LPWSTR** | Required | The model for the sensor. |
| DEVPKEY_Sensor_PersistentUniqueId | **VT_CLSID** | Required | A GUID that identifies the sensor. This value must be unique for each sensor of the same model on a device. This requirement applies to both internally and externally connected sensors. |
| DEVPKEY_Sensor_VendorDefinedSubType | **VT_CLSID** | Required for custom sensors. | A GUID that identifies a sensor category subtype that was defined by a vendor.</br></br>For non-custom sensors, this key isn't required. |
| DEVPKEY_SensorData_LightLevel_AutoBrightnessPreferred | **VT_BOOL** | Optional | The light sensor is preferred for auto-brightness. |
| DEVPKEY_SensorData_LightLevel_ColorCapable | **VT_BOOL** | Optional</br></br>Required if supporting chromaticity and light temperature. | The light sensor supports light temperature and/or chromaticity x/y. |

## Related topics

- [PROPVARIANT structure](/windows/win32/api/propidlbase/ns-propidlbase-propvariant)
- **[SensorConnectionType](/windows-hardware/drivers/ddi/sensorsclassextension/ne-sensorsclassextension-__midl___midl_itf_windowssensorclassextension_0000_0000_0002)**
- **[SensorsCxSensorCreate](/windows-hardware/drivers/ddi/sensorscx/nf-sensorscx-sensorscxsensorcreate)**
- [Sensor properties](./common-sensor-properties.md)
- [Sensor type GUIDs](./about-sensor-constants.md)
