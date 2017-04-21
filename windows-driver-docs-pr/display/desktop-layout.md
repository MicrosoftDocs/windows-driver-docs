---
title: Desktop Layout
description: Desktop Layout
ms.assetid: f1c074ec-2fce-4e46-ba0d-62e05ca8a9e7
keywords:
- connecting displays WDK Windows 7 display , CCD concepts, desktop layout
- connecting displays WDK Windows Server 2008 R2 display , CCD concepts, desktop layout
- configuring displays WDK Windows 7 display , CCD concepts, desktop layout
- configuring displays WDK Windows Server 2008 R2 display , CCD concepts, desktop layout
- CCD concepts WDK Windows 7 display , desktop layout
- CCD concepts WDK Windows Server 2008 R2 display , desktop layout
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Desktop Layout


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The caller uses the **position** member of the [**DISPLAYCONFIG\_SOURCE\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff553986) structure in a call to the [**SetDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569533) CCD function to control the arrangement of source surfaces on the desktop. The **position** member specifies the position in desktop coordinates of the upper-left corner of the source surface. The source surface that is positioned at (0, 0) is consider the primary surface. GDI has strict rules about how the source surfaces can be arranged in the desktop space. For example, GDI does not allow any gaps between source surfaces and no overlaps in source surfaces.

Although [**SetDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569533) attempts to rearrange sources surfaces to enforce these GDI layout rules, the caller should specify the layout of the sources surfaces. It is undefined how GDI will rearrange the sources surfaces to enforce its layout rules, and the resultant layout of sources surfaces might not be what the caller wanted to achieve.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Desktop%20Layout%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




