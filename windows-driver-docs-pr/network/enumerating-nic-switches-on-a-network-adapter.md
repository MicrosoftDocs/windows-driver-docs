---
title: Enumerating NIC Switches on a Network Adapter
description: Enumerating NIC Switches on a Network Adapter
ms.assetid: 0799A879-2BC0-43C5-A6B6-6D46C74A26FB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating NIC Switches on a Network Adapter


An overlying driver or user application can obtain a list of all NIC switches that have been created on a network adapter that supports single root I/O virtualization (SR-IOV). The driver or application issues an object identifier (OID) query request of [OID\_NIC\_SWITCH\_ENUM\_SWITCHES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-enum-switches) to obtain this list.

After a successful return from this OID request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to a buffer that contains the following:

-   An [**NDIS\_NIC\_SWITCH\_INFO\_ARRAY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_nic_switch_delete_vport_parameters) structure that defines the number of elements within the array.

-   An array of [**NDIS\_NIC\_SWITCH\_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_nic_switch_info) structures. Each of these structures contains the information about a single NIC switch created on the network adapter.

    **Note**  If the network adapter has no NIC switches, the driver sets the **NumElements** member of the [**NDIS\_NIC\_SWITCH\_INFO\_ARRAY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_nic_switch_delete_vport_parameters) structure to zero and no [**NDIS\_NIC\_SWITCH\_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_nic_switch_info) structures are returned.

     

**Note**  Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*, and is referenced by the NDIS\_DEFAULT\_SWITCH\_ID identifier.

 

NDIS handles the [OID\_NIC\_SWITCH\_ENUM\_SWITCHES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-enum-switches) request for miniport drivers. NDIS returns the information from an internal cache of the data that it maintains from the following sources:

-   The standardized SR-IOV keyword settings in the registry. For more information on these keywords, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

-   OID requests of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-create-switch) and [OID\_NIC\_SWITCH\_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-parameters).

**Note**  NDIS also provides the enumeration of the switches in the **NicSwitchArray** member in the [**NDIS\_BIND\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_bind_parameters) and [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_filter_attach_parameters) structures. Therefore, the overlying protocol and filter drivers do not have to issue [OID\_NIC\_SWITCH\_ENUM\_SWITCHES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-enum-switches) requests to obtain this information.

 

 

 





