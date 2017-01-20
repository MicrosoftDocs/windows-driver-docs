---
title: Best practices for connecting to the mobile broadband network
description: Best practices for connecting to the mobile broadband network
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6106d026-1c5f-4990-8ef2-467c1a77a38e
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Best%20practices%20for%20connecting%20to%20the%20mobile%20broadband%20network%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





