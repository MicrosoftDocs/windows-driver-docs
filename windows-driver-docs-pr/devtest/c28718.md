---
title: C28718
description: Warning C28718 Unannotated buffer.
ms.assetid: 8417AB73-B645-451D-A359-9A66A793A78D
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
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28718%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





