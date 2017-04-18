---
title: C28741
description: Warning C28741 Unannotated buffer in the function.
ms.assetid: 85F071C2-C91B-43D6-8F59-F1D1F955ECC1
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28741%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




