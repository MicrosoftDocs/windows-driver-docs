---
title: Unified extensible firmware interface (UEFI) 
description: Unified extensible firmware interface (UEFI) 
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 05/15/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

[UEFI Specification Documents](http://www.uefi.org/specifications)




--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


