---
title: Virtualized Networking Concepts and Terms
description: Virtualized Networking Concepts and Terms
ms.assetid: 467996B2-9319-47F9-BAEB-5AC1F20B6E01
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Virtualized Networking Concepts and Terms


The following list gives definitions of key concepts and terms that are used in the Virtualized Networking section. We recommend that you become familiar with these terms before you read the other topics in this section:

<a href="" id="child-partition"></a>Child Partition  
In Hyper-V, the child partition is a software-based virtual machine (VM) that has unprivileged access to the physical resources of the host computer.

Each child partition is created through the parent partition. There can be one or more child partitions that run under Hyper-V on the host computer. Each child partition hosts a guest operating system.

In general, child partitions do not have direct access to the physical hardware resources and are presented a virtual view of the resources as virtual devices. Requests to the virtual devices are redirected, either through the VM bus (VMBus) or the hypervisor, to the parent partition where these requests are handled. In addition, child partitions cannot create other partitions.

**Note**  Starting with Windows Server 2012, child partitions do have direct access to the resources of a physical network adapter that supports single root I/O virtualization (SR-IOV).

 

<a href="" id="emulated-network-adapter"></a>Emulated Network Adapter  
A Hyper-V extensible switch Ethernet adapter that is exposed in the guest operating system that runs in a Hyper-V child partition. An emulated network adapter is a type of VM network adapter. The emulated network adapter mimics an Intel network adapter and uses hardware emulation to forward packets to and from the extensible switch port.

This adapter is exposed in a guest operating system that is Windows XP, Windows Vista, or later versions of Windows. This adapter is also exposed in a guest operating system that is a non-Windows operating system.

<a href="" id="external-extensible-switch-"></a>External Extensible Switch   

A virtual Ethernet switch over which packets are routed between the Hyper-V parent partition, one or more Hyper-V child partitions, and the physical networking interface of the host. This type of switch allows packets to be sent or received between all Hyper-V partitions and the physical network interface on the host.

Also, applications and drivers that run in the management operating system can send or receive packets through this type of switch.

<a href="" id="external-network-adapter"></a>External Network Adapter  
A Hyper-V extensible switch Ethernet adapter that is exposed in the management operating system that runs in the Hyper-V parent partition. The external network adapter is bound to one or more physical network adapters on the host.

The external network adapter routes packets between the Hyper-V partitions and the physical network interface on the host.

**Note**  Each instance of an extensible switch supports no more than one external network adapter.

 

<a href="" id="extensible-switch-team"></a>Extensible Switch Team  
This is a configuration in which the extensible switch external network adapter is bound to the virtual miniport edge of an NDIS multiplexer (MUX) intermediate driver. The MUX intermediate driver is bound to a team of one or more physical networks on the host.

In this configuration, the extensible switch extensions are exposed to every network adapter in the team. This allows the forwarding extension in the extensible switch driver stack to manage the configuration and use of individual network adapters in the team. For example, the extension can provide support for a load balancing failover (LBFO) solution over the team by forwarding outgoing packets to individual adapters. Such an extension is known as a *teaming provider*.

For more information, see [NDIS MUX Intermediate Drivers](ndis-mux-intermediate-drivers.md).

<a href="" id="guest-operating-system"></a>Guest Operating System  
The operating system that runs in a Hyper-V child partition. Each child partition can host only one operating system. However, many different operating systems can be hosted in child partitions. This includes different versions of Windows and Linux.

<a href="" id="hypervisor"></a>Hypervisor  
In Hyper-V, the hypervisor is a layer of software that runs between the physical hardware and one or more operating systems that run in Hyper-V partitions.

The hypervisor's main purpose is to provide isolated execution environments called *partitions*. The hypervisor provides each partition with a set of hardware resources, such memory, devices, and CPU cycles. The hypervisor controls and arbitrates access from each partition to the underlying hardware.

<a href="" id="hyper-v-extensible-switch"></a>Hyper-V Extensible Switch  
A virtual Ethernet switch that runs in the management operating system. Each instance of the extensible switch routes packets between ports that are connected to the Hyper-V extensible switch network adapters.

