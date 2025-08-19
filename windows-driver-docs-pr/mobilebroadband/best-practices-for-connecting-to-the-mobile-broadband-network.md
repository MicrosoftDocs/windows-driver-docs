---
title: Best Practices for Connecting to the Mobile Broadband Network
description: Best practices for connecting to the mobile broadband network
ms.date: 04/21/2025
ms.topic: best-practice
---

# Best practices for connecting to the mobile broadband network

Active connections to the mobile broadband network can be an unnecessary drain on battery life and account data quotas. We recommend that you use careful judgment to determine whether a connection is necessary.

Use the following best practices regarding connectivity to the mobile broadband network:

- Do not use the provisioning agent’s &lt;*Activation*&gt; directives. These directives are intended only for specific circumstances after activation.

- Use the Mobile Broadband API to establish temporary connectivity. This API provides connection operation results and an easy way to disconnect.

- Keep the connection lifetime to a minimum.

- Use connectivity through Internet-connected interfaces whenever they are available. You can observe availability by using the [**NetworkInformation**](/uwp/api/Windows.Networking.Connectivity.NetworkInformation) API.

## Related topics

[Best practices for handling account arrival and removal events](best-practices-for-handling-account-arrival-and-removal-events.md)