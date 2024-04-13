---
title: C28617 Warning
description: Warning C28617 Avoid using the return value of _beginthread(). Use _beginthreadex() instead.
ms.date: 04/20/2017
f1_keywords: 
  - "C28617"
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

