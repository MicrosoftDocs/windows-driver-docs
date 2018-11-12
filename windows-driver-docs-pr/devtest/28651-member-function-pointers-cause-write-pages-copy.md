---
title: C28651
description: Warning C28651 Static initializer causes copy on write pages due to member function pointers.
ms.assetid: 2E7B61A7-FF15-46C3-87B4-36CAA2E52CAC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28651


warning C28651: Static initializer causes copy on write pages due to member function pointers

Static initializers of global or static const variables can often be fully evaluated at compile time, thus generated in RDATA. However if any initializer is a pointer-to-member function where it is a non-static function, the entire initializer may be placed in copy-on-write pages, which has a performance cost.

For binaries that require fast loading and minimizing copy on write pages, consider making sure all function pointers in the static initializer are not pointer-to-member functions. If a pointer-to-member function is required, write a simple static member function that wraps a call to the actual member function.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code example generates this error.

```
void Func()
{
    WCHAR*pszBuf=newWCHAR[MAX_PATH];
    DPA_InsertPtr(_hdpa, DA_LAST, pszBuf);
}

void CleanupDPA()
{
    int count = DPA_GetCount(_hdpa);
    for (int i = 0; i < count; i++)
{
    delete [] (LPWSTR)DPA_GetPtr(_hdpa, i);
}
}  
```

The following code example avoids this error.

```
class MyClass
{
    ...
    bool memberFunc();
    static bool memberFuncWrap(MyClass *thisPtr)
        { return thisPtr->memberFunc(); }
    ...
};
const StructType MyStruct[] = {
    ...
    &MyClass::memberFuncWrap,
    ...
};  
```









