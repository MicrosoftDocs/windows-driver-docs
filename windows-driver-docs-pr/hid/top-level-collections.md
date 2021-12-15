---
title: Top-Level Collections
description: Top-Level Collections
keywords:
- top-level collections WDK HID
ms.date: 04/20/2017
---

# Top-Level Collections




A *Top Level Collection* is a grouping of functionality that targets a particular software consumer (or type of consumer) of the functionality. For example, a Top Level Collection may be described as Keyboard, Mouse, Consumer Control, Sensor, Display, etc. In the HID spec, these Top Level Collections are also referred to as *Application Collections*. The HID device describes the purpose of each Top Level Collection, in order to allow the consumers of HID functionality to identify Top Level Collections in which they might be interested. In Windows, the HID device setup class (HIDClass) generates a unique physical device object (PDO) for each Top Level Collection described by the Report Descriptor.
Microsoft defines a *top-level collection* as a [HID collection](hid-collections.md) that is not nested within another collection. An unnested collection is always a top-level collection, regardless of its HID type. In particular, a top-level collection does not have to be an **Application** collection, as defined by the USB HID Standard.

A report descriptor can include more than one top-level collection. The HID class driver enumerates the top-level collections of an input device and creates a physical device object (*PDO*) for each top-level collection. User-mode applications or kernel-mode drivers can access a top-level collection by opening its PDO and using the [HIDClass support routines](/windows-hardware/drivers/ddi/_hid/#hidclass-support-routines) and the [HID class driver IOCTLs](/windows-hardware/drivers/ddi/_hid/#hid-class-driver-ioctls).

The internal structure and capability of a top-level collection is described by the following:

-   A [**HIDP\_CAPS**](/windows-hardware/drivers/ddi/hidpi/ns-hidpi-_hidp_caps) structure summarizes a top-level [collection's capability](collection-capability.md).

-   [Link collections](link-collections.md) describe the organization of the nested subcollections contained within a top-level collection.

-   [Button capability arrays](button-capability-arrays.md) and [value capability arrays](value-capability-arrays.md) describe the capability of the controls supported by the top-level collection.

