---
title: SR-IOV Architecture Overview and Key Components
description: Learn about single root I/O virtualization (SR-IOV) architecture, its components, and how it improves network virtualization performance. Explore key features and boost your network efficiency.
ms.date: 05/22/2025
---

# SR-IOV architecture

This article explains single root I/O virtualization (SR-IOV) architecture, its key components, and how SR-IOV enables efficient network virtualization for improved performance.

The following diagram shows the components of SR-IOV starting with NDIS 6.30 in Windows Server 2012.

:::image type="content" source="images/sriovarchitecture.png" alt-text="Screenshot of SR-IOV architecture stack diagram with a management parent partition and two child partitions containing guest operating systems.":::

The SR-IOV interface consists of the following components:

## Hyper-V extensible switch module 

The extensible switch module configures the NIC switch on the SR-IOV network adapter to provide network connectivity to Hyper-V child partitions.

> [!NOTE]
> Hyper-V child partitions are known as *virtual machines (VMs)*.

If a child partition connects to a PCI Express (PCIe) virtual function (VF), the extensible switch module doesn't participate in data traffic between the VM and the network adapter. Instead, data traffic passes directly between the VM and the attached VF.

For more information about the extensible switch, see [Hyper-V Extensible Switch](hyper-v-extensible-switch.md).

## Physical function (PF)  

The PF is a PCI Express (PCIe) function of a network adapter that supports the SR-IOV interface. The PF includes the SR-IOV extended capability in the PCIe configuration space. This capability lets you set up and manage the SR-IOV functionality of the network adapter, like enabling virtualization and exposing VFs.

For more information, see [SR-IOV Physical Function (PF)](sr-iov-physical-function--pf-.md).

## PF miniport driver  

The PF miniport driver is responsible for managing resources on the network adapter that are used by one or more VFs. Because of this, the PF miniport driver is loaded in the management operating system before any resources are allocated for a VF. The PF miniport driver is halted after all resources that were allocated for VFs are freed.

For more information, see [Writing SR-IOV PF Miniport Drivers](writing-sr-iov-pf-miniport-drivers.md).

## Virtual function (VF)  

A VF is a lightweight PCIe function on a network adapter that supports the SR-IOV interface. Each VF represents a virtualized instance of the network adapter and has its own PCI configuration space. Each VF also shares one or more physical resources on the network adapter, like an external network port, with the PF and other VFs.

For more information, see [SR-IoV Virtual Functions (VFs)](sr-iov-virtual-functions--vfs-.md).

## VF miniport driver  

The VF miniport driver installs in the VM to manage the VF. Any operation the VF miniport driver performs can't affect any other VF or the PF on the same network adapter.

For more information, see [Writing SR-IOV VF Miniport Drivers](writing-sr-iov-vf-miniport-drivers.md).

## Network interface card (NIC) switch  

The NIC switch is a hardware component of the network adapter that supports the SR-IOV interface. The NIC switch forwards network traffic between the physical port on the adapter and internal virtual ports (VPorts). Each VPort attaches to either the PF or a VF.

For more information, see [NIC Switches](nic-switches.md).

## Virtual ports (VPorts)  

A VPort is a data object that represents an internal port on the NIC switch of a network adapter that supports the SR-IOV interface. Similar to a port on a physical switch, a VPort on the NIC switch delivers packets to and from a PF or VF the port attaches to.

For more information, see [NIC Switches](nic-switches.md).

## Physical port  

The physical port is a hardware component of the network adapter that supports the SR-IOV interface. The physical port connects the adapter to the external networking medium.









