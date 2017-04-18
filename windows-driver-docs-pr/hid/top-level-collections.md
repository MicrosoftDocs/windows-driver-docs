---
title: Top-Level Collections
author: windows-driver-content
description: Top-Level Collections
ms.assetid: dcbee8e3-d03a-45c8-92e4-0897b9f55177
keywords: ["top-level collections WDK HID"]
---

# Top-Level Collections


## <a href="" id="ddk-top-level-collections-kg"></a>

A *Top Level Collection* is a grouping of functionality that targets a particular software consumer (or type of consumer) of the functionality. For example, a Top Level Collection may be described as Keyboard, Mouse, Consumer Control, Sensor, Display, etc. In the HID spec, these Top Level Collections are also referred to as *Application Collections*. The HID device describes the purpose of each Top Level Collection, in order to allow the consumers of HID functionality to identify Top Level Collections in which they might be interested. In Windows, the HID device setup class (HIDClass) generates a unique physical device object (PDO) for each Top Level Collection described by the Report Descriptor.
Microsoft defines a *top-level collection* as a [HID collection](hid-collections.md) that is not nested within another collection. An unnested collection is always a top-level collection, regardless of its HID type. In particular, a top-level collection does not have to be an **Application** collection, as defined by the USB HID Standard.

A report descriptor can include more than one top-level collection. The HID class driver enumerates the top-level collections of an input device and creates a physical device object ([*PDO*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdo)) for each top-level collection. User-mode applications or kernel-mode drivers can access a top-level collection by opening its PDO and using the [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865) and the [HID class driver IOCTLs](https://msdn.microsoft.com/library/windows/hardware/ff539849).

The internal structure and capability of a top-level collection is described by the following:

-   A [**HIDP\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539697) structure summarizes a top-level [collection's capability](collection-capability.md).

-   [Link collections](link-collections.md) describe the organization of the nested subcollections contained within a top-level collection.

-   [Button capability arrays](button-capability-arrays.md) and [value capability arrays](value-capability-arrays.md) describe the capability of the controls supported by the top-level collection.

 



--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Top-Level%20Collections%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


