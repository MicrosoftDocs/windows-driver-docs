---
title: Best practices for connecting to the mobile broadband network
description: Best practices for connecting to the mobile broadband network
ms.assetid: 6106d026-1c5f-4990-8ef2-467c1a77a38e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Best practices for connecting to the mobile broadband network


Active connections to the mobile broadband network can be an unnecessary drain on battery life and account data quotas. We recommend that you use careful judgment to determine whether a connection is necessary.

Use the following best practices regarding connectivity to the mobile broadband network:

-   Do not use the provisioning agent’s &lt;*Activation*&gt; directives. These directives are intended only for specific circumstances after activation.

-   Use the Mobile Broadband API to establish temporary connectivity. This API provides connection operation results and an easy way to disconnect.

-   Keep the connection lifetime to a minimum.

-   Use connectivity through Internet-connected interfaces whenever they are available. You can observe availability by using the [**NetworkInformation**](https://msdn.microsoft.com/library/windows/apps/br207293) API.

## <span id="related_topics"></span>Related topics


[Best practices for using Mobile Broadband Windows Runtime API](best-practices-for-using-mobile-broadband-windows-runtime-api.md)

 

 






