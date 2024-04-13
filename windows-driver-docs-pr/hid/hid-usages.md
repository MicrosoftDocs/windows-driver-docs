---
title: HID Usages
description: HID usages identify the intended use of HID controls and what the controls actually measure.
keywords:
- Human Interface Devices WDK , usages
- HID WDK , usages
- interactive input devices WDK , usages
- input devices WDK , usages
- Human Interface Devices WDK , controls
- HID WDK , controls
- interactive input devices WDK , controls
- input devices WDK , controls
- controls WDK HID
- usage pages WDK HID
- usage IDs WDK HID
- extended usage WDK HID
- usage ranges WDK HID
- aliased usages WDK HID
- usage WDK HID
ms.date: 04/20/2017
---

#  HID Usages


*HID usages* identify the intended use of HID controls and what the controls actually measure.




The following concepts and terminology are used throughout the HID documentation in the WDK:

[Usage Page](#usage-page)

[Usage ID](#usage-id)

[Extended Usage](#extended-usage)

[Usage Range](#usage-range)

[Aliased Usages](#aliased-usages)

For specific examples of usages that Windows components access, see [Top-Level Collections Opened by Windows for System Use](top-level-collections-opened-by-windows-for-system-use.md).

For more information about how to determine the usages that a HIDClass device supports, see:

[Collection Capability](collection-capability.md)

[Button Capability Arrays](button-capability-arrays.md)

[Value Capability Arrays](value-capability-arrays.md)

[Interpreting HID Reports](interpreting-hid-reports.md)

For detailed information about industry standard HID usage, see the Universal Serial Bus (USB) specification **HID Usage Tables** that is located at the [USB Implementers Forum](https://www.usb.org/hid) website.

### Usage Page

HID usages are organized into *usage pages* of related controls. A specific control usage is defined by its usage page, a [usage ID](#usage-id), a name, and a description. A usage page value is a 16-bit unsigned value.

Examples of usage pages include:

| Page ID | Page Name                | *hidusage.h* constant  |
|:-------:|--------------------------|------------------------|
| 0x01    | Generic Desktop Controls | HID_USAGE_PAGE_GENERIC |
| 0x05    | Game Controls            | HID_USAGE_PAGE_GAME    |
| 0x08    | LEDs                     | HID_USAGE_PAGE_LED     |
| 0x09    | Button                   | HID_USAGE_PAGE_BUTTON  |

### Usage ID

In the context of a usage page, a valid usage identifier, or *usage ID*, indicates a usage in a usage page. A usage ID of zero is reserved. A usage ID value is an unsigned 16-bit value.

Examples of controls that are listed on the **Generic Desktop Controls** usage page:

| Usage ID | Usage Name            | *hidusage.h* constant                    |
|:--------:|-----------------------|------------------------------------------|
| 0x01     | Pointer               | HID_USAGE_GENERIC_POINTER                |
| 0x02     | Mouse                 | HID_USAGE_GENERIC_MOUSE                  |
| 0x04     | Joystick              | HID_USAGE_GENERIC_JOYSTICK               |
| 0x05     | Game Pad              | HID_USAGE_GENERIC_GAMEPAD                |
| 0x06     | Keyboard              | HID_USAGE_GENERIC_KEYBOARD               |
| 0x07     | Keypad                | HID_USAGE_GENERIC_KEYPAD                 |
| 0x08     | Multi-axis Controller | HID_USAGE_GENERIC_MULTI_AXIS_CONTROLLER  |

### Extended Usage

An *extended usage* is a 32-bit value that specifies a 16-bit [usage page](#usage-page) value in the most-significant two bytes and a 16-bit [usage ID](#usage-id) in the least significant two bytes of the extended usage value.

### Usage Range

A *usage range* is an inclusive, consecutive range of [usage IDs](#usage-id), all of which are on the same [usage page](#usage-page). A usage range is specified by usage minimum and usage maximum items in a report descriptor.

### Aliased Usages

More than one usage can be specified for a [**link collection**](link-collections.md) or a HID control. For a given collection or control, a group of such usages are aliases of one another, and are referred to as *aliased usages*. Delimiter items are used to specify aliased usages. [Usage ranges](#usage-range) cannot be aliased.

For information about how aliased usages are specified in a top-level collection's capability arrays, see [Button Capability Arrays](button-capability-arrays.md) and [Value Capability Arrays](value-capability-arrays.md).

 

 




