---
title: UMDF Objects and Interfaces
description: UMDF Objects and Interfaces
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: da816fef-a24f-4456-9d4a-36f291afe8b5
keywords: ["User Mode Driver Framework WDK objects", "user mode drivers WDK UMDF objects", "objects WDK UMDF", "UMDF objects WDK", "interfaces WDK UMDF", "framework objects WDK UMDF"]
---

# UMDF Objects and Interfaces


\[This topic applies to UMDF 1.*x*.\]

The User-Mode Driver Framework (UMDF) is composed of a set of cooperating objects. The UMDF creates and manages a series of objects exposed to the user-mode device driver. Some of theses objects are created by the UMDF in response to application-triggered actions, such as an I/O request, while other UMDF objects are created when the driver calls UMDF interface methods. For example, to create an I/O queue object, the driver calls the [**IWDFDevice::CreateIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff557020) method.

The following topics describe the core framework objects, the subset of the Component Object Model (COM) on which they are based, and the UMDF DDI programming model:

-   [Framework Objects](framework-objects.md)
-   [Framework Object Hierarchy](framework-object-hierarchy.md)
-   [UMDF Based on COM Subset](umdf-based-on-com-subset.md)
-   [UMDF DDI Programming Model](umdf-ddi-programming-model.md)
-   [Managing the Lifetime of Objects](managing-the-lifetime-of-objects.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20UMDF%20Objects%20and%20Interfaces%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




