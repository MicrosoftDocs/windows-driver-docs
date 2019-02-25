---
Description: This topic lists the headers and libraries required for writing a Windows Driver Model (WDM) USB client driver.
title: Headers and libraries required by a USB client driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Headers and libraries required by a USB client driver


This topic lists the headers and libraries required for writing a Windows Driver Model (WDM) USB client driver.

To find the header and library for a specific device driver interface (DDI), consult the reference pages in the [USB Reference](https://msdn.microsoft.com/library/windows/hardware/ff540134).

## Headers


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Header file</th>
<th>Path</th>
<th>Includes</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>hubbusif.h</td>
<td>Include\km</td>
<td></td>
<td>Defines services that are exported by the USB port driver and are available for use by a USB hub driver.</td>
</tr>
<tr class="even">
<td>usb.h</td>
<td>Include\shared</td>
<td></td>
<td>Defines <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923" data-raw-source="[&lt;strong&gt;URB&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538923)"><strong>URB</strong></a> structures for USB Request Blocks (URBs) required by a client driver to send requests to the USB driver stack.</td>
</tr>
<tr class="odd">
<td>usb100.h</td>
<td>Include\shared</td>
<td></td>
<td>Defines USB descriptors, as per the official USB 1.0 specification.</td>
</tr>
<tr class="even">
<td>usb200.h</td>
<td>Include\shared</td>
<td><p>usb100.h</p></td>
<td>Defines USB descriptors, as per the official USB 2.0 specification.</td>
</tr>
<tr class="odd">
<td>usbbusif.h</td>
<td>Include\km</td>
<td></td>
<td>Defines bus interfaces that are defined for a USB client driver (FDO) that wants to link directly to the port driver instead of linking directly to Usbd.sys.</td>
</tr>
<tr class="even">
<td>usbdi.h</td>
<td>Include\shared</td>
<td><p>usb.h</p>
<p>usbioctl.h</p></td>
<td>Defines helper macros for formatting URBs for specific types of requests.</td>
</tr>
<tr class="odd">
<td>usbdlib.h</td>
<td>Include\km</td>
<td></td>
<td>Defines DDIs that are used by a USB client driver to send requests to the USB driver stack.</td>
</tr>
<tr class="even">
<td>usbdrivr.h</td>
<td>Include\km</td>
<td><p>usb.h</p>
<p>usbdlib.h</p>
<p>usbioctl.h</p>
<p>usbbusif.h</p></td>
<td>Defines USB_KERNEL_IOCTL.</td>
</tr>
<tr class="odd">
<td>usbioctl.h</td>
<td>Include\shared</td>
<td><p>usbiodef.h</p>
<p>usb200.h</p></td>
<td>Defines IOCTL codes supported by the USB driver stack. Includes kernel-mode IOCTL codes for client drivers; user-mode IOCTL codes for applications.</td>
</tr>
<tr class="even">
<td>usbiodef.h</td>
<td>Include\shared</td>
<td></td>
<td>Defines interface and WMI GUIDs.</td>
</tr>
<tr class="odd">
<td>usbkern.h</td>
<td>Include\km</td>
<td><p>usbioctl.h</p></td>
<td>Deprecated.</td>
</tr>
<tr class="even">
<td>usbrpmif.h</td>
<td>Include\um</td>
<td><p>usb100.h</p>
<p>windef.h</p>
<p>winapifamily.h</p></td>
<td>Defines functions for an application to register itself in order to perform driver redirection operations for a USB device.</td>
</tr>
<tr class="odd">
<td>usbspec.h</td>
<td>Include\shared</td>
<td></td>
<td>Defines device driver interfaces, as per the official USB specifications.</td>
</tr>
<tr class="even">
<td>usbuser.h</td>
<td>Include\um</td>
<td></td>
<td>Defines user-mode IOCTL codes that are supported by the USB port driver.</td>
</tr>
<tr class="odd">
<td>winusb.h</td>
<td>Include\um</td>
<td><p>winapifamily.h</p>
<p>winusbio.h</p></td>
<td>Defines <a href="https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb" data-raw-source="[WinUSB functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb)">WinUSB functions</a> exposed by Winusb.dll, which are used by applications that want to send requests to Winusb.sys that is installed as the function driver for a USB device.</td>
</tr>
<tr class="even">
<td>winusbio.h</td>
<td>Include\shared</td>
<td><p>winapifamily.h</p>
<p>usb.h</p></td>
<td>Defines flags for <a href="https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb" data-raw-source="[WinUSB functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb)">WinUSB functions</a>.</td>
</tr>
</tbody>
</table>

 

## Libraries


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Library</th>
<th>Path</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>usbd.lib</td>
<td><p>\Lib\win8\km&lt;em&gt;&lt;arch&gt;</em></p>
<p>\Lib\win7\km&lt;em&gt;&lt;arch&gt;</em></p>
<p>\Lib\winv6.3\km&lt;em&gt;&lt;arch&gt;</em></p></td>
<td>Provides helper routines for getting information from the USB driver stack and formatting URBs for requests.</td>
</tr>
<tr class="even">
<td>usbrpm.lib</td>
<td><p>\Lib\win8\km&lt;em&gt;&lt;arch&gt;</em></p>
<p>\Lib\win7\km&lt;em&gt;&lt;arch&gt;</em></p>
<p>\Lib\winv6.3\km&lt;em&gt;&lt;arch&gt;</em></p></td>
<td>Provides functions for an application to perform operations for replacing a Microsoft-provided driver with a third-party RPM driver.</td>
</tr>
<tr class="odd">
<td>usbdex.lib</td>
<td><p>\Lib\win8\km&lt;em&gt;&lt;arch&gt;</em></p>
<p>\Lib\win7\km&lt;em&gt;&lt;arch&gt;</em></p>
<p>\Lib\winv6.3\km&lt;em&gt;&lt;arch&gt;</em></p></td>
<td>Provides helper routines for client drivers to send requests to the underlying USB driver stack. The library gets loaded and statically linked to the client driver module when it is built. A client driver that calls these routines can run on Windows Vista and later versions of Windows.</td>
</tr>
<tr class="even">
<td>winusb.lib</td>
<td><p>\Lib\win8\km&lt;em&gt;&lt;arch&gt;</em></p>
<p>\Lib\win8\um&lt;em&gt;&lt;arch&gt;</em></p>
<p>\Lib\win7\km&lt;em&gt;&lt;arch&gt;</em></p>
<p>\Lib\win7\um&lt;em&gt;&lt;arch&gt;</em></p>
<p>\Lib\winv6.3\km&lt;em&gt;&lt;arch&gt;</em></p>
<p>\Lib\winv6.3\um&lt;em&gt;&lt;arch&gt;</em></p></td>
<td>Provides functions for a user-mode client driver or an application to communicate with a USB device that has Winusb.sys loaded as its function driver.</td>
</tr>
</tbody>
</table>

 

## Header Changes in Windows 8


Starting in Windows Driver Kit (WDK) for Windows 8, header file usbspec.h replaces USBProtocolDefs.h.

The new header file, usbspec.h, provides protocol definitions for the DDIs that are defined, as per the official USB specifications. The header file includes DDIs for the USB 3.0 specification.

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  
[Header files in the Windows Driver Kit](https://msdn.microsoft.com/library/windows/hardware/ff554695)  
[Getting started with USB client driver development](getting-started-with-usb-client-driver-development.md)  



