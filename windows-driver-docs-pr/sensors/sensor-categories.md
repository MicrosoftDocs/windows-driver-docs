---
title: Sensor categories
description: Sensor categories
ms.assetid: 609C57BA-1C3E-435B-BAAE-C01C3669D59D
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Sensor categories

Sensor categories represent broad classes of sensor devices. Categories provide a way to group sensors that are likely to provide similar types of information, or are otherwise related in some way. Each category is represented by a GUID constant. Two sensors of different types can belong to the same category or two different categories. For example, an accelerometer and a gyroscope may both be classified under the GUID_SensorCategory_Motion category, while an ambient light sensor may be classified under the GUID_SensorCategory_Light category. Each sensor category is represented by a GUID constant.

Sensor category GUIDs are defined in SensorsDef.h

| Name | Description |
| --- | --- |
| GUID_SensorCategory_All| This GUID identifies all of the sensors. The sensor class extension adds a sensor to this category unless a driver explicitly provides one of the categories below. |
| GUID_SensorCategory_Biometric | This GUID identifies the biometric sensor category. |
| GUID_SensorCategory_Electrical | This GUID identifies the electrical sensor category. |
| GUID_SensorCategory_Environmental| This GUID identifies the environmental sensor category. |
| GUID_SensorCategory_Light| This GUID identifies the light sensor category. |
| GUID_SensorCategory_Location | This GUID identifies the location sensor category. |
| GUID_SensorCategory_Mechanical| This GUID identifies the mechanical sensor category. |
| GUID_SensorCategory_Motion| This GUID identifies the motion sensor category. |
| GUID_SensorCategory_Orientation | This GUID identifies the orientation sensor category. |
| GUID_SensorCategory_Other | This GUID identifies a category for sensors that are supported, but do not fit into any of the predefined categories. |
| GUID_SensorCategory_Scanner| This GUID identifies the scanner sensor category. |
| GUID_SensorCategory_Unsupported| This GUID identifies a category for sensors that are unsupported. |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors/sensors%5D:%20sensor%20categories%20%20RELEASE:%20%2802/19/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
