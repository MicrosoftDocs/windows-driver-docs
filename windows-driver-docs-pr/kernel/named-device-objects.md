---
title: Named Device Objects
description: Named Device Objects
keywords: ["device objects WDK kernel , named", "named device objects WDK kernel"]
ms.date: 09/28/2017
---

# Named Device Objects





A device object, like all object manager objects, can be named or unnamed. When a user-mode application makes an I/O request, it specifies the target of the operation by name. The object manager resolves the name to determine the destination of the I/O request.

> [!IMPORTANT]
> To help increase driver security name device objects only when necessary. Named device objects are generally only necessary for legacy reasons, for example if you have an application that expects to open the device using a particular name or if you’re using a non-PNP device/control device.  Note that WDF drivers do not need to name their PnP device in order to create a symbolic link using [WdfDeviceCreateSymbolicLink](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreatesymboliclink).

A driver can specify a name for a device object when it calls [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice) or [**IoCreateDeviceSecure**](/windows-hardware/drivers/ddi/wdmsec/nf-wdmsec-wdmlibiocreatedevicesecure) to create the device object. For more information about when and how to name a device object, see [NT Device Names](nt-device-names.md).
  
A named device object can also have an MS-DOS device name, which is a symbolic link created by [**IoCreateSymbolicLink**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatesymboliclink) or [**IoCreateUnprotectedSymbolicLink**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreateunprotectedsymboliclink). WDM drivers do not in general require an MS-DOS device name. For more information, see [MS-DOS Device Names](introduction-to-ms-dos-device-names.md).

> [!IMPORTANT]
> If you use a named device object you can use [IoCreateDeviceSecure](/windows-hardware/drivers/ddi/wdmsec/nf-wdmsec-wdmlibiocreatedevicesecure) and specify a SDDL to help secure it. When you implement [IoCreateDeviceSecure](/windows-hardware/drivers/ddi/wdmsec/nf-wdmsec-wdmlibiocreatedevicesecure) always specify a custom class GUID for DeviceClassGuid. You should not specify an existing class GUID here. Doing so has the potential to break security settings or compatibility for other devices belonging to that class. For more information, see [WdmlibIoCreateDeviceSecure](/windows-hardware/drivers/ddi/wdmsec/nf-wdmsec-wdmlibiocreatedevicesecure).
> 
> In order to allow applications or other WDF drivers to access your PnP device, you should use device interfaces. For more information, see [Using Device Interfaces](../wdf/using-device-interfaces.md). A device interface serves as a symbolic link to your device stack’s PDO. Once way to control access to the PDO is by specifying an SDDL string in your INF. If the SDDL string is not in the INF file, Windows will apply a default security descriptor. For more information, see [Securing Device Objects](./controlling-device-access.md) and [SDDL for Device Objects](./sddl-for-device-objects.md).


This section contains the following subsections:

[NT Device Names](nt-device-names.md)

[MS-DOS Device Names](introduction-to-ms-dos-device-names.md)

