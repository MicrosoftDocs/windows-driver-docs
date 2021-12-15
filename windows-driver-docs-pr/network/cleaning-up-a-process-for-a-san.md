---
title: Cleaning up a Process for a SAN
description: Cleaning up a Process for a SAN
keywords:
- SAN process cleanups WDK
- cleaning up SAN process WDK
ms.date: 04/20/2017
---

# Cleaning up a Process for a SAN





When an application is ready to clean up the process in which it is running, it initiates a call to the Windows Sockets switch's **WSPCleanup** function. The switch, in turn, calls the [**WSPCleanup**](/previous-versions/windows/hardware/network/ff566270(v=vs.85)) function of the TCP/IP provider and all SAN service providers. All providers are expected to release any resources that they were using. Resources can include, for example, objects used to synchronize events and memory used to perform data transfers.

 

