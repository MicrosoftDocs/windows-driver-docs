---
title: InfiniteLoop (Supplemental Windows Driver CodeQL Query)
description: InfiniteLoop a Supplemental Windows Driver CodeQL Query
ms.date: 01/11/2021
ms.localizationpriority: medium
---

# InfiniteLoop (Windows Driver CodeQL Query)

## Overview

Comparisons between types of different widths in a loop condition can cause the loop to fail to terminate.

## Recommendation

Use appropriate types in the loop condition.

## Example

In this example, the result of the comparison may result in an infinite loop if the value for argument: *a* is larger than *SHRT_MAX*:

```cpp
void InfiniteLoop(int a)
{
    for (short i = 0; i < a; i++) // BUG: infinite loop
    {
        // ...
    }
}
```

To fix the bug, we are changing the type for the variable *i* to match the width of *a*:

```cpp
void NotInfiniteLoop(int a)
{
    for (int i = 0; i < a; i++) 
    {
        // ...
    }
}
```

## Additional Details

This query can be found in the [Microsoft GitHub CodeQL repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools).  See the [CodeQL and the Static Tools Logo Test](./static-tools-and-codeql.md) page for details on how Windows Driver developers can download and run CodeQL.
