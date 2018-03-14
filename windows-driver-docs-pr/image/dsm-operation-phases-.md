---
title: DSM Operation Phases.
author: windows-driver-content
description: DSM Operation Phases.
ms.assetid: 6cd9418d-fd34-4b7b-acce-23e4ba3854aa
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DSM Operation Phases.


The DSM model defines three phases:

-   [Scan Job Setup](scan-job-setup.md)

-   [Scan Job Execution](scan-job-execution.md)

-   [Post-Scan Job Execution](post-scan-job-execution.md)

DSM also supports job concurrency for phases. A DSM Device may execute more than one scan job at a time. A DSM Device may manage data transfer such that data from a previous scan job can still be transferring to the DSM Scan Server when another scan job is initiated. The number of scan jobs that the DSM Device can process at the same time is limited by the DSM Device.

 

 




