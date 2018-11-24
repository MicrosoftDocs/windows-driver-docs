---
title: Loading the Notify Object DLL and Class Object
description: Loading the Notify Object DLL and Class Object
ms.assetid: 846c0ed8-5299-4803-983a-9347e912d96b
keywords:
- notify objects WDK networking , loading objects
- network notify objects WDK , loading objects
- loading objects WDK notify objects
- DLLs WDK notify objects
- class objects WDK notify objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Loading the Notify Object DLL and Class Object





Notify objects for network components should be implemented as Component Object Model (COM) objects. These COM objects reside in DLLs that are COM component servers. For more information about developing DLL COM servers, see the Microsoft Windows SDK.

The DLL for a particular notify object should be implemented to export a set of entry-point functions:

-   A **DllMain** function to let the network configuration subsystem load the DLL into the virtual address space for the subsystem.

-   **DllRegisterServer** and **DllUnregisterServer** functions to put information into the operating system registry for the DLL's class objects. The network configuration subsystem uses this registry information to locate and load a network component's notify object.

-   A **DllCanUnloadNow** function to let the network configuration subsystem determine whether the DLL is in use. If the DLL is not in use, the subsystem can safely unload the DLL from memory.

In order for a notify object DLL to be a COM server, it must expose a class factory for the notify object the server supports. This class factory lets the network configuration subsystem create an instance of the notify object. The class factory should inherit from the **IClassFactory** interface. For more information about implementing classes that inherit from **IClassFactory**, see the Windows SDK.

 

 





