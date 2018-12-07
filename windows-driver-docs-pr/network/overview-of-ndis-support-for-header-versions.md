---
title: Overview of NDIS Support for Header Versions
description: Overview of NDIS Support for Header Versions
ms.assetid: f73baf8d-f6da-486c-b0e2-c3c57aeab269
keywords:
- NDIS version information WDK , structure requirements
- NDIS version information WDK , header member
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of NDIS Support for Header Versions





Many NDIS structures include structure version information. NDIS or NDIS drivers initialize the **Header** member in such structures as required for each structure. NDIS drivers should check the version information, if any, in each structure before they access the structure members.

The **Header** member is an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure. This structure contains the revision number, type, and size of the structure that includes the **Header** member.

Structures that include the **Header** member meet the following requirements:

-   The structure will have a new revision value if new information is added to the member list for a new NDIS version. For example, if the NDIS 6.1 version of the structure has new members at the end of the member list, in a union, or in a bitmask, it will have a different revision value from the NDIS 6.0 version.

-   After a structure is changed, the size of the later revision of the structure can be equal to or larger than the size of the earlier revision of the structure, but it will not be smaller. If the new size is larger than the size of the earlier revision, the new members are added at the end of the member list.

-   A structure will only have a new revision if the earlier revision information is still valid and complete. That is, the new version of the structure contains a superset of the older versions members.
    **Note**  If any of the preceding conditions cannot be met, NDIS provides a new structure with a new name that replaces the existing structure instead of providing a revised version of the existing structure.

     

-   NDIS drivers should always use the predefined revision values. NDIS provides such definitions in the form Xxx\_REVISION\_Nn, and NDIS\_SIZEOF\_Xxx\_REVISION\_Nn, for the **Revision** and **Size** members of [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) respectively. Also, Xxx represents the name of the structure and Nn is the revision number. For example, the revision and size for the first revision of the [**NDIS\_FILTER\_PARTIAL\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565544) structure are NDIS\_FILTER\_PARTIAL\_CHARACTERISTICS\_REVISION\_1 and NDIS\_SIZEOF\_FILTER\_PARTIAL\_CHARACTERISTICS\_REVISION\_1 respectively.

-   The **Header.Size** value must be consistent with the **Header.Revision** value. That is, if the **Revision** member contains Xxx\_REVISION\_1, the **Size** member value must be equal to or greater than NDIS\_SIZEOF\_Xxx\_REVISION\_1.

## Related topics


[Overview of NDIS versions](overview-of-ndis-versions.md)

[Specifying NDIS Version Information](specifying-ndis-version-information.md)

 

 






