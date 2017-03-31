---
title: C28644
description: Warning C28644 Return value from DPA\_InsertPtr not checked.
ms.assetid: F145330F-E597-405F-935E-B12D65F64DDB
---

# C28644


warning C28644: Return value from DPA\_InsertPtr not checked

This warning indicates that memory might be leaked.

Most calls to the [**DPA\_InsertPtr**](https://msdn.microsoft.com/library/windows/desktop/bb775625) function use a variable that was allocated on the heap. Functions then use the DPA and free all the objects stored in the DPA. When **DPA\_InsertPtr** fails, the allocated object can no longer be freed by the DPA cleanup code, so the caller of **DPA\_InsertPtr** needs to free the memory. Notice the call to **CleanupDPA** in the following example. If your code does not free the allocated objects in a manner similar to **CleanupDPA** you might not have to fix anything. This defect assumes we're relying on the DPA to keep track of all the objects that we have to later free.

The following code example generates this warning:

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

The following code examples avoids this warning:

```
void Func()
{
    WCHAR*pszBuf=newWCHAR[MAX_PATH];
    if (DPA_ERR == DPA_InsertPtr(_hdpa, DA_LAST, pszBuf))
    {
        delete [] pszBuf;
    }

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28644%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




