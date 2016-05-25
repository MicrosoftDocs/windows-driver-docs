---
title: IRP\_MJ\_CREATE Dispatch Routine
author: windows-driver-content
description: IRP\_MJ\_CREATE Dispatch Routine
ms.assetid: 1ff7915a-0949-43fe-9cf4-c0ad9abf6592
keywords: ["IRP_MJ_CREATE", "security WDK file systems , adding security checks", "security checks WDK file systems , IRP_MJ_CREATE"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP_MJ_CREATE%20Dispatch%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


