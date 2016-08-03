---
title: Collection Capability
author: windows-driver-content
description: Collection Capability
MS-HAID:
- 'hidclass\_85321b44-d36f-45c8-9567-b139e927098d.xml'
- 'hid.collection\_capability'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 228fab4f-ff90-43c5-bc68-26b29e8a7dd6
keywords: ["capabilities WDK HID collections", "summary capabilities WDK HID"]
---

# Collection Capability


## <a href="" id="ddk-collection-capability-kg"></a>


The capability of a collection is defined by its usage, reports, link collections, and controls. To obtain a summary of a collection's capability, a user-mode application or kernel-mode driver calls [**HidP\_GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff539715) to obtain a [**HIDP\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539697) structure. This structure contains the following information about a collection's [link collections](link-collections.md), [button capability arrays](button-capability-arrays.md), and [value capability arrays](value-capability-arrays.md):

-   The collection's [usage page](hid-usages.md#usage-page) and [usage ID](hid-usages.md#usage-id)

-   The size, in bytes, of the collection's input, output, and feature reports (see [Introduction to HID Concepts](introduction-to-hid-concepts.md))

-   The number of [**HIDP\_LINK\_COLLECTION\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff539764) structures in the collection's [link collection array](link-collections.md#ddk-link-collection-array-kg)

-   For each report type, the number of [**HIDP\_BUTTON\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539693) structures in the button capability array returned by [**HidP\_GetButtonCaps**](https://msdn.microsoft.com/library/windows/hardware/ff539707)

-   For each report type, the number of [**HIDP\_VALUE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff539832)structures in the value capability array returned by [**HidP\_GetValueCaps**](https://msdn.microsoft.com/library/windows/hardware/ff539754)

-   For each report type, the number of buttons and values supported by the collection, as specified by the **Number***Xxx***DataIndices** member.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Collection%20Capability%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


