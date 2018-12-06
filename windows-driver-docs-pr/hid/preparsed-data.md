---
title: Preparsed Data
description: Preparsed Data
ms.assetid: 50ac2877-4c45-4d55-b5cc-013486892fbf
keywords:
- parsed data WDK HID
- preparsed data WDK HID
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Preparsed Data





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

 

 




