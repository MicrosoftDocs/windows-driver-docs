---
title: Preparsed Data
description: Preparsed Data
keywords:
- parsed data WDK HID
- preparsed data WDK HID
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Preparsed Data





*Preparsed data* is report descriptor data associated with a [top-level collection](top-level-collections.md). User-mode applications or kernel-mode drivers use preparsed data to extract information about specific HID controls without having to obtain and interpret a device's entire report descriptor. A user-mode application obtains a collection's preparsed data by using [**HidD\_GetPreparsedData**](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getpreparseddata) and a kernel-mode driver uses an [**IOCTL\_HID\_GET\_COLLECTION\_DESCRIPTOR**](/windows-hardware/drivers/ddi/hidclass/ni-hidclass-ioctl_hid_get_collection_descriptor) request.

The following [HIDClass support routines](/windows-hardware/drivers/ddi/_hid) support extracting and setting button and value data:

[**HidP\_GetButtons**](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)

[**HidP\_SetButtons**](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)

[**HidP\_UnsetButtons**](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)

[**HidP\_GetUsageValue**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevalue)

[**HidP\_SetUsageValue**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevalue)

[**HidP\_GetScaledUsageValue**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getscaledusagevalue)

[**HidP\_SetScaledUsageValue**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setscaledusagevalue)

[**HidP\_GetUsageValueArray**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevaluearray)

[**HidP\_SetUsageValueArray**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevaluearray)