For more information, see [Hyper-V Extensible Switch](hyper-v-extensible-switch.md).

**Note**  The Hyper-V extensible switch is supported in NDIS 6.30 and later versions of NDIS.

 

<a href="" id="hyper-v-extensible-switch-extension"></a>Hyper-V Extensible Switch Extension  
A Hyper-V extensible switch extension is an NDIS filter driver that attaches to the extensible switch driver stack. Once attached, the extension can capture, filter, or forward network packets and NDIS OIDs. Packets and OIDs can be forwarded to network adapters that are connected to extensible switch ports.

Hyper-V extensible switch extensions are supported in NDIS 6.30 and later versions of NDIS.

**Note**  The Windows Filtering Platform (WFP) provides an in-box extensible switch filtering extension (Wfplwfs.sys ). This extension allows WFP filters or callout drivers to intercept packets along the Hyper-V extensible switch data path. This allows the filters or callout drivers to perform packet inspection or modification by using the WFP management and system functions. For an overview of WFP, see [Windows Filtering Platform](porting-packet-processing-drivers-and-apps-to-wfp.md).

 

<a href="" id="hyper-v-extensible-switch-network-adapter"></a>Hyper-V Extensible Switch Network Adapter  
A network adapter that is managed by the Hyper-V extensible switch. These network adapters connect to ports on the extensible switch, and consist of the following adapter types:

-   The external and internal network adapters that are exposed in the management operating system that runs in the Hyper-V parent partition.

-   The synthetic or emulated VM network adapters that are exposed in the guest operating system that runs in a Hyper-V child partition.

<a href="" id="internal-extensible-switch"></a>Internal Extensible Switch  
A virtual Ethernet switch over which packets are routed between the Hyper-V parent partition and one or more Hyper-V child partitions. This type of switch excludes packet traffic from the physical network interface on the host.

Also, applications and drivers that run in the management operating system can send or receive packets through this type of switch.

<a href="" id="internal-network-adapter"></a>Internal Network Adapter  
A Hyper-V extensible switch Ethernet adapter that is exposed in the management operating system that runs in the Hyper-V parent partition. The internal network adapter sends or receives packets between all Hyper-V partitions. However, the internal network adapter is not bound to a physical networking interface of the host.

<a href="" id="i-o-memory-management-unit--iommu-"></a>I/O Memory Management Unit (IOMMU)  
An IOMMU is used to remap physical memory addresses to the addresses that are used by the child partitions. The IOMMU operates independently of the memory management hardware that is used by the processor.

<a href="" id="load-balancing-failover--lbfo--team"></a>Load Balancing Failover (LBFO) Team  
This is a configuration in which the extensible switch external network adapter is bound to the virtual miniport edge of an LBFO provider. The LBFO provider itself can bind to a team of one or more physical network adapters.

In this configuration, the extensible switch extensions are exposed to only the underlying virtual miniport edge as a network adapter. This allows the provider to support an LBFO solution by binding to multiple physical network adapters. These adapters are not managed by a forwarding extension that runs in the extensible switch driver stack.

<a href="" id="management-operating-system"></a>Management Operating System  
The operating system that runs in the Hyper-V parent partition. The parent partition runs the operating system that is running on the host computer. For Hyper-V, the host computer must run x64 versions of Windows Server 2008 or later versions of Windows Server.

<a href="" id="network-virtual-service-client--netvsc--driver"></a>Network Virtual Service Client (NetVSC) Driver  
An NDIS driver that runs in the guest operating system of a Hyper-V child partition. The NetVSC exposes a virtualized network adapter that is known as a *VM network adapter*.

The NetVSC accesses the Hyper-V extensible switch to forward packets over the network interface managed by the switch. The NetVSC does this by passing messages over the VMBus to the associated NetVSP driver. This driver runs in the management operating system of the Hyper-V parent partition.

In most cases, the NetVSC sends and receives packets by connecting to a port on the Hyper-V extensible switch. However, the NetVSC could be configured to connect to a Virtual Function (VF) of a physical network adapter that supports the SR-IOV interface. In this case, the NetVSC sends and receives packets directly over the underlying physical adapter.

