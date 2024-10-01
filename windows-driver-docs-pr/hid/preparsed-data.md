---
title: Preparsed Data
description: Preparsed data is report descriptor data associated with a top-level collection.
keywords:
- parsed data WDK HID
- preparsed data WDK HID
ms.date: 09/18/2024
---

# Preparsed Data

Preparsed data is report descriptor data associated with a [top-level collection](top-level-collections.md). User-mode applications or kernel-mode drivers use preparsed data to extract information about specific HID controls without having to obtain and interpret a device's entire report descriptor. A user-mode application obtains a collection's preparsed data by using **[HidD_GetPreparsedData](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getpreparseddata)** and a kernel-mode driver uses an **[IOCTL_HID_GET_COLLECTION_DESCRIPTOR](/windows-hardware/drivers/ddi/hidclass/ni-hidclass-ioctl_hid_get_collection_descriptor)** request.

The following [HIDClass support routines](/windows-hardware/drivers/ddi/_hid) support extracting and setting button and value data:

- **[HidP_GetButtons](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)**
- **[HidP_SetButtons](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)**
- **[HidP_UnsetButtons](/windows-hardware/drivers/ddi/hidpi/#functionsfunctions)**
- **[HidP_GetUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevalue)**
- **[HidP_SetUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevalue)**
- **[HidP_GetScaledUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getscaledusagevalue)**
- **[HidP_SetScaledUsageValue](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setscaledusagevalue)**
- **[HidP_GetUsageValueArray](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagevaluearray)**
- **[HidP_SetUsageValueArray](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusagevaluearray)**
