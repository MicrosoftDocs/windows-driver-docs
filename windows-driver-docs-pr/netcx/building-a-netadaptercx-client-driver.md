---
title: Building a NetAdapterCx Client Driver
---

# Building a NetAdapterCx Client Driver

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

To obtain the latest version of Visual Studio and the Windows Driver Kit (WDK), please visit the [Hardware Dev Center](https://developer.microsoft.com/windows/hardware/windows-driver-kit).

Use the following steps to create a new NetAdapter client driver in Visual Studio:

1. Open Microsoft Visual Studio. On the File menu, choose **New > Project**.
2. In the **New Project > Templates > Visual C++ > Windows Driver > WDF** dialog box, select **Kernel Mode Driver (KMDF) Template**.
3. To open the Driver Property Page dialog, choose **Project > Properties**.
4. In the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, select the **Link to the Network Adapter Class Extension** dropdown and set to **Yes**.
5. In the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, select **Network Adapter Major Version** and **Network Adapter Minor Version**.
6. Add the following header to every source file (or to your common/precompiled header):
```cpp
#include <netadaptercx.h>
```

To watch a video that shows how to create a new NetAdapter client driver in Visual Studio, see [Network Adapter Class Extension: Your First Driver](https://aka.ms/netadapter/video2).
