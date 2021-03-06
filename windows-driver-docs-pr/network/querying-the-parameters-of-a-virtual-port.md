---
title: Querying the Parameters of a Virtual Port
description: Querying the Parameters of a Virtual Port
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying the Parameters of a Virtual Port


An overlying driver can obtain the parameters for a virtual port (VPort) on a NIC switch on a network adapter that supports single root I/O virtualization (SR-IOV). The driver issues an object identifier (OID) method request of [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](./oid-nic-switch-vport-parameters.md) to obtain these parameters.

Before the overlying driver issues this OID method request, it must initialize an [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure. The driver must set the members of this structure in the following way:

-   The **SwitchId** member must be set to the identifier of the NIC switch for which parameters are to be returned.

    **Note**  Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*. The **SwitchId** member must be set to NDIS\_DEFAULT\_SWITCH\_ID.

     

-   The **VPortId** member must be set to the identifier associated with the VPort. The overlying driver obtains the VPort identifier through one of the following ways:

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md).

    -   From a previous OID method request of [OID\_NIC\_SWITCH\_ENUM\_VPORTS](./oid-nic-switch-enum-vports.md).

After a successful return from this OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure. This structure contains the parameters for the specified VPort.

NDIS handles the [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](./oid-nic-switch-vport-parameters.md) request for miniport drivers. NDIS returns the information from an internal cache of the data that it maintains from inspecting the following sources:

-   OID method requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md).

-   OID set requests of [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](./oid-nic-switch-vport-parameters.md).

 

