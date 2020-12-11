---
title: Setting the Parameters of a NIC Switch
description: Setting the Parameters of a NIC Switch
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Parameters of a NIC Switch


An overlying driver can change the parameters for a NIC switch that has been created on a network adapter that supports single root I/O virtualization (SR-IOV). The driver issues an object identifier (OID) set request of [OID\_NIC\_SWITCH\_PARAMETERS](./oid-nic-switch-parameters.md) to change these parameters. Only the miniport driver for the PCI Express (PCIe) Physical Function (PF) of the SR-IOV adapter handles this OID set request.

Before the overlying driver issues this OID set request, it must initialize an [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure with the parameters to be changed on the NIC switch. The driver then initializes an [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure for the OID request, and sets the **InformationBuffer** member to a pointer of the **NDIS\_NIC\_SWITCH\_PARAMETERS** structure.

Only a limited subset of configuration parameters for a NIC switch can be changed. The overlying driver specifies the parameter to change by setting the following members of the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure:

-   The **SwitchId** member is set to the identifier of the NIC switch whose parameters will be changed.

    **Note**  Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*. The **SwitchId** member must be set to NDIS\_DEFAULT\_SWITCH\_ID.

     

-   The appropriate NDIS\_NIC\_SWITCH\_PARAMETERS\_*Xxx*\_CHANGED flags are set in the **Flags** member. Members of the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure can only be changed if a corresponding NDIS\_NIC\_SWITCH\_PARAMETERS\_*Xxx*\_CHANGED flag is defined in Ntddndis.h.

-   The members of the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure, which correspond to the NDIS\_NIC\_SWITCH\_PARAMETERS\_*Xxx*\_CHANGED flags set in the **Flags** member, are set with the NIC switch configuration parameters that are to be changed.

    **Note**  Starting with Windows Server 2012, only the **SwitchName** member of the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure can be changed through an OID set request of [OID\_NIC\_SWITCH\_PARAMETERS](./oid-nic-switch-parameters.md).

     

The PF miniport driver must follow these guidelines when it receives the OID set request of [OID\_NIC\_SWITCH\_PARAMETERS](./oid-nic-switch-parameters.md)

-   If the PF miniport driver can apply the changes without requiring a reinitialization of the network adapter, the driver applies the changes to the hardware and completes the OID request with NDIS\_STATUS\_SUCCESS.

    If this status code is returned, NDIS updates the NIC switch configuration information in the registry.

-   If the PF miniport driver requires a reinitialization of the network adapter to apply the changes, the driver completes the OID request with NDIS\_STATUS\_REINIT\_REQUIRED.

    If this status code is returned, NDIS also updates the NIC switch configuration information in the registry. However, the overlying driver that issued the OID set request must reinitialize the network adapter so that the changes can take effect.

    **Note**  PF miniport drivers that support static NIC creation and configuration can return NDIS\_STATUS\_REINIT\_REQUIRED to make sure that the adapter is reinitialized for the new parameters to take effect.

     

-   If the PF miniport driver cannot apply the changes requested in the OID, it must fail the OID and return the appropriate NDIS\_STATUS\_*Xxx* code.

    In this case, NDIS does not update the NIC switch configuration information in the registry.

 

