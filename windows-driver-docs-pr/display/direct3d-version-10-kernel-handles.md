---
title: Direct3D Version 10 Kernel Handles
description: Direct3D Version 10 Kernel Handles
ms.assetid: 48378f27-4c08-4931-9592-878a1a2b2556
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Direct3D Version 10 Kernel Handles


The Direct3D version 10 kernel handle life spans are typically controlled by the user-mode display driver explicitly. Such handles allow the user-mode display driver to manipulate allocations. Such handles can also allow the user-mode display driver to perform other interactions with the kernel (including interactions with the display miniport driver).

The following shows an example of a kernel handle for a resource:

```
// Strongly typed handle to identify a resource object to the driver: 
typedef struct D3D10DDI_HKMRESOURCE
{
    D3DKMT_HANDLE handle;
} D3D10DDI_HKMRESOURCE;
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Direct3D%20Version%2010%20Kernel%20Handles%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




