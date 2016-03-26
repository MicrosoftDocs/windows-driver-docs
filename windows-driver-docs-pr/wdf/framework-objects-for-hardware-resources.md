---
title: Framework Objects for Hardware Resources
description: Framework Objects for Hardware Resources
ms.assetid: 64eb628f-ce3d-494b-9fc1-7179a722c5f2
keywords: ["hardware resources WDK KMDF , framework objects", "framework objects WDK KMDF , hardware resources", "framework resource-requirements-list objects WDK KMDF", "framework resource-range-list objects WDK KMDF", "framework resource-list objects WDK KMDF", "resource-list objects WDK KMDF", "resource-range-list objects WDK KMDF", "resource-requirements-list objects WDK KMDF", "hardware resources WDK KMDF , specifying"]
---

# Framework Objects for Hardware Resources


The framework defines the following three objects, which the framework and drivers use to specify a device's hardware resources:

<a href="" id="framework-resource-requirements-list-objects"></a>*Framework resource-requirements-list objects*  
Each framework resource-requirements-list object represents a [resource requirements list](https://msdn.microsoft.com/library/windows/hardware/ff547012). Handles to these objects have a type of WDFIORESREQLIST. The object defines [framework resource-requirements-list object methods](https://msdn.microsoft.com/library/windows/hardware/dn265665). A resource requirements list consists of a set of logical configurations.

<a href="" id="framework-resource-range-list-objects"></a>*Framework resource-range-list objects*  
Each framework resource-range-list object represents a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) (that is, a set of ranges of resources that the device is capable of using) in a resource requirements list. Handles to these objects have a type of WDFIORESLIST. The object defines [framework resource-range-list object methods](https://msdn.microsoft.com/library/windows/hardware/dn265665).

<a href="" id="framework-resource-list-objects"></a>*Framework resource-list objects*  
Each framework resource-list object represents a logical configuration (that is, a set of specific resources) in a [resource list](https://msdn.microsoft.com/library/windows/hardware/ff547012). Handles to these objects have a type of WDFCMRESLIST. The object defines [framework resource-list object methods](https://msdn.microsoft.com/library/windows/hardware/dn265665).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Objects%20for%20Hardware%20Resources%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




