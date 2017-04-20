---
title: RAW Format Data Transfer
author: windows-driver-content
description: RAW Format Data Transfer
ms.assetid: 8541b5ce-fd55-47b0-9687-162fb2b4e6aa
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# RAW Format Data Transfer


## <a href="" id="ddk-raw-format-data-transfer-si"></a>


Beginning with Windows Vista, WIA supports the RAW format for data transfers. The advantage of the RAW format for WIA transfers is that it supports the full capabilities of your scan head.

The [**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property can be set to the GUID symbolic name for RAW format, **WiaImgFmt\_RAW**.

```

```

To add support for RAW format data transfers, a scanner driver must supply all of the standard [WIA scanner properties](properties-for-wia-scanner-minidrivers.md). The standard scanner properties include those for the picture extent, resolution, and channels per pixel. Your driver must also supply the number of bits per channel in the [**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551641) property.

The RAW format is *not* intended to be a file format; it is only part of the data transmission. Imaging applications convert raw data to a standard imaging file format. The [**WIA\_IPA\_FILENAME\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff551549) property must be set to an empty string (meaning "" and not **NULL**, as **NULL** can be a problem for some applications).

The scan lines must be DWORD-aligned. A scan line might need to be padded at the end so that its length is a multiple of 4 bytes. Pixels within each scan line must be packed. Image data can be compressed or uncompressed.

**Note**   For uncompressed image data, the data must be in packed pixel format; planar scans should be converted by mini-drivers to packed pixel format.

 

This section provides additional information on the following topics:

[WIA RAW Data Header](wia-raw-data-header.md)

[Property Validation for RAW Format Transfers](property-validation-for-raw-format-transfers.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20RAW%20Format%20Data%20Transfer%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


