---
title: Obtaining Preparsed Data
description: Obtaining preparsed data
keywords:
- collections WDK HID , preparsed data
- HID collections WDK , preparsed data
- preparsed data WDK HID
ms.date: 01/11/2024
---

# Obtaining preparsed data

This section describes how user-mode applications and kernel-mode drivers obtain a HID collection's [preparsed data](preparsed-data.md), which is an opaque structure that describes a collection's HID reports.

## User-Mode Application

A user-mode application must obtain a collection's preparsed data before calling any of the [HIDClass support routines](/windows-hardware/drivers/ddi/_hid) that require the preparsed data. An application should retain access to a collection's preparsed data as long as it has an open file on the device.

After opening a file on a HID collection, an application calls **[HidD_GetPreparsedData](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_getpreparseddata)** to return a collection's preparsed data in a routine-allocated buffer.

Applications should call **[HidD_FreePreparsedData](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_freepreparseddata)** when the application no longer requires access to a collection.

## Kernel-Mode Driver

After a kernel-mode driver opens a HID collection, the driver obtains a collection's [preparsed data](preparsed-data.md) in the following way:

- Obtains the length of the collection's preparsed data

- Obtains the collection's preparsed data

To determine the length of the preparsed data, the driver uses an **[IOCTL_HID_GET_COLLECTION_INFORMATION](/windows-hardware/drivers/ddi/hidclass/ni-hidclass-ioctl_hid_get_collection_information)** request. This request returns a **[HID_COLLECTION_INFORMATION](/windows-hardware/drivers/ddi/hidclass/ns-hidclass-_hid_collection_information)** structure. The **DescriptorSize** member of this structure specifies the size, in bytes, of a collection's preparsed data. The driver must allocate a buffer from nonpaged pool of at least this size to hold the preparsed data.

After allocating the buffer for the preparsed data, the driver uses an **[IOCTL_HID_GET_COLLECTION_DESCRIPTOR](/windows-hardware/drivers/ddi/hidclass/ni-hidclass-ioctl_hid_get_collection_descriptor)** request to obtain the preparsed data.

After obtaining the preparsed data, the driver can use it with the **HidP_***Xxx* HID support routines to obtain information about the capabilities of the HID collection and to extract control data from HID reports.
