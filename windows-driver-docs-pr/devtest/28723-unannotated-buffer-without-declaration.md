---
title: C28723 Warning
description: Warning C28723 Unannotated buffer in function definition that has no corresponding declaration.
ms.date: 04/20/2017
f1_keywords: 
  - "C28723"
---

# C28723


warning C28723: Unannotated buffer in function definition that has no corresponding declaration

This warning indicates that a buffer passed as a function parameter or returned by a function should be annotated with the Microsoft Source Code Annotation language (SAL). Static analysis tools can use such annotations to detect buffer overruns.

Currently, only non-constant buffers are diagnosed with this warning.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code example generates this warning.

```
    int foo( LPTSTR buffer, size_t cch )
{
    ...
}  
```

The following code example avoids this warning.

```
    int foo( _Out_writes_(cch) LPTSTR buffer, size_t cch )
{
    ...
}
```









