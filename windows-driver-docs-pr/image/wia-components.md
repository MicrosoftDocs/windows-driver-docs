---
title: WIA Components
description: WIA components
ms.date: 05/04/2023
---

# WIA components

WIA consists of several layers that intercede between the user and the hardware. The user interacts with the WIA application, which can have optional user interfaces. This application communicates with the WIA service, which sends the user's requests to the minidriver. The minidriver communicates with the relevant kernel-mode bus driver. Finally, the bus driver communicates with the hardware. The following diagram illustrates the software components that make up the WIA interface.

![diagram illustrating the software components that make up the wia interface.](images/art-1.png)

## Imaging applications

Imaging applications do not communicate directly with the minidriver, but they communicate with the WIA service through the WIA application programming interface (WIA API) to access images and acquire data from WIA devices. These applications can use the system-supplied user interface (UI) or one that the device's manufacturer supplies. The UI is used to select items for transfer and to set relevant properties. Note that it is the application, not the driver, that transfers the selected items after the UI is dismissed. For more information about the WIA API for imaging applications, see the Microsoft Windows SDK documentation.

## WIA service

The WIA service is a system-supplied component that communicates with imaging applications and WIA minidrivers. The WIA service is a collection of the COM interfaces that are listed in the following table, all of which are described in the Microsoft Windows SDK documentation. The WIA service runs in a separate process from applications but in the same process as WIA minidrivers. Applications direct device requests to the WIA service. The WIA service then directs these requests to the appropriate minidriver, through a WIA device driver interface (WIA DDI). The following table lists the APIs that a WIA application can implement.

| WIA API | Description |
|--|--|
| **IEnumWIA_DEV_CAPS** | Enumerates the capabilities of the WIA hardware device. Device capabilities include commands and events that the device supports. |
| **IEnumWIA_DEV_INFO** | Enumerates the WIA hardware devices and their properties. Device information properties describe the installation and configuration of WIA hardware devices. |
| **IEnumWIA_FORMAT_INFO** | Enumerates the format and media-type information for a device. |
| **IEnumWiaItem** | Enumerates **IWiaItem** objects in the current folder of a tree. The WIA run-time system represents every WIA hardware device to an application as a hierarchical tree of **IWiaItem** objects. |
| **IWiaDataCallback** | Provides an application callback mechanism during data transfers from WIA hardware devices to applications. |
| **IWiaDataTransfer** | Supports a shared memory window to transfer data from the device object to the application, and eliminates unnecessary data copies during marshalling. |
| **IWiaDevMgr** | Used by applications to create and manage image acquisition devices. They also use it to register to receive device events. |
| **IWiaEventCallback** | Used by applications to receive notification of WIA hardware device events. |
| **IWiaItem** | Enables applications to query devices for their capabilities. **IWiaItem** also provides access to data transfer interfaces and item properties. In addition, this interface provides methods to enable applications to control the device. |
| **IWiaPropertyStorage** | Provides access to information about an **IWiaItem** object's properties. |

## WIA driver services library

The [WIA driver services library](wia-driver-services-library.md) is a system-supplied component that provides helper functions for WIA minidrivers. A minidriver can call helper functions to perform tasks, such as the following:

- Initialize the [WIA driver item tree](wia-driver-item-tree.md).

- Read, write, and validate device properties.

- Transfer data.

Alternatively, a minidriver can perform such tasks itself. By using the helper functions, you can reduce development time and the size of a WIA minidriver and still have the flexibility to develop individual solutions.

## WIA utility library

The [WIA utility library](wia-utility-library.md) includes a collection of debugging functions (**wiauDbg***Xxx*), a collection of general utility helper functions, and three classes: the **CWiauDbgFn** class, the **CWiauFormatConverter** class, and the **CWiauPropertyList** class.

## WIA minidrivers

[WIA minidrivers](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv) are vendor-supplied, user-mode components that direct WIA property changes and commands to an imaging device. A minidriver implements the WIA DDI, which the WIA service calls to communicate with the minidriver.

A WIA minidriver provides a device-specific, user-mode interface to a kernel-mode still image driver, which drives the imaging device through a driver, such as a USB driver. A minidriver communicates with the kernel-mode drivers by calling the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea), **ReadFile**, **WriteFile**, and [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) Microsoft Win32 functions (which are described in the Microsoft Windows SDK documentation).

An imaging application cannot directly call the WIA minidriver. Only the WIA service can call the driver directly.

## Kernel I/O drivers

Kernel-mode still image drivers are system-supplied or IHV-supplied components that package data for delivery to still image devices and for transfer from still image devices. A kernel-mode still image driver is bus-specific.

Microsoft provides Microsoft Windows Driver Model (WDM)-based kernel-mode still image drivers for the USB, SCSI, serial, and IEEE 1394 buses. For more information about these drivers, see [Accessing kernel-mode drivers for still image devices](accessing-kernel-mode-drivers-for-still-image-devices.md).

A vendor must provide a kernel-mode still image driver only if its imaging device is incompatible with Microsoft-supplied kernel-mode I/O drivers.

You can retrieve version information from the driver. The [**WIA_DIP_WIA_VERSION**](./wia-dip-wia-version.md) property contains the WIA version, and the [**WIA_DIP_DRIVER_VERSION**](./wia-dip-driver-version.md) property contains the driver DLL version. The WIA service creates and maintains these properties; they are added automatically by the WIA service when the driver is loaded. Windows Me does not include these properties.