<a href="" id="network-virtual-service-producer--netvsp--driver"></a>Network Virtual Service Producer (NetVSP) Driver  
An NDIS driver that runs in the management operating system of the Hyper-V parent partition. This driver provides services to support networking access by the Hyper-V child partitions.

<a href="" id="nic-switch"></a>NIC Switch  
The NIC switch is a hardware component of a network adapter that supports single root I/O virtualization (SR-IOV). This switch bridges network traffic between the adapter's physical network interface and the Physical Function (PF) and one or more VFs on the adapter.

<a href="" id="partition"></a>Partition  
A partition is managed by the hypervisor. Each partition represents a logical unit of isolated processor and memory resources. This allows multiple isolated operating systems to share a single hardware platform.

The hypervisor also manages policies for memory and device access on the host computer. These policies are different for parent and child partitions.

<a href="" id="parent-partition"></a>Parent Partition  
In Hyper-V, the parent partition is the first partition on the host computer. This partition has privileged access to the physical resources of the host computer, such as access to memory and devices. In addition, the parent partition is responsible for starting the hypervisor and creating child partitions.

There is only one parent partition that runs under Hyper-V on the host computer. The parent partition hosts the management operating system.

**Note**  The parent partition is also known as the *root* partition.

 

<a href="" id="physical-function--pf-"></a>Physical Function (PF)  
A PCI Express (PCIe) function that supports the single root I/O virtualization (SR-IOV) interface. SR-IOV extends the PCIe interface to enable multiple VMs to share the same PCIe physical hardware resources. The PF contains the PCIe SR-IOV Extended Capability structure in its PCI configuration space.

<a href="" id="pf-vf-backchannel"></a>PF/VF Backchannel  
A private software-based communication interface between the miniport drivers of a PCIe Virtual Function (VF) and the PCIe Physical Function (PF). Each VF miniport driver can issue requests over the backchannel to the PF miniport driver. The PF miniport driver can issue status notifications over the backchannel to individual VF miniport drivers.

Data exchanged between the PF and VF miniport drivers over the backchannel interface involves the use of a *VF configuration block*. Each VF configuration block is similar in concept to an interprocess communication (IPC) message, in which each block has a proprietary format, length, and block identifier. The independent hardware vendor (IHV) can define one or more VF configuration blocks for the PF and VF miniport drivers.

<a href="" id="private-extensible-switch-"></a>Private Extensible Switch   
A virtual Ethernet switch over which packets are routed between one or more Hyper-V child partitions. This type of switch excludes packet traffic from the Hyper-V parent partition and the physical network interface on the host.

**Note**  Applications and drivers that run in the management operating system cannot send or receive packets through this type of switch.

 

<a href="" id="single-root-i-o-virtualization--sr-iov-"></a>Single Root I/O Virtualization (SR-IOV)  
SR-IOV is a method by which a PCIe network adapter can be partitioned into one Physical Function (PF) and one or more virtual functions (VF). Each function on the adapter is assigned a unique PCIe requester ID. This enables the adapter to apply memory and interrupt translations so that different network traffic streams can be delivered directly to the appropriate PF or VF. By avoiding the routing of network traffic through the Hyper-V extensible switch component, SR-IOV reduces the I/O overhead in the virtualized networking environment.

For more information, see [Single Root I/O Virtualization (SR-IOV)](single-root-i-o-virtualization--sr-iov-.md).

**Note**  SR-IOV is supported in NDIS 6.30 and later versions of NDIS.

 

<a href="" id="synthetic-data-path"></a>Synthetic Data Path  
The networking data path between a VM network adapter exposed in a guest operating system and the Hyper-V extensible switch component in the management operating system.

<a href="" id="synthetic-network-adapter"></a>Synthetic Network Adapter  
A Hyper-V extensible switch Ethernet adapter that is exposed in the guest operating system that runs in a Hyper-V child partition. A synthetic network adapter is a type of VM network adapter. The network virtual service client (NetVSC) that runs in the VM exposes this synthetic network adapter. NetVSC forwards packets to and from the extensible switch port over the VM bus (VMBus) to the associated NetVSP driver.

This network adapter is exposed in a guest operating system that is Windows Vista or a later version of Windows.

