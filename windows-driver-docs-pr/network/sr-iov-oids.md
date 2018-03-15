---
title: SR-IOV OIDs
description: This section describes Single Root I/O Virtualization (SR-IOV) OIDs and their characteristics.
keywords: ["SR-IOV OIDs", "Single Root I/O Virtualization OIDs", "WDK SR-IOV OIDs", "SR-IOV object identifiers"]
ms.assetid: E93751BF-17BC-4BE7-89F7-53F6C9941120
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
The PF driver must support these OIDs. The driver must also list these OIDs in the **SupportedOidList** member of the [NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure that the driver passes in the *MiniportAttributes* parameter of the call to [NdisMSetMiniportAttributes](https://msdn.microsoft.com/library/windows/hardware/ff563672).
- V  
The OID request is issued only to the miniport driver of one of the network's virtual functions (VFs).  
The VF driver must support these OIDs. The driver must also list these OIDs in the **SupportedOidList** member of the [NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure that the driver passes in the *MiniportAttributes* parameter of the call to [NdisMSetMiniportAttributes](https://msdn.microsoft.com/library/windows/hardware/ff563672).

| Name                                                                                                 | Q | S | M | N | P | V |
|---                                                                                                   |---|---|---|---|---|---|
| [OID_NIC_SWITCH_ALLOCATE_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814)           |   |   | X |   | X |   | 
| [OID_NIC_SWITCH_CREATE_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451815)         |   |   | X |   | X |   | 
| [OID_NIC_SWITCH_CREATE_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816)          |   |   | X |   | X |   |
| [OID_NIC_SWITCH_CURRENT_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569760)  | X |   |   | X |   |   |  
| [OID_NIC_SWITCH_DELETE_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451817)         |   | X |   |   | X |   |  
| [OID_NIC_SWITCH_DELETE_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451818)          |   | X |   |   | X |   | 
| [OID_NIC_SWITCH_ENUM_SWITCHES](https://msdn.microsoft.com/library/windows/hardware/hh451819)         | X |   |   | X |   |   |   
| [OID_NIC_SWITCH_ENUM_VFS](https://msdn.microsoft.com/library/windows/hardware/hh451820)              | X |   |   | X |   |   |   
| [OID_NIC_SWITCH_ENUM_VPORTS](https://msdn.microsoft.com/library/windows/hardware/hh451821)           | X |   |   | X |   |   |  
| [OID_NIC_SWITCH_FREE_VF](https://msdn.microsoft.com/library/windows/hardware/hh451822)               |   | X |   |   | X |   | 
| [OID_NIC_SWITCH_HARDWARE_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569761) | X |   |   | X |   |   |   
| [OID_NIC_SWITCH_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451823)            |   |   | X |   | X |   | 
| [OID_NIC_SWITCH_VF_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451824)         |   |   | X |   | X |   | 
| [OID_NIC_SWITCH_VPORT_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451825)      |   |   | X |   | X |   | 
| [OID_SRIOV_BAR_RESOURCES](https://msdn.microsoft.com/library/windows/hardware/hh451852)              |   | X |   |   | X |   | 
| [OID_SRIOV_CURRENT_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/hh451859)       | X |   |   | X |   |   |   
| [OID_SRIOV_HARDWARE_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/hh451862)      | X |   |   | X |   |   |   
| [OID_SRIOV_PF_LUID](https://msdn.microsoft.com/library/windows/hardware/hh451864)                    | X |   |   | X |   |   |   
| [OID_SRIOV_PROBED_BARS](https://msdn.microsoft.com/library/windows/hardware/hh451870)                | X |   |   |   | X |   | 
| [OID_SRIOV_READ_VF_CONFIG_BLOCK](https://msdn.microsoft.com/library/windows/hardware/hh451874)       |   |   | X |   | X |   | 
| [OID_SRIOV_READ_VF_CONFIG_SPACE](https://msdn.microsoft.com/library/windows/hardware/hh451879)       |   |   | X |   | X |   | 
| [OID_SRIOV_RESET_VF](https://msdn.microsoft.com/library/windows/hardware/hh451889)                   |   | X |   |   | X |   | 
| [OID_SRIOV_SET_VF_POWER_STATE](https://msdn.microsoft.com/library/windows/hardware/hh451896)         |   | X |   |   | X |   |  
| [OID_SRIOV_VF_INVALIDATE_CONFIG_BLOCK](https://msdn.microsoft.com/library/windows/hardware/hh451903) |   |   | X |   |   | X | 
| [OID_SRIOV_VF_SERIAL_NUMBER](https://msdn.microsoft.com/library/windows/hardware/hh451909)           | X |   |   | X |   |   |   
| [OID_SRIOV_VF_VENDOR_DEVICE_ID](https://msdn.microsoft.com/library/windows/hardware/hh451913)        |   |   | X |   | X |   | 
| [OID_SRIOV_WRITE_VF_CONFIG_BLOCK](https://msdn.microsoft.com/library/windows/hardware/hh451918)      |   | X |   |   | X |   | 
| [OID_SRIOV_WRITE_VF_CONFIG_SPACE](https://msdn.microsoft.com/library/windows/hardware/hh451925)      |   | X |   |   | X |   |


