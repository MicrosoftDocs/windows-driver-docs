---
title: SR-IOV Architecture
description: SR-IOV Architecture
ms.assetid: 548856F5-823A-4064-A6C3-28CA9FBA3860
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SR-IOV Architecture


This section provides a brief overview of the single root I/O virtualization (SR-IOV) interface and its components.

The following figure shows the components of the SR-IOV starting with NDIS 6.30 in Windows Server 2012.

![stack diagram showing sr-iov adapter with a management parent partition and two child partitions containing guest operating systems](images/sriovarchitecture.png)

The SR-IOV interface consists of the following components:

<a href="" id="hyper-v-extensible-switch-module"></a>Hyper-V Extensible Switch Module  
The extensible switch module that configures the NIC switch on the SR-IOV network adapter to provide network connectivity to the Hyper-V child partitions.

**Note**  Hyper-V child partitions are known as *virtual machines (VMs)*.

 

If the child partitions are connected to a PCI Express (PCIe) Virtual Function (VF), the extensible switch module does not participate in data traffic between the VM and the network adapter. Instead, data traffic is passed directly between the VM and the VF to which it is attached.

For more information about the extensible switch, see [Hyper-V Extensible Switch](hyper-v-extensible-switch.md).

<a href="" id="physical-function--pf-"></a>Physical Function (PF)  
The PF is a PCI Express (PCIe) function of a network adapter that supports the SR-IOV interface. The PF includes the SR-IOV Extended Capability in the PCIe Configuration space. The capability is used to configure and manage the SR-IOV functionality of the network adapter, such as enabling virtualization and exposing VFs.

For more information, see [SR-IOV Physical Function (PF)](sr-iov-physical-function--pf-.md).

<a href="" id="pf-miniport-driver"></a>PF Miniport Driver  
The PF miniport driver is responsible for managing resources on the network adapter that are used by one or more VFs. Because of this, the PF miniport driver is loaded in the management operating system before any resources are allocated for a VF. The PF miniport driver is halted after all resources that were allocated for VFs are freed.

For more information, see [Writing SR-IOV PF Miniport Drivers](writing-sr-iov-pf-miniport-drivers.md).

<a href="" id="virtual-function--vf-"></a>Virtual Function (VF)  
A VF is a lightweight PCIe function on a network adapter that supports the SR-IOV interface. The VF is associated with the VF on the network adapter, and represents a virtualized instance of the network adapter. Each VF has its own PCI Configuration space. Each VF also shares one or more physical resources on the network adapter, such as an external network port, with the PF and other VFs.

For more information, see [SR-IOV Virtual Functions (VFs)](sr-iov-virtual-functions--vfs-.md).

<a href="" id="vf-miniport-driver"></a>VF Miniport Driver  
The VF miniport driver is installed in the VM to manage the VF. Any operation that is performed by the VF miniport driver must not affect any other VF or the PF on the same network adapter.

For more information, see [Writing SR-IOV VF Miniport Drivers](writing-sr-iov-vf-miniport-drivers.md).

<a href="" id="network-interface-card--nic--switch"></a>Network Interface Card (NIC) Switch  
The NIC switch is a hardware component of the network adapter that supports the SR-IOV interface. The NIC switch forwards network traffic between the physical port on the adapter and internal virtual ports (VPorts). Each VPort is attached to either the PF or a VF.

For more information, see [NIC Switches](nic-switches.md).

<a href="" id="virtual-ports--vports-"></a>Virtual Ports (VPorts)  
A VPort is a data object that represents an internal port on the NIC switch of a network adapter that supports the SR-IOV interface. Similar to a port on a physical switch, a VPort on the NIC switch delivers packets to and from a PF or VF to which the port is attached.

For more information, see [NIC Switches](nic-switches.md).

<a href="" id="physical-port"></a>Physical Port  
The physical port is a hardware component of the network adapter that supports the SR-IOV interface. The physical port provides the interface on the adapter to the external networking medium.

 

 





