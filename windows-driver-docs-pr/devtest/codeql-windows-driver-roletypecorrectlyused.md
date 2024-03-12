---
title: RoleTypeCorrectlyUsed (Supplemental Windows Driver CodeQL Query)
description: RoleTypeCorrectlyUsed a Supplemental Windows Driver CodeQL Query
ms.date: 02/06/2024
---

# RoleTypeCorrectlyUsed (Windows Driver CodeQL Query)

## Overview

Driver entry point functions should be declared with a function role type.

For more information, see [C28158 warning - Windows Drivers](/windows-hardware/drivers/devtest/declaring-functions-using-function-role-types-for-wdm-drivers)

## Recommendation

Make sure the role type of the function being used matches the expected role type.

## Example

```cpp
// Copyright (c) Microsoft Corporation.
// Licensed under the MIT license.

//Macros to enable or disable a code section that may or maynot conflict with this test.
#define SET_DISPATCH 1

//Template function. Not used for this test.
void top_level_call(){
}
```

## Additional Details

This query can be found in the [Microsoft GitHub CodeQL repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools).  See the [CodeQL and the Static Tools Logo Test](./static-tools-and-codeql.md) page for details on how Windows Driver developers can download and run CodeQL.
