---
title: Proximity Sensor Property
description: This property is an optional enumeration property.
ms.date: 11/27/2023
ms.topic: reference
---

# Proximity Sensor Property

This property is an optional enumeration property.

| Property key | Type | Access (R/O, R/W) | Required/Optional | Description |
|---|---|---|---|---|
| DEVPKEY_Sensor_ProximityType | VT_UI4 | R/O | Optional | Describes the type of proximity being detected. It can be HumanProximity or ObjectProximity. For more information, see the ProximityType enumeration.  |
| DEVPKEY_Sensor_HumanPresenceDetectionType | VT_UI4 | R/O | Required for HumanProximity  | Describes the type of biometric detection type that is used by the sensor. See table below. |
| PKEY_Sensor_Proximity_SensorCapabilities | VT_UI4 | R/O | Required for HumanProximity | The s bitmap to advertise the capabilities of the proximity sensor. Bit 0 indicates if sensor is Human Presence Capable.  Bit 1 indicates Attention Detection Support and Bits 2- 31 are reserved.|

## Human Proximity Detection Types

For sensors reporting HumanProximity the sensor must report the detection techology used by the sensor using the `DEVPKEY_Sensor_HumanPresenceDetectionType` based on the definitions below.

| HumanPresenceDetectionType | Description |
|---|---|
| Vendor-Defined Non-Biometric | Presence (of one or more people) is detected utilizing a vendor-defined, but non-biometric method. This is used to give positive affirmation that the sensor is using detection unrelated to biometrics as defined below. Without this, a Host cannot assume biometrics aren’t utilized by the device.|
| Vendor-Defined Biometric | Presence (of one or more people) is detected utilizing vendor-defined human biometrics. This is a catch-all for a Human Presence sensor that utilizes biometrics not already defined below. |
| Facial Biometric | Human presence is detected by scanning (e.g. by a low-resolution video camera) for human faces (e.g. using Viola-Jones object detection). Distinguishing between faces or detection of facial attributes is not performed. Such detection is similar to that of existing digital cameras that can place a bounding-box around a face. |
| Audio Biometric |Human presence is detected by scanning (e.g. by a microphone) for ‘human’ sounds (e.g. a predefined keyword, general talking, loud noises, clapping). Distinguishing between voices/users or detection of audio characteristics are not performed. |

## Requirements

| &nbsp; |&nbsp; |
|---|---|
| **Header** | Sensorsdef.h |
