---
title: Known Issues
description: This topic identifies known issues in the tool outupt.
ms.date: 01/11/2024
---

# Known issues

This topic identifies known issues in the tool output.

## SENSOR_PROPERTY_DEVICE_ID

The **SENSOR_PROPERTY_DEVICE_ID** property, which the tool displays in the property list, corresponds to **SENSOR_PROPERTY_DEVICE_PATH** property which is defined in the header file sensors.h.

## Ambient Light Sensor (ALR) Curve

The tool returns ALR curve values as \[Offset, LUX\] pairs (rather than \[LUX, Offset\] pairs).
