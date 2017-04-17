---
title: HID Architecture
author: windows-driver-content
description: This section describes the driver stack for devices that support HID over the I²C transport.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 99384729-552C-4847-AA35-E0D413018104
---

# Architecture and overview


This section describes the driver stack for devices that support HID over the I²C transport.

## Architecture and overview


The HID I²C driver stack consists of existing and new components supplied by Microsoft, as well as components provided by the I²C silicon manufacturer. The following illustration depicts the stack and these components.

![hid over i2c driver stack](images/hid-i2c-arch.png)

Windows 8 provides an interface for low-power, simple buses to communicate effectively with the operating system. This interface is referred to as simple peripheral bus (SPB), and it supports buses like Inter-Integrated Circuit (I²C) and Serial Peripheral Interface (SPI). For additional details about SPB, refer to the Simple Peripheral Buses topic.

Windows 8 provides a KMDF-based HID miniport driver that implements version 1.0 of the protocol specification for HID over I²C. This driver is named HIDI2C.sys. Windows loads this driver based on a compatible ID match, which is exposed by the Advanced Configuration and Power Interface (ACPI). The driver ensures that apps that use HID IOCTLs application level compatibility for software that leverages the HID IOCTLs and API set. A device will assert the host when it requires attention or has data. However, before the assertion occurs, a GPIO connection must exist.

**Note**  The HIDI2C.sys device driver supports only the I²C bus. It does not support SPI, SMBUS, or other low-power buses in Windows 8.

 

## <a href="" id="the-i2c-controller-driver"></a>The I²C Controller Driver


The I²C controller driver exposes a Serial Peripheral Bus (SPB) IOCTL interface to perform read and write operations. This driver provides the actual controller intrinsics (for example, I²C). The SPB Class Extension, on behalf of the controller driver, handles all interaction with the resource hub and implements necessary queues to manage simultaneous targets.

**Note**  The HID I²C driver will not function on systems that do not have an I²C bus that is compatible with the SPB platform. Contact your system manufacturer to determine whether the I²C bus on your device system is compatible with the SPB platform.

 

## The GPIO Controller Driver


The General Purpose Input/Output (GPIO) controller delivers interrupts from the device over GPIO. This is often a simple slave component that uses GPIO pins to signal Windows of new data or other events. GPIO can also control the device by approaches other than the I²C channel.

## The Resource Hub


Connections on a SoC platform are typically non-discoverable, because there are no standards for device enumeration on the buses that are used on SoC. As a result, these devices must be statically defined in the Advanced Configuration and Power Interface (ACPI). Furthermore, components often have multiple dependencies spanning multiple buses, as opposed to a strict branching tree structure.

The resource hub is a proxy that manages the connections among all devices and bus controllers. The HIDI²C driver uses the resource hub to reroute device-open requests to the appropriate controller driver. For more information about the resource hub, refer to the [Connection IDs for SPB Connected Devices](https://msdn.microsoft.com/library/windows/hardware/hh698216) topic.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Architecture%20and%20overview%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


