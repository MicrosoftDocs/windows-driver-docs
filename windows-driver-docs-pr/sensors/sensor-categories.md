---
title: Sensor categories
description: Sensor categories
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

