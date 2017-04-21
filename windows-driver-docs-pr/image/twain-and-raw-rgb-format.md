---
title: TWAIN and Raw RGB Format
author: windows-driver-content
description: TWAIN and Raw RGB Format
ms.assetid: 0de4a547-6c8e-4fbf-a7a3-7af440bf72f3
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# TWAIN and Raw RGB Format


## <a href="" id="ddk-twain-and-raw-rgb-format-si"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20TWAIN%20and%20Raw%20RGB%20Format%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


