---
title: Storing and Transferring Thumbnail Data
author: windows-driver-content
description: Storing and Transferring Thumbnail Data
ms.assetid: 4c27f93f-859e-42e3-95ea-9bfd8d0329d6
---

# Storing and Transferring Thumbnail Data


## <a href="" id="ddk-storing-and-transferring-thumbnail-data-si"></a>


WIA thumbnail information is controlled by three WIA properties: [**WIA\_IPC\_THUMBNAIL**](https://msdn.microsoft.com/library/windows/hardware/ff552550), [**WIA\_IPC\_THUMBNAIL\_WIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff552558), and [**WIA\_IPC\_THUMBNAIL\_HEIGHT**](https://msdn.microsoft.com/library/windows/hardware/ff552552). In Windows Me, and in Windows XP and later, the thumbnail data is 24-bits per pixel only.

<a href="" id="wia-ipc-thumbnail"></a>WIA\_IPC\_THUMBNAIL  
The property contains the thumbnail data in RGB format, with 24 bits per pixel, and aligned on 32-bit boundaries.

<a href="" id="wia-ipc-thumb-width"></a>WIA\_IPC\_THUMB\_WIDTH  
The property contains the thumbnail image width, in pixels.

<a href="" id="wia-ipc-thumbnail-height"></a>WIA\_IPC\_THUMBNAIL\_HEIGHT  
The property contains the thumbnail image height, in pixels.

An application reads the WIA\_IPC\_THUMB\_WIDTH and WIA\_IPC\_THUMB\_HEIGHT properties to create the property BITMAPINFOHEADER structure (described in the Microsoft Windows SDK documentation). The application then reads the WIA\_IPC\_THUMBNAIL property for the actual thumbnail data. The thumbnail data should be uncompressed, 24-bits per pixel data aligned on 32-bit boundaries.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Storing%20and%20Transferring%20Thumbnail%20Data%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


