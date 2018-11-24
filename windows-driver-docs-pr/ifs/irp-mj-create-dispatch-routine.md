---
title: IRP_MJ_CREATE Dispatch Routine
description: IRP_MJ_CREATE Dispatch Routine
ms.assetid: 1ff7915a-0949-43fe-9cf4-c0ad9abf6592
keywords:
- IRP_MJ_CREATE
- security WDK file systems , adding security checks
- security checks WDK file systems , IRP_MJ_CREATE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_CREATE Dispatch Routine


A major portion of Windows security checking occurs inside the [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) dispatch routine. This is because the bulk of the Windows security model is related to access validation. Access validation results are stored as part of the handle that is created as a result of this operation. Subsequent operations are validated against the rights computed at this point.

If the access rights on the file change after the file or directory has been opened, the original access rights provided during the IRP\_MJ\_CREATE operation continue to be valid. These access rights are associated with the handle, so as long as the handle persists, the access granted under it governs subsequent operations.

This section includes the following topics:

[Checking for Traverse Privilege on IRP\_MJ\_CREATE](checking-for-traverse-privilege-on-irp-mj-create.md)

[Checking for Other Special Cases on IRP\_MJ\_CREATE](checking-for-other-special-cases--on-irp-mj-create.md)

[Adding Auditing on IRP\_MJ\_CREATE](adding-auditing-on-irp-mj-create.md)

[Management of Access Control Lists on IRP\_MJ\_CREATE](management-of-access-control-lists-on-irp-mj-create.md)

[Assigning Security to a New File on IRP\_MJ\_CREATE](assigning-security-to-a-new-file-on-irp-mj-create.md)

[Handling Quotas on IRP\_MJ\_CREATE](handling-quotas-on-irp-mj-create.md)

 

 




