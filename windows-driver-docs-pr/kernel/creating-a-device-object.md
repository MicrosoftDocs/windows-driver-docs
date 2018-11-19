---
title: Creating a Device Object
description: Creating a Device Object
ms.assetid: 3eda8eb2-8a83-4753-a099-2531bfb9aeeb
keywords: ["device objects WDK kernel , creating", "non-WDM driver device objects WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Creating a Device Object





A monolithic driver must create a device object for each physical, logical, or virtual device for which it handles I/O requests. A driver that does not create a device object for a device does not receive any IRPs for the device.

In some technology areas, a minidriver that is associated with a class driver or port driver does not have to create its own device objects. Instead, the class or port driver creates the device object, and receives all IRPs for the device. The class or port driver then uses a driver-specific method to pass the I/O request to the minidriver. See the documentation for your particular technology area to determine if Microsoft supplies a class or port driver that creates device objects on behalf of your driver.

Drivers call either [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) or [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407) to create their device objects. For more information about which routine to use, see the following sections.

[Creating Device Objects for WDM Function and Filter Drivers](#creating-device-objects-for-wdm-function-and-filter-drivers)

[Creating Device Objects for WDM Bus Drivers](#creating-device-objects-for-wdm-bus-drivers)

[Creating Device Objects for Non-WDM Drivers](#creating-device-objects-for-non-wdm-drivers)

When the driver creates a device object, it supplies the following information to **IoCreateDevice** or **IoCreateDeviceSecure**:

-   The size of the device's *device extension*. The device extension is a system-allocated storage area that the driver can use for device-specific storage. For more information, see [Device Extensions](device-extensions.md).

-   A system-defined constant, indicating the **DeviceType** represented by the device object. For more information, see [Specifying Device Types](specifying-device-types.md).

-   One or more ORed, system-defined constants that indicate the device characteristics for the device. For more information, see [Specifying Device Characteristics](specifying-device-characteristics.md).

-   A Boolean value, named *Exclusive*, that specifies whether a bit in the device object's **Flags** should be set with DO\_EXCLUSIVE, indicating the driver services an exclusive device, such as a video, serial, parallel, or sound device. WDM drivers must set *Exclusive* to **FALSE**. For more information, see [Specifying Exclusive Access to Device Objects](specifying-exclusive-access-to-device-objects.md).

-   A pointer to the driver object for the driver. A WDM function or filter driver receives a pointer to its driver object as a parameter to its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine. All drivers receive a pointer to their driver object in their [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. The system uses this pointer to associate the driver with its device object.

-   An optional pointer to a null-terminated Unicode string (*DeviceName*) naming the device. WDM drivers, other than bus drivers, do not supply a device name; doing so bypasses the PnP manager's security features. For more information, see [Named Device Objects](named-device-objects.md).

If the call to [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) or [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407) succeeds, the I/O manager provides storage for the device object itself and for all other data structures associated with the device object, including the device extension, which it initializes with zeros.

### Creating Device Objects for WDM Function and Filter Drivers

WDM drivers, other than bus drivers, call **IoCreateDevice** to create their device objects. Most WDM drivers create their device objects from within their *AddDevice* routines. Some drivers, such as disk drivers that must respond to drive layout IOCTLs, call **IoCreateDevice** from a dispatch routine.

Unless device type-specific sections of the Windows Driver Kit (WDK) documentation state otherwise, your driver should create its device objects in its *AddDevice* routine. For more information, see [Writing an AddDevice Routine](writing-an-adddevice-routine.md).

### Creating Device Objects for WDM Bus Drivers

A WDM bus driver creates a PDO when it is enumerating a new device in response to an [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff551670) request, if the relation type is **BusRelations**.

The following rules determine if a bus driver calls **IoCreateDevice** or **IoCreateDeviceSecure** to create a device object:

-   If a device can be used in [*raw mode*](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raw-mode), then it must call **IoCreateDeviceSecure**.

-   If the device is not raw-mode capable, then the bus driver can use either **IoCreateDevice** or **IoCreateDeviceSecure**. **IoCreateDevice** can be used when the default system security for devices on the bus is adequate; **IoCreateDeviceSecure** can be used to specify a more stringent security descriptor. For more information, see [Controlling Device Access](controlling-device-access.md).

### Creating Device Objects for Non-WDM Drivers

A non-WDM driver uses **IoCreateDevice** to create unnamed device objects, and **IoCreateDeviceSecure** to create named device objects. Note the unnamed device objects of a non-WDM driver are not accessible from user mode, so the driver usually must create at least one named object.

 

 




