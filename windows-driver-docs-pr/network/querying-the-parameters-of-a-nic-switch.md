---
title: Querying the Parameters of a NIC Switch
description: Querying the Parameters of a NIC Switch
ms.date: 04/20/2017
---

# Querying the Parameters of a NIC Switch


An overlying driver or user application can obtain the parameters for a NIC switch that has been created on a network adapter that supports single root I/O virtualization (SR-IOV). The driver or application issues an object identifier (OID) method request of [OID\_NIC\_SWITCH\_PARAMETERS](./oid-nic-switch-parameters.md) to obtain these parameters.

Before the overlying driver or user application issues this OID method request, it must initialize an [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure. The driver or application must set the **SwitchId** member to the identifier of the NIC switch for which parameters are to be returned.

**Note**  Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*, and is referenced by the NDIS\_DEFAULT\_SWITCH\_ID identifier.

 

After a successful return from this OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure. This structure contains the parameters for the specified switch.

NDIS handles the [OID\_NIC\_SWITCH\_PARAMETERS](./oid-nic-switch-parameters.md) request for miniport drivers. NDIS returns the information from an internal cache of the data that it maintains from the following sources:

-   The standardized SR-IOV keyword settings in the registry. For more information on these keywords, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

-   OID requests of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](./oid-nic-switch-create-switch.md) and [OID\_NIC\_SWITCH\_PARAMETERS](./oid-nic-switch-parameters.md).

 

