---
title: Handling Quotas on IRP_MJ_CREATE
description: Handling Quotas on IRP_MJ_CREATE
keywords:
- IRP_MJ_CREATE
- quotas WDK file systems
- security checks WDK file systems , IRP_MJ_CREATE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Quotas on IRP\_MJ\_CREATE


## <span id="ddk_handling_quotas_on_irp_mj_create_if"></span><span id="DDK_HANDLING_QUOTAS_ON_IRP_MJ_CREATE_IF"></span>


Some logic could also be included to acquire quota information if the file system supports quotas. One strategy a file system could adopt would be to acquire a block of quota information about [**IRP\_MJ\_CREATE**](./irp-mj-create.md) that is later checked and updated by dispatch routines for other IRP requests that can change the size of a file (delete and write operations, for example).

 

