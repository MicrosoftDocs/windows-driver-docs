---
title: Introduction to MS-DOS Device Names
description: Introduction to MS-DOS Device Names
ms.assetid: 44b2f871-56e1-46d3-aab4-c38f498d089d
keywords: ["MS-DOS device names WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to MS-DOS Device Names





A named device object that is created by a non-WDM driver typically has an MS-DOS device name. An MS-DOS device name is a symbolic link in the object manager with a name of the form **\\DosDevices\\**<em>DosDeviceName</em>.

An example of a device with an MS-DOS device name is the serial port, COM1. It has the MS-DOS device name **\\DosDevices\\COM1**. Likewise, the C drive has the name **\\DosDevices\\C:**.

WDM drivers do not usually supply MS-DOS device names for their devices. Instead, WDM drivers use the [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) routine to register a device interface. The device interface specifies devices by their capabilities, rather than by a particular naming convention. For more information, see [Device Interface Classes](https://msdn.microsoft.com/library/windows/hardware/ff541339).

Drivers are required to supply an MS-DOS device name only if the device is required to have a specific well-known MS-DOS device name to work with user-mode programs.

A driver supplies an MS-DOS device name for a device object by using the [**IoCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549043) routine to create a symbolic link to the device. For example, the following code example creates a symbolic link from **\\DosDevices\\**<em>DosDeviceName</em> to **\\Device\\**<em>DeviceName</em>.

```cpp
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

```cpp
file = CreateFileW(L"\\\\.\\DosDeviceName",
  GENERIC READ | GENERIC WRITE,
    0,
    NULL,
    OPEN_EXISTING,
    0,
    NULL);
```

A symbolic link can also be created from a user-mode application by using the user-mode **DefineDosDevice** routine. For more information, see the Microsoft Windows SDK.

 

 




