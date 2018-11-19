---
title: Determining the WDM Version
description: Determining the WDM Version
ms.assetid: 7ed288d9-6447-4b08-baf2-e7b743654ebd
keywords: ["WDM drivers WDK kernel , versions", "versions WDK WDM", "compatibility WDK WDM", "cross-system compatibility WDK WDM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Determining the WDM Version





A cross-system WDM driver should use the [**IoIsWdmVersionAvailable**](https://msdn.microsoft.com/library/windows/hardware/ff549382) routine to determine which version of WDM is supported by the system on which it is running. The reference page for **IoIsWdmVersionAvailable** provides a list of WDM version numbers.

For information about differences in WDM that drivers should handle, see [Differences in WDM Versions](differences-in-wdm-versions.md).

 

 




