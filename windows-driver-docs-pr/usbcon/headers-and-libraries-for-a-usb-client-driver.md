---
title: Headers and libraries required by a USB client driver
description: This article lists the headers and libraries required for writing a Windows Driver Model (WDM) USB client driver.
ms.date: 01/20/2023
---

# Headers and libraries required by a USB client driver

This article lists the headers and libraries required for writing a Windows Driver Model (WDM) USB client driver.

To find the header and library for a specific device driver interface (DDI), consult the reference pages in the [USB Reference](/windows-hardware/drivers/ddi/_usbref/).

## Headers

| Header file | Path | Includes | Description |
|---|---|---|---|
| hubbusif.h | Include\km | | Defines services that are exported by the USB port driver and are available for use by a USB hub driver. |
| usb.h | Include\shared | | Defines **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structures for USB Request Blocks (URBs) required by a client driver to send requests to the USB driver stack. |
| usb100.h | Include\shared | | Defines USB descriptors, as per the official USB 1.0 specification. |
| usb200.h | Include\shared | usb100.h | Defines USB descriptors, as per the official USB 2.0 specification. |
| usbbusif.h | Include\km | | Defines bus interfaces that are defined for a USB client driver (FDO) that wants to link directly to the port driver instead of linking directly to Usbd.sys. |
| usbdi.h | Include\shared | usb.h</br>usbioctl.h | Defines helper macros for formatting URBs for specific types of requests. |
| usbdlib.h | Include\km | | Defines DDIs that are used by a USB client driver to send requests to the USB driver stack. |
| usbdrivr.h | Include\km | usb.h</br>usbdlib.h</br>usbioctl.h</br>usbbusif.h | Defines USB_KERNEL_IOCTL. |
| usbioctl.h | Include\shared | usbiodef.h</br>usb200.h | Defines IOCTL codes supported by the USB driver stack. Includes kernel-mode IOCTL codes for client drivers; user-mode IOCTL codes for applications. |
| usbiodef.h | Include\shared | | Defines interface and WMI GUIDs. |
| usbkern.h | Include\km | usbioctl.h | Deprecated. |
| usbrpmif.h | Include\um | usb100.h</br>windef.h</br>winapifamily.h | Defines functions for an application to register itself in order to perform driver redirection operations for a USB device. |
| usbspec.h | Include\shared | | Defines device driver interfaces, as per the official USB specifications. |
| usbuser.h | Include\um | | Defines user-mode IOCTL codes that are supported by the USB port driver. |
| winusb.h | Include\um | winapifamily.h</br>winusbio.h | Defines [WinUSB functions](/windows/win32/api/winusb/#functions) exposed by Winusb.dll, which are used by applications that want to send requests to Winusb.sys that is installed as the function driver for a USB device. |
| winusbio.h | Include\shared | winapifamily.h</br>usb.h | Defines flags for [WinUSB functions](/windows/win32/api/winusb/#functions). |

## Libraries

| Library | Path | Description |
|---|---|---|
| usbd.lib | *\Lib\win8\km*</br>*\Lib\win7\km*</br>*\Lib\winv6.3\km* | Provides helper routines for getting information from the USB driver stack and formatting URBs for requests. |
| usbrpm.lib | *\Lib\win8\km*</br>*\Lib\win7\km*</br>*\Lib\winv6.3\km* | Provides functions for an application to perform operations for replacing a Microsoft-provided driver with a third-party RPM driver. |
| usbdex.lib | *\Lib\win8\km*</br>*\Lib\win7\km*</br>*\Lib\winv6.3\km* | Provides helper routines for client drivers to send requests to the underlying USB driver stack. The library gets loaded and statically linked to the client driver module when it is built. A client driver that calls these routines can run on Windows Vista and later versions of Windows. |
| winusb.lib | *\Lib\win8\km*</br>*\Lib\win8\um*</br>*\Lib\win7\km*</br>*\Lib\win7\um*</br>*\Lib\winv6.3\km*</br>*\Lib\winv6.3\um* | Provides functions for a user-mode client driver or an application to communicate with a USB device that has Winusb.sys loaded as its function driver. |

## Header Changes in Windows 8

Starting in Windows Driver Kit (WDK) for Windows 8, header file usbspec.h replaces USBProtocolDefs.h.

The new header file, usbspec.h, provides protocol definitions for the DDIs that are defined, as per the official USB specifications. The header file includes DDIs for the USB 3.0 specification.

## Related topics

- [Universal Serial Bus (USB)](../index.yml)
- [Header files in the Windows Driver Kit](../gettingstarted/header-files-in-the-windows-driver-kit.md)
- [Getting started with USB client driver development](getting-started-with-usb-client-driver-development.md)
