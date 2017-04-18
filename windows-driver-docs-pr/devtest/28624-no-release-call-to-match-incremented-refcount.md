---
title: C28624
description: Warning C28624 No call to Release() to match incremented refcount from LResultFromObject.
ms.assetid: e769d232-ef6e-4b70-8cac-f4dd43807e1d
---

# C28624


warning C28624: No call to Release() to match incremented refcount from LResultFromObject

**LresultFromObject** increases the refcount on new IAccessible objects.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example generates this warning.

```
{
 IAccessible *pacc = CreateNewIAccessible();
 LRESULT lTemp = LresultFromObject(riid, NULL, pacc );
}

{
 IAccessible *pacc = NULL;
 // Get new interface (from same object)
 QueryInterface( & pacc );

 // Lresult will internally bump up the refcount
 // to hold onto the object.
 
 LRESULT lTemp = LresultFromObject( riid, NULL, pacc );
}
```

The following example avoids the error.

```
{
 IAccessible *pacc = CreateNewIAccessible();
 // Lresult internally increases the refcount to
 // hold onto the object.
 LRESULT lTemp = LresultFromObject(riid, NULL, pacc );

 // We no longer need our pacc interface, so we release it.

 pacc->Release();
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28624%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




