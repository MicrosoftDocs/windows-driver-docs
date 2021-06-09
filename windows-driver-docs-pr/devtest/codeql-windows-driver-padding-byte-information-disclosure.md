---
title: PaddingByteInformationDisclosure (Supplemental Windows Driver CodeQL Query)
description: PaddingByteInformationDisclosure a Supplemental Windows Driver CodeQL Query
ms.date: 01/11/2021
ms.localizationpriority: medium
---

# PaddingByteInformationDisclosure (Windows Driver CodeQL Query)

## Overview

A newly allocated struct or class that is initialized member-by-member may leak information if it includes padding bytes.

## Recommendation

Make sure that all padding bytes in the struct or class are initialized.

If possible, use *memset* to initialize the whole structure/class.

## Example

The following example shows a scenario where padding between the first and second elements are not initialized:

```cpp
typedef enum { Unknown = 0, Known = 1, Other = 2 } MyStructType;
struct MyStruct { MyStructType type; UINT64 id; };
MyStruct testReturn() 
{
	// BAD: Padding between the first and second elements not initialized.
	MyStruct myBadStackStruct = { Unknown };
	return myBadStackStruct;
}
```

To correct it, we will initialize all bytes using *memset*:

```cpp
typedef enum { Unknown = 0, Known = 1, Other = 2 } MyStructType;
struct MyStruct { MyStructType type; UINT64 id; };
MyStruct testReturn()
{
	// GOOD: All padding bytes initialized
	MyStruct* myGoodHeapStruct = (struct MyStruct*)malloc(sizeof(struct MyStruct));
	memset(myGoodHeapStruct, 0, sizeof(struct MyStruct));
	return *myGoodHeapStruct;
}
```

## Additional Details

This query can be found in the [Microsoft GitHub CodeQL repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools).  See the [CodeQL and the Static Tools Logo Test](./static-tools-and-codeql.md) page for details on how Windows Driver developers can download and run CodeQL.
