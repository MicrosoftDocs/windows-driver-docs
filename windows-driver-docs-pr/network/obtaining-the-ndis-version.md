---
title: Obtaining the NDIS Version
description: Obtaining the NDIS Version
ms.assetid: f7bbd11c-b6ec-4adb-8c42-ec438d518ed8
keywords: ["NDIS version information WDK , versus operating system version"]
---

# Obtaining the NDIS Version


## <a href="" id="ddk-obtaining-the-ndis-version-ng"></a>


NDIS versions might not be the same as the operating system versions. For example, if you use the [**RtlGetVersion**](https://msdn.microsoft.com/library/windows/hardware/ff561910) and [**RtlVerifyVersionInfo**](https://msdn.microsoft.com/library/windows/hardware/ff563026) routines to get the operating system version, you do not get a guaranteed association with a particular NDIS version. Therefore, NDIS drivers must get the NDIS version and the operating system version separately. NDIS drivers can get the NDIS version with the [**NdisGetVersion**](https://msdn.microsoft.com/library/windows/hardware/ff562680) function.

## Related topics


[NDIS Versions in Network Drivers](ndis-versions-in-network-drivers.md)

[Specifying NDIS Version Information](specifying-ndis-version-information.md)

 

 






