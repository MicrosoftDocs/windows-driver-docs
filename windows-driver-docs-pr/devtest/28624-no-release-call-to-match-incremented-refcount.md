---
title: C28624
description: Warning C28624 No call to Release() to match incremented refcount from LResultFromObject.
ms.assetid: e769d232-ef6e-4b70-8cac-f4dd43807e1d
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





