---
title: C28652
description: Warning C28652 Static initializer causes copy on write pages due to overloaded bitwise operators.
ms.assetid: 763A7F2E-ABFF-41D2-9077-4F60B8EBD338
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28652


warning C28652: Static initializer causes copy on write pages due to overloaded bitwise operators

Static initializers of global or static const variables can often be fully evaluated at compile time, and thus can be generated in .rdata sections. However, if any initializer requires a function call, the entire initializer may be put in copy-on-write pages, which has a performance cost. This initialization has calls to overloaded bitwise operators on enum types. If the overloaded implementations have the obvious semantics, using appropriate casts or macros can produce the same effect without requiring copy-on-write.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code example generates this warning.

```
#include <nt.h>

typedef enum
{
    ENUM_VAL_1 = 0x1,
    ENUM_VAL_2 = 0x2,
    ENUM_VAL_3 = 0x4
} ENUM_VALS;

DEFINE_ENUM_FLAG_OPERATORS(ENUM_VALS);

const ENUM_VALS rgValsRuntime[] = {
    ENUM_VAL_1 | ENUM_VAL_2,    // Runtime init!
    ENUM_VAL_3                  // Compile time init
};  
```

The following code example avoids this warning.

```
#include <nt.h>

typedef enum
{
    ENUM_VAL_1 = 0x1,
    ENUM_VAL_2 = 0x2,
    ENUM_VAL_3 = 0x4
} ENUM_VALS;

DEFINE_ENUM_FLAG_OPERATORS(ENUM_VALS);

const ENUM_VALS rgValsRuntime[] = {
    (ENUM_VALS) COMPILETIME_OR_2FLAGS(ENUM_VAL_1, ENUM_VAL_2),
    ENUM_VAL_3                  // Compile time init
};
```









