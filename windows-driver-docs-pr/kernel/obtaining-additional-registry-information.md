---
title: Obtaining Additional Registry Information
description: Obtaining Additional Registry Information
keywords: ["filtering registry calls WDK kernel , additional information to obtain", "registry filtering drivers WDK kernel , additional information to obtain"]
ms.date: 06/16/2017
---

# Obtaining Additional Registry Information


Registry filtering drivers that run on Windows Vista and later operating system versions can obtain the following additional information about registry operations:

-   Object identifiers and names

    The [**CmCallbackGetKeyObjectIDEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmcallbackgetkeyobjectidex) routine retrieves the registry key identifier and object name that are associated with a specified registry key object.

-   Transaction objects

    The [**CmGetBoundTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmgetboundtransaction) routine returns a pointer to the transaction object that represents the [transaction](introduction-to-ktm.md), if any, that is associated with a registry key object.

-   Version information

    The [**CmGetCallbackVersion**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmgetcallbackversion) routine retrieves the major and minor version numbers for the current version of the configuration manager's registry callback feature.

 

