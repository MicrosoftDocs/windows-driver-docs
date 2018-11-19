---
title: Initializing a VF Miniport Driver
description: Initializing a VF Miniport Driver
ms.assetid: 23EB2086-E882-4CB6-A910-D8E99E0212E5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a VF Miniport Driver


This topic describes the guidelines for writing a [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function for the miniport driver for a PCI Express (PCIe) Virtual Function (VF). The VF is exposed by a network adapter that supports single root I/O virtualization (SR-IOV).

> [!NOTE]
> These guidelines only apply to VF miniport drivers of the SR-IOV network adapter. For initialization guidelines for the miniport driver of a PCIe Physical Function (PF) of the adapter, see [Initializing a PF Miniport Driver](initializing-a-pf-miniport-driver.md). 

The VF miniport driver follows the same steps as any NDIS miniport driver when its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called. For more information about these steps, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

In addition to these steps, the VF miniport driver must follow these additional steps when NDIS calls the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function:

- The VF miniport driver calls the [**NdisGetHypervisorInfo**](https://msdn.microsoft.com/library/windows/hardware/ff562635) function to verify that it is running in the Hyper-V child partition. This function returns an [**NDIS\_HYPERVISOR\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565708) structure which defines the partition type. If the partition type is reported as **NdisHypervisorPartitionMsHvChild**, the miniport driver is running in a Hyper-V child partition that is attached to the PF on the adapter.

  > [!NOTE] 
  > If the partition type is reported as **NdisHypervisorPartitionMsHvParent**, the miniport driver is running in the Hyper-V parent partition that is attached to the PF on the adapter. In this case, the miniport driver must not initialize as a VF driver. If possible, the driver must initialize as a PF driver as described in [Initialization Sequence for PF Miniport Drivers](initialization-sequence-for-pf-miniport-drivers.md).     

- Unlike the PF miniport driver, the VF miniport driver must not be installed with the SR-IOV standardized keywords and must not attempt to read these keywords. For more information about these keywords, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

- The VF miniport driver reports the SR-IOV hardware capabilities of the underlying virtual network adapter through an [**NDIS\_SRIOV\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451677) structure that is initialized in the following way:

  1. The miniport driver initializes the **Header** member. The driver sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_DEFAULT.

     Starting with NDIS 6.30, the miniport driver sets the **Revision** member of **Header** to NDIS\_SRIOV\_CAPABILITIES \_REVISION\_1 and the **Size** member to NDIS\_SIZEOF\_SRIOV\_CAPABILITIES\_REVISION\_1.

  2. The miniport driver sets the NDIS\_SRIOV\_CAPS\_PF\_MINIPORT flag in the **SriovCapabilities** member to report SR-IOV capabilities.

     > [!NOTE]
     > The VF miniport driver must set both the NDIS\_SRIOV\_CAPS\_VF\_MINIPORT flag and the NDIS\_SRIOV\_CAPS\_SRIOV\_SUPPORTED flag.         

  The VF miniport driver registers the SR-IOV capabilities of the network adapter by following these steps:

  1.  The miniport driver initializes an [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

      The miniport driver sets the **HardwareSriovCapabilities** and **CurrentSriovCapabilities** members to a pointer to the previouslyinitialized [**NDIS\_SRIOV\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451677) structure.

  2.  The driver calls [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) and sets the *MiniportAttributes* parameter to a pointer to the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

- The VF miniport driver must not advertise virtual machine queue (VMQ) capabilities. However, the driver can advertise support for other NDIS technologies, such as power management and receive side scaling (RSS).

  For more information about RSS, see [Receive Side Scaling](ndis-receive-side-scaling2.md).

 

 





