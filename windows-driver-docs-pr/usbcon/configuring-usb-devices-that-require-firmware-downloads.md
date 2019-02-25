---
Description: Firmware is internal to a device, and is independent of the operating system. However, firmware downloads can cause operating system errors.
title: Configuring a USB Device for Firmware Update
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring a USB Device for Firmware Update


Firmware is internal to a device and is independent of the operating system. However, firmware downloads can cause operating system errors.

-   In Windows XP, attaching your device to the system might cause multiple plug and unplug sounds, leading to a poor end user experience.

-   Because firmware is downloaded every time the device starts, it might not function immediately after it has been plugged in, or after the operating system resumes from an S3 or S4 power state.

-   On a resume from S3 or S4, your device might cause the surprise removal dialog box to pop up because most machines cut off power to self-powered devices in S4 mode.

To avoid system errors:

-   Make sure that the device has two separate sets of vendor and device IDs.

    Devices that are capable of firmware updates are enumerated twice by the system. When the device is detected by the system, it loads a preliminary driver by using the vendor and device ID. This driver facilitates the firmware download.

    After the firmware is loaded, the preliminary driver resets the bus causing the system to enumerate the device again. The new firmware gives a different set of vendor and device ID. During the second enumeration, the system uses the new set of IDs and loads the main device driver.

-   Make sure that the vendor and device IDs are unique and specific to your product.

    If your device includes a programmable USB chip by a third party, the chip might identify itself by using a standard set of IDs. If the same chip is used with another device on the same system, there might be contention between the two devices for the same set of IDs, causing the operating system to malfunction.

## Related topics
[Building USB devices for Windows](building-usb-devices-for-windows.md)  
