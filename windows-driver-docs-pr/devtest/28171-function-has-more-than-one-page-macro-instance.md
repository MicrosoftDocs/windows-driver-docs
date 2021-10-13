---
title: C28171 warning
description: Warning C28171 The function has more than one instance of PAGED_CODE or PAGED_CODE_LOCKED.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium 
f1_keywords: 
  - "C28171"
---

# C28171


warning C28171: The function has more than one instance of PAGED\_CODE or PAGED\_CODE\_LOCKED

This warning indicates that there is more than one instance of the PAGED\_CODE or PAGED\_CODE\_LOCKED macro in a function. This error is reported at the second or subsequent instances of the PAGED\_CODE or PAGED\_CODE\_LOCKED macro.

Functions in a paged section must have exactly one instance of the PAGED\_CODE or PAGED\_CODE\_LOCKED macro and the macro should appear at the beginning of the function between the first brace (**{**) and the first conditional statement, and after any declarations.

PREfast for Drivers uses these macros when **\#pragma alloc\_text** or **\#pragma code\_seg** is used to move a function into a pageable code section. The Code Analysis tool infers that a section is pageable when the section name begins with PAGE. For more information, see [Warning C28170](28170-pageable-code-macro-not-found.md).

 

 





