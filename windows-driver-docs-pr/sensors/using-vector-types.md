---
title: Using vector types with sensors
author: windows-driver-content
description: Using vector types with sensors
ms.assetid: cadc2cd3-10aa-4a4a-926f-edc01b046f27
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using vector types with sensors


Some properties and data fields contain arrays of information. For example, the SENSOR\_PROPERTY\_LIGHT\_RESPONSE\_CURVE property contains an array of 4-byte unsigned integers. However, when applications receive such arrays through the Sensor API, they are always represented as type VT\_VECTOR|UI1, an array of single-byte characters.

For information about which properties and data fields contain arrays, see [Constants](https://msdn.microsoft.com/library/windows/hardware/ff545409).

The following code example shows how to create an [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) object that contains values for SENSOR\_PROPERTY\_LIGHT\_RESPONSE\_CURVE. The variable named m\_pSensorProperties is a pointer to the [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) interface.

```
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
InitPropVariantFromBuffer(responseCurve, 10 * sizeof (UINT), &amp;pvCurve);

// Add the values to the IPortableDeviceValues object.
hr = m_pSensorProperties->SetValue(SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE, &amp;pvCurve);

PropVariantClear(&amp;pvCurve);

```

## Related topics
[The Sensors Geolocation Driver Sample](https://msdn.microsoft.com/library/windows/hardware/hh768273)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Using%20vector%20types%20with%20sensors%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


