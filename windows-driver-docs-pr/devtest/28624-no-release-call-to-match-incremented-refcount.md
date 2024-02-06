---
title: C28624 Warning
description: Warning C28624 No call to Release() to match incremented refcount from LResultFromObject.
ms.date: 04/20/2017
f1_keywords: 
  - "C28624"
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

