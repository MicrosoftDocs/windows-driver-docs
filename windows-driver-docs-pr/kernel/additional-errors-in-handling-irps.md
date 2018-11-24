---
title: Additional Errors in Handling IRPs
description: Additional Errors in Handling IRPs
ms.assetid: fb46e7a8-8181-46d3-a929-cec01fd71f20
keywords: ["reliability WDK kernel , double-completed IRPs", "double-completed IRPs WDK kernel", "lost IRPs WDK kernel", "reliability WDK kernel , lost IRPs", "converging public IOCTL and private IOCTL paths", "reliability WDK kernel , converge public and private IOCTL paths"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Additional Errors in Handling IRPs





The following are additional errors that drivers sometimes make when handling IRPs.

### Lost or double-completed IRPs

These problems, along with missing calls to I/O manager routines such as [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358), often occur in error-handling paths. Quick reviews of driver paths can find such problems.

### Converging public IOCTL and private IOCTL paths

As a general rule, drivers should contain separate execution paths for public and private IOCTLs (or FSCTLs). A driver cannot determine whether an IOCTL or FSCTL request originates in kernel mode or user mode by looking at the control code. Consequently, handling both public and private codes in the same execution path (or performing minimal validation and then calling the same routines) can open a driver to security breaches. If a private IOCTL or FSCTL is privileged, then unprivileged users who know the control codes might be able to gain access to it. Therefore, if your driver supports private IOCTL or FSCTL requests, make sure it handles such requests separately from any public IOCTLs or FSCTLs it must also support.

 

 




