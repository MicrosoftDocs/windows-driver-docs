---
title: Enumerating Virtual Ports on a Network Adapter
description: Enumerating Virtual Ports on a Network Adapter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Virtual Ports on a Network Adapter


An overlying driver or user application can obtain a list of all virtual ports (VPorts) on a NIC switch of a network adapter that supports single root I/O virtualization (SR-IOV). The driver or application issues an object identifier (OID) method request of [OID\_NIC\_SWITCH\_ENUM\_VPORTS](./oid-nic-switch-enum-vports.md) to obtain this list.

After a successful return from this OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a buffer that contains the following:

-   An [**NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_info_array) structure that defines the number of elements within the array.

-   An array of [**NDIS\_NIC\_SWITCH\_VPORT\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_info) structures. Each of these structures contains information about a VPort on the network adapter's NIC switch.

    **Note**  If no VPorts have been created on the network adapter, the driver sets the **NumElements** member of the [**NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_info_array) structure to zero and no [**NDIS\_NIC\_SWITCH\_VPORT\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_info) structures are returned.

     

Before the overlying driver or user application issues the [OID\_NIC\_SWITCH\_ENUM\_VPORTS](./oid-nic-switch-enum-vports.md) request, it must initialize an [**NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_info_array) structure that is passed along with the request. The driver or application must follow these guidelines when initializing the **NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY** structure:

-   If the NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY\_ENUM\_ON\_SPECIFIC\_SWITCH flag is set in the **Flags** member, information is returned for all VPorts created on a specified NIC switch. The NIC switch is specified by the **SwitchId** member of that structure.

    **Note**  Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*, and is referenced by the NDIS\_DEFAULT\_SWITCH\_ID identifier. Regardless of the flags that are set in the **Flags** member, the **SwitchId** member must be set to NDIS\_DEFAULT\_SWITCH\_ID.

     

-   If the NDIS\_NIC\_SWITCH\_VPORT\_INFO\_ARRAY\_ENUM\_ON\_SPECIFIC\_FUNCTION flag is set in the **Flags** member, information is returned for all VPorts attached to a specified PCI Express (PCIe) Physical Function (PF) or Virtual Function (VF) on the network adapter. The PF or VF is specified by the **AttachedFunctionId** member of that structure.

    If the **AttachedFunctionId** member is set to NDIS\_PF\_FUNCTION\_ID, information is returned for all VPorts. This includes the default VPort that is attached to the PF. If the **AttachedFunctionId** member is set to a valid VF identifier, information is returned for all VPorts attached to the specified VF.

    **Note**  Starting with Windows Server 2012, only one nondefault VPort can be attached to a VF. However, multiple VPorts (including the default VPort) can be attached to the PF.

     

-   If the **Flags** member is set to zero, information is returned for all VPorts attached to the PF or VF on the network adapter. In this case, the values of the **SwitchId** and **AttachedFunctionId** are ignored.

NDIS handles the [OID\_NIC\_SWITCH\_ENUM\_VPORTS](./oid-nic-switch-enum-vports.md) request for miniport drivers. NDIS returns the information from an internal cache of the data that it maintains from inspecting the following sources:

-   OID method requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md).

-   OID set requests of [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](./oid-nic-switch-vport-parameters.md).

 

