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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# COM in the Kernel


## <span id="com_in_the_kernel"></span><span id="COM_IN_THE_KERNEL"></span>


Audio port and miniport drivers export device driver interfaces (DDIs) that conform to the Component Object Model (COM). For background information about COM interfaces, see the COM section of the Microsoft Windows SDK documentation.

All COM interfaces inherit from the **IUnknown** interface, which has the methods **AddRef**, **QueryInterface**, and **Release**. Because these methods are common to all COM interfaces, the reference pages for the WDM audio driver interfaces do not explicitly describe them.

This section discusses the following topics:

[Function Tables for Miniport Drivers](function-tables-for-miniport-drivers.md)

[Creating Audio Driver Objects](creating-audio-driver-objects.md)

[Reference-Counting Conventions for COM Objects](reference-counting-conventions-for-com-objects.md)

 

 




