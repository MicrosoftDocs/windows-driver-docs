---
title: Preparsed Data
author: windows-driver-content
description: Preparsed Data
ms.assetid: 50ac2877-4c45-4d55-b5cc-013486892fbf
keywords: ["parsed data WDK HID", "preparsed data WDK HID"]
---

# Preparsed Data


## <a href="" id="ddk-preparsed-data-kg"></a>


*Preparsed data* is report descriptor data associated with a [top-level collection](top-level-collections.md). User-mode applications or kernel-mode drivers use preparsed data to extract information about specific HID controls without having to obtain and interpret a device's entire report descriptor. A user-mode application obtains a collection's preparsed data by using [**HidD\_GetPreparsedData**](https://msdn.microsoft.com/library/windows/hardware/ff539679) and a kernel-mode driver uses an [**IOCTL\_HID\_GET\_COLLECTION\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541089) request.

The following [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865) support extracting and setting button and value data:

[**HidP\_GetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539708)

[**HidP\_SetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539779)

[**HidP\_UnsetButtons**](https://msdn.microsoft.com/library/windows/hardware/ff539812)

[**HidP\_GetUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539748)

[**HidP\_SetUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539797)

[**HidP\_GetScaledUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539729)

[**HidP\_SetScaledUsageValue**](https://msdn.microsoft.com/library/windows/hardware/ff539787)

[**HidP\_GetUsageValueArray**](https://msdn.microsoft.com/library/windows/hardware/ff539750)

[**HidP\_SetUsageValueArray**](https://msdn.microsoft.com/library/windows/hardware/ff539801)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Preparsed%20Data%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


