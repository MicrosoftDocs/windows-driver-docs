---
title: Enumerating NIC Switches on a Network Adapter
description: Enumerating NIC Switches on a Network Adapter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating NIC Switches on a Network Adapter


An overlying driver or user application can obtain a list of all NIC switches that have been created on a network adapter that supports single root I/O virtualization (SR-IOV). The driver or application issues an object identifier (OID) query request of [OID\_NIC\_SWITCH\_ENUM\_SWITCHES](./oid-nic-switch-enum-switches.md) to obtain this list.

After a successful return from this OID request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a buffer that contains the following:

-   An [**NDIS\_NIC\_SWITCH\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_delete_vport_parameters) structure that defines the number of elements within the array.

-   An array of [**NDIS\_NIC\_SWITCH\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_info) structures. Each of these structures contains the information about a single NIC switch created on the network adapter.

    **Note**  If the network adapter has no NIC switches, the driver sets the **NumElements** member of the [**NDIS\_NIC\_SWITCH\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_delete_vport_parameters) structure to zero and no [**NDIS\_NIC\_SWITCH\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_info) structures are returned.

     

**Note**  Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*, and is referenced by the NDIS\_DEFAULT\_SWITCH\_ID identifier.

 

NDIS handles the [OID\_NIC\_SWITCH\_ENUM\_SWITCHES](./oid-nic-switch-enum-switches.md) request for miniport drivers. NDIS returns the information from an internal cache of the data that it maintains from the following sources:

-   The standardized SR-IOV keyword settings in the registry. For more information on these keywords, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

-   OID requests of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](./oid-nic-switch-create-switch.md) and [OID\_NIC\_SWITCH\_PARAMETERS](./oid-nic-switch-parameters.md).

**Note**  NDIS also provides the enumeration of the switches in the **NicSwitchArray** member in the [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) and [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_attach_parameters) structures. Therefore, the overlying protocol and filter drivers do not have to issue [OID\_NIC\_SWITCH\_ENUM\_SWITCHES](./oid-nic-switch-enum-switches.md) requests to obtain this information.

 

 

