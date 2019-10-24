---
title: Object Manager Support Routines
description: Object Manager Support Routines
ms.assetid: 64dc1cfb-faf6-4fe0-a8d9-99f6da6d59b7
ms.date: 09/30/2019
ms.localizationpriority: medium
---

# Object Manager Support Routines

The following table lists the subset of system-supplied object management support routines that can be used by kernel-mode file systems and file system (minifilter and legacy) filter drivers, with some reserved for system use. These routines cannot be used by device drivers.

In addition to the routines documented here, file systems and file system filter drivers can also call any of the **Ob**_Xxx_ routines that are described in the Kernel-Mode Driver Architecture Reference and that are declared in *ntifs.h*.

**Header File:** *ntifs.h*

**Prefix: Ob**_Xxx_

| Function or Macro | Description |
| ----------------- | ----------- |
| **ObInsertObject** | Reserved for system use. |
| **ObIsKernelHandle** | Determines whether the specified handle is a kernel handle. |
| **ObMakeTemporaryObject** | Reserved for system use. |
| **ObOpenObjectByPointer** | Opens an object referenced by a pointer and returns a handle to the object. |
| **ObQueryNameString** | Supplies the name, if there is one, of a given object to which the caller has a pointer. |
| **ObQueryObjectAuditingByHandle** | Reserved for system use. |
