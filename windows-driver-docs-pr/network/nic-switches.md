---
title: NIC Switches
description: NIC Switches
ms.assetid: 7681DBB2-6645-4B06-9D95-64E7FD379029
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NIC Switches


A network adapter that supports single root I/O virtualization (SR-IOV) must implement a hardware bridge that forwards network traffic between the physical port on the adapter and internal [virtual ports (VPorts)](virtual-ports--vports-.md). This bridge is known as the *NIC switch* and is shown in the following figure.

![stack diagram showing sr-iov adapter with a management parent partition and two child partitions containing guest operating systems](images/sriovarchitecture.png)

Each NIC switch contains the following components:

-   One external, or *physical*, port that provides network connectivity to the external physical network.

-   One internal port that provides the PCI Express (PCIe) Physical Function (PF) on the network adapter with access to the external physical network. An internal port is known as a *virtual port (VPort)*.

    The PF always has a VPort that is created and assigned to it. This VPort is known as the *default VPort*, and is referenced by the DEFAULT\_VPORT\_ID identifier.

    For more information about VPorts, see [Virtual Ports (VPorts)](virtual-ports--vports-.md).

-   One or more VPorts that provide a PCIe Virtual Function (VF) on the network adapter with access to the external physical network.

    **Note**  Additional VPorts can be created and allocated to the PF for network access.

     

**Note**  Starting with NDIS 6.30 in Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*, and is referenced by the NDIS\_DEFAULT\_SWITCH\_ID identifier.

 

The hardware resources for the NIC switch are managed by the PF miniport driver for the SR-IOV network adapter. The driver creates and configures the NIC switch through one of the following methods:

-   Static creation based on standardized SR-IOV and NIC switch INF keywords. For more information on these keywords, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

-   Dynamic creation based on object identifier (OID) method requests of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451815). NDIS or the Hyper-V extensible switch module issues these OID requests to create NIC switches on the SR-IOV network adapter.

For more information on how NIC switches are created, configured, and managed, see [Managing NIC Switches](managing-nic-switches.md).

 

 





