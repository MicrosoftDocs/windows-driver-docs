---
title: Building a NetAdapterCx Client Driver
---

# Building a NetAdapterCx Client Driver

To obtain the latest version of Visual Studio and the Windows Driver Kit (WDK), please visit the [Hardware Dev Center](https://developer.microsoft.com/windows/hardware/windows-driver-kit).

Use the following steps to create a new NetAdapter client driver in Visual Studio:

1. Open Microsoft Visual Studio. On the File menu, choose **New > Project**.
2. In the **New Project** dialog box, select **WDF**.
3. In the middle pane, select **NetAdapter Driver** if available.  Otherwise, select **Kernel Mode Driver (KMDF)**.
5. Link against NetAdapterCxStub.lib (located in `Windows Kits\10\Lib\<latest_windows_version>\km\<architecture>\netadaptercx\1.0`).
6. Add the following header to every source file (or to your common/precompiled header):
```cpp
#include <netadaptercx.h>
```

To watch a video that shows how to create a new NetAdapter client driver in Visual Studio, see [Network Adapter Class Extension: Your First Driver](https://aka.ms/netadapter/video2).
