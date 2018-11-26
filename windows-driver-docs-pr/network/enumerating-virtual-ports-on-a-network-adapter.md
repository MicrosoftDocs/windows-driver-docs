---
title: Enumerating Virtual Ports on a Network Adapter
description: Enumerating Virtual Ports on a Network Adapter
ms.assetid: 437C3356-4CC7-4128-9E61-FD01157F4FD9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Virtual Ports on a Network Adapter


An overlying driver or user application can obtain a list of all virtual ports (VPorts) on a NIC switch of a network adapter that supports single root I/O virtualization (SR-IOV). The driver or application issues an object identifier (OID) method request of [OID\_NIC\_SWITCH\_ENUM\_VPORTS](https://msdn.microsoft.com/library/windows/hardware/hh451821) to obtain this list.

After a successful return from this OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer that contains the following:

-   An [**NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451595) structure that defines the number of elements within the array.

-   An array of [**NDIS\_NIC\_SWITCH\_VPORT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451594) structures. Each of these structures contains information about a VPort on the network adapter's NIC switch.

    **Note**  If no VPorts have been created on the network adapter, the driver sets the **NumElements** member of the [**NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451595) structure to zero and no [**NDIS\_NIC\_SWITCH\_VPORT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451594) structures are returned.

     

Before the overlying driver or user application issues the [OID\_NIC\_SWITCH\_ENUM\_VPORTS](https://msdn.microsoft.com/library/windows/hardware/hh451821) request, it must initialize an [**NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh451595) structure that is passed along with the request. The driver or application must follow these guidelines when initializing the **NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY** structure:

-   If the NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY\_ENUM\_ON\_SPECIFIC\_SWITCH flag is set in the **Flags** member, information is returned for all VPorts created on a specified NIC switch. The NIC switch is specified by the **SwitchId** member of that structure.

    **Note**  Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*, and is referenced by the NDIS\_DEFAULT\_SWITCH\_ID identifier. Regardless of the flags that are set in the **Flags** member, the **SwitchId** member must be set to NDIS\_DEFAULT\_SWITCH\_ID.

     

-   If the NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY\_ENUM\_ON\_SPECIFIC\_FUNCTION flag is set in the **Flags** member, information is returned for all VPorts attached to a specified PCI Express (PCIe) Physical Function (PF) or Virtual Function (VF) on the network adapter. The PF or VF is specified by the **AttachedFunctionId** member of that structure.

    If the **AttachedFunctionId** member is set to NDIS\_PF\_FUNCTION\_ID, information is returned for all VPorts. This includes the default VPort that is attached to the PF. If the **AttachedFunctionId** member is set to a valid VF identifier, information is returned for all VPorts attached to the specified VF.

    **Note**  Starting with Windows Server 2012, only one nondefault VPort can be attached to a VF. However, multiple VPorts (including the default VPort) can be attached to the PF.

     

-   If the **Flags** member is set to zero, information is returned for all VPorts attached to the PF or VF on the network adapter. In this case, the values of the **SwitchId** and **AttachedFunctionId** are ignored.

NDIS handles the [OID\_NIC\_SWITCH\_ENUM\_VPORTS](https://msdn.microsoft.com/library/windows/hardware/hh451821) request for miniport drivers. NDIS returns the information from an internal cache of the data that it maintains from inspecting the following sources:

-   OID method requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816).

-   OID set requests of [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451825).

 

 





