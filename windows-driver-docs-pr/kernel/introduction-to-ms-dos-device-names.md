---
title: Introduction to MS-DOS Device Names
author: windows-driver-content
description: Introduction to MS-DOS Device Names
ms.assetid: 44b2f871-56e1-46d3-aab4-c38f498d089d
keywords: ["MS-DOS device names WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to MS-DOS Device Names


## <a href="" id="ddk-introduction-to-ms-dos-device-names-kg"></a>


A named device object that is created by a non-WDM driver typically has an MS-DOS device name. An MS-DOS device name is a symbolic link in the object manager with a name of the form **\\DosDevices\\***DosDeviceName*.

An example of a device with an MS-DOS device name is the serial port, COM1. It has the MS-DOS device name **\\DosDevices\\COM1**. Likewise, the C drive has the name **\\DosDevices\\C:**.

WDM drivers do not usually supply MS-DOS device names for their devices. Instead, WDM drivers use the [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) routine to register a device interface. The device interface specifies devices by their capabilities, rather than by a particular naming convention. For more information, see [Device Interface Classes](https://msdn.microsoft.com/library/windows/hardware/ff541339).

Drivers are required to supply an MS-DOS device name only if the device is required to have a specific well-known MS-DOS device name to work with user-mode programs.

A driver supplies an MS-DOS device name for a device object by using the [**IoCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549043) routine to create a symbolic link to the device. For example, the following code example creates a symbolic link from **\\DosDevices\\***DosDeviceName* to **\\Device\\***DeviceName*.

```
UNICODE_STRING DeviceName;
UNICODE_STRING DosDeviceName;
NTSTATUS status;

RtlInitUnicodeString(&DeviceName, L"\\Device\\DeviceName");
RtlInitUnicodeString(&DosDeviceName, L"\\DosDevices\\DosDeviceName");
status = IoCreateSymbolicLink(&DosDeviceName, &DeviceName);
if (!NT_SUCCESS(status)) {
  /* Symbolic link creation failed.  Handle error appropriately. */
}
```

Note that the system supports multiple versions of the **\\DosDevices** directory. Make sure that your driver creates its symbolic links in the version that you intend. For more information, see [Local and Global MS-DOS Device Names](local-and-global-ms-dos-device-names.md).

To access the **DosDevices** namespace from user mode, specify **\\\\.\\** when you open a file name. You can open a corresponding device in user mode by calling **CreateFile()**.

For example, the following code example opens the \\\\DosDevices\\\\*DosDeviceName* device in user mode.

```
file = CreateFileW(L"\\\\.\\DosDeviceName",
  GENERIC READ | GENERIC WRITE,
    0,
    NULL,
    OPEN_EXISTING,
    0,
    NULL);
```

A symbolic link can also be created from a user-mode application by using the user-mode **DefineDosDevice** routine. For more information, see the Microsoft Windows SDK.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20MS-DOS%20Device%20Names%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


