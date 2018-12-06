---
title: C28741
description: Warning C28741 Unannotated buffer in the function.
ms.assetid: 85F071C2-C91B-43D6-8F59-F1D1F955ECC1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28741


warning C28741: Unannotated buffer in the function

This warning indicates that a buffer passed as a function parameter or returned by a function should be annotated with the Microsoft Source Code Annotation language (SAL). Static analysis tools can use such annotations to detect buffer overruns.

Currently, only non-constant string buffers are diagnosed with this warning. Ideally, all buffers passed as function parameters or returned by functions should be annotated. Arrays of **wchar\_t** or **char** are candidates for this warning. Unsigned chars currently are not.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The code following example generates this warning.

```
  int foo( LPTSTR buffer, size_t cch );
```

The following code example avoids this warning by using the SAL annotation **\_Out\_writes\_** to specify that the called function writes to the buffer and that the buffer cannot be NULL. The annotation indicates that the buffer is of *cch* elements.

```
    int foo(_Out_writes_(cch) LPTSTR buffer, size_t cch );
```

 

 





