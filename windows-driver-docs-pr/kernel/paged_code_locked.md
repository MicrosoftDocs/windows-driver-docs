---
title: PAGED_CODE_LOCKED macro
description: PAGED_CODE_LOCKED macro
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# PAGED_CODE_LOCKED

Defined in: Wdm.h

The **PAGED_CODE_LOCKED** macro asserts that the currently running code section is pageable and must have been locked into memory before it was run.

**Return value**

**VOID**

Pageable code must obey certain restrictions (such as IRQL <= APC_LEVEL), unless it is locked into place. A pageable routine that must be locked into place to work correctly should begin with a call to **PAGED_CODE_LOCKED**.

For more information about locking a code section into place, see [Locking Pageable Code or Data](locking-pageable-code-or-data.md).


