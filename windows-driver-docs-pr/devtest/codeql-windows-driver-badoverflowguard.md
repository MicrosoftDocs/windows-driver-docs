---
title: BadOverflowGuard (Supplemental Windows Driver CodeQL Query)
description: BadOverflowGuard a Supplemental Windows Driver CodeQL Query
ms.date: 01/11/2021
---

# BadOverflowGuard (Windows Driver CodeQL Query)

## Overview

Checking for overflow of an addition by comparing against one of the arguments of the addition fails if the size of all the argument types are smaller than 4 bytes. This is because the result of the addition is promoted to a 4 byte int.

## Recommendation

Check the overflow by comparing the addition against a value that is at least 4 bytes.

## Example

In this example, the result of the comparison will result in an integer overflow:

```cpp
unsigned short CheckForInt16OverflowBadCode(unsigned short v, unsigned short b)
{
    if (v + b < v) // BUG: "v + b" will be promoted to 32 bits
    {
        // ... do something
    }
    return v + b;
}
```

To fix the bug, check the overflow by comparing the addition against a value that is at least 4 bytes:

```cpp
unsigned short CheckForInt16OverflowCorrectCode(unsigned short v, unsigned short b)
{
    if (v + b > 0x00FFFF)
    {
        // ... do something
    }
    return v + b;
}
```

## Additional Details

This query can be found in the [Microsoft GitHub CodeQL repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools).  See the [CodeQL and the Static Tools Logo Test](./static-tools-and-codeql.md) page for details on how Windows Driver developers can download and run CodeQL.
