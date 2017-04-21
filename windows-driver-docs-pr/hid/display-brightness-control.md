---
title: Display brightness control
author: windows-driver-content
description: Allows keyboards (external or embedded on laptops), to control a laptop’s or tablet’s screen brightness through HID.
ms.assetid: B22BA244-C5C6-4A50-AFE6-4E773194F18C
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Display brightness control


Starting with Windows 8, a standardized solution has been added to allow keyboards (external or embedded on laptops), to control a laptop’s or tablet’s screen brightness through HID.

This solution is described in the HID committee's recently approved [HID Review Request 41](http://www.usb.org/developers/hidpage#approved-usage-table-review-requests).

## Architecture and overview


Windows 8 provides support for screen brightness increase/decrease as part of the consumer controls top level collection. Windows 8 supports the HID usages listed in the following table:

| Usage ID | Usage Name           | Usage Type               |
|----------|----------------------|--------------------------|
| 0x006F   | Brightness Increment | Re-trigger Control (RTC) |
| 0x0070   | Brightness Decrement | Re-trigger Control (RTC) |

 

**Note**  These HID usages operate only on mobile systems (battery powered) and require Windows 8.

 

## Sample report descriptor


The following section provides sample report descriptors that PC Manufacturers must leverage. Please note that if the Top Level Collection is part of a report descriptor that already has another Top Level Collection, a Report ID MUST be included (not shown in samples below).

``` syntax
Usage Page (Consumer)
Usage (Consumer Control)
Collection (Application)
   Logical Minimum (0x00)
   Logical Maximum (0x3FF)
   Usage Minimum (0x00)
   Usage Maximum (0x3FF)
   Report Size (16)
   Report Count (1)
   Input (Data, Array, Absolute)
End Collection
```

*Important Notes*

-   When a user presses a key, an input report is generated to identify the key. When the key is released an input report with usage value=0 is issued.
-   Only one usage is active and sent at a time. Consumer controls do not allow multiple buttons to be pressed simultaneously. When a new usage is sent, it is assumed that the usage for the previous key is released.
-   Brightness up/down are retriggering keys and their rate of repeat is handled by Windows. Hardware should not keep resending the usage when these keys are kept depressed by user. Hardware should only send an input report when button is pressed down and another when the key is released.

## Troubleshooting common errors


Tip \#1: Brightness increment/decrement HID usages only operate only on Mobile systems (battery powered) and require Windows 8.

Tip \#2: If the system is attached to an external monitor, the brightness increment/decrement will not function as legacy monitor transports do not support the ability to channel HID messages to them / from them.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Display%20brightness%20control%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


