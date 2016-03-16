---
title: Framework I/O Target Object
description: Framework I/O Target Object
ms.assetid: 355a1818-88c9-4989-9141-8445f511f501
keywords: ["UMDF objects WDK I/O target objects", "framework objects WDK UMDF I/O target objects", "I/O target objects WDK UMDF", "IWDFIoTarget", "targets WDK UMDF"]
---

# Framework I/O Target Object


\[This topic applies to UMDF 1.*x*.\]

The framework I/O target object is exposed to drivers by the [IWDFIoTarget](https://msdn.microsoft.com/library/windows/hardware/ff559170) interface. It retrieves information about an I/O target, which typically represents a lower driver in the stack but can also represent another UMDF driver or the kernel-mode portion of the stack. The I/O target object provides UMDF drivers a way to send requests to another device.

UMDF drivers can also use the [IWDFIoTargetStateManagement](https://msdn.microsoft.com/library/windows/hardware/ff559198) interface to manage and monitor the state of an I/O target object.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20I/O%20Target%20Object%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




