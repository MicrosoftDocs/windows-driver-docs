---
title: SR-IOV OIDs
description: This section describes Single Root I/O Virtualization (SR-IOV) OIDs and their characteristics.
keywords: ["SR-IOV OIDs", "Single Root I/O Virtualization OIDs", "WDK SR-IOV OIDs", "SR-IOV object identifiers"]
ms.assetid: E93751BF-17BC-4BE7-89F7-53F6C9941120
ms.date: 04/20/2017
ms.localizationpriority: medium
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
The PF driver must support these OIDs. The driver must also list these OIDs in the **SupportedOidList** member of the [NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure that the driver passes in the *MiniportAttributes* parameter of the call to [NdisMSetMiniportAttributes](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes).
- V  
The OID request is issued only to the miniport driver of one of the network's virtual functions (VFs).  
The VF driver must support these OIDs. The driver must also list these OIDs in the **SupportedOidList** member of the [NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure that the driver passes in the *MiniportAttributes* parameter of the call to [NdisMSetMiniportAttributes](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes).

| Name                                                                                                 | Q | S | M | N | P | V |
|---                                                                                                   |---|---|---|---|---|---|
| [OID_NIC_SWITCH_ALLOCATE_VF](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-allocate-vf)           |   |   | X |   | X |   | 
| [OID_NIC_SWITCH_CREATE_SWITCH](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-create-switch)         |   |   | X |   | X |   | 
| [OID_NIC_SWITCH_CREATE_VPORT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-create-vport)          |   |   | X |   | X |   |
| [OID_NIC_SWITCH_CURRENT_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-current-capabilities)  | X |   |   | X |   |   |  
| [OID_NIC_SWITCH_DELETE_SWITCH](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-delete-switch)         |   | X |   |   | X |   |  
| [OID_NIC_SWITCH_DELETE_VPORT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-delete-vport)          |   | X |   |   | X |   | 
| [OID_NIC_SWITCH_ENUM_SWITCHES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-enum-switches)         | X |   |   | X |   |   |   
| [OID_NIC_SWITCH_ENUM_VFS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-enum-vfs)              | X |   |   | X |   |   |   
| [OID_NIC_SWITCH_ENUM_VPORTS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-enum-vports)           | X |   |   | X |   |   |  
| [OID_NIC_SWITCH_FREE_VF](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-free-vf)               |   | X |   |   | X |   | 
| [OID_NIC_SWITCH_HARDWARE_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-hardware-capabilities) | X |   |   | X |   |   |   
| [OID_NIC_SWITCH_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-parameters)            |   |   | X |   | X |   | 
| [OID_NIC_SWITCH_VF_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-vf-parameters)         |   |   | X |   | X |   | 
| [OID_NIC_SWITCH_VPORT_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-vport-parameters)      |   |   | X |   | X |   | 
| [OID_SRIOV_BAR_RESOURCES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-bar-resources)              |   | X |   |   | X |   | 
| [OID_SRIOV_CURRENT_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-current-capabilities)       | X |   |   | X |   |   |   
| [OID_SRIOV_HARDWARE_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-hardware-capabilities)      | X |   |   | X |   |   |   
| [OID_SRIOV_PF_LUID](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-pf-luid)                    | X |   |   | X |   |   |   
| [OID_SRIOV_PROBED_BARS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-probed-bars)                | X |   |   |   | X |   | 
| [OID_SRIOV_READ_VF_CONFIG_BLOCK](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-read-vf-config-block)       |   |   | X |   | X |   | 
| [OID_SRIOV_READ_VF_CONFIG_SPACE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-read-vf-config-space)       |   |   | X |   | X |   | 
| [OID_SRIOV_RESET_VF](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-reset-vf)                   |   | X |   |   | X |   | 
| [OID_SRIOV_SET_VF_POWER_STATE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-set-vf-power-state)         |   | X |   |   | X |   |  
| [OID_SRIOV_VF_INVALIDATE_CONFIG_BLOCK](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-vf-invalidate-config-block) |   |   | X |   |   | X | 
| [OID_SRIOV_VF_SERIAL_NUMBER](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-vf-serial-number)           | X |   |   | X |   |   |   
| [OID_SRIOV_VF_VENDOR_DEVICE_ID](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-vf-vendor-device-id)        |   |   | X |   | X |   | 
| [OID_SRIOV_WRITE_VF_CONFIG_BLOCK](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-write-vf-config-block)      |   | X |   |   | X |   | 
| [OID_SRIOV_WRITE_VF_CONFIG_SPACE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-write-vf-config-space)      |   | X |   |   | X |   |


