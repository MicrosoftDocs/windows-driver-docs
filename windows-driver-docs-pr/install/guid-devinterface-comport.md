---
title: GUID_DEVINTERFACE_COMPORT
description: The GUID_DEVINTERFACE_COMPORT device interface class is defined for COM ports.
keywords: ["GUID_DEVINTERFACE_COMPORT Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_COMPORT
api_location:
- Ntddser.h
api_type:
- HeaderDef
ms.date: 01/17/2023
ms.topic: reference
---

# GUID_DEVINTERFACE_COMPORT

The GUID_DEVINTERFACE_COMPORT [device interface class](./overview-of-device-interface-classes.md) is defined for [COM ports](/previous-versions/ff546485(v=vs.85)).

| Attribute | Setting |
|--|--|
| Identifier | GUID_DEVINTERFACE_COMPORT |
| Class GUID | {86E0D1E0-8089-11D0-9CE4-08003E301F73} |

## Remarks

Drivers for serial ports register instances of this device interface class to notify the operating system and applications of the presence of COM ports.

The system-supplied function driver for serial ports registers an instance of this device interface class for a [serial port](../serports/using-serial-sys-and-serenum-sys.md).

Using the device interface (GUID_DEVINTERFACE_COMPORT) is the recommended way to discover and access a COM port. Using legacy COM port names is prone to name collisions and doesn't provide state change notifications to a client. 
Refer to the sample code that illustrates [how to access a device using this device interface](/windows-hardware/drivers/serports/device-interface-publication-sercx#accessing-the-serial-port-device-interface).

The following samples (on GitHub) register an instance of this class for a serial port:

-   [The Serial sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/serial/serial)
-   [The Virtual serial driver sample](../wdf/user-mode-driver-framework-design-guide.md) (UMDF 1.0)
-   [The Virtual serial2 driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/serial/VirtualSerial2) (KMDF)

[**GUID_CLASS_COMPORT**](guid-class-comport.md) is an obsolete identifier for this device interface class; for new instances of this class, use GUID_DEVINTERFACE_COMPORT instead.

## Requirements

|&nbsp;| &nbsp;|
|--|--|
| Version | Available in Microsoft Windows 2000 and later versions of Windows. |
| Header | Ntddser.h (include Ntddser.h) |

## See also

- **[GUID_CLASS_COMPORT](guid-class-comport.md)**
