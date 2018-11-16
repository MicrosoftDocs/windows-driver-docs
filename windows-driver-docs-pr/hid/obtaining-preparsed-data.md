---
title: Obtaining Preparsed Data
description: Obtaining Preparsed Data
ms.assetid: 7a2bdbd1-a970-421f-bbaa-40fe589bb49a
keywords:
- collections WDK HID , preparsed data
- HID collections WDK , preparsed data
- preparsed data WDK HID
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining Preparsed Data





This section describes how user-mode applications and kernel-mode drivers obtain a HID collection's [preparsed data](preparsed-data.md), which is an opaque structure that describes a collection's HID reports.

### User-Mode Application

A user-mode application must obtain a collection's preparsed data before calling any of the [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865) that require the preparsed data. An application should retain access to a collection's preparsed data as long as it has an open file on the device.

After opening a file on a HID collection, an application calls [**HidD\_GetPreparsedData**](https://msdn.microsoft.com/library/windows/hardware/ff539679) to return a collection's preparsed data in a routine-allocated buffer.

Applications should call [**HidD\_FreePreparsedData**](https://msdn.microsoft.com/library/windows/hardware/ff538893) when the application no longer requires access to a collection.

### Kernel-Mode Driver

After a kernel-mode driver opens a HID collection, the driver obtains a collection's [preparsed data](preparsed-data.md) in the following way:

-   Obtains the length of the collection's preparsed data

-   Obtains the collection's preparsed data

To determine the length of the preparsed data, the driver uses an [**IOCTL\_HID\_GET\_COLLECTION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff541092) request. This request returns a [**HID\_COLLECTION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff539870) structure. The **DescriptorSize** member of this structure specifies the size, in bytes, of a collection's preparsed data. The driver must allocate a buffer from nonpaged pool of at least this size to hold the preparsed data.

After allocating the buffer for the preparsed data, the driver uses an [**IOCTL\_HID\_GET\_COLLECTION\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541089) request to obtain the preparsed data.

After obtaining the preparsed data, the driver can use it with the **HidP\_**<em>Xxx</em> HID support routines to obtain information about the capabilities of the HID collection and to extract control data from HID reports.

 

 




