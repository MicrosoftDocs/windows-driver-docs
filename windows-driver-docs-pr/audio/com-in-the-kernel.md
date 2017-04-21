---
title: COM in the Kernel
description: COM in the Kernel
ms.assetid: 2ce13ef1-9868-4f6d-9c42-b71f9e3d5615
keywords:
- audio miniport drivers WDK , COM
- miniport drivers WDK audio , COM
- COM interfaces WDK audio
- IUnknown interface
- port class drivers WDK audio
- PortCls WDK audio , COM
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# COM in the Kernel


## <span id="com_in_the_kernel"></span><span id="COM_IN_THE_KERNEL"></span>


Audio port and miniport drivers export device driver interfaces (DDIs) that conform to the Component Object Model (COM). For background information about COM interfaces, see the COM section of the Microsoft Windows SDK documentation.

All COM interfaces inherit from the **IUnknown** interface, which has the methods **AddRef**, **QueryInterface**, and **Release**. Because these methods are common to all COM interfaces, the reference pages for the WDM audio driver interfaces do not explicitly describe them.

This section discusses the following topics:

[Function Tables for Miniport Drivers](function-tables-for-miniport-drivers.md)

[Creating Audio Driver Objects](creating-audio-driver-objects.md)

[Reference-Counting Conventions for COM Objects](reference-counting-conventions-for-com-objects.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20COM%20in%20the%20Kernel%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


