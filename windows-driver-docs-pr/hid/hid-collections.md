---
title: HID Collections
author: windows-driver-content
description: A HID collection is a meaningful grouping of HID controls and their respective HID usages.
ms.assetid: 2d3efb38-4eba-43db-8cff-9fac30209952
keywords: ["Human Interface Devices WDK , collections", "HID WDK , collections", "interactive input devices WDK , collections", "input devices WDK , collections", "collections WDK HID", "collections WDK HID , about HID collections", "subcollections WDK HID", "Human Interface Devices WDK , controls", "HID WDK , controls", "interactive input devices WDK , controls", "input devices WDK , controls", "controls WDK HID", "HID collections WDK", "HID collections WDK , about HID collections"]
---

# HID Collections


A *HID collection* is a meaningful grouping of HID controls and their respective [HID usages](hid-usages.md).

Controls should be grouped together if they are logically related or are functionally dependent on one another. For instance, a SHIFT key and a letter key on a keyboard should not belong to separate collections. Collections can have nested *subcollections*, also referred to as [link collections](link-collections.md). Report descriptors define one or more [top-level collections](top-level-collections.md), and the report items, associated with each collection, define one or more HID reports.

## <a href="" id="ddk-hid-collections-kg"></a>


Windows extends the concept of a HID collection to include the following:

[Top-level collections](top-level-collections.md)

[Top-level collections opened by Windows for system use](top-level-collections-opened-by-windows-for-system-use.md)

[Preparsed data](preparsed-data.md)

[Link collections](link-collections.md)

[Collection capability](collection-capability.md)

[Button capability arrays](button-capability-arrays.md)

[Value capability arrays](value-capability-arrays.md)

[Data indices](data-indices.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20HID%20Collections%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


