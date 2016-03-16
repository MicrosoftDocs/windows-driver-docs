---
title: WDM Interface Restrictions
description: WDM Interface Restrictions
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 89f3793e-8561-4d8a-a01a-1ff7aecca64a
keywords: ["KMDF WDK WDM", "Kernel Mode Driver Framework WDK WDM", "WDM drivers WDK KMDF", "framework based drivers WDK KMDF WDM"]
---

# WDM Interface Restrictions


\[Applies to KMDF only\]

## <a href="" id="ddk-framework-compatibility-with-wdm-df"></a>


If your framework-based driver accesses WDM interfaces, you must be aware of the following restrictions:

-   Framework-based drivers must not use the **Tail.Overlay.DriverContext** member of the [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) structure, because the framework uses this member.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDM%20Interface%20Restrictions%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




