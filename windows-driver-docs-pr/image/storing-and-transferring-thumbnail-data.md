---
title: Storing and Transferring Thumbnail Data
description: Storing and Transferring Thumbnail Data
ms.assetid: 4c27f93f-859e-42e3-95ea-9bfd8d0329d6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storing and Transferring Thumbnail Data





WIA thumbnail information is controlled by three WIA properties: [**WIA\_IPC\_THUMBNAIL**](https://msdn.microsoft.com/library/windows/hardware/ff552550), [**WIA\_IPC\_THUMBNAIL\_WIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff552558), and [**WIA\_IPC\_THUMBNAIL\_HEIGHT**](https://msdn.microsoft.com/library/windows/hardware/ff552552). In Windows Me, and in Windows XP and later, the thumbnail data is 24-bits per pixel only.

<a href="" id="wia-ipc-thumbnail"></a>WIA\_IPC\_THUMBNAIL  
The property contains the thumbnail data in RGB format, with 24 bits per pixel, and aligned on 32-bit boundaries.

<a href="" id="wia-ipc-thumb-width"></a>WIA\_IPC\_THUMB\_WIDTH  
The property contains the thumbnail image width, in pixels.

<a href="" id="wia-ipc-thumbnail-height"></a>WIA\_IPC\_THUMBNAIL\_HEIGHT  
The property contains the thumbnail image height, in pixels.

An application reads the WIA\_IPC\_THUMB\_WIDTH and WIA\_IPC\_THUMB\_HEIGHT properties to create the property BITMAPINFOHEADER structure (described in the Microsoft Windows SDK documentation). The application then reads the WIA\_IPC\_THUMBNAIL property for the actual thumbnail data. The thumbnail data should be uncompressed, 24-bits per pixel data aligned on 32-bit boundaries.

 

 




