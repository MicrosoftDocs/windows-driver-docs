---
title: Reserving Processors for Applications
description: Reserving Processors for Applications
ms.assetid: e09790e9-29a7-4ff6-a122-b4bd99de8bc7
keywords: ["CPU configuration WDK RSS", "reserving processors for applications WDK RSS", "processors WDK RSS"]
---

# Reserving Processors for Applications


## <a href="" id="ddk-reserving-processors-for-applications-ng"></a>


The receive side scaling (RSS) interface enables an administrator to reserve a set of processors for applications to use. The administrator can reserve a set of processors starting at logical CPU number 0 and ending at a specified CPU number. The RSS *base CPU number* is the CPU number of the first CPU that RSS can use. RSS cannot use the CPUs that are numbered below the base CPU number. For example, on a quad-core system with hyper-threading turned off, if base CPU number is set to 1, processors 1, 2, and 3 can be used for RSS.

NDIS uses the default value of 0 for base CPU number, but an administrator can change this value. The RSS interface does not permit the administrator to reserve a non-contiguous, arbitrary subset of CPUs for applications to use.

In Microsoft Windows Server 2003 with the Scalable Networking Pack, administrators can set the base CPU number with the **RssBaseCpu** registry keyword in **HKEY\_LOCAL\_MACHINE\\\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters**. The **RssBaseCpu** value is a DWORD type and, if it is not present, NDIS uses the default value of 0.

In Windows Server 2008, administrators can set the base CPU number with the **RssBaseCpu** registry keyword in **HKEY\_LOCAL\_MACHINE\\\\SYSTEM\\CurrentControlSet\\Services\\NDIS\\Parameters**. The **RssBaseCpu** value is a DWORD type and, if it is not present, NDIS uses the default value of 0.

 

 





