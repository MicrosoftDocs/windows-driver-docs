---
title: Why a UMDF Driver Consumes Excessive Memory
description: Describes how to use Wudfext.dll to determine why a UMDF version 1 driver consumes an excessive amount of memory.
ms.assetid: 01316c4e-24e8-467c-af52-900b3fe042db
keywords:
- debugging scenarios WDK UMDF , UMDF driver consumes excessive memory
- UMDF WDK , debugging scenarios, UMDF driver consumes excessive memory
- UMDF WDK , UMDF driver consumes excessive memory
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining Why a UMDF Driver Consumes an Excessive Amount of Memory

[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

This topic describes how you can use the Wudfext.dll debugger extensions in conjunction with a User-Mode Driver Framework (UMDF) version 1 driver to determine why a UMDF driver consumes an excessive amount of memory.

Starting with UMDF version 2, you should instead use the Wdfkd.dll debugger extensions. For more info, see [Windows Driver Framework Extensions (Wdfkd.dll)](https://msdn.microsoft.com/library/windows/hardware/ff551876).

To investigate memory usage, use the following steps:

1.  View the outstanding object in the object tree by using the **!wudfext.wudfobject** UMDF debugger extension.

    The **!wudfext.wudfobject** extension displays information about a WDF object, which includes its parent and child relationships. If you set bit 0 of the *Flags* parameter to 1 (0x01), **!wudfext.wudfobject** performs a recursive dump of the object tree that is rooted at the object that you passed. To view the complete object tree, use the following example command:

    **!wudfext.wudfobject &lt;IWDFDriver\*&gt; 1**

2.  Determine if you see more outstanding objects than you expect.

    Your driver might eventually leak these objects (for more information about leaking WDF objects, see [Determining If a Driver Leaks Framework Objects](determining-if-a-driver-leaks-framework-objects.md)).

    These objects might be in the object tree and would therefore eventually be freed. However, they are being accumulated unnecessarily. These objects might require:

    -   Corrections to their parent objects.
    -   Explicit deletion by using the [**IWDFObject::DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) method.

 

 





