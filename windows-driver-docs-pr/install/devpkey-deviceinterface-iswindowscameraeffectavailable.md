---
title: DEVPKEY_DeviceInterface_IsWindowsCameraEffectAvailable
description: The DEVPKEY_DeviceInterface_IsWindowsCameraEffectAvailable device property represents a Boolean flag that indicates whether Windows Camera Effects are available and can be enabled on the device.
ms.date: 10/03/2022
---

# DEVPKEY_DeviceInterface_IsWindowsCameraEffectAvailable

The **DEVPKEY_DeviceInterface_IsWindowsCameraEffectAvailable** device property represents a Boolean flag that indicates whether Windows Camera Effects are available.

| Attribute | Value |
|--|--|
| **Property key** | DEVPKEY_DeviceInterface_IsWindowsCameraEffectAvailable |
| **Property-data-type identifier** | [**DEVPROP_BOOLEAN**](devprop-type-boolean.md) |
| **Property access** | Read-only access by installation applications and installers |
| **Localized?** | No |

## Syntax

```cpp
// {6EDC630D-C2E3-43B7-B2D1-20525A1AF120}, 4
DEFINE_DEVPROPKEY(DEVPKEY_DeviceInterface_IsWindowsCameraEffectAvailable, 0x6EDC630D, 0xC2E3, 0x43B7, 0xB2, 0xD1, 0x20, 0x52, 0x5A, 0x1A, 0xF1, 0x20, 4);    // DEVPROP_TYPE_BOOLEAN
```

## Remarks

**DEVPKEY_DeviceInterface_IsWindowsCameraEffectAvailable** is defined in the Mfvirtualcamera.h header file included in the Windows SDK version 10.0.22621.0 and later.

If the **DEVPKEY_DeviceInterface_IsWindowsCameraEffectAvailable** property is present and set to DEVPROP_TRUE, Windows Camera Effects are available and can be enabled on the device.

If the property is not available on the device or the property is not set to DEVPROP_TRUE, Windows Camera Effects are not supported.

### How to detect if the system is capable of running a Windows Studio camera

Use the **DEVPKEY_DeviceInterface_IsWindowsCameraEffectAvailable** dev prop key to deduce if a camera is a Windows Studio opted-in camera from its driver .inf.

To do this:

1. Check if the **DEVPKEY_DeviceInterface_IsWindowsCameraEffectAvailable** dev prop key is exposed.

1. Check if the device is a front facing camera.

    For example, using the [**DEVPKEY_Device_PhysicalDeviceLocation**](devpkey-device-physicaldevicelocation.md), check if the panel is front (if ACPI_PLD_V2_BUFFER.Panel == ACPI_PLD_PANEL::AcpiPldPanelFront).

If both checks return true, it is ok to assume the camera is a Windows Studio opted-in camera and that therefore BackgroundSegmentation, EyeGazeCorrection and DigitalWindow are implemented by the Windows Studio component.

## Requirements

**Version**: Windows 11, version 22H2

**Header**: Mfvirtualcamera.h
