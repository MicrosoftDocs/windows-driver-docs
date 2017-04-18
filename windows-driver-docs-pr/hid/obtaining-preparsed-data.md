---
title: Obtaining Preparsed Data
author: windows-driver-content
description: Obtaining Preparsed Data
ms.assetid: 7a2bdbd1-a970-421f-bbaa-40fe589bb49a
keywords: ["collections WDK HID , preparsed data", "HID collections WDK , preparsed data", "preparsed data WDK HID"]
---

# Obtaining Preparsed Data


## <a href="" id="ddk-obtaining-preparsed-data-kg"></a>


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

After obtaining the preparsed data, the driver can use it with the **HidP\_***Xxx* HID support routines to obtain information about the capabilities of the HID collection and to extract control data from HID reports.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Obtaining%20Preparsed%20Data%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


