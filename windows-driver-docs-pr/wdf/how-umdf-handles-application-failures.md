---
title: How UMDF Handles Application Failures
description: Describes actions that User-Mode Driver Framework (UMDF) and the operating system take when an application fails. It applies to both UMDF versions 1 and 2.
ms.assetid: ac59a5fe-5975-455f-9da3-318c0692bf9c
keywords:
- User-Mode Driver Framework WDK , application failures
- UMDF WDK , application failures
- failed applications WDK UMDF
- application failures WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How UMDF Handles Application Failures


This topic describes actions that User-Mode Driver Framework (UMDF) and the operating system take when an application fails. It applies to both UMDF versions 1 and 2.

When an application fails, the following events occur:

-   The reflector receives [**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff550718).

-   The cleanup request is sent to the host process on the "cancel" IPC channel.

-   The host process and UMDF driver complete pending I/O requests.

 

 





