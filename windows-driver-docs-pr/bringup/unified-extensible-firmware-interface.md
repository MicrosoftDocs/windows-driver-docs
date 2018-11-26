---
title: Unified extensible firmware interface (UEFI) 
description: Unified extensible firmware interface (UEFI) 
ms.date: 05/07/2018
ms.localizationpriority: medium
---


# Unified extensible firmware interface (UEFI) 


As of Windows 10, version 1703 (at the time this document was written), Microsoft requires UEFI Specification version 2.3.1c. Since UEFI.org has continued to update specification documents and improve the source with these updates, this requirement will eventually change.

Within Microsoft, we felt that there was some wording ambiguity in UEFI specification 2.5 and 2.6. Therefore we have not updated to these specification versions. However, the specification version does not affect the UEFI Source code tree. 

When implementing UEFI code, please ensure that your source branch is built using the latest bits from the main branch and built using the guidance from the latest UEFI Specification document.

There are features that are updated in the UEFI Specification documents that pertain to various security features. For example UEFI Spec 2.6, page 107 in section "4.6 EFI Configuration Table & Properties Table" specifically adds in support for "EFI_MEMORY_ATTRIBUTES_TABLE".

-   Memory Attributes Table (MAT):

    -   EFI\_MEMORY\_ATTRIBUTES\_TABLE. The entire UEFI runtime must be described by this table.

    -   All entries must include attributes EFI\_MEMORY\_RO, EFI\_MEMORY\_XP, or both. Memory MUST be either readable and executable OR writeable and non-executable.

As of Windows 10, version 1703, the latest updates to the UEFI Specification regarding Secure Boot modes are not fully supported by Windows. Support for new Secure Boot Modes is being investigated for a future Windows release.

## Related resources

[UEFI Specification Documents](https://www.uefi.org/specifications)





