---
title: Top-Level Collections
description: A top-level collection is a grouping of functionality that targets a particular software consumer of the functionality.
ms.date: 06/27/2024
keywords:
- top-level collections WDK HID
ms.topic: concept-article
---

# Top-level collections

A *top-level collection* is a grouping of functionality that targets a particular software consumer (or type of consumer) of the functionality. For example, a top-level collection can be described as keyboard, mouse, consumer control, sensor, display, and so on. In the HID spec, these top-level collections are also referred to as *application collections*. The HID device describes the purpose of each top-level collection, allowing the consumers of HID functionality to identify top-level collections in which they're interested. In Windows, the HID device setup class (HIDClass) generates a unique physical device object (PDO) for each top-level collection described by the report descriptor.
Microsoft defines a *top-level collection* as a [HID collection](hid-collections.md) that isn't nested within another collection. An unnested collection is always a top-level collection, regardless of its HID type. In particular, a top-level collection doesn't have to be an application collection, as defined by the USB HID Standard.

A report descriptor can include more than one top-level collection. The HID class driver enumerates the top-level collections of an input device and creates a physical device object (*PDO*) for each top-level collection. User-mode applications or kernel-mode drivers can access a top-level collection by opening its PDO and using the [HIDClass support routines](/windows-hardware/drivers/ddi/_hid/#hidclass-support-routines) and the [HID class driver IOCTLs](/windows-hardware/drivers/ddi/_hid/#hid-class-driver-ioctls).

The following list describes the internal structure and capability of a top-level collection:

- A [**HIDP_CAPS**](/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_hidp_caps) structure summarizes a [top-level collection's capability](collection-capability.md).
- [Link collections](link-collections.md) describe the organization of the nested collections contained within a top-level collection.
- [Button capability arrays](button-capability-arrays.md) and [value capability arrays](value-capability-arrays.md) describe the capability of the controls supported by the top-level collection.
