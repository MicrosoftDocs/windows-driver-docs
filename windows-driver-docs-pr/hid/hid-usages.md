---
title: HID Usages
author: windows-driver-content
description: HID usages identify the intended use of HID controls and what the controls actually measure.
ms.assetid: 84fed314-3554-4291-b51c-734d874a4bab
keywords: ["Human Interface Devices WDK , usages", "HID WDK , usages", "interactive input devices WDK , usages", "input devices WDK , usages", "Human Interface Devices WDK , controls", "HID WDK , controls", "interactive input devices WDK , controls", "input devices WDK , controls", "controls WDK HID", "usage pages WDK HID", "usage IDs WDK HID", "extended usage WDK HID", "usage ranges WDK HID", "aliased usages WDK HID", "usage WDK HID"]
---

#  HID Usages


*HID usages* identify the intended use of HID controls and what the controls actually measure.

## <a href="" id="ddk-hid-usages-kg"></a>


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

For detailed information about industry standard HID usage, see the Universal Serial Bus (USB) specification *HID Usage Tables* that is located at the [USB Implementers Forum](https://go.microsoft.com/fwlink/?linkid=830142) website. (This resource may not be available in some languages and countries.)

### Usage Page

HID usages are organized into *usage pages* of related controls. A specific control usage is defined by its usage page, a [usage ID](#usage-id), a name, and a description. Examples of usage pages include Generic Desktop Controls, Game Controls, LEDs, Button, and so on. Examples of controls that are listed on the Generic Desktop Controls usage page include pointers, mouse and keyboard devices, joysticks, and so on. A usage page value is a 16-bit unsigned value.

### Usage ID

In the context of a usage page, a valid usage identifier, or *usage ID*, indicates a usage in a usage page. A usage ID of zero is reserved. A usage ID value is an unsigned 16-bit value.

### Extended Usage

An *extended usage* is a 32-bit value that specifies a 16-bit [usage page](#usage-page) value in the most-significant two bytes and a 16-bit [usage ID](#usage-id) in the least significant two bytes of the extended usage value.

### Usage Range

A *usage range* is an inclusive, consecutive range of [usage IDs](#usage-id), all of which are on the same [usage page](#usage-page). A usage range is specified by usage minimum and usage maximum items in a report descriptor.

### Aliased Usages

More than one usage can be specified for a [**link collection**](link-collections.md) or a HID control. For a given collection or control, a group of such usages are aliases of one another, and are referred to as *aliased usages*. Delimiter items are used to specify aliased usages. [Usage ranges](#usage-range) cannot be aliased.

For information about how aliased usages are specified in a top-level collection's capability arrays, see [Button Capability Arrays](button-capability-arrays.md) and [Value Capability Arrays](value-capability-arrays.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20%20HID%20Usages%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


