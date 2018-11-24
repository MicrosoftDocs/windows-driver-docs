---
Description: Handling the Entry and Exit Points
title: Handling the Entry and Exit Points
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Entry and Exit Points


Each time a device is loaded in a driver's host process, the user-mode driver framework (UMDF) adds a device object. And, each time the framework adds an object, it calls methods in the **IDriverEntry** interface. These methods are found in the CDriver class. The following table describes the methods that are found in this class.

| Method                           | Description                            |
|----------------------------------|----------------------------------------|
| **IDriverEntry::OnDeinitialize** | Performs necessary cleanup operations. |
| **IDriverEntry::OnDeviceAdd**    | Adds a new device to the system.       |
| **IDriverEntry::OnInitialize**   | Handles driver initialization.         |

 

In the WpdHelloWorldDriver, the **OnDeviceAdd** method is the only method that does meaningful work; the **OnInitialize** method simply returns S\_OK and the **OnDeinitialize** method returns no value.

The code for the **OnDeviceAdd** method completes the following steps:

1.  Creates a device callback object.
2.  Creates a WDF device.
3.  Creates the WpdBaseDriver object and assigns it to the WDF device object.
4.  Creates a queue callback object.
5.  Creates the default queue.

CDriver also implements **IObjectCleanup::OnCleanup**, which contains code to release a reference to the WpdBaseDriver object that is held by the WDF device object during **OnDeviceAdd**.

For more information about each interface and its methods, see the [UMDF](http://go.microsoft.com/fwlink/p/?linkid=153678) documentation.

 

 




