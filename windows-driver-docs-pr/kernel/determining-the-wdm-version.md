---
title: Determining the WDM Version
description: Determining the WDM Version
keywords: ["WDM drivers WDK kernel , versions", "versions WDK WDM", "compatibility WDK WDM", "cross-system compatibility WDK WDM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Determining the WDM Version





A cross-system WDM driver should use the [**IoIsWdmVersionAvailable**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioiswdmversionavailable) routine to determine which version of WDM is supported by the system on which it is running. The reference page for **IoIsWdmVersionAvailable** provides a list of WDM version numbers.

For information about differences in WDM that drivers should handle, see [Differences in WDM Versions](differences-in-wdm-versions.md).

 

