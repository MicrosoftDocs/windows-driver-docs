---
title: SR-IOV OIDs
description: This section describes Single Root I/O Virtualization (SR-IOV) OIDs and their characteristics.
keywords: ["SR-IOV OIDs", "Single Root I/O Virtualization OIDs", "WDK SR-IOV OIDs", "SR-IOV object identifiers"]
ms.date: 04/20/2017
---

# SR-IOV OIDs

The single root I/O virtualization (SR-IOV) object identifiers (OIDs) apply to miniport and overlying drivers that support the SR-IOV interface. This interface is supported in NDIS version 6.30 and later versions. 

The following table defines the characteristics of the SR-IOV OIDs. The following abbreviations are used to specify the OIDs' characteristics in the table.

- Q  
The OID is used only in query requests.
- S  
The OID is used only in set requests.
- M  
The OID is used only in method requests. These requests could be issued for set or query operations.
- N  
The OID request is handled directly by NDIS and not by the miniport driver. The driver will not be issued these OIDs.
- P  
The OID request is issued only to the miniport driver of the network adapter's physical function (PF).  
The PF driver must support these OIDs. The driver must also list these OIDs in the **SupportedOidList** member of the [NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure that the driver passes in the *MiniportAttributes* parameter of the call to [NdisMSetMiniportAttributes](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes).
- V  
The OID request is issued only to the miniport driver of one of the network's virtual functions (VFs).  
The VF driver must support these OIDs. The driver must also list these OIDs in the **SupportedOidList** member of the [NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure that the driver passes in the *MiniportAttributes* parameter of the call to [NdisMSetMiniportAttributes](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes).

| Name                                                                                                 | Q | S | M | N | P | V |
|---                                                                                                   |---|---|---|---|---|---|
| [OID_NIC_SWITCH_ALLOCATE_VF](./oid-nic-switch-allocate-vf.md)           |   |   | X |   | X |   | 
| [OID_NIC_SWITCH_CREATE_SWITCH](./oid-nic-switch-create-switch.md)         |   |   | X |   | X |   | 
| [OID_NIC_SWITCH_CREATE_VPORT](./oid-nic-switch-create-vport.md)          |   |   | X |   | X |   |
| [OID_NIC_SWITCH_CURRENT_CAPABILITIES](./oid-nic-switch-current-capabilities.md)  | X |   |   | X |   |   |  
| [OID_NIC_SWITCH_DELETE_SWITCH](./oid-nic-switch-delete-switch.md)         |   | X |   |   | X |   |  
| [OID_NIC_SWITCH_DELETE_VPORT](./oid-nic-switch-delete-vport.md)          |   | X |   |   | X |   | 
| [OID_NIC_SWITCH_ENUM_SWITCHES](./oid-nic-switch-enum-switches.md)         | X |   |   | X |   |   |   
| [OID_NIC_SWITCH_ENUM_VFS](./oid-nic-switch-enum-vfs.md)              | X |   |   | X |   |   |   
| [OID_NIC_SWITCH_ENUM_VPORTS](./oid-nic-switch-enum-vports.md)           | X |   |   | X |   |   |  
| [OID_NIC_SWITCH_FREE_VF](./oid-nic-switch-free-vf.md)               |   | X |   |   | X |   | 
| [OID_NIC_SWITCH_HARDWARE_CAPABILITIES](./oid-nic-switch-hardware-capabilities.md) | X |   |   | X |   |   |   
| [OID_NIC_SWITCH_PARAMETERS](./oid-nic-switch-parameters.md)            |   |   | X |   | X |   | 
| [OID_NIC_SWITCH_VF_PARAMETERS](./oid-nic-switch-vf-parameters.md)         |   |   | X |   | X |   | 
| [OID_NIC_SWITCH_VPORT_PARAMETERS](./oid-nic-switch-vport-parameters.md)      |   |   | X |   | X |   | 
| [OID_SRIOV_BAR_RESOURCES](./oid-sriov-bar-resources.md)              |   | X |   |   | X |   | 
| [OID_SRIOV_CURRENT_CAPABILITIES](./oid-sriov-current-capabilities.md)       | X |   |   | X |   |   |   
| [OID_SRIOV_HARDWARE_CAPABILITIES](./oid-sriov-hardware-capabilities.md)      | X |   |   | X |   |   |   
| [OID_SRIOV_PF_LUID](./oid-sriov-pf-luid.md)                    | X |   |   | X |   |   |   
| [OID_SRIOV_PROBED_BARS](./oid-sriov-probed-bars.md)                | X |   |   |   | X |   | 
| [OID_SRIOV_READ_VF_CONFIG_BLOCK](./oid-sriov-read-vf-config-block.md)       |   |   | X |   | X |   | 
| [OID_SRIOV_READ_VF_CONFIG_SPACE](./oid-sriov-read-vf-config-space.md)       |   |   | X |   | X |   | 
| [OID_SRIOV_RESET_VF](./oid-sriov-reset-vf.md)                   |   | X |   |   | X |   | 
| [OID_SRIOV_SET_VF_POWER_STATE](./oid-sriov-set-vf-power-state.md)         |   | X |   |   | X |   |  
| [OID_SRIOV_VF_INVALIDATE_CONFIG_BLOCK](./oid-sriov-vf-invalidate-config-block.md) |   |   | X |   |   | X | 
| [OID_SRIOV_VF_SERIAL_NUMBER](./oid-sriov-vf-serial-number.md)           | X |   |   | X |   |   |   
| [OID_SRIOV_VF_VENDOR_DEVICE_ID](./oid-sriov-vf-vendor-device-id.md)        |   |   | X |   | X |   | 
| [OID_SRIOV_WRITE_VF_CONFIG_BLOCK](./oid-sriov-write-vf-config-block.md)      |   | X |   |   | X |   | 
| [OID_SRIOV_WRITE_VF_CONFIG_SPACE](./oid-sriov-write-vf-config-space.md)      |   | X |   |   | X |   |
