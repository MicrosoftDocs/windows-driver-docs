---
title: WS-DSD Operations
author: windows-driver-content
description: WS-DSD Operations
ms.assetid: aaf8d20c-99e3-4046-89b0-af5251b26577
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WS-DSD Operations


The following operations are defined for WS-DSD and must be supported by conforming DSM Device implementations:

**GetActiveJobs** - returns a list of all currently active scan jobs on the DSM Device and a subset of each scan job's elements.

**GetJobElements** - returns the job elements of a particular scan job.

**GetJobHistory** - returns a list of recently completed scan jobs on the DSM Device and a subset of the job elements of each scan job.

**GetScannerElements** - requests information about the DSM Device.

**ValidateScanTicket** - validates a scan ticket on the DSM Device to ensure the settings in the scan ticket will work in a future scan job.

 

 




