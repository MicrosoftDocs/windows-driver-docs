---
title: Determining Why a UMDF Driver Consumes an Excessive Amount of Memory
description: This topic describes how you can use the Wudfext.dll debugger extensions in conjunction with a User Mode Driver Framework (UMDF) version 1 driver to determine why a UMDF driver consumes an excessive amount of memory.
ms.assetid: 01316c4e-24e8-467c-af52-900b3fe042db
keywords: ["debugging scenarios WDK UMDF UMDF driver consumes excessive memory", "UMDF WDK debugging scenarios UMDF driver consumes excessive memory", "UMDF WDK UMDF driver consumes excessive memory"]
---

# Determining Why a UMDF Driver Consumes an Excessive Amount of Memory


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Determining%20Why%20a%20UMDF%20Driver%20Consumes%20an%20Excessive%20Amount%20of%20Memory%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




