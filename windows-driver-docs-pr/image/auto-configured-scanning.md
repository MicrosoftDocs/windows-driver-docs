---
title: Auto-Configured Scanning
description: Auto-Configured Scanning
ms.assetid: 6904e216-3eb7-419f-a6ca-198defaeebe0
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




