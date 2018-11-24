---
title: Querying the Parameters of a Virtual Function
description: Querying the Parameters of a Virtual Function
ms.assetid: D834762D-9141-4F0F-B76D-5C8ABB016B64
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying the Parameters of a Virtual Function


An overlying driver or a user-mode application can obtain the current parameters for a PCI Express (PCIe) Virtual Function (VF) on a network adapter that supports single root I/O virtualization (SR-IOV). The driver or application issues an object identifier (OID) method request of [OID\_NIC\_SWITCH\_VF\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451824) to obtain these parameters.

Before the overlying driver issues this OID method request, it must initialize an [**NDIS\_NIC\_SWITCH\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451593) structure. The driver or application must set the **VFId** member to the identifier of the VF for which parameters are to be returned. The VF identifier can be obtained in the following ways:

-   By issuing an OID method request of [OID\_NIC\_SWITCH\_ENUM\_VFS](https://msdn.microsoft.com/library/windows/hardware/hh451820).

    If this OID request is completed successfully, the overlying driver or user-mode application receives a list of all VFs allocated on the network adapter. Each element within the list is an [**NDIS\_NIC\_SWITCH\_VF\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451591) structure, with the VF identifier specified by the **VFId** member.

-   By issuing an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814).

    If this OID request is completed successfully, the overlying driver receives the identifier of the newly created VF in the **VFId** member of the returned [**NDIS\_NIC\_SWITCH\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451593) structure.

    **Note**  Only overlying drivers can obtain the VF identifier in this manner.

     

After a successful return from the OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451593) structure. This structure contains the configuration parameters for the specified VF.

NDIS handles the [OID\_NIC\_SWITCH\_VF\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451824) request for miniport drivers. NDIS returns the information from an internal cache of the data that it maintains from inspecting the following sources:

-   OID method requests of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814).

-   OID set requests of [OID\_NIC\_SWITCH\_VF\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451824).

 

 





