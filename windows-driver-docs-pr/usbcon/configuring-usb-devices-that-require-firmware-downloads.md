---
Description: Firmware is internal to a device, and is independent of the operating system. However, firmware downloads can cause operating system errors.
title: Configuring a USB Device for Firmware Update
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Configuring a USB Device for Firmware Update


Firmware is internal to a device, and is independent of the operating system. However, firmware downloads can cause operating system errors.

-   In Windows XP, attaching your device to the system might cause multiple plug and unplug sounds, leading to poor end user experience.

-   Because firmware is downloaded every time the device starts, it might not function immediately after it has been plugged in, or after the operating system resumes from an S3 or S4 power state.

-   On a resume from S3 or S4, your device might cause the surprise removal dialog box to pop up, because most machines cut off power to self powered devices in S4 mode.

To avoid system errors:

-   Make sure that the device has two separate sets of vendor and device IDs.

    Devices that are capable of firmware updates, are enumerated twice by the system. When the device is detected by the system, it loads a preliminary driver by using the vendor and device ID. This driver facilitates the firmware download.

    After the firmware is loaded, the preliminary driver resets the bus causing the system to enumerate the device again. The new firmware gives a different set of vendor and device ID. During second enumeration, the system uses the new set of IDs and loads the main device driver.

-   Make sure that the vendor and device IDs are unique and specific to your product.

    If your device includes a programmable USB chip by a third party, the chip might identify itself by using a standard set of IDs. If the same chip is used with another device on the same system, there might be contention between the two devices for the same set of IDs, causing the operating system to malfunction.

## Related topics
[Building USB devices for Windows](building-usb-devices-for-windows.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Configuring%20a%20USB%20Device%20for%20Firmware%20Update%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


