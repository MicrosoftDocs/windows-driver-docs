---
title: SR-IOV OIDs
description: This section describes Single Root I/O Virtualization (SR-IOV) OIDs and their characteristics.
keywords: ["SR-IOV OIDs", "Single Root I/O Virtualization OIDs", "WDK SR-IOV OIDs", "SR-IOV object identifiers"]
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


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")