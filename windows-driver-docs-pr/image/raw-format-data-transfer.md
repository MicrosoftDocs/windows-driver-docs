---
title: RAW Format Data Transfer
description: RAW Format Data Transfer
ms.assetid: 8541b5ce-fd55-47b0-9687-162fb2b4e6aa
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# RAW Format Data Transfer

WIA supports the RAW format for data transfers. The advantage of the RAW format for WIA transfers is that it supports the full capabilities of your scan head.

The [**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property can be set to the GUID symbolic name for RAW format, **WiaImgFmt\_RAW**.

To add support for RAW format data transfers, a scanner driver must supply all of the standard [WIA scanner properties](properties-for-wia-scanner-minidrivers.md). The standard scanner properties include those for the picture extent, resolution, and channels per pixel. Your driver must also supply the number of bits per channel in the [**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551641) property.

The RAW format is *not* intended to be a file format; it is only part of the data transmission. Imaging applications convert raw data to a standard imaging file format. The [**WIA\_IPA\_FILENAME\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff551549) property must be set to an empty string (meaning "" and not **NULL**, as **NULL** can be a problem for some applications).

The scan lines must be DWORD-aligned. A scan line might need to be padded at the end so that its length is a multiple of 4 bytes. Pixels within each scan line must be packed. Image data can be compressed or uncompressed.

**Note**   For uncompressed image data, the data must be in packed pixel format; planar scans should be converted by mini-drivers to packed pixel format.

This section provides additional information on the following topics:

[WIA RAW Data Header](wia-raw-data-header.md)

[Property Validation for RAW Format Transfers](property-validation-for-raw-format-transfers.md)
