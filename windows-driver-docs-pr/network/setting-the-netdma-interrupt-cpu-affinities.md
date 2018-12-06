---
title: Setting the NetDMA Interrupt CPU Affinities
description: Setting the NetDMA Interrupt CPU Affinities
ms.assetid: 61804166-1888-4cdb-bf6f-c9d84e302698
keywords:
- interrupts WDK NetDMA , CPU affinities
- CPU affinities WDK NetDMA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the NetDMA Interrupt CPU Affinities


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




If a computer supports MSI-X, the NetDMA interface, while in the context of the [**NetDmaRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568336) function, calls the NetDMA provider driver's [**ProviderSetDmaChannelCpuAffinity**](https://msdn.microsoft.com/library/windows/hardware/ff570402) function to specify the CPU affinities of the interrupts that are associated with DMA channels. The NetDMA interface passes the *ProviderSetDmaChannelCpuAffinity* function an array of [**NET\_DMA\_CHANNEL\_CPU\_AFFINITY**](https://msdn.microsoft.com/library/windows/hardware/ff568731) structures at the *CpuAffinityArray* parameter.

Because the actual number of DMA channels is not known before a NetDMA provider is started, the NetDMA interface specifies the CPU affinities for the maximum number of channels. The NetDMA provider supplies the maximum number of channels in the **MaxDmaChannelCount** member of the [**NET\_DMA\_PROVIDER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff568738) structure that the provider passes to the [**NetDmaRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568336) function. The NetDMA provider driver supplies the actual number of DMA channels in the **DmaChannelCount** member of the [**NET\_DMA\_PROVIDER\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff568737) structure that it passes to the [**NetDmaProviderStart**](https://msdn.microsoft.com/library/windows/hardware/ff568334) function.

On computers that do not support MSI-X, the NetDMA interface can specify CPU affinities for the interrupt deferred procedure calls (DPCs), but not for the interrupts. For interrupt DPCs, the NetDMA interface specifies a list of possible CPUs for the interrupt DPC in the **ProcessorAffinityMask** member of the [**NET\_DMA\_CHANNEL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff568732) structure. The NetDMA provider driver calls the [**KeSetTargetProcessorDpc**](https://msdn.microsoft.com/library/windows/hardware/ff553278) routine to set the target CPU of the interrupt DPC to match one of the specified affinity mask bits.

On computers that support MSI-X, because the NetDMA interface specifies CPU affinities during NetDMA provider registration, the NetDMA provider driver can specify interrupt affinities while handling the [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550874) IRP. After the [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine successfully returns, the Plug and Play (PnP) manager sends the IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS IRP for the NetDMA provider. The NetDMA provider driver must attempt to allocate MSI-X interrupt resources according to affinity parameters that the NetDMA interface passed to [**ProviderSetDmaChannelCpuAffinity**](https://msdn.microsoft.com/library/windows/hardware/ff570402).

The NetDMA provider driver must be prepared to handle IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS immediately after the [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine returns. IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS provides a resource list as an [**IO\_RESOURCE\_REQUIREMENTS\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff550609) structure at **Irp-&gt;IoStatus.Information**. The resources in the list are described by [**IO\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff550598) structures.

A NetDMA provider driver can modify the interrupt affinity policy for each resource of type **CmResourceTypeInterrupt** that describes an MSI-X message. If an affinity policy requests targeting for a specific set of processors, the NetDMA provider driver also sets a [**KAFFINITY**](https://docs.microsoft.com/windows-hardware/drivers/kernel/interrupt-affinity-and-priority#about-kaffinity) mask at **Interrupt.TargetedProcessors** in the IO\_RESOURCE\_DESCRIPTOR structure.

 

 





