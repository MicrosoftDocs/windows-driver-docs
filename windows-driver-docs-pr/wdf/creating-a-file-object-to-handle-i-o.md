---
title: Creating a File Object to Handle I/O
description: Creating a File Object to Handle I/O
ms.assetid: 3cd826fc-5c67-4ab4-800a-b5aa4bd5244f
keywords:
- file object to handle I/O WDK UMDF
- file object to handle I/O WDK UMDF , creating
- I/O requests WDK UMDF , file object
- User-Mode Driver Framework WDK , file object to handle I/O
- UMDF WDK , file object to handle I/O
- user-mode drivers WDK UMDF , file object to handle I/O
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a File Object to Handle I/O

[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

When an application opens a file handle, the I/O manager creates a file object. The framework in turn creates a framework file object to represent the I/O manager's file object.

Unless the driver sets the **UmdfFileObjectPolicy** directive to **AllowNullAndUnknownFileObjects**, UMDF requires each I/O request to be associated with a file object. For more information about this directive, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

If your UMDF driver sends I/O that is independent of the application to the next driver in the stack (for example, during device initialization or to get notification of device events), the driver must create its own file object to associate with the request.

The following sections describe the differences between driver-created file objects and application-created file objects, and how the driver creates and uses a file object.

-   [Driver-Created Versus Application-Created File Objects](driver-created-versus-application-created-file-objects.md)
-   [Creating and Using Driver-Created File Objects](creating-and-using-driver-created-file-objects.md)

 

 





