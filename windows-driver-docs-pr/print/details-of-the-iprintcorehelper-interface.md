---
title: Details of the IPrintCoreHelper Interface
author: windows-driver-content
description: Details of the IPrintCoreHelper Interface
ms.assetid: df736ca2-425e-4fc8-bdcb-bdbd5caa3e22
keywords:
- IPrintCoreHelper
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Details of the IPrintCoreHelper Interface


The **IPrintCoreHelper** interface is roughly based on the Pscript5 UI replacement interface. However, there are two ways in which the **IPrintCoreHelper** interface is fundamentally different from the original Pscript5 helper interface.

-   The **IPrintCoreHelper** interface does not have a **QuerySimulatedCapabilities** method. Instead, the **IPrintCoreHelper** interface maps simulated features to the regular list of features and options in a well-defined and recognizable way.

-   In the **IPrintCoreHelper** interface, the caller is asked to pass in a [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure instead of an [**OEMUIOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff559571) structure.

If you use the **IPrintCoreHelper** interface or the interfaces that inherit from it, you should consider the following points:

-   For the **IPrintCoreHelper** interface, the strings that are used for the **GetOption** or **SetOptions** methods are the GPD strings, not the GDL strings, so features and options that are defined in an \#ifdef GDL block are not available to the helper interface methods.

-   If a method on the **IPrintCoreHelper** interface (and its subinterfaces) has an OUT parameter and if the method fails, the OUT parameter retains the value it had when the method was called.

-   The memory model for the **IPrintCoreHelper** interface is slightly different from that of the previous Pscript5 interface. The caller is not responsible for cleaning up parameters that are passed back from the helper interface, and the caller does not need to allocate buffers to be passed in. The core driver handles these types of memory management.

This section provides the following topics:

[Details of the IPrintCoreHelperUni Interface](details-of-the-iprintcorehelperuni-interface.md)

[Details of the IPrintCoreHelperPS Interface](details-of-the-iprintcorehelperps-interface.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Details%20of%20the%20IPrintCoreHelper%20Interface%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


