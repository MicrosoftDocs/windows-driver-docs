---
title: C28651
description: Warning C28651 Static initializer causes copy on write pages due to member function pointers.
ms.assetid: 2E7B61A7-FF15-46C3-87B4-36CAA2E52CAC
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28651%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




