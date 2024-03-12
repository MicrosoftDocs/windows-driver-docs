---
title: KeSetEventPageable (Supplemental Windows Driver CodeQL Query)
description: KeSetEventPageable a Supplemental Windows Driver CodeQL Query
ms.date: 02/06/2024
---

# KeSetEventPageable (Windows Driver CodeQL Query)

## Overview

KeSetEvent must not be called in a paged segment when the Wait argument is set to TRUE.  This can cause a system crash the segment is paged out.

For more information, see [KeSetEvent (wdm.h)](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesetevent).

## Recommendation

Adjust the KeSetEvent call to pass FALSE to the wait parameter.

## Example

```cpp
// Copyright (c) Microsoft Corporation.
// Licensed under the MIT license.
//
// driver_snippet.c
//

#define SET_DISPATCH 1

// Template. Not called in this test.
void top_level_call() {}

#include <wdm.h>

void KeSetEventIrql_Fail1(PRKEVENT Event);

_IRQL_always_function_min_(APC_LEVEL) 
void KeSetEventIrql_Fail2(PRKEVENT Event);

_IRQL_always_function_min_(PASSIVE_LEVEL) 
void KeSetEventIrql_Pass1(PRKEVENT Event);

_IRQL_always_function_min_(PASSIVE_LEVEL) 
void KeSetEventIrql_Pass2(PRKEVENT Event);

#pragma alloc_text(PAGE, KeSetEventIrql_Fail1)
#pragma alloc_text(PAGE, KeSetEventIrql_Fail2)
#pragma alloc_text(PAGE, KeSetEventIrql_Pass2)

void KeSetEventIrql_Fail1(PRKEVENT Event)
{
    // This is a paged function.  We assume a lower limit of PASSIVE_LEVEL and an upper limit of APC_LEVEL on the IRQL.

    KeSetEvent(Event, HIGH_PRIORITY, TRUE); // ERROR: Calling with wait set to TRUE in a pageable context
}

void KeSetEventIrql_Fail2(PRKEVENT Event)
{
    // This is a paged function.  Even though it runs at APC_LEVEL, not PASSIVE_LEVEL, that's still an error.

    KeSetEvent(Event, HIGH_PRIORITY, TRUE); // ERROR: Calling with wait set to TRUE in a pageable context
}

void KeSetEventIrql_Pass1(PRKEVENT Event)
{
    // This function will potentially run at passive level but it's not pageable, so there's no issue.

    KeSetEvent(Event, HIGH_PRIORITY, TRUE);
}

void KeSetEventIrql_Pass2(PRKEVENT Event)
{
    // This function will runs at passive level and is pageable, but correctly uses FALSE in its call to KeSetEvent.

    KeSetEvent(Event, HIGH_PRIORITY, FALSE);
}

// TODO multi-threaded tests
// function has max IRQL requirement, creates two threads where one is above that requirement and one is below
```

## Additional Details

This query can be found in the [Microsoft GitHub CodeQL repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools).  See the [CodeQL and the Static Tools Logo Test](./static-tools-and-codeql.md) page for details on how Windows Driver developers can download and run CodeQL.
