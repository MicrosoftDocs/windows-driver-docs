---
Description: Guidance for the Hardware Vendor
title: Guidance for the Hardware Vendor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Guidance for the Hardware Vendor


If you manufacture a portable device and require connectivity with Windows, you have the following options:

-   For devices with a non-class protocol, provide a WPD driver. For example, if your device uses a custom protocol over RS232 to communicate with the computer, you must provide a WPD driver so that WPD applications can access the device.
-   For portable music player devices, implement a class protocol such as MTP on the device. This will enable your device to be compatible with WPD, without the need to supply a driver (since Microsoft provides one).
-   For digital still cameras, implement a class protocol such as PTP/MTP. MTP offers enhancements over PTP, and is therefore the more optimal choice. However, for compatibility reasons, it is recommended that your MTP implementation be backward compatible with PTP.
-   For cellular phones and other multi-function devices, implement a class protocol, such as MTP, on the device.

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 





