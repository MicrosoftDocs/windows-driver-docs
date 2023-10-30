---
title: PAGED_CODE macro
description: PAGED_CODE macro
ms.date: 10/17/2018
ms.topic: reference
---

# PAGED_CODE

Defined in: Wdm.h

The **PAGED_CODE** macro ensures that the calling thread is running at an IRQL that is low enough to permit paging.

**Return value**

**VOID**

If the IRQL > APC_LEVEL, the **PAGED_CODE** macro causes the system to ASSERT.

A call to this macro should be made at the beginning of every driver routine that either contains pageable code or accesses pageable code.

The **PAGED_CODE** macro checks the IRQL only at the point at which the driver code executes the macro.

If the code subsequently raises the IRQL, the macro will not detect this change.

Driver developers should use [Static Driver Verifier](../devtest/static-driver-verifier.md) and [Driver Verifier](../devtest/driver-verifier.md) to detect when the IRQL is raised improperly during the execution of a driver routine.

The **PAGED_CODE** macro works only in checked builds.

Available starting with Windows 2000.
