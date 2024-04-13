---
title: C28722 Warning
description: Warning C28722 Unannotated buffer in function declaration.
ms.date: 04/20/2017
f1_keywords: 
  - "C28722"
---

# C28722


warning C28722: Unannotated buffer in function declaration

This warning indicates that a buffer passed as a function parameter or returned by a function should be annotated with the Microsoft Source Code Annotation language (SAL). Static analysis tools can use such annotations to detect buffer overruns at compile time.

Currently, only non-constant buffers are diagnosed with this warning.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code example generates this warning.

```CSS
int foo( LPTSTR buffer, size_t cch );  
```

The following code example avoids this warning by using the SAL annotation **\_Out\_writes\_** to specify that the called function writes to the buffer and that the buffer cannot be NULL. The annotation indicates that the buffer is of *cch* elements.

```
int foo( _Out_writes_(cch) LPTSTR buffer, size_t cch );
```

