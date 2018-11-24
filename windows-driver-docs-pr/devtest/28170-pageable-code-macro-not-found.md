---
title: C28170
description: Warning C28170 The function has been declared to be in a paged segment, but neither PAGED_CODE nor PAGED_CODE_LOCKED was found.
ms.assetid: 9efffcc8-54b6-46f8-b037-53c66a8eace2
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28170


warning C28170: The function has been declared to be in a paged segment, but neither PAGED\_CODE nor PAGED\_CODE\_LOCKED was found

The Code Analysis tool reports this error when **\#pragma alloc\_text** or **\#pragma code\_seg** is used to move a function that does not contain a PAGED\_CODE or PAGED\_CODE\_LOCKED macro into a pageable code section. This error is reported at the line number that corresponds to the first brace (**{**) in the function.

The Code Analysis tool infers that a section is pageable when the section name begins with PAGE. The functions in pageable code must contain a PAGED\_CODE or PAGED\_CODE\_LOCKED macro at the beginning of the function between the first brace (**{** ) and the first conditional statement.

These macros allow the Code Analysis tool and a run-time checker to determine whether pageable code might be run at an elevated IRQL. If a page fault occurs while the system is running at an elevated level, the system will crash.

If the functions in a paged segment are subsequently locked into memory, use PAGED\_CODE\_LOCKED instead of PAGED\_CODE. The PAGE\_CODE\_LOCKED macro permits the driver to make calls that raise the IRQL without encountering a PREfast for Drivers warning.

This condition is often very difficult to find while testing (unless the PAGED\_CODE macro is used to cause the Driver Verifier to check for the error), because the code must actually be paged out for the page fault to occur.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
void func();
#pragma alloc_text("PAGED_CODE", func);

void func1()
{
   // paged, no PAGED_CODE: error
}
```

The following code example avoids this warning.

```
void func();
#pragma alloc_text("PAGED_CODE", func);

void func2()
{
   PAGED_CODE(); // includes PAGED_CODE macro
}
```

 

 





