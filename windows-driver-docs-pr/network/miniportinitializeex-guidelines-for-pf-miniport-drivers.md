---
title: MiniportInitializeEx Guidelines for PF Miniport Drivers
description: MiniportInitializeEx Guidelines for PF Miniport Drivers
ms.assetid: 338035E7-7677-49FE-A06D-CCFD813B0C10
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MiniportInitializeEx Guidelines for PF Miniport Drivers


This topic describes the guidelines for writing a [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function for the miniport driver of the PCI Express (PCIe) Physical Function (PF). The PF is a component of a network adapter that supports single root I/O virtualization (SR-IOV).

**Note**  These guidelines only apply to PF miniport drivers. For initialization guidelines for the miniport driver of a PCIe Virtual Function (VF) of the adapter, see [Initializing a VF Miniport Driver](initializing-a-vf-miniport-driver.md).

 

The PF miniport driver follows the same steps as any NDIS miniport driver when its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function. For more information about these steps, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

In addition to these steps, the PF miniport driver must follow these additional steps when NDIS calls the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function:

1.  The PF miniport driver calls the [**NdisGetHypervisorInfo**](https://msdn.microsoft.com/library/windows/hardware/ff562635) function to verify that it is running in the Hyper-V parent partition. This function returns an [**NDIS\_HYPERVISOR\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565708) structure that defines the partition type. If the partition type is reported as **NdisHypervisorPartitionMsHvParent**, the miniport driver is running in the Hyper-V parent partition that is attached to the PF on the adapter.

    **Note**  If the partition type is reported as **NdisHypervisorPartitionMsHvChild**, the miniport driver is running in the Hyper-V child partition that is attached to a VF on the adapter. In this case, the miniport driver must not initialize as a PF driver. If possible, the driver must initialize as a VF driver as described in [Initializing a VF Miniport Driver](initializing-a-vf-miniport-driver.md).

     

2.  The PF miniport driver must read the SR-IOV standardized keywords to determine whether SR-IOV is enabled and obtain the NIC switch configuration settings. For more information about these keywords, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

    **Note**  If the PF miniport driver registered an entry point to a [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function, the driver may have previously obtained these settings from the registry when NDIS called *MiniportSetOptions*.

     

3.  If the network adapter supports SR-IOV, virtual machine queue (VMQ), or RSS, the miniport driver must determine which feature to enable on the network adapter. For more information on how to determine this, see [Handling SR-IOV, VMQ, and RSS Standardized INF Keywords](handling-sr-iov--vmq--and-rss-standardized-inf-keywords.md).

4.  Along with RSS and VMQ hardware capabilities (if supported), the miniport driver must report its full set of hardware SR-IOV capabilities. These capabilities must be advertised regardless of the SR-IOV standardized keyword settings in the registry.

    If SR-IOV is enabled on the network adapter, the miniport driver must also report the currentlyenabled SR-IOV settings on the adapter.

    For more information on reporting the SR-IOV capabilities, see [Determining SR-IOV Capabilities](determining-sr-iov-capabilities.md).

5.  The miniport driver must report its full set of hardware NIC switch capabilities. These capabilities must be advertised regardless of the SR-IOV standardized keyword settings in the registry.

    If SR-IOV is enabled on the network adapter, the miniport driver must also report the currentlyenabled NIC switch settings on the adapter.

    For more information on reporting the NIC switch capabilities, see [Determining NIC Switch Capabilities](determining-nic-switch-capabilities.md).

6.  The miniport driver must report its full set of hardware receive filtering capabilities. These capabilities must be advertised regardless of the SR-IOV standardized keyword settings in the registry.

    If SR-IOV is enabled on the network adapter, the miniport driver must also report the currentlyenabled receive filtering settings on the adapter.

    For more information on reporting the receive filtering capabilities, see [Determining Receive Filtering Capabilities](determining-receive-filtering-capabilities.md).

7.  If the miniport driver supports static NIC switch creation, it must do the following in the context of the call to [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389).

    -   The driver configures the adapter hardware based on the NIC switch standardized keyword settings. Based on these settings, the driver allocates the necessary hardware and software resources for the NIC switch.

    -   The miniport driver calls [**NdisMEnableVirtualization**](https://msdn.microsoft.com/library/windows/hardware/hh451481) to enable SR-IOV and set the number of VFs on the network adapter. This function configures the SR-IOV Extended Capability in the adapter's PCI configuration space. If this function returns NDIS\_STATUS\_SUCCESS, SR-IOV is enabled and the VFs are exposed over the PCIe interface.

    For more information, see [Static Creation of a NIC Switch](static-creation-of-a-nic-switch.md).

    **Note**  If the miniport driver supports dynamic NIC switch creation, it creates the switch and enables virtualization when it handles an object identifier (OID) method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451815). For more information, see [Dynamic Creation of a NIC Switch](dynamic-creation-of-a-nic-switch.md).

     

 

 





