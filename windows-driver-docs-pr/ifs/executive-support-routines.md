---
title: Executive Support Routines
description: Executive Support Routines
ms.assetid: f86b942c-9a3f-495b-9623-fd0656ec4a7a
ms.date: 09/30/2019
ms.localizationpriority: medium
---

# Executive Support Routines

The following system-supplied executive support functions and macros can be called by kernel-mode file systems and by minifilter and legacy filter drivers, but not by device drivers. Some functions are reserved for system use.

In addition to the routines documented here, file systems and filter drivers can also call any of the **Ex**_Xxx_ routines that are described in the Kernel-Mode Driver Architecture Reference section that are declared in *ntifs.h*.

**Header File:** *ntifs.h*

**Prefix: Ex*Xxx***

| Function or Macro | Description |
| ----------------- | ----------- |
| **ExAdjustLookasideDepth** | Reserved for system use. |
| **ExDisableResourceBoost** | Reserved for system use. |
| **ExDisableResourceBoostLite** | Reserved for system use. |
| **ExInitializeWorkItem** | Initializes a work-queue item with a caller-supplied context and callback routine to be queued for execution when a system worker thread is given control. Use this routine with extreme caution.|
| **ExQueryPoolBlockSize** | Obsolete. |
| **ExQueueWorkItem** | Inserts a given work item into a queue from which a system worker thread removes the item and gives control to the routine that the caller supplied to ExInitializeWorkItem. Use this routine with extreme caution. |
