---
title: Details of the IPrintCoreHelper Interface
description: Details of the IPrintCoreHelper Interface
ms.assetid: df736ca2-425e-4fc8-bdcb-bdbd5caa3e22
keywords:
- IPrintCoreHelper
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




