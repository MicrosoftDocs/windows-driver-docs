---
title: Controlling Device Access in KMDF Drivers
description: Controlling Device Access in KMDF Drivers
keywords:
- device access controls WDK KMDF
- names WDK device objects
- device objects WDK KMDF
- framework objects WDK KMDF , device access controls
- security descriptors WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Controlling Device Access in KMDF Drivers


Drivers must help to prevent users from inappropriately accessing a computer's devices and files. To prevent unauthorized access to devices and files, you must:

-   Name device objects only when necessary.

-   Provide security descriptors for device objects and interfaces.

### <a href="" id="naming-device-objects-only-when-necessary"></a> Naming Device Objects Only When Necessary

Like most Windows Driver Model (WDM) drivers, framework-based drivers typically do not name their device objects. Applications can access a device by specifying a device object name, so each additional device object name represents an additional path that an application can use to access the device.

To prevent unauthorized access to a device, each driver can specify a security descriptor when it names a device object. However, the file name that the operating system provides to a driver (see [**WdfFileObjectGetFileName**](/windows-hardware/drivers/ddi/wdffileobject/nf-wdffileobject-wdffileobjectgetfilename)) does not include the device object name that the application used. Therefore, if several drivers in your driver's stack provide names for their device objects, your driver cannot determine which object name the application used to open the device. As a result, an application might open the device with a less restrictive security descriptor than your driver expects.

Physical device objects (PDOs) must have names. Typically, framework-based bus drivers do not specify a name for a PDO, because the framework (by default) instructs the operating system to generate a name.

On the other hand, a framework-based driver can assign a device name to a device object by calling [**WdfDeviceInitAssignName**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignname). A driver should name a functional device object (FDO), filter device object (filter DO), or PDO only if the driver must support an older application that expects a specific device name, or if the driver belongs to an older driver stack whose architecture requires object names.

Instead of naming FDOs and filter DOs, WDM drivers and framework-based drivers should provide device interfaces that applications can access. The operating system obtains a device interface's security descriptor from the device's PDO and from registry entries that a driver package's INF file specifies. A bus driver can provide device interfaces for a PDO if the driver's devices operate in raw mode, without a function driver.

Some drivers must call [**WdfDeviceCreateSymbolicLink**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreatesymboliclink) to create symbolic link names for their devices. For example, a driver might create an [MS-DOS device name](../kernel/introduction-to-ms-dos-device-names.md) if applications expect to see an MS-DOS name for the device. If your driver creates a symbolic link name for an unnamed FDO or filter DO, the framework associates the symbolic link name with the PDO's name. (Control devices are not associated with a PDO, so your driver cannot create a symbolic link name for an unnamed control device.)

### <a href="" id="providing-security-descriptors-for-device-objects-and-interfaces"></a> Providing Security Descriptors for Device Objects and Interfaces

Every named device object must have a security descriptor. The operating system uses the device object's security descriptor to determine the types of users that are allowed to access a device and its device interfaces. Security descriptors can be assigned to device objects by:

-   The operating system, which provides a default security descriptor for device objects (see [Controlling Device Access](../kernel/controlling-device-access.md)).

-   The framework, which provides a default security descriptor (by using the SDDL\_DEVOBJ\_SYS\_ALL\_ADM\_ALL value) if your driver calls [**WdfDeviceInitAssignName**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignname) to assign a name to a device object (see [SDDL for Device Objects](../kernel/sddl-for-device-objects.md)).

-   Your driver, which can override the framework's default security descriptor by calling [**WdfDeviceInitAssignSDDLString**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignsddlstring).

By default, the operating system also uses the device PDO's security descriptor to determine access rights to the device interfaces that a driver provides.

A driver package can provide an INF file that specifies a device's security descriptors with an [**INF AddReg directive**](../install/inf-addreg-directive.md) within an [**INF DDInstall.HW section**](../install/inf-ddinstall-hw-section.md).

For more information about specifying security descriptors in INF files, see [Creating Secure Device Installations](../install/creating-secure-device-installations.md).

If your driver creates PDOs for devices that operate in raw mode, the driver must specify a [device setup class](../install/overview-of-device-setup-classes.md) when it calls [**WdfPdoInitAssignRawDevice**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitassignrawdevice). Additionally, if your driver creates control devices, it can call [**WdfDeviceInitSetDeviceClass**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetdeviceclass) to specify a device setup class. In both of these cases, system administrators can use the registry key of the specified setup class to store security descriptors for the device.

For information about how the operating system determines which security descriptor to use for a device, see [Controlling Device Access](../kernel/controlling-device-access.md).

When the framework creates a device object, it always sets the FILE\_DEVICE\_SECURE\_OPEN flag so that the operating system will check a device's security descriptor before allowing an application to access any names within the device's namespace. For more information about the FILE\_DEVICE\_SECURE\_OPEN flag and device namespace, see [Controlling Device Namespace Access](../kernel/controlling-device-namespace-access.md).

 

