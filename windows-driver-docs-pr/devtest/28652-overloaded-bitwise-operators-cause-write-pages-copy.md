---
title: C28652
description: Warning C28652 Static initializer causes copy on write pages due to overloaded bitwise operators.
ms.assetid: 763A7F2E-ABFF-41D2-9077-4F60B8EBD338
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28652%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




