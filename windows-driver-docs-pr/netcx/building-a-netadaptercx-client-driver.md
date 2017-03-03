---
title: Building a NetAdapterCx Client Driver
---

# Building a NetAdapterCx Client Driver

Use the following steps to build a NetAdapter client drive in Visual Studio:

1. Open Microsoft Visual Studio. On the File menu, choose **New > Project**.
2. In the **New Project** dialog box, select **WDF**.
3. In the middle pane, select **Kernel Mode Driver (KMDF)**.
5. Link against NetAdapterCxStub.lib (located in `Windows Kits\10\Lib\<latest_windows_version>\km\<architecture>\netadaptercx\1.0`).
6. Add the following header to every source file (or to your common/precompiled header):
```cpp
#include <netadaptercx.h>
```

<!--will there be an NCX option in VS?-->