<a href="" id="virtual-function--vf-"></a>Virtual Function (VF)  
A PCIe function that is associated with a PF on a network adapter that supports SR-IOV. A VF shares one or more physical resources on the adapter, such as the physical Ethernet port, with the PF and other VFs that are associated with the same PF.

<a href="" id="vf-data-path"></a>VF Data Path  
The networking data path between a VM network adapter exposed in a guest operating system and the VF on an SR-IOV network adapter. In this data path, the VM network adapter is teamed with the VF network adapter in the guest operating system. The VF miniport driver forwards packets to or from the VM network adapter to the VF. The NIC switch on the SR-IOV network adapter then forwards packets to or from the VF to the physical network interface on the adapter.

<a href="" id="vf-network-adapter"></a>VF Network Adapter  
The virtual network adapter that is exposed in the guest operating system for the VF. When resources are allocated for the VF and it becomes attached to a child partition, the VPCI bus driver in the guest operating system of that partition exposes the VF network adapter. The VPCI bus driver also loads the VF miniport driver for this adapter.

<a href="" id="virtual-machine--vm-"></a>Virtual Machine (VM)  
A virtual guest computer that is implemented in software and is hosted within a physical host computer. A virtual machine emulates a complete hardware system, from processor to network adapter, in a self-contained, isolated software environment. This enables concurrent operation of otherwise incompatible operating systems.

Each guest operating system runs in its own isolated software virtual machine.

**Note**  In Hyper-V, a child partition is also known as a VM.

 

<a href="" id="virtual-machine-bus--vmbus-"></a>Virtual Machine Bus (VMBus)  
A virtual communications bus that passes control and data messages between the Hyper-V parent and child partitions. Access to the physical resources on the host computer by child partitions is made through messages that are passed over the VMBus between Virtual Service Client (VSC) and Virtual Service Provider (VSP) components.

<a href="" id="virtual-machine--vm--network-adapter"></a>Virtual Machine (VM) Network Adapter  
A Hyper-V extensible switch virtual network adapter that is exposed in the guest operating system of a Hyper-V child partition.

The VM network adapter supports the following virtualization types:

-   The VM network adapter could be a synthetic virtualization of a network adapter (*synthetic network adapter*). In this case, the network virtual service client (NetVSC) that runs in the VM exposes this virtual network adapter. NetVSC forwards packets to and from the extensible switch port over the VM bus (VMBus).

-   The VM network adapter could be an emulated virtualization of a physical network adapter (*emulated network adapter*). In this case, the VM network adapter mimics an Intel network adapter and uses hardware emulation to forward packets to and from the extensible switch port.

A VM network adapter can be configured to access either the Hyper-V external, internal, or private network interfaces.

<a href="" id="virtual-machine-queue--vmq-"></a>Virtual Machine Queue (VMQ)  
A VMQ-capable network adapter uses DMA to transfer all incoming frames directly to VM memory. VMQ also improves network throughput by distributing the processing of network traffic for multiple VMs among multiple processors.

For more information, see [Virtual Machine Queue (VMQ)](virtual-machine-queue--vmq-.md).

**Note**  VMQ is supported in NDIS 6.20 and later versions of NDIS.

 

<a href="" id="virtual-pci--vpci--driver"></a>Virtual PCI (VPCI) Driver  
The PCI bus driver that runs in the guest operating system of a Hyper-V child partition. This driver exposes the VF as a virtual network adapter in the guest operating system.

The VPCI driver is a Hyper-V VSC and communicates with the VPCI VSP that runs in the management operating system in the Hyper-V parent partition. Communication between the VPCI VSP and VSC components occurs over VMBUS.

For more information about the VPCI interface, see [GUID\_PCI\_VIRTUALIZATION\_INTERFACE](https://msdn.microsoft.com/library/windows/hardware/hh451143).

<a href="" id="virtualization-stack"></a>Virtualization Stack  
A collection of software components that manages the creation and execution of child partitions under Hyper-V. The virtualization stack manages the access by child partitions to the hardware resources on the host computer. The virtualization stack runs in the Hyper-V parent partition.

 

 





