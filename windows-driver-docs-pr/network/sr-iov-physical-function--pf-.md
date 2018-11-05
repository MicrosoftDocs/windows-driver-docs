---
title: SR-IOV Physical Function (PF)
description: SR-IOV Physical Function (PF)
ms.assetid: 176ABEA4-B6BE-41D6-9171-8E9A537F8CA1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SR-IOV Physical Function (PF)


The Physical Function (PF) is a PCI Express (PCIe) function of a network adapter that supports the single root I/O virtualization (SR-IOV) interface. The PF includes the SR-IOV Extended Capability in the PCIe Configuration space. The capability is used to configure and manage the SR-IOV functionality of the network adapter, such as enabling virtualization and exposing PCIe Virtual Functions (VFs).

The PF is exposed as a virtual network adapter in the management operating system of the Hyper-V parent partition. The PF miniport driver is an NDIS miniport driver that manages the PF in the management operating system. The configuration and provisioning of the VFs, together with other hardware and software resources for the support of VFs, is performed through the PF miniport driver. The PF miniport driver uses the traditional NDIS miniport driver functionality to provide the access to the networking I/O resources to the management operating system. The PF driver is also used as a way to manage the resources allocated on the adapter for the VFs.

The PF supports the SR-IOV Extended Capability structure in its PCIe configuration space. This structure is defined in the PCI-SIG [Single Root I/O Virtualization and Sharing 1.1](http://go.microsoft.com/fwlink/p/?linkid=221742) specification. This structure includes the following members:

<a href="" id="totalvfs"></a>**TotalVFs**  
A read-only field that specifies the maximum number of VFs that can be associated with the PF.

<a href="" id="numvfs"></a>**NumVFs**  
A read-write field that specifies the current number of VFs that are available on the SR-IOV network adapter.

<a href="" id="sr-iov-control"></a>**SR-IOV Control**  
A read-write field that specifies various control bits that enable or disable SR-IOV functionality on the network adapter. For example, if the **VF Enable** bit is set to one, VFs can be associated with the PF on the adapter. If this bit is set to zero, VFs are disabled and not visible on the adapter.

The PF also provides the mechanism for the management operating system to communicate with the external physical network. The PF provides network connectivity to the all virtual network adapters that are connected to the Hyper-V extensible switch module. This includes the following:

-   Virtual network adapters that provide network connectivity to the Hyper-V parent partition.

-   Virtual network adapters that provide network connectivity to the Hyper-V child partitions that do not have VFs allocated to them.

The PF miniport driver is responsible for managing resources on the network adapter that are used by one or more VFs. Because of this, the PF miniport driver is loaded in the management operating system before any resources are allocated for a VF. The PF miniport driver is halted after all resources that were allocated for VFs are freed.

 

 





