---
title: The Filter Driver's Control Device Object
description: The Filter Driver's Control Device Object
keywords:
- control device objects WDK file system
- CDOs WDK file system
ms.date: 02/23/2023
---

# The Filter Driver's Control Device Object

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

A file system is required to create and use a named control device object (CDO). Unlike a file system, a legacy file system filter driver isn't required to have a CDO. If it does, this optionally named CDO represents the filter driver to the system. Its role is to receive I/O requests from a user-mode application (or, less commonly, another kernel-mode driver), and to act on them appropriately.

Most file system filter drivers create and use a CDO. However, support for I/O requests on the CDO is optional. To provide this support, when the filter driver calls [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice) to create the CDO, it must supply a device name for the object. The user-mode application can then obtain a handle to the named CDO by calling [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea), supplying the user-mode version of the device name.

For example, consider a hypothetical "MyLegacyFilter" kernel-mode driver. This driver can create a CDO with the name:

```cpp
\Device\MyLegacyFilter
```

and call [**IoCreateSymbolicLink**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatesymboliclink) to link this name to an equivalent user-mode-visible name. This naming is done so that MyLegacyFilter's user-mode application can open a handle to the kernel-mode driver's CDO by supplying the name:

```cpp
\\.\MyLegacyFilter
```

when it calls [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea).

## Types of I/O Requests That Are Sent to the Filter Driver's Control Device Object

File system filter drivers aren't required to support any I/O operations on the control device object (CDO). However, most filters permit the following types of I/O requests to be sent to the filter's CDO:

- [**IRP_MJ_CREATE**](./irp-mj-create.md) (to open a handle to the target device object, and give that handle to a user application)

- [**IRP_MJ_CLEANUP**](./irp-mj-cleanup.md) (to close a user-mode application's handle to the target device object)

- [**IRP_MJ_CLOSE**](./irp-mj-close.md) (to close the last remaining open handle to the target device object)

- [**IRP_MJ_DEVICE_CONTROL**](./irp-mj-device-control.md), [**IRP_MJ_FILE_SYSTEM_CONTROL**](./irp-mj-file-system-control.md), or **FastIoDeviceControl** (to send private IOCTLs or FSCTLs to the filter driver)

Unlike all other device objects that a file system filter driver creates, the CDO isn't attached to a driver stack. No device objects are attached above or below the filter driver's CDO. Thus, for any I/O request it receives, the CDO can safely assume that it's the sole intended recipient. This isn't true for filter device objects or file system CDOs. Accordingly, the CDO must eventually complete every IRP it receives. For fast I/O requests, it must return TRUE or FALSE.
