---
title: Obtaining the NDIS Version
description: Obtaining the NDIS Version
ms.assetid: f7bbd11c-b6ec-4adb-8c42-ec438d518ed8
keywords:
- NDIS version information WDK , versus operating system version
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining the NDIS Version





NDIS versions might not be the same as the operating system versions. For example, if you use the [**RtlGetVersion**](https://msdn.microsoft.com/library/windows/hardware/ff561910) and [**RtlVerifyVersionInfo**](https://msdn.microsoft.com/library/windows/hardware/ff563026) routines to get the operating system version, you do not get a guaranteed association with a particular NDIS version. Therefore, NDIS drivers must get the NDIS version and the operating system version separately. NDIS drivers can get the NDIS version with the [**NdisGetVersion**](https://msdn.microsoft.com/library/windows/hardware/ff562680) function.

## Related topics


[Overview of NDIS versions](overview-of-ndis-versions.md)

[Specifying NDIS Version Information](specifying-ndis-version-information.md)

 

 






