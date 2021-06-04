---
title: Summary of changes to port a protocol driver to NDIS 6.20
description: Summary of Changes Required to Port a Protocol Driver to NDIS 6.20
keywords:
- NDIS 6.20 WDK , porting protocol drivers
- porting protocol drivers to NDIS 6.20 WDK
- protocol drivers WDK
- protocol drivers WDK , porting to NDIS 6.20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of Changes Required to Port a Protocol Driver to NDIS 6.20





This topic summarizes the changes that are required to port an NDIS 6.*x* protocol driver to NDIS 6.20.

NDIS 6.20 retains backward compatibility with earlier NDIS versions. For more information about backward compatibility, see [NDIS 6.20 Backward Compatibility](ndis-6-20-backward-compatibility.md).

To update a protocol driver to support the NDIS 6.20 environment, you must modify the NDIS 6.x protocol driver as follows:

<a href="" id="build-environment-------"></a>**Build Environment**   
Replace the preprocessor definition NDIS61 or NDIS60 with NDIS620.

<a href="" id="general-porting-requirements-------"></a>**General Porting Requirements**   
-   Replace obsolete interfaces with NDIS 6.20 versions. For more information about obsolete interfaces, see [Obsolete Interfaces in NDIS 6.20](obsolete-interfaces-in-ndis-6-20.md).

-   Update the following interfaces to support more than 64 processors:

    -   Receive side scaling (RSS)
    -   Processor information device driver interfaces
    -   Resource allocation
    -   Read and write locks

    For more information about supporting more than 64 processors, see [Support for More than 64 Processors in NDIS 6.20](support-for-more-than-64-processors-in-ndis-6-20.md).

<a href="" id="driver-initialization-------"></a>**Driver Initialization**   
-   Set the NDIS version to 6.20 in the **MajorNdisVersion** and **MinorNdisVersion** members of the [**NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_driver_characteristics) structure that is passed to the [**NdisRegisterProtocolDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver) function.

-   Set the protocol driver version in the **MajorDriverVersion** and **MinorDriverVersion** members of the NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS structure to an appropriate driver-specific value.

<a href="" id="protocol-bind-and-unbind-operations-------"></a>**Protocol Bind and Unbind Operations**   
-   Use the latest version of the miniport adapter capabilities advertisement interfaces. The following interfaces have updated capabilities:
    -   Power Management
    -   Power Management
    -   Receive side scaling (RSS)
    -   Hardware assist (VMQ)
-   Use the updated versions of these structures:

    -   [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters)
    -   [**NDIS\_OFFLOAD\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload_parameters)

    For information about NDIS structure version information, see [Specifying NDIS Version Information](specifying-ndis-version-information.md).

<a href="" id="send-and-receive-data-paths-------"></a>**Send and Receive Data Paths**   
-   Use the updated version of the [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structure.

-   Optionally support the virtual machine queue (VMQ) interface. For more information about VMQ, see [Virtual Machine Queue (VMQ) in NDIS 6.20](virtual-machine-queue--vmq--in-ndis-6-20.md).

 

