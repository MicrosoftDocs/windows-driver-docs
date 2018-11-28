---
title: Display brightness control
description: Allows keyboards (external or embedded on laptops), to control a laptop’s or tablet’s screen brightness through HID.
ms.assetid: B22BA244-C5C6-4A50-AFE6-4E773194F18C
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




