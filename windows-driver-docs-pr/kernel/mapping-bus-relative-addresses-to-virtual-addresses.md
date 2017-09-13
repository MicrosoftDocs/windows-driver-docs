---
title: Mapping Bus-Relative Addresses to Virtual Addresses
author: windows-driver-content
description: Mapping Bus-Relative Addresses to Virtual Addresses
ms.assetid: 16496465-8a30-4250-9d64-afd36a788ae2
keywords: ["virtual address space mappings WDK kernel", "physical address space mappings WDK kernel", "mapping memory", "address space mappings WDK kernel", "translating address space WDK kernel", "memory management WDK kernel , mapping addresses", "bus-relative memory space WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Mapping Bus-Relative Addresses to Virtual Addresses


## <a href="" id="ddk-mapping-bus-relative-addresses-to-virtual-addresses-kg"></a>


Some processors implement separate memory and I/O address spaces, while other processors do not. Because of these differences in hardware platforms, the mechanism drivers use to access I/O- or memory-resident device resources differs from platform to platform.

A driver requests device I/O and memory resources in response to the PnP manager's [**IRP\_MN\_QUERY\_RESOURCE\_REQUIREMENTS**](https://msdn.microsoft.com/library/windows/hardware/ff551715) IRP. Depending on the hardware architecture, the HAL can assign I/O resources in I/O space or in memory space, and can assign memory resources in I/O space or in memory space.

If the HAL uses bus-relative memory space to access device resources (such as device registers), a driver must map I/O space into virtual memory so that it can access these resources. The driver can determine whether the resources are I/O- or memory-resident by inspecting the translated resources passed to the driver by the PnP manager at device startup. If the HAL uses I/O space, no mapping is required.

Specifically, when a driver receives an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request, it should examine the structures at **IrpSp-&gt;Parameters.StartDevice.AllocatedResources** and **IrpSp-&gt;Parameters.StartDevice.AllocatedResourcesTranslated**, which describe the raw (bus-relative) and translated resources, respectively, that the PnP manager has assigned to the device. Drivers should save a copy of each resource list in the device extension as an aid to debugging.

The resource lists are paired [**CM\_RESOURCE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff541994) structures, in which each element of the raw list corresponds to the same element of the translated list. For example, if **AllocatedResources.List**\[0\] describes a raw I/O port range, **AllocatedResourcesTranslated.List**\[0\] describes the same range after translation. Each translated resource includes a physical address and the type of the resource.

If a driver is assigned a translated memory resource (**CmResourceTypeMemory**), it must call [**MmMapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff554618) to map the physical address into a virtual address through which it can access device registers. For a driver to operate in a platform-independent manner, it should check every returned, translated resource and map it, if necessary.

**A kernel-mode driver should take the following steps, in response to an IRP\_MN\_START\_DEVICE request, to ensure access to all device resources**

1.  Copy **IrpSp-&gt;Parameters.StartDevice.AllocatedResources** to the device extension.

2.  Copy **IrpSp-&gt;Parameters.StartDevice.AllocatedResourcesTranslated** to the device extension.

3.  In a loop, inspect each descriptor element in **AllocatedResourcesTranslated**. If the descriptor resource type is **CmResourceTypeMemory**, call **MmMapIoSpace**, passing the physical address and length of the translated resource.

When the driver receives an [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) or [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request from the PnP manager, it must release the mappings by calling [**MmUnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff556387) in a similar loop. The driver should also call **MmUnmapIoSpace** if it must fail the **IRP\_MN\_START\_DEVICE** request.

The raw resource type indicates which HAL access routine a driver should call (**READ\_REGISTER\_*XXX***, **WRITE\_REGISTER\_*XXX***, **READ\_PORT\_*XXX***, **WRITE\_PORT\_*XXX***). Most drivers do not have to check the raw resource list to determine which of these routines to use, because the driver itself requested the resource or the driver writer knows the required type given the nature of the device hardware.

For a resource in I/O space (**CmResourceTypePort**, **CmResourceTypeInterrupt**, **CmResourceTypeDma**), the driver should use the low-order 32 bits of the returned physical address to access the device resource, for example, through the HAL's read and write **READ\_REGISTER\_*XXX***, **WRITE\_REGISTER\_*XXX***, **READ\_PORT\_*XXX***, and **WRITE\_PORT\_*XXX*** routines.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Mapping%20Bus-Relative%20Addresses%20to%20Virtual%20Addresses%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


