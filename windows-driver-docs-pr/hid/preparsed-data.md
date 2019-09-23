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





*Preparsed data* is report descriptor data associated with a [top-level collection](top-level-collections.md). User-mode applications or kernel-mode drivers use preparsed data to extract information about specific HID controls without having to obtain and interpret a device's entire report descriptor. A user-mode application obtains a collection's preparsed data by using [**HidD\_GetPreparsedData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidsdi/nf-hidsdi-hidd_getpreparseddata) and a kernel-mode driver uses an [**IOCTL\_HID\_GET\_COLLECTION\_DESCRIPTOR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidclass/ni-hidclass-ioctl_hid_get_collection_descriptor) request.

The following [HIDClass support routines](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index) support extracting and setting button and value data:

[**HidP\_GetButtons**](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros)

[**HidP\_SetButtons**](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros)

[**HidP\_UnsetButtons**](https://docs.microsoft.com/windows-hardware/drivers/hid/hdpi-h-macros)

[**HidP\_GetUsageValue**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidpi/nf-hidpi-hidp_getusagevalue)

[**HidP\_SetUsageValue**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidpi/nf-hidpi-hidp_setusagevalue)

[**HidP\_GetScaledUsageValue**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidpi/nf-hidpi-hidp_getscaledusagevalue)

[**HidP\_SetScaledUsageValue**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidpi/nf-hidpi-hidp_setscaledusagevalue)

[**HidP\_GetUsageValueArray**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidpi/nf-hidpi-hidp_getusagevaluearray)

[**HidP\_SetUsageValueArray**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hidpi/nf-hidpi-hidp_setusagevaluearray)

 

 




