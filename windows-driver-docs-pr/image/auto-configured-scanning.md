---
title: Auto-Configured Scanning
author: windows-driver-content
description: Auto-Configured Scanning
ms.assetid: 6904e216-3eb7-419f-a6ca-198defaeebe0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Auto-Configured Scanning


In Windows 7 and later, a WIA minidriver can support *auto-configured scanning*. A WIA scanner device that implements auto-configured scanning can automatically configure its device settings in response to the requirements of the scanning job, to changes in the device state, and to user actions. Without the ability to perform auto-configured scanning, a device must typically rely on a WIA application running on a desktop computer to configure the settings.

Auto-configured scanning provides opportunities for WIA scanner devices to perform device-specific optimizations that WIA applications might be unable to perform.

In addition, auto-configured scanning can relieve WIA applications of the responsibility for deciding how to configure the selected input source (flatbed, automatic document feeder, or film-scanning adapter) for a scanning operation. A device that supports push-scanning (also called device-initiated scanning) enables the user to initiate a scanning operation from the device instead of from the application's user interface. Typically, if a device performs push-scanning and has more than one input source, users expect to be able to select the input source for the scanning operation from the device. To avoid the task of configuring the selected input source, the application can use auto-configured scanning to offload this task to the device.

WIA 2.0 minidrivers can support auto-configured scanning for all types of WIA scanner devices, including scanners that connect to serial and parallel ports, scanners that connect to USB, SCSI, and IEEE 1394 buses, and network-connected Web Services scanners.

In Windows Vista, the Microsoft Web Services for Devices (WSD) scan class driver includes a custom driver extension to support auto-configured scanning. This driver provides auto-configured scanning only for networked WIA scanner devices that implement the Windows Device Protocol (WDP) 1.0 for scanners. In Windows 7, the WSD scan class driver implements auto-configured scanning as a standard feature, as described in the preceding paragraphs, instead of as a custom driver extension. For more information about the WSD scan class driver, see [WIA with Web Services for Devices](wia-with-web-services-for-devices.md). For more information about WDP for scanners, see [Web Services for Devices Scan Service Schema](https://msdn.microsoft.com/library/windows/hardware/ff547963).

### Examples

As an example of auto-configured scanning, a WIA scanner device might have both a flatbed and an automatic document feeder. If the user places a document in the feeder, the device detects the implicit selection of an input source, and it automatically scans from this source when the user presses the start-scan button. Based on the selected input source, the device can automatically configure itself to use scan settings that are appropriate for the source. In addition, the device might have a front panel through which the user can select settings that the device configures automatically, without intervention by the application.

A WIA scanner device with one input source (for example, a flatbed) can also use auto-configured scanning. The device can automatically configure its scan settings based on the requirements of a scanning job, or the device can apply the settings that the user selects from the device's front panel.

This section contains the following topics:

[Auto Item](auto-item.md)

[WIA Properties Supported by an Auto Item](wia-properties-supported-by-an-auto-item.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Auto-Configured%20Scanning%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


