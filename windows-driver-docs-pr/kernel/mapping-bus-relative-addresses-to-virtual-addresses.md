---
title: Mapping Bus-Relative Addresses to Virtual Addresses
description: Mapping Bus-Relative Addresses to Virtual Addresses
keywords: ["virtual address space mappings WDK kernel", "physical address space mappings WDK kernel", "mapping memory", "address space mappings WDK kernel", "translating address space WDK kernel", "memory management WDK kernel , mapping addresses", "bus-relative memory space WDK kernel"]
ms.date: 06/16/2017
---

# Mapping Bus-Relative Addresses to Virtual Addresses





Some processors implement separate memory and I/O address spaces, while other processors do not. Because of these differences in hardware platforms, the mechanism drivers use to access I/O- or memory-resident device resources differs from platform to platform.

A driver requests device I/O and memory resources in response to the PnP manager's [**IRP\_MN\_QUERY\_RESOURCE\_REQUIREMENTS**](./irp-mn-query-resource-requirements.md) IRP. Depending on the hardware architecture, the HAL can assign I/O resources in I/O space or in memory space, and can assign memory resources in I/O space or in memory space.

If the HAL uses bus-relative memory space to access device resources (such as device registers), a driver must map I/O space into virtual memory so that it can access these resources. The driver can determine whether the resources are I/O- or memory-resident by inspecting the translated resources passed to the driver by the PnP manager at device startup. If the HAL uses I/O space, no mapping is required.

Specifically, when a driver receives an [**IRP\_MN\_START\_DEVICE**](./irp-mn-start-device.md) request, it should examine the structures at **IrpSp-&gt;Parameters.StartDevice.AllocatedResources** and **IrpSp-&gt;Parameters.StartDevice.AllocatedResourcesTranslated**, which describe the raw (bus-relative) and translated resources, respectively, that the PnP manager has assigned to the device. Drivers should save a copy of each resource list in the device extension as an aid to debugging.

The resource lists are paired [**CM\_RESOURCE\_LIST**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_cm_resource_list) structures, in which each element of the raw list corresponds to the same element of the translated list. For example, if **AllocatedResources.List**\[0\] describes a raw I/O port range, **AllocatedResourcesTranslated.List**\[0\] describes the same range after translation. Each translated resource includes a physical address and the type of the resource.

If a driver is assigned a translated memory resource (**CmResourceTypeMemory**), it must call [**MmMapIoSpace**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmapiospace) to map the physical address into a virtual address through which it can access device registers. For a driver to operate in a platform-independent manner, it should check every returned, translated resource and map it, if necessary.

**A kernel-mode driver should take the following steps, in response to an IRP\_MN\_START\_DEVICE request, to ensure access to all device resources**

1.  Copy **IrpSp-&gt;Parameters.StartDevice.AllocatedResources** to the device extension.

2.  Copy **IrpSp-&gt;Parameters.StartDevice.AllocatedResourcesTranslated** to the device extension.

3.  In a loop, inspect each descriptor element in **AllocatedResourcesTranslated**. If the descriptor resource type is **CmResourceTypeMemory**, call **MmMapIoSpace**, passing the physical address and length of the translated resource.

When the driver receives an [**IRP\_MN\_STOP\_DEVICE**](./irp-mn-stop-device.md) or [**IRP\_MN\_REMOVE\_DEVICE**](./irp-mn-remove-device.md) request from the PnP manager, it must release the mappings by calling [**MmUnmapIoSpace**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunmapiospace) in a similar loop. The driver should also call **MmUnmapIoSpace** if it must fail the **IRP\_MN\_START\_DEVICE** request.

The raw resource type indicates which HAL access routine a driver should call (**READ\_REGISTER\__XXX_**, **WRITE\_REGISTER\__XXX_**, **READ\_PORT\__XXX_**, **WRITE\_PORT\__XXX_**). Most drivers do not have to check the raw resource list to determine which of these routines to use, because the driver itself requested the resource or the driver writer knows the required type given the nature of the device hardware.

 For a resource in I/O space (**CmResourceTypePort**, **CmResourceTypeInterrupt**, **CmResourceTypeDma**), the driver should use the low-order 32 bits of the returned physical address to access the device resource, for example, through the HAL's read and write **READ\_REGISTER\__XXX_**, **WRITE\_REGISTER\__XXX_**, **READ\_PORT\__XXX_**, **WRITE\_PORT\__XXX_** routines.
 
 

