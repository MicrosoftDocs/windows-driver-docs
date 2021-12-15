---
title: Obtaining the NDIS Version
description: Obtaining the NDIS Version
keywords:
- NDIS version information WDK , versus operating system version
ms.date: 04/20/2017
---

# Obtaining the NDIS Version





NDIS versions might not be the same as the operating system versions. For example, if you use the [**RtlGetVersion**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlgetversion) and [**RtlVerifyVersionInfo**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlverifyversioninfo) routines to get the operating system version, you do not get a guaranteed association with a particular NDIS version. Therefore, NDIS drivers must get the NDIS version and the operating system version separately. NDIS drivers can get the NDIS version with the [**NdisGetVersion**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetversion) function.

## Related topics


[Overview of NDIS versions](overview-of-ndis-versions.md)

[Specifying NDIS Version Information](specifying-ndis-version-information.md)

 

