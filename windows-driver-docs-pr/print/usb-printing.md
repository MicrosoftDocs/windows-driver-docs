---
title: Microsoft USB Printer Driver (Usbprint.sys)
author: windows-driver-content
description: Usbprint.sys is the Microsoft-provided device driver for USB printers. Usbprint.sys works with Usbmon.dll to provide end-to-end connectivity between USB printers and high-level printer drivers.
MS-HAID:
- 'usbprnt\_39d931b8-11cd-42c5-a212-da319bedddb8.xml'
- 'print.usb\_printing'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6fc1635d-b819-43ba-a549-2488995fa9b0
keywords: ["printer drivers WDK , USB", "USB printers WDK"]
---

# Microsoft USB Printer Driver (Usbprint.sys)


Usbprint.sys is the Microsoft-provided device driver for USB printers. Usbprint.sys works with Usbmon.dll to provide end-to-end connectivity between USB printers and high-level printer drivers.

## <a href="" id="ddk-usbprint-interface-gg"></a>


Unlike some USB device class drivers, Usbprint.sys does not "drive" the printer. Instead, Usbprint.sys provides a communication conduit by which higher-level drivers can control the printer. As is true for parallel printers, USB printers require a printer driver to render print jobs, and might also require a language monitor to manage high-level communication with the printer.

During the installation of a USB printer, the system-supplied INF file, Usbprint.inf, obtains Usbprint.sys from the local file Driver.cab. Because Driver.cab was installed with the operating system, the printer installer typically does not need the original installation media to install Usbprint.sys. For more information about Usbprint.inf, see [Printer Connected to a USB Port](printer-connected-to-a-usb-port.md). For more information about Driver.cab, see [Printer Installation and the Plug and Play Manager](printer-installation-and-the-plug-and-play-manager.md).

This section contains the following topic:

[Programming Considerations for USBPRINT](programming-considerations-for-usbprint.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Microsoft%20USB%20Printer%20Driver%20%28Usbprint.sys%29%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


