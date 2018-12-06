---
title: Receive Side Scaling
description: Receive Side Scaling
ms.assetid: 380feb24-1f5e-4faa-9c98-1b3c8fdc27cb
keywords:
- network drivers WDK , receive-side scaling
- receive-side scaling WDK networking , NDIS 6.0
- RSS WDK networking , NDIS 6.0
- network receive processing WDK RSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receive Side Scaling





Receive side scaling (RSS) improves the system performance related to handling of network data on multiprocessor systems.

For introductory information about RSS, see [Introduction to Receive Side Scaling](introduction-to-receive-side-scaling.md).

Starting with Windows 10, version 1709, RSS Version 2 (RSSv2) is available for miniport drivers. RSSv2 improves on the base RSS model by offering per-VPort spreading. For more info, see [Receive Side Scaling Version 2 (RSSv2)](receive-side-scaling-version-2-rssv2-.md). RSSv2 is preview only in Windows 10, version 1709.

The following topics describe the RSS implementations that are possible with different levels of hardware and software support:

[Non-RSS Receive Processing](non-rss-receive-processing.md)

[RSS with a Single Hardware Receive Queue](rss-with-a-single-hardware-receive-queue.md)

[RSS with Hardware Queuing](rss-with-hardware-queuing.md)

[RSS with Message Signaled Interrupts](rss-with-message-signaled-interrupts.md)

The following topics provide additional information about RSS:

[RSS Hashing Types](rss-hashing-types.md)

[RSS Hashing Functions](rss-hashing-functions.md)

[Verifying the RSS Hash Calculation](verifying-the-rss-hash-calculation.md)

[RSS Configuration](rss-configuration.md)

[Setting the RSS CPU Configuration](setting-the-rss-cpu-configuration.md)

[Standardized INF Keywords for RSS](standardized-inf-keywords-for-rss.md)

[Indicating RSS Receive Data](indicating-rss-receive-data.md)

[Supporting RSS in Intermediate Drivers or Filter Drivers](supporting-rss-in-intermediate-drivers-or-filter-drivers.md)

 

 





