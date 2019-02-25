---
title: Moving a Receive Filter to a Virtual Port
description: Moving a Receive Filter to a Virtual Port
ms.assetid: 6315FB18-3F57-43C2-B864-3759058092BB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Moving a Receive Filter to a Virtual Port


The overlying driver issues an object identifier (OID) set request of [OID\_RECEIVE\_FILTER\_MOVE\_FILTER](https://msdn.microsoft.com/library/windows/hardware/hh451845) to move a receive filter from a virtual port (VPort) to another VPort on the NIC switch. Typically, the overlying driver, such as the virtualization stack, issues this OID request if any of the following conditions are true:

-   The virtualization stack sets a receive filter on the default VPort. This filter contains the media access control (MAC) address and virtual LAN (VLAN) parameters for the virtual machine (VM) network adapter that is exposed in the Hyper-V child partition. This allows packets to be forwarded between the VM network adapter and the underlying network adapter over the software-based synthetic data path.

    After resources for a PCI Express (PCIe) Virtual Function (VF) are allocated and the VF is attached to a child partition, the virtualization stack creates a nondefault VPort on the VF. The virtualization stack then moves the receive filter for the VM network adapter from the default VPort to the nondefault VPort attached to the VF. This allows packets to be forwarded between the VM network adapter and the underlying network adapter over the hardware-based VF data path.

    For more information about these data paths, see [SR-IOV Data Paths](sr-iov-data-paths.md).

-   A VF has been detached from a Hyper-V child partition in which the guest operating system is still running. In this case, the overlying driver issues the OID set request to move the receive filter for the VM network adapter from the nondefault VPort to the default VPort attached to the PF. When this happens, packet traffic reverts to the synthetic data path.

To move a receive filter from one VPort to another VPort, an overlying driver issues an OID set request of [OID\_RECEIVE\_FILTER\_MOVE\_FILTER](https://msdn.microsoft.com/library/windows/hardware/hh451845). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_MOVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567166) structure.

Before the overlying driver issues the [OID\_RECEIVE\_FILTER\_MOVE\_FILTER](https://msdn.microsoft.com/library/windows/hardware/hh451845) request, it must initialize an [**NDIS\_RECEIVE\_FILTER\_MOVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451651) structure in the following way:

-   The driver sets the **FilterId** member to the identifier of the identifier of the previously allocated receive filter.

    **Note**  The overlying driver obtained the filter identifier from an earlier OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) or [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569787).

     

-   The driver sets the **SourceQueueId** member to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

-   The driver sets the **SourceVPortId** member to the identifier of the VPort on which this filter was previously set.

-   The driver sets the **DestQueueId** member to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

-   The driver sets the **DestVPortId** member to the identifier of the VPort on which this filter is to be moved.

NDIS validates the members of the [**NDIS\_RECEIVE\_FILTER\_MOVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451651) before it forwards the OID set request to the PF miniport driver.

When the PF miniport driver handles this OID set request, it must move the receive filter in an atomic operation. The driver must be able to configure the network adapter to simultaneously remove the filter from a receive queue and VPort and set it on a different receive queue and VPort.

 

 





