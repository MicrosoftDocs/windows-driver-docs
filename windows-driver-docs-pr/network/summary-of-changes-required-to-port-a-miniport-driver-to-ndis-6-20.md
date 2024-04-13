---
title: Summary of changes to port a miniport driver to NDIS 6.20
description: Summary of Changes Required to Port a Miniport Driver to NDIS 6.20
keywords:
- NDIS 6.20 WDK , porting miniport drivers
- porting miniport drivers to NDIS 6.20 WDK
- miniport drivers WDK
- miniport drivers WDK , porting to NDIS 6.20
ms.date: 03/02/2023
---

# Summary of Changes Required to Port a Miniport Driver to NDIS 6.20





This topic summarizes the changes that are required to port an NDIS 6.x miniport driver to NDIS 6.20.

NDIS 6.20 retains backward compatibility with earlier NDIS versions. For more information about backward compatibility, see [NDIS 6.20 Backward Compatibility](ndis-6-20-backward-compatibility.md).

To update a miniport driver to support the NDIS 6.20 environment, you must modify the NDIS 6.x miniport driver as follows:

<a href="" id="build-environment"></a>**Build Environment**  
Replace the preprocessor definition NDIS60\_MINIPORT\_DRIVER or NDIS61\_MINIPORT\_DRIVER with NDIS620\_MINIPORT\_DRIVER.

<a href="" id="general-porting-requirements"></a>**General Porting Requirements**  
-   Replace obsolete interfaces with NDIS 6.20 versions. For more information about obsolete interfaces, see [Obsolete Interfaces in NDIS 6.20](obsolete-interfaces-in-ndis-6-20.md).

-   Update the following interfaces to support more than 64 processors:

    -   Receive side scaling (RSS)
    -   Processor information device driver interfaces
    -   Resource allocation
    -   Read and write locks

    For more information about supporting more than 64 processors, see [Support for More than 64 Processors in NDIS 6.20](support-for-more-than-64-processors-in-ndis-6-20.md).

<a href="" id="driver-initialization"></a>**Driver Initialization**  
-   Set the NDIS version to 6.20 in the **MajorNdisVersion** and **MinorNdisVersion** members of the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure, which is passed to the [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) function.

-   Set the miniport driver version in the **MajorDriverVersion** and **MinorDriverVersion** members of the NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS structure to an appropriate driver-specific value.

-   Define direct OID request entry points in the NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS structure. Support for the direct OID request interface was optional for NDIS 6.1 drivers but it is mandatory for NDIS 6.20 drivers. For more information about the miniport driver direct OID request interface, see [Miniport Adapter OID Requests](miniport-adapter-oid-requests.md).

<a href="" id="miniport-adapter-initialization"></a>**Miniport Adapter Initialization**  
-   Use the latest version of the miniport adapter capabilities advertisement interfaces. The following interfaces have updated capabilities:
    -   Power Management
    -   Receive side scaling (RSS)
    -   Hardware assist (VMQ)
-   Use the updated versions of these structures:

    -   [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes)
    -   [**NDIS\_RESTART\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_restart_general_attributes)
    -   [**NDIS\_RECEIVE\_SCALE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters)
    -   [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_hardware_assist_attributes)

    For information about NDIS structure version information, see [Specifying NDIS Version Information](specifying-ndis-version-information.md).

<a href="" id="send-and-receive-code-paths"></a>**Send and Receive Code Paths**  
-   NDIS 6.20 drivers must support receive-side throttle (RST) in processing receive interrupts. The *ReceiveThrottleParameters* parameters of the [*MiniportInterruptDPC*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_interrupt_dpc) and [*MiniportMessageInterruptDPC*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt_dpc) DPC handler functions point to an [**NDIS\_RECEIVE\_THROTTLE\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_receive_throttle_parameters) structure. On entry to the deferred procedure call (DPC) handler, the **MaxNblsToIndicate** member of the NDIS\_RECEIVE\_THROTTLE\_PARAMETERS structure specifies the maximum number of [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures that the miniport driver should indicate in the DPC. For more information about RST, see [Receive Side Throttle in NDIS 6.20](receive-side-throttle-in-ndis-6-20.md).

-   Use the updated version of the [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structure.

-   Optionally support the virtual machine queue (VMQ) interface. For more information about VMQ, see [Virtual Machine Queue (VMQ) in NDIS 6.20](virtual-machine-queue--vmq--in-ndis-6-20.md).

 

