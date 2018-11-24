---
title: MiniportAddDevice Guidelines for PF Miniport Drivers
description: MiniportAddDevice Guidelines for PF Miniport Drivers
ms.assetid: D67FDBA0-C020-4557-9199-B9FF6F91DE6B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MiniportAddDevice Guidelines for PF Miniport Drivers


This topic describes the guidelines for writing a [*MiniportAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559332) function for the miniport driver of the PCI Express (PCIe) Physical Function (PF). The PF is a component of a network adapter that supports single root I/O virtualization (SR-IOV).

**Note**  These guidelines only apply to PF miniport drivers. For initialization guidelines for the miniport driver of a PCIe Virtual Function (VF) of the adapter, see [Initializing a VF Miniport Driver](initializing-a-vf-miniport-driver.md).

 

The Plug and Play (PnP) Manager calls the NDIS [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) function to create the functional device object (FDO) for the network adapter. If the PF miniport driver registered a [*MiniportAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559332) entry point when it called [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654), NDIS calls the driver's *MiniportAddDevice* function.

When [*MiniportAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559332) is called, the PF miniport driver can allocate additional software resources for the SR-IOV and the network interface card (NIC) switch. Typically, these are resources that must be allocated before NDIS calls the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function.

The driver can do the following within the context of the call to [*MiniportAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559332):

-   The PF miniport driver can call [**NdisReadConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564511) to read the SR-IOV and NIC switch configuration settings from the registry. These configuration settings are defined through the standardized SR-IOV keywords. For more information about these keywords, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

-   Based on these configuration settings, the PF miniport driver allocates the additional software resources for the SR-IOV network adapter.

**Note**  The actual allocation of hardware resources and the enabling of SR-IOV in the PCI configuration space must only be done within the context of the call to [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389). Because the network adapter's memory-mapped I/O (MMIO) space is uninitialized when [*MiniportAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559332) is called, the miniport driver must not read or write to the adapter until *MiniportInitializeEx* is called.

 

 

 





