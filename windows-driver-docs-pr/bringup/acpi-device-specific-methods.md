---
title: Device-specific methods (_DSM)
description: To support increased functionality and extension to select technology stacks, Windows define Device-Specific Methods (_DSM) for the device.
ms.date: 08/17/2021
ms.localizationpriority: medium
---

# Device-specific methods (_DSM)

To support increased functionality and extension to select technology stacks, Windows define Device-Specific Methods (_DSM) for the device.

The [ACPI 5.0 specification](https://uefi.org/specifications) introduces several device-specific methods that are used by Windows to support hardware platforms that use System on a Chip (SoC) integrated circuits. The topics in this section describe the arguments and return values that are defined for these methods.

## In this section

| Topic | Description |
|--|--|
| [GPIO controller Device-Specific Method (_DSM)](gpio-controller-device-specific-method---dsm-.md) |
| To support a variety of device-class-specific communications between the general-purpose I/O (GPIO) driver stack in Windows and the platform firmware, Microsoft defines a Device-Specific Method (_DSM) that can be included under a GPIO controller in the ACPI namespace. |
| [Battery Device-Specific Method](battery-device-specific-method.md) | To support the passive thermal management of the battery by the platform, Microsoft defines a _DSM method to communicate to the platform firmware the thermal throttling limit set by the battery's thermal zone. |
| [Device-Specific Method for Microsoft thermal extensions](device-specific-method-for-microsoft-thermal-extensions.md) | To support more flexible design of thermal zones and thermal sensors, Windows supports extensions to the ACPI thermal zone model. Specifically, Windows supports a thermal minimum throttle limit (MTL) for each thermal zone, and also supports sharing a temperature sensor between thermal zones. |
| [USB Device-Specific Method (_DSM)](usb-device-specific-method---dsm-.md) | To support device-class-specific configuration of the USB subsystem, Windows defines a Device-Specific Method (_DSM) that has the functions that are described in this article. |
| [HIDI2C Device-Specific Method (_DSM)](hidi2c-device-specific-method---dsm-.md) | The _DSM method is defined in section 9.14.1, "_DSM (Device Specific Method)", in the [ACPI 5.0 specification](https://uefi.org/specifications). This method provides for individual, device-specific data and control functions that can be called by a device driver without conflicting with other such device-specific methods. |
| [Windows button array Device-Specific Method (_DSM)](windows-button-array-device-specific-method---dsm-.md) | To support evolution of the Windows Button user interface (UI), Windows defines a Device-Specific Method (_DSM) for the Windows button array device with the function that is described in this article. |

## Other _DSMs defined for Windows

To support device-class-specific communications between the driver stack in Windows and the platform firmware, Microsoft defines Device-Specific Methods (_DSM) to be used with drivers.

| Topic | Description |
|--|--|
| [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](../storage/-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) | The _DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1) is designed to map to the JEDEC Byte Addressable Energy Backed Interface standard in order to minimize BIOS complexity. It provides a common basis of reporting device functions & capabilities, such that OS software can interact with various implementations through the same mechanisms. Further, it allows support for vendor-specific functionality through access to I2C registers. |
| [_DSM (Device Specific Method) for SATA](/previous-versions/windows/hardware/design/dn613874(v=vs.85)) | This method enables management of each port of a SATA controller separate from the host controller as a whole. |
