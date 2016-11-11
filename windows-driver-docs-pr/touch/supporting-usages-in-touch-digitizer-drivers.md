---
title: Supporting Usages in Touch Digitizer Drivers (Windows 7)
description: Supporting Usages in Touch Digitizer Drivers (Windows 7)
ms.assetid: 5e7e96a3-abe7-4df0-88db-a73d13e51906
keywords: ["Windows Touch WDK , touch digitizer driver", "touch digitizer driver WDK Touch", "digitizer driver WDK Touch"]
---

# Supporting Usages in Touch Digitizer Drivers (Windows 7)


In the context of Windows Touch, *touch* refers to support of a single trackable contact point. This topic outlines required and optional HID usages for a touch digitizer driver. If your digitizer device supports more than one contact point, see [Supporting Usages in Multi-touch Digitizer Drivers](supporting-usages-in-multitouch-digitizer-drivers.md).

Usage identifier values are defined in the [HID Usage Tables](http://www.usb.org/developers/hidpage/Hut1_12v2.pdf).

### <span id="required_hid_usages"></span><span id="REQUIRED_HID_USAGES"></span> Required HID Usages

For Windows 7, a touch digitizer must appear through HID as a touch screen (page 0x0D, usage 0x04).

The following usages are required:

-   X (page 0x01, usage 0x30) and Y (page 0x01, usage 0x31)

    Report x and y position location.

-   Tip switch (page 0x0D, usage 0x42)

    Use the tip switch to indicate finger contact and liftoff from the digitizer surface, similar to how a pen reports contact with the digitizer.

-   In-range (page 0x0D, usage 0x32)

    If the device supports z-axis detection, it reports in-range when the transducer is within the region where digitizing is possible. If the device does not support z-axis detection, the driver should set in-range and tip switch when a finger comes in contact with the digitizer.

    Versions of Windows earlier than Windows 7 have different guidelines for how touch digitizer drivers should handle in-range reporting.

### <span id="optional_hid_usages"></span><span id="OPTIONAL_HID_USAGES"></span> Optional HID Usages

The following usages are optional, but you should implement them if the digitizer hardware supports them. These usages were added to the USB HID Usage Tables in the Windows Vista timeframe.

-   Confidence (page 0x0D, usage 0x47)

    Confidence is a suggestion from the device about whether the touch contact was an intended or accidental touch. Your device should reject accidental touches as thoroughly as it can and report that information by using the confidence usage. The operating system uses confidence to help improve accidental touch rejection. In addition to the confidence value, Windows 7 applies additional heuristics to the touch input stream to improve accidental touch rejection. If your device does not report confidence, it is completely up to your device to provide accidental touch rejection.

-   Width and height (page 0x0D, usages 0x48 and 0x49)

    The width and height usages represent the width and height of the touch contact. Width and height are also exposed to application developers through the [Windows Touch platform](http://go.microsoft.com/fwlink/p/?linkid=155047).

-   Pressure (page 0x0D, usage 0x30)

    Pressure is a measure of the force that the finger exerts against the digitizer surface.

For a sample touch descriptor, see [Sample Report Descriptor for a Touch Digitizer Device](sample-report-descriptor-for-a-touch-digitizer-device.md).

 

 




