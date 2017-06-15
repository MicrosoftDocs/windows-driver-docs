---
title: Resource Manager Objects
author: windows-driver-content
description: Resource Manager Objects
MS-HAID:
- 'ktm\_dg\_5d3ec12b-c492-47c0-be10-4577cdba88f3.xml'
- 'kernel.resource\_manager\_objects'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b44f2035-ee9f-453b-b12d-89ca36a8b280
keywords: ["resource managers WDK KTM , objects", "resource managers WDK KTM", "resource managers WDK KTM , routines", "Kernel Transaction Manager WDK , resource managers", "KTM WDK , resource managers", "resource manager objects WDK KTM"]
---

# Resource Manager Objects


*Resource manager objects* represent resource managers. Each resource manager must call [**ZwCreateResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff566427) to register itself to KTM.

KTM provides a set of [resource manager object routines](https://msdn.microsoft.com/library/windows/hardware/ff561098) that kernel-mode resource managers can call. KTM also provides a similar set of user-mode routines that user-mode applications can call. For more information about the user-mode routines, see the Microsoft Windows SDK.

KTM creates a resource manager object when a resource manager calls **ZwCreateResourceManager**.

[TPS components](understanding-tps-components.md) can call [**ZwOpenResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff567026) to open additional handles to a resource manager object. But most TPS designs do not require additional open handles.

Resource managers close their handles to resource manager objects by calling [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417). If the last handle is closed, and if the resource manager still has enlistments to transactions that have not been committed, KTM sends TRANSACTION\_NOTIFY\_ROLLBACK notifications to all resource managers for the transactions that are associated with those enlistments.

The operating system deletes the object after the last handle is closed and KTM has released all its references to the object.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Resource%20Manager%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


