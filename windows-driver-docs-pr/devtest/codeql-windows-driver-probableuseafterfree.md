---
title: ProbableUseAfterFree (Supplemental Windows Driver CodeQL Query)
description: UseAfterFree, Low Precision a Supplemental Windows Driver CodeQL Query
ms.date: 01/11/2021
---

# Probable UseAfterFree (Windows Driver CodeQL Query)

## Overview

This [CodeQL query](./static-tools-and-codeql.md) has lower precision than the high-precision [UseAfterFree](./codeql-windows-driver-useafterfree.md) CodeQL query. It detects some additional scenarios, but also has a higher rate of false positives.

A [UseAfterFree defect](http://cwe.mitre.org/data/definitions/416.html) occurs when an allocated memory block is used after it has been freed (also known as a "dangling pointer").

Behavior in such cases is undefined and in practice may have unintended consequences including memory corruption, use of incorrect values, or arbitrary code execution.

## Recommendation

Set pointers to NULL immediately after they are freed.

## Example
In the following example, `pSomePointer` is freed only if `Status` value was not zero, and before dereferencing `pSomePointer` to call `Method`, `Status` is checked again.  Unfortunately `Status` was changed between the two references to `pSomePointer`, which allows for the possiblity that the call to `pSomePointer->Method()` is being performed over a previously freed pointer.

```c
NTSTATUS Status = x();

if (Status != 0)
{
    // Release pSomePointer if the call to x() failed

    ExFreePool(pSomePointer);
}

Status = y();

if (Status == 0)
{
    // Because Status may no longer be the same value than it was before the pointer was released,
    // this code may be using pSomePointer after it was freed, potentially executing arbitrary code.

    Status = pSomePointer->Method();
}
```
In the corrected example, `pSomePointer` is set to `NULL` immediately after being freed, and the condition to check if it is safe to call `pSomePointer->Method()` checks for this additional condition to prevent the possible bug.


```c
NTSTATUS Status = x();

if (Status != 0)
{
    // Release pSomePointer if the call to x() failed

    ExFreePool(pSomePointer);

    // Setting pSomePointer to NULL after being freed
    pSomePointer = NULL;
}

Status = y();

// If pSomePointer was freed above, its value must have been set to NULL
if (Status == 0 && pSomePointer != NULL)
{
    Status = pSomePointer->Method();
}
```

## Additional Details

This query can be found in the [Microsoft GitHub CodeQL repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools).  See the [CodeQL and the Static Tools Logo Test](./static-tools-and-codeql.md) page for details on how Windows Driver developers can download and run CodeQL.
