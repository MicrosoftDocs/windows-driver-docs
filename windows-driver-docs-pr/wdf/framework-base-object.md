---
title: Framework Base Object
description: Framework Base Object
ms.assetid: 9d400192-faf0-4d8f-849b-6b955105e21a
keywords: ["UMDF objects WDK , base objects", "framework objects WDK UMDF , base objects", "base objects WDK UMDF", "IWDFObject"]
---

# Framework Base Object


\[This topic applies to UMDF 1.*x*.\]

The framework base object is exposed to drivers by the [IWDFObject](https://msdn.microsoft.com/library/windows/hardware/ff560200) interface. It provides basic functionality that is common across all framework object types. All framework objects are derived from this root object.

When drivers create framework base objects through a call to the [**IWDFDriver::CreateWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff558906) method, they can initially register their [IObjectCleanup](https://msdn.microsoft.com/library/windows/hardware/ff556754) interfaces so that the framework notifies the driver when the objects are about to be destroyed. Later, drivers can use the [**IWDFObject::AssignContext**](https://msdn.microsoft.com/library/windows/hardware/ff560208) method to change how they receive notifications on the framework base object instance.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Base%20Object%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




