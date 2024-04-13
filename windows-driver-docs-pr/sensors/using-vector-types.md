---
title: Using Vector Types With Sensors
description: Using vector types with sensors
ms.date: 01/11/2024
---

# Using vector types with sensors

Some properties and data fields contain arrays of information. For example, the SENSOR\_PROPERTY\_LIGHT\_RESPONSE\_CURVE property contains an array of 4-byte unsigned integers. However, when applications receive such arrays through the Sensor API, they are always represented as type VT\_VECTOR|UI1, an array of single-byte characters.

For information about which properties and data fields contain arrays, see [Constants](about-sensor-constants.md).

The following code example shows how to create an [IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues) object that contains values for SENSOR\_PROPERTY\_LIGHT\_RESPONSE\_CURVE. The variable named m\_pSensorProperties is a pointer to the [IPortableDeviceValues](/windows-hardware/drivers/ddi/portabledevicetypes/nn-portabledevicetypes-iportabledevicevalues) interface.

```cpp
UINT responseCurve[10] = {0}; // Array to contain the response curve data.
// ****************************************************************************************
// The response curve consists of an array of byte pairs.
// The first byte contains the percentage brightness offset to be applied to the display.
// The second byte contains the corresponding ambient light value (in LUX).
// ****************************************************************************************
// (0, 10)
responseCurve[0] = 0; responseCurve[1] = 10;
// (10, 40)
responseCurve[2] = 10; responseCurve[3] = 40;
// (40, 80)
responseCurve[4] = 40; responseCurve[5] = 80;
// (68, 100)
responseCurve[6] = 68; responseCurve[7] = 100;
// (90, 150)
responseCurve[8] = 90; responseCurve[9] = 150;

// Create the buffer.
PROPVARIANT pvCurve = {0};
InitPropVariantFromBuffer(responseCurve, 10 * sizeof (UINT), &pvCurve);

// Add the values to the IPortableDeviceValues object.
hr = m_pSensorProperties->SetValue(SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE, &pvCurve);

PropVariantClear(&pvCurve);
```

## Related topics

- [The Sensors Geolocation Driver Sample](../gnss/sensors-geolocation-driver-sample.md)
