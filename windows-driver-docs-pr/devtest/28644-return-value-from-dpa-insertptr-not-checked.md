---
title: C28644
description: Warning C28644 Return value from DPA_InsertPtr not checked.
ms.assetid: F145330F-E597-405F-935E-B12D65F64DDB
ms.date: 04/20/2017
ms.localizationpriority: medium
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









