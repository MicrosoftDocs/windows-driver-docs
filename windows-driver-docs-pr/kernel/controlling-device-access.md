---
title: Controlling Device Access
author: windows-driver-content
description: Controlling Device Access
ms.assetid: b5e562ad-573b-4b0f-9d85-2410fda16e4e
keywords: ["device objects WDK kernel , security", "security WDK device objects", "device access controls WDK kernel", "non-WDM driver device access WDK kernel", "security descriptors WDK device objects"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Controlling Device Access


## <a href="" id="ddk-controlling-device-access-kg"></a>


Access to a device is controlled by a security descriptor (and the ACL it contains). A security descriptor for a device object can be specified when the device object is created, or set in the registry.

### Controlling Device Access for WDM Drivers

When a WDM driver (other than certain bus drivers) creates a device object, the Plug and Play manager determines a security descriptor for the device. The order of operations is as follows.

1.  The PnP manager calls the driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine.

2.  The driver's *AddDevice* routine calls [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) to create the device object and attach it to the device object stack.

3.  The PnP manager updates the security descriptor for the newly-created device object.

For a WDM driver, the PnP manager determines the security descriptor for the device object as follows.

1.  If the device has a security descriptor setting in the registry, it is applied to every object in the device stack.

2.  Otherwise, if the device's setup class has a security descriptor setting in the registry, it is applied to every object in the device stack.

3.  Otherwise, the PnP manager leaves the default security descriptor for each object unchanged. In this case, the default security descriptor for the stack is determined by the device type and device characteristics of the PDO.

For most device types and characteristics, the default security descriptor gives full access (GENERIC\_ALL) to administrators, and read, write, and execute access (GENERIC\_READ | GENERIC\_WRITE | GENERIC\_EXECUTE) access to everyone else.

For more information about how to set a security descriptor for a device or device setup class in the registry, see [Setting Device Object Properties in the Registry](setting-device-object-properties-in-the-registry.md).

If a device is operated in raw mode, then the PnP manager cannot determine a security descriptor for the device object. In that case, the bus driver must provide a security descriptor; see below.

### Controlling Device Access for WDM Bus Drivers

A WDM bus driver must provide a security descriptor for the PDO of every device that can be operated in raw mode. Use [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407) to create the device object with a security descriptor.

If the bus driver does not operate a device in raw mode, then it is not required to supply a security descriptor. The PnP manager determines the security descriptor, as described above. The bus driver can supply a security descriptor if it must ensure that its PDOs have stricter security settings than the default descriptor. Any descriptor specified by the bus driver is overridden by settings in the registry.

For more information about creating device objects, see [Creating a Device Object](creating-a-device-object.md).

### Controlling Device Access for Non-WDM Drivers

Non-WDM drivers must specify a default security descriptor and class GUID for any named device objects they create.

Use the **IoCreateDeviceSecure** routine to create the named device object and to specify the default security descriptor and class GUID for that device. The security descriptor is specified in a subset of SDDL. For more information, see [SDDL for Device Objects](sddl-for-device-objects.md).

The system overrides the default security descriptor with any security settings in the registry for the specified class GUID. The driver must specify its own unique GUID for the device. Use the GuidGen tool to generate a unique GUID. (GuidGen is included in the Microsoft Windows SDK.)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Controlling%20Device%20Access%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


