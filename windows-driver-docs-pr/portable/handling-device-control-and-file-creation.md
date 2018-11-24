---
Description: Handling Device Control and File Creation
title: Handling Device Control and File Creation
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Device Control and File Creation


Each time a Windows-based application calls the **DeviceIoControl** Win32 function, the user-mode driver framework (UMDF) notifies the driver by calling one of the methods in the **IQueueCallbackDeviceIlControl** interface. Each time a Windows-based application calls the **CreateFile** Win32 function, UMDF notifies the driver by calling a method in the **IQueueCallbackCreate** interface. All this functionality is found in the sample driver's *Queue.cpp* and *Queue.h* modules.

The following table describes the methods that are found in these modules.

| Method                                               | Description                                                                                                   |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **IObjectCleanup::OnCleanup**                        | Releases the reference to the client context map that is assigned by **OnCreateFile** to the WDF file object. |
| **IQueueCallbackCreate::OnCreateFile**               | Opens the device as a result of an application that calls the Win32 **CreateFile** function.                  |
| **IQueueCallbackDeviceIoControl::OnDeviceIoControl** | Performs a device operation as a result of an application that calls the **DeviceIOControl** function.        |

 

Refer to the [UMDF](http://go.microsoft.com/fwlink/p/?linkid=153678) documentation for a description of each interface and its methods.

 

 




