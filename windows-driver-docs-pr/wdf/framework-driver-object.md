---
title: Framework Driver Object
author: windows-driver-content
description: Framework Driver Object
ms.assetid: 6e9e568c-7e4f-48bd-b351-4be0e12cc15b
keywords: ["UMDF objects WDK , driver objects", "framework objects WDK UMDF , driver objects", "driver objects WDK UMDF", "IWDFDriver"]
---

# Framework Driver Object


\[This topic applies to UMDF 1.*x*.\]

The framework driver object is exposed to drivers by the [IWDFDriver](https://msdn.microsoft.com/library/windows/hardware/ff558893) interface. It is the framework representation of the driver image loaded in the driver host process. The framework creates a new driver object for each driver loaded in the driver host process. The **IWDFDriver** interface is passed to the driver by the [**IDriverEntry::OnInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff554900) method, which is the main entry point for the user-mode driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Driver%20Object%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




