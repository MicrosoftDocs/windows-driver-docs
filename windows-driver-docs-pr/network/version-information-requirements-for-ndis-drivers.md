---
title: Version Information Requirements for NDIS Drivers
description: Version Information Requirements for NDIS Drivers
ms.assetid: a05e7dde-d1f9-458d-8d7b-ead9bb9af7af
keywords:
- NDIS version information WDK , NDIS responsibilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Version Information Requirements for NDIS Drivers





NDIS structures that provide version information have a **Header** member that is defined as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure and NDIS drivers must provide support for such version information.

NDIS can support drivers that support a higher or lower NDIS version than the *current version of NDIS* (that is, the version of NDIS that is supported on the version of the operating system that a computer is running). Also the *registered NDIS version* (that is, the version that the driver reported during initialization) of the driver can be lower than the highest version that the driver supports. For example, an NDIS 5.1 driver or an NDIS 6.1 driver can run on a version of the operating system that is running NDIS 6.0. The NDIS 5.1 driver simply registers as an NDIS 5.1 driver during initialization. However, the NDIS 6.1 driver must check the current version of NDIS and must register as a driver that supports the highest level of NDIS that is available (in this example, NDIS 6.0). For more information about how to obtain the current NDIS version, see [Obtaining the NDIS Version](obtaining-the-ndis-version.md).

**Note**  A driver is not required to support all the features in a later revision of a structure. For example, a miniport driver can create a version 2 structure and supply values that are appropriate for a version 1 structure.

 

To access the members in structures that have version information, NDIS drivers must complete the following process:

-   Check the **Header.Revision** and **Header.Size** members before accessing any members in the structure.

-   For earlier version structures (that is, structures that have a lower revision number than the number that is associated with the NDIS version that the driver supports):
    -   The driver must verify that the **Header.Size** value is correct for the **Header.Revision** value. For example, the value of NDIS\_SIZEOF\_Xxx\_REVISION\_1 is correct for Xxx\_REVISION\_1 but it is too small for Xxx\_REVISION\_2.
    -   The **Header.Size** value must be equal to or greater than NDIS\_SIZEOF\_Xxx\_REVISION\_Nn (where *Nn* is the revision number of the structure that the driver is using) and the driver must correctly handle the information in the structure as is appropriate for that revision.
-   For later version structures (that is, structures that have a higher revision number than the number that is associated with the NDIS version that the driver supports), the driver can use the structure as if it were an older revision of the structure. The higher version structure is always compatible with the older version.

-   Drivers must use the correct revision of a structure for the registered NDIS version of the driver. For example, an NDIS 6.1 driver must report its offload capabilities in [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599) structures by setting the members in the [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure to indicate NDIS\_OFFLOAD\_REVISION\_2. However, the driver does not have to support all the features that are included with NDIS\_OFFLOAD\_REVISION\_2.

-   A driver that successfully handles an OID set request must set the **SupportedRevision** member in the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure upon return from the OID set request. The **SupportedRevision** member notifies the initiator of the request of the revision that the driver supported. For example, a miniport driver can create an Xxx\_REVISION\_2 structure, supply values that are appropriate for an Xxx\_REVISION\_1 structure, and fill the rest of the structure with zeros. The miniport driver would report Xxx\_REVISION\_1 in the **SupportedRevision** member. In this case, a protocol driver that can support an Xxx\_REVISION\_2 will use Xxx\_REVISION\_1 information that the miniport driver supported.

-   To determine what information was successfully handled by an underlying driver, overlying drivers that issue OID requests must check the value in the **SupportedRevision** member in the NDIS\_OID\_REQUEST structure after the OID request returns.

## Related topics


[Overview of NDIS versions](overview-of-ndis-versions.md)

[Specifying NDIS Version Information](specifying-ndis-version-information.md)

 

 






