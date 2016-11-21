---
title: C28617
description: Warning C28617 Avoid using the return value of \_beginthread(). Use \_beginthreadex() instead.
ms.assetid: b0de0809-1583-4c1d-ad70-c3e27afc3e6d
---

# C28617


warning C28617: Avoid using the return value of \_beginthread(). Use \_beginthreadex() instead

It is safer to use **\_beginthreadex** than **\_beginthread**. If the thread spawned by **\_beginthread** exits quickly, the handle returned to the caller of **\_beginthread** may be invalid or, worse, point to another thread. However, the handle returned by **\_beginthreadex** has to be closed by the caller of **\_beginthreadex**, so it is guaranteed to be a valid handle if **\_beginthreadex** did not return an error.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

The following code example generates this warning.

```
hThread = (HANDLE)_beginthread (&SecondThreadFunc, 0, &args);
WaitForSingleObject (hThread, INFINITE);
```

The following code example avoids the warning.

```
hThread = (HANDLE)_beginthreadex ( NULL, 0,
                                   &SecondThreadFunc,
                                   &args, 0, &threadID);
WaitForSingleObject (hThread, INFINITE);
CloseHandle(hThread);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28617%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




