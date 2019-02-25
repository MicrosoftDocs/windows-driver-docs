---
title: Architecture of UMDF
description: This topic describes how the driver manager builds a user-mode device stack, and how the host process, reflector, and driver manager process an I/O request that an application sends to a User-Mode Driver Framework (UMDF) driver.
ms.assetid: 118e5fe8-ba1e-4012-9632-fd92f4cee6f1
keywords:
- User-Mode Driver Framework WDK , architecture
- UMDF WDK , architecture
- user-mode drivers WDK UMDF , architecture
- architecture WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Architecture of UMDF


This topic describes how the driver manager builds a user-mode device stack, and how the host process, reflector, and driver manager process an I/O request that an application sends to a User-Mode Driver Framework (UMDF) driver.

Similar to a kernel-mode stack, the construction and tear down of a user-mode stack is driven by Plug and Play (PnP) events. After the kernel-mode stack has been built, the reflector notifies the driver manager to start construction of the user-mode stack. The driver manager launches the driver host process and provides sufficient information to the launched process to build the user-mode stack. In this way, the user-mode stack can be considered an extension of the kernel-mode stack.

The driver host process provides the execution environment for user-mode drivers and routes messages between drivers in the user-mode stack. The reflector uses a message-based interprocess communication mechanism to communicate with the driver manager and host process.

![umdf components including up and down device objects in reflector](images/umdfarch4.gif)

To send an I/O request to a UMDF driver, an application calls a Win32 file I/O function, such as [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858), **ReadFileEx**, **CancelIoEx**, or [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216). When the reflector receives a request from the client application, it sends the request to the appropriate driver host process. The driver host process then routes the request to the top of the correct user-mode device stack.

The request is either completed by one of the drivers in the user-mode stack or forwarded by one of the drivers back to the reflector. When the reflector receives a request from the user-mode driver stack, it sends the request down the kernel-mode stack for completion.

 

 





