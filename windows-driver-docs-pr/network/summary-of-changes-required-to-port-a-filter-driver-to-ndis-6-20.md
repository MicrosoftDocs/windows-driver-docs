---
title: Summary of Changes Required to Port a Filter Driver to NDIS 6.20
description: Summary of Changes Required to Port a Filter Driver to NDIS 6.20
ms.assetid: faf83399-b9ac-41b3-a891-0142ded422b3
keywords:
- NDIS 6.20 WDK , porting filter drivers
- porting filter drivers to NDIS 6.20 WDK
- filter drivers WDK
- filter drivers WDK , porting to NDIS 6.20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of Changes Required to Port a Filter Driver to NDIS 6.20





This topic summarizes the changes that are required to port an NDIS 6.*x* filter driver to NDIS 6.20.

NDIS 6.20 retains backward compatibility with earlier NDIS versions. For more information about backward compatibility, see [NDIS 6.20 Backward Compatibility](ndis-6-20-backward-compatibility.md).

To update a filter driver to support the NDIS 6.20 environment, you must modify the NDIS 6.x filter driver as follows:

<a href="" id="build-environment"></a>**Build Environment**  
Replace the preprocessor definition NDIS61 or NDIS60 with NDIS620.

<a href="" id="general-porting-requirements"></a>**General Porting Requirements**  
-   Replace obsolete interfaces with NDIS 6.20 versions. For more information about obsolete interfaces, see [Obsolete Interfaces in NDIS 6.20](obsolete-interfaces-in-ndis-6-20.md).

-   Update the following interfaces to support more than 64 processors:

    -   Receive side scaling (RSS)
    -   Processor information device driver interfaces
    -   Resource allocation
    -   Read and write locks

    For more information about supporting more than 64 processors, see [Support for More than 64 Processors in NDIS 6.20](support-for-more-than-64-processors-in-ndis-6-20.md).

<a href="" id="driver-initialization"></a>**Driver Initialization**  
-   Set the NDIS version to 6.20 in the **MajorNdisVersion** and **MinorNdisVersion** members of the [**NDIS\_FILTER\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565515) structure that is passed to the [**NdisFRegisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562608) function.

-   Set the filter driver version in the **MajorDriverVersion** and **MinorDriverVersion** members of the NDIS\_FILTER\_DRIVER\_CHARACTERISTICS structure to an appropriate driver-specific value.

<a href="" id="filter-module-attach-and-detach-operations"></a>**Filter Module Attach and Detach Operations**  
-   Use the latest version of the miniport adapter capabilities advertisement interfaces. The following interfaces have updated capabilities:
    -   Power Management
    -   Receive-side scaling (RSS)
    -   Hardware assist (VMQ)
-   Use the updated versions of these structures:

    -   [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481)
    -   [**NDIS\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566706)

    For information about NDIS structure version information, see [Specifying NDIS Version Information](specifying-ndis-version-information.md).

<a href="" id="send-and-receive-data-paths"></a>**Send and Receive Data Paths**  
-   Use the updated version of the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

-   Optionally support the virtual machine queue (VMQ) interface. For more information about VMQ, see [Virtual Machine Queue (VMQ) in NDIS 6.20](virtual-machine-queue--vmq--in-ndis-6-20.md).

 

 





