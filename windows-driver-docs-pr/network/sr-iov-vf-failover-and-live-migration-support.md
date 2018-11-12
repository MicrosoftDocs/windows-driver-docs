---
title: SR-IOV VF Failover and Live Migration Support
description: SR-IOV VF Failover and Live Migration Support
ms.assetid: 93D6EFC7-B701-4D10-8114-FA437E80096B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SR-IOV VF Failover and Live Migration Support


After the Hyper-V child partition is started, network traffic flows over the synthetic data path. If the physical network adapter supports the Single Root I/O Virtualization (SR-IOV) interface, it can enable one or more PCI Express (PCIe) Virtual Functions (VFs). Each VF can be attached to a Hyper-V child partition. When this happens, network traffic flows over the hardware-optimized [SR-IOV VF Data Path](sr-iov-vf-data-path.md).

After the VF data path is established, network traffic can revert to the [synthetic data path](sr-iov-vf-data-path.md) if any of the following conditions is true:

-   A VF was attached to a Hyper-V child partition but becomes detached. For example, the virtualization stack could detach a VF from one child partition and attach it to another child partition. This might occur when there are more Hyper-V child partitions that are running than there are VF resources on the underlying SR-IOV network adapter.

    The process of failing over to the synthetic data path from the VF data path is known as *VF failover*.

-   The Hyper-V child partition is being live migrated to a different host.

The following figure shows the various data paths that are supported over an SR-IOV network adapter.

![stack diagram showing a sr-iov adapter underneath a management parent partition communicating using a vm bus communicating to child partition \#1 containing a guest operating system communicating using a vm bus, in addition child partition \#2 is communicating using a vf miniport to the sr-iov adapter](images/sriovdatapaths.png)

The NetVSC exposes a Virtual Machine (VM) network adapter which is bound to the VF miniport driver to support the VF data path. During the transition to the synthetic data path, the VF network adapter is gracefully removed if possible from the guest operating system. If the VF cannot be removed gracefully and times out, it will be surprise removed. Then the VF miniport driver is halted, and the Network Virtual Service Client (NetVSC) is unbound from the VF miniport driver.

The transition between the VF and synthetic data paths occurs with minimum loss of packets and prevents the loss of TCP connections. Before the transition to the synthetic data path is complete, the virtualization stacks follows these steps:

1.  The virtualization stack moves the Media Access Control (MAC) and Virtual LAN (VLAN) filters for the VM network adapter to the default Virtual Port (VPort) that is attached to the PCIe Physical Function (PF). The VM network adapter is exposed in the guest operating system of the child partition.

    After the filters are moved to the default VPort, the synthetic data path is fully operational for network traffic to and from the networking components that run in the guest operating system. The PF miniport driver indicates received packets on the default PF VPort which uses the synthetic data path to indicate the packets to the guest operating system. Similarly, all transmitted packets from the guest operating system are routed through the synthetic data path and transmitted through the default PF VPort.

    For more information about VPorts, see [Virtual Ports (VPorts)](virtual-ports--vports-.md).

2.  The virtualization stack deletes the VPort that is attached to the VF by issuing an Object Identifier (OID) set request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451818) to the PF miniport driver. The miniport driver frees any hardware and software resources associated with the VPort and completes the OID request.

    For more information, see [Deleting a Virtual Port](deleting-a-virtual-port.md).

3.  The virtualization stack requests a PCIe Function Level Reset (FLR) of the VF before its resources are deallocated. The stack does this by issuing an OID set request of [OID\_SRIOV\_RESET\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451889)to the PF miniport driver. The FLR brings the VF on the SR-IOV network adapter into a quiescent state and clears any pending interrupt events for the VF.

4.  After the VF has been reset, the virtualization stack requests a deallocation of the VF resources by issuing an OID set request of [OID\_NIC\_SWITCH\_FREE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451822) to the PF miniport driver. This causes the miniport driver to free the hardware resources associated with the VF.

For more information about this process, see [Virtual Function Teardown Sequence](virtual-function-teardown-sequence.md).

 

 





