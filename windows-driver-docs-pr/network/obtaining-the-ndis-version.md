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





NDIS versions might not be the same as the operating system versions. For example, if you use the [**RtlGetVersion**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlgetversion) and [**RtlVerifyVersionInfo**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlverifyversioninfo) routines to get the operating system version, you do not get a guaranteed association with a particular NDIS version. Therefore, NDIS drivers must get the NDIS version and the operating system version separately. NDIS drivers can get the NDIS version with the [**NdisGetVersion**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetversion) function.

## Related topics


[Overview of NDIS versions](overview-of-ndis-versions.md)

[Specifying NDIS Version Information](specifying-ndis-version-information.md)

 

 






