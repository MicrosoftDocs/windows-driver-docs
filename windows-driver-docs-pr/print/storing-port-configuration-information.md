---
title: Storing Port Configuration Information
description: Storing Port Configuration Information
ms.assetid: b1c83729-d7d2-4920-9402-4e00baa12633
keywords:
- port management WDK print , storing configuration information
- registry WDK print
- print spooler registry information WDK print monitor
- storing print port configuration information
- spooler registry information WDK print monitor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storing Port Configuration Information





The Windows 2000 and later print spooler can operate in either a clustered or nonclustered server environment. When the spooler is operating in a server cluster, print monitor configuration information must be stored in the cluster registry. On the other hand, if the spooler is operating on a single, nonclustered server system, print monitor configuration information must be stored in the server's local registry.

The print spooler defines a set of registry functions for use by print monitors. These functions direct configuration data to the appropriate registry, so the print monitor does not have to determine if the server is clustered. Print monitors must not use the Win32 registry API or the cluster registry API directly; all configuration data must be stored and accessed using the spooler's registry functions. Addresses of these functions are supplied to the print monitor in a [**MONITORREG**](https://msdn.microsoft.com/library/windows/hardware/ff557537) structure when the spooler calls the monitor's [**InitializePrintMonitor2**](https://msdn.microsoft.com/library/windows/hardware/ff551605) function.

In a server cluster, multiple instances of the spooler can coexist. Specifically, each cluster node possesses its own instance, and an additional instance exists for the cluster itself. One of the input parameters of the spooler registry functions is a spooler handle. This handle is received by the monitor's **InitializePrintMonitor2** function and identifies the spooler instance (node or cluster) that has opened the monitor. Using the spooler handle, the spooler registry functions maintain subkeys for each spooler instance.

 

 




