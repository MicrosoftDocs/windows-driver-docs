---
title: Resource Manager Objects
description: Resource Manager Objects
keywords: ["resource managers WDK KTM , objects", "resource managers WDK KTM", "resource managers WDK KTM , routines", "Kernel Transaction Manager WDK , resource managers", "KTM WDK , resource managers", "resource manager objects WDK KTM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Resource Manager Objects


*Resource manager objects* represent resource managers. Each resource manager must call [**ZwCreateResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateresourcemanager) to register itself to KTM.

KTM provides a set of resource manager object routines that kernel-mode resource managers can call. KTM also provides a similar set of user-mode routines that user-mode applications can call. For more information about the user-mode routines, see the Microsoft Windows SDK.

KTM creates a resource manager object when a resource manager calls **ZwCreateResourceManager**.

[TPS components](understanding-tps-components.md) can call [**ZwOpenResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopenresourcemanager) to open additional handles to a resource manager object. But most TPS designs do not require additional open handles.

Resource managers close their handles to resource manager objects by calling [**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose). If the last handle is closed, and if the resource manager still has enlistments to transactions that have not been committed, KTM sends TRANSACTION\_NOTIFY\_ROLLBACK notifications to all resource managers for the transactions that are associated with those enlistments.

The operating system deletes the object after the last handle is closed and KTM has released all its references to the object.

 

