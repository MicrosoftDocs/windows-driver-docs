---
title: C28172
description: Warning C28172 The function has PAGED_CODE or PAGED_CODE_LOCKED but is not declared to be in a paged segment.
ms.assetid: c97bf9e8-583c-41ca-9c50-ac2af3dd5dc0
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28172


warning C28172: The function has PAGED\_CODE or PAGED\_CODE\_LOCKED but is not declared to be in a paged segment

A function that contains a PAGED\_CODE or PAGED\_CODE\_LOCKED macro has not been placed in paged memory by using **\#pragma alloc\_text** or **\#pragma code\_seg**. The Code Analysis tool infers that a section is pageable when the section name begins with PAGE. This error is reported at the line number corresponding to the first brace (**{**) in the function.

This error usually occurs when the function was intended to be paged, but one of the pragmas was omitted or misplaced, or when a function changed from paged to non-paged. For more information, see [Warning C28170](28170-pageable-code-macro-not-found.md).

 

 





