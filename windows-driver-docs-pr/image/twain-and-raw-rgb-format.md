---
title: TWAIN and Raw RGB Format
description: TWAIN and Raw RGB Format
ms.assetid: 0de4a547-6c8e-4fbf-a7a3-7af440bf72f3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TWAIN and Raw RGB Format





When an application transfers an image whose format GUID is WiaImgFmt\_RAWRGB (defined in header file *wiadef.h*), the following properties on the image must contain the correct values for the image:

-   WIA\_IPA\_CHANNELS\_PER\_PIXEL

-   WIA\_IPA\_BITS\_PER\_CHANNEL

-   WIA\_IPA\_PIXELS\_PER\_LINE

-   WIA\_IPA\_NUMBER\_OF\_LINES

-   WIA\_IPS\_XRES

-   WIA\_IPS\_YRES

Furthermore, the WIA\_IPA\_DATATYPE property should be set to WIA\_DATA\_COLOR and the WIA\_IPA\_DEPTH property should be set to 24 or higher. For more information about these properties, see the Microsoft Windows SDK documentation.

Any data in the raw RGB format to be transferred must be:

-   Uncompressed

-   Arranged in RGB byte order

-   Aligned on DWORD boundaries

The data must be transferred with no image header. The **IWiaDataCallback::BandedDataCallback** method (described in the Windows SDK documentation) sends only the image bits.

The TWAIN compatibility layer (see [Support for TWAIN-Compatible Applications](support-for-twain-compatible-applications.md)) supports the WiaImgFmt\_RAWRGB format GUID. This enables TWAIN applications to transfer images with pixel depths greater than 32 bits, using a memory-callback transfer.

 

 




