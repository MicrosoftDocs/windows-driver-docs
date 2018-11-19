---
title: C28718
description: Warning C28718 Unannotated buffer.
ms.assetid: 8417AB73-B645-451D-A359-9A66A793A78D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28718


warning C28718: Unannotated buffer

This warning is reported when a buffer that is passed to a function or returned by a function does not have Source Code Annotation Language (SAL) annotations. Static analysis tools can use such annotations to detect buffer overruns. For information about adding annotations, see [Using SAL Annotations to Reduce C/C++ Code Defects](http://go.microsoft.com/fwlink/p/?linkid=247283) and **Annotating Function Parameters and Return Values**.

Currently, only non-constant string buffers are diagnosed with this warning. Ideally, all buffers passed as function parameters or returned by functions should be annotated. Arrays of **wchar\_t** or **char** are candidates for this warning. Unsigned chars currently are not.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code example generates this warning.

```
int foo( LPTSTR buffer, size_t cch );  
```

The following code example avoids this warning.

```
int foo( _Out_writes_(cch) LPTSTR buffer, size_t cch );
```

## <span id="related_topics"></span>Related topics


[Using SAL Annotations to Reduce C/C++ Code Defects](http://go.microsoft.com/fwlink/p/?linkid=247283)

**Annotating Function Parameters and Return Values**
 

 






