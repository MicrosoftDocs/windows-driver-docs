---
title: DIF_INSTALLDEVICEFILES
description: A DIF_INSTALLDEVICEFILES request allows an installer to participate in copying the files to support a device or to make a list of the files for a device.
keywords: ["DIF_INSTALLDEVICEFILES Device and Driver Installation"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DIF_INSTALLDEVICEFILES
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.date: 12/19/2024
---

# DIF_INSTALLDEVICEFILES

A DIF_INSTALLDEVICEFILES request allows an installer to participate in copying the files to support a device or to make a list of the files for a device. The device files include files for the selected driver, any device interfaces, and any co-installers.

##  

### When sent

The [system-provided device installation components](./index.md) send this DIF request for a variety of reasons. Some device installation components send this DIF request before DIF_REGISTER_COINSTALLERS, DIF_INSTALLINTERFACES, and DIF_INSTALL_DEVICE to ensure that all the relevant files can be copied before proceeding with the installation. Some device installation components omit this DIF request and expect the files to be copied during the handling of those three DIF requests. In addition, some device installation components send this DIF request to retrieve the list of the files associated with a device.

### Who handles

| Class co-installer | Can handle |
|--|--|
| Device co-installer | Does not handle |
| Class installer | Can handle |

### Installer input

#### *DeviceInfoSet*

Supplies a handle to the [device information set](./device-information-sets.md) that contains the device whose supporting files are to be copied.

#### *DeviceInfoData*

Supplies a pointer to an **[SP_DEVINFO_DATA](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data)** structure that identifies the device in the device information set.

Device Installation Parameters

There are device installation parameters (**[SP_DEVINSTALL_PARAMS](/windows/win32/api/setupapi/ns-setupapi-sp_devinstall_params_a)**) associated with the *DeviceInfoData*.

If the DI_NOVCP flag is set, the device installation parameters contain a valid **FileQueue** handle and installers that handle this DIF request add their file operations to this queue and do not commit the queue.

### Class installation parameters

None

### Installer output

Device Installation Parameters

An installer can modify the **FileQueue**, if there is one.

### Installer return value

A co-installer can return NO_ERROR, ERROR_DI_POSTPROCESSING_REQUIRED, or a Win32 error code.

If a class installer successfully handles this request and **[SetupDiCallClassInstaller](/windows/win32/api/setupapi/nf-setupapi-setupdicallclassinstaller)** should subsequently call the default handler, the class installer returns ERROR_DI_DO_DEFAULT.

If the class installer successfully handles this request, including directly calling the default handler, the class installer should return NO_ERROR and **SetupDiCallClassInstaller** will not subsequently call the default handler again.

> [!NOTE]
> The class installer can directly call the default handler, but the class installer should never attempt to supersede the operations of the default handler.

For more information about calling the default handler, see [Calling Default DIF Code Handlers](./calling-the-default-dif-code-handlers.md).

If the class installer encounters an error, the installer should return an appropriate Win32 error code and **SetupDiCallClassInstaller** will not subsequently call the default handler.

### Default DIF code handler

**[SetupDiInstallDriverFiles](/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldriverfiles)**

### Installer operation

In response to a DIF_INSTALLDEVICEFILES request an installer specifies any necessary file operations. For example, an installer can specify an additional file to be copied that is required for device installation. If the DI_NOVCP flag is set, an installer specifies file operations by adding them to the **FileQueue** in the device installation parameters. See the Microsoft Windows SDK for information about how to use file queues and for reference pages on file-queuing functions such as **SetupInstallFilesFromInfSection**.

If this DIF request is sent during device installation, and the installer returns a Microsoft Win32 error code, Windows stops the installation.

If a [system-provided device installation component](./index.md) sends this DIF request to retrieve a list of the files associated with a device, the component retrieves the file queue but does not commit the queue.

For more information about DIF codes, see [Handling DIF Codes](./handling-dif-codes.md).

## Requirements

| &nbsp; | &nbsp; |
|--|--|
| Version | Microsoft Windows 2000 and later |
| Header | Setupapi.h (include Setupapi.h) |

## See also

- **[SetupDiInstallDriverFiles](/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldriverfiles)**
- **[SP_DEVINFO_DATA](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data)**
- **[SP_DEVINSTALL_PARAMS](/windows/win32/api/setupapi/ns-setupapi-sp_devinstall_params_a)**
