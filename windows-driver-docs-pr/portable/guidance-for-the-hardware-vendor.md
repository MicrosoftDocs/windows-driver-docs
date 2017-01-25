---
Description: Guidance for the Hardware Vendor
MS-HAID: 'wpddk.guidance\_for\_the\_hardware\_vendor'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Guidance for the Hardware Vendor
---

# Guidance for the Hardware Vendor


If you manufacture a portable device and require connectivity with Windows, you have the following options:

-   For devices with a non-class protocol, provide a WPD driver. For example, if your device uses a custom protocol over RS232 to communicate with the computer, you must provide a WPD driver so that WPD applications can access the device.
-   For portable music player devices, implement a class protocol such as MTP on the device. This will enable your device to be compatible with WPD, without the need to supply a driver (since Microsoft provides one).
-   For digital still cameras, implement a class protocol such as PTP/MTP. MTP offers enhancements over PTP, and is therefore the more optimal choice. However, for compatibility reasons, it is recommended that your MTP implementation be backward compatible with PTP.
-   For cellular phones and other multi-function devices, implement a class protocol, such as MTP, on the device.

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Guidance%20for%20the%20Hardware%20Vendor%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




