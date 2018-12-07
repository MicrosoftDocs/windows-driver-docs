---
title: Obtaining Additional Registry Information
description: Obtaining Additional Registry Information
ms.assetid: 989acf63-3bb1-4d9a-a7a8-3eea1e2bc68a
keywords: ["filtering registry calls WDK kernel , additional information to obtain", "registry filtering drivers WDK kernel , additional information to obtain"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Obtaining Additional Registry Information


Registry filtering drivers that run on Windows Vista and later operating system versions can obtain the following additional information about registry operations:

-   Object identifiers and names

    The [**CmCallbackGetKeyObjectIDEx**](https://msdn.microsoft.com/library/windows/hardware/jj215789) routine retrieves the registry key identifier and object name that are associated with a specified registry key object.

-   Transaction objects

    The [**CmGetBoundTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff541905) routine returns a pointer to the transaction object that represents the [transaction](using-kernel-transaction-manager.md), if any, that is associated with a registry key object.

-   Version information

    The [**CmGetCallbackVersion**](https://msdn.microsoft.com/library/windows/hardware/ff541912) routine retrieves the major and minor version numbers for the current version of the configuration manager's registry callback feature.

 

 




