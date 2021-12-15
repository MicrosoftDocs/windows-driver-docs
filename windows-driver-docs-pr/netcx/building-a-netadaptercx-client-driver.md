---
title: Building a NetAdapterCx client driver
description: Building a NetAdapterCx client driver
keywords:
- building a NetAdapterCx client driver, building a NIC driver
ms.date: 06/05/2017
---

# Building a NetAdapterCx client driver

To obtain the latest version of Visual Studio and the Windows Driver Kit (WDK), please visit the [Hardware Dev Center](../download-the-wdk.md).

Use the following steps to create a new NetAdapter client driver in Visual Studio:

1. Open Microsoft Visual Studio. On the File menu, choose **New > Project**.
2. In the **New Project > Templates > Visual C++ > Windows Driver > WDF** dialog box, select **Kernel Mode Driver (KMDF) Template**.
3. To open the Driver Property Page dialog, choose **Project > Properties**.
4. In the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, select the **Link to the Network Adapter Class Extension** dropdown and set to **Yes**.
5. In the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, select **Network Adapter Major Version** and **Network Adapter Minor Version**.
    1. The current version of NetAdapterCx is **2.0**. For more information, see [NetAdapterCx version overview](netadaptercx-version-overview.md).
6. Add the following header to every source file (or to your common/precompiled header):

```C++
#include <ntddk.h>
#include <wdf.h>
#include <netadaptercx.h>
```

To watch a video that shows how to create a new NetAdapter client driver in Visual Studio, see the [Network Adapter Class Extension: Your First Driver](/teamblog/LearnTVAnnouncement) video on Channel 9.
