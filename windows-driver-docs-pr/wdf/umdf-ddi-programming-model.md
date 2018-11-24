---
title: UMDF DDI Programming Model
description: UMDF DDI Programming Model
ms.assetid: d4bf0791-d2c4-4504-84ad-020880124363
keywords:
- UMDF objects WDK , DDI
- framework objects WDK UMDF , DDI
- UMDF DDI WDK
- DDI WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UMDF DDI Programming Model


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The framework and the UMDF driver communicate through the UMDF DDI. The UMDF DDI is similar to the KMDF DDI except that the UMDF DDI is based on COM. Therefore, driver writers familiar with KMDF will understand UMDF.

For each type of framework object, the UMDF defines an interface through which to manipulate instances of the object. Each interface supports methods and properties. Methods define actions that can be taken on behalf of the object and properties set and retrieve the characteristics of the object. Some interfaces are implemented by the framework and others are implemented by the driver. Interfaces that are exposed by a framework object are of the form IWDF&lt;object&gt;, while the event callback interfaces exposed by a driver are of the form I&lt;object&gt;&lt;action&gt;, where &lt;object&gt; represents a queue, request, and so on, and &lt;action&gt; indicates what the interface does. Methods of the callback interfaces begin with "On".

The UMDF driver communicates with the framework's objects through their methods and properties. The framework communicates with the driver through event notifications, which are callback functions that the framework can call to notify the driver about specific events. To register callback functions, the driver can call, for example, the following framework object methods and can pass a pointer to the **IUnknown** interface associated with all the interfaces for the callback functions that the driver supports.

-   [**IWDFDevice::CreateIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff557020)

-   [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899)

-   [**IWDFDriver::CreateWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff558906)

As an example of driver to framework communication, consider a device's default I/O queue object. A driver can call methods, such as [**IWDFIoQueue::GetState**](https://msdn.microsoft.com/library/windows/hardware/ff558959), to retrieve status information about the I/O queue, or [**IWDFIoQueue::RetrieveNextRequest**](https://msdn.microsoft.com/library/windows/hardware/ff558967) to retrieve a request from the I/O queue. A driver can also request for notifications on the I/O queue by calling the [**IWDFDevice::CreateIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff557020) method to register callback interfaces, such as [IQueueCallbackRead](https://msdn.microsoft.com/library/windows/hardware/ff556872) and [IQueueCallbackWrite](https://msdn.microsoft.com/library/windows/hardware/ff556882). The methods of these interfaces are subsequently called by the framework when an application sends read and write requests.

The framework provides any synchronization required across driver callback methods. By default, the framework synchronizes at device object level; that is, the framework does not concurrently call the event callback methods at or below the device object level. A driver can override this default by requesting no synchronization. For more information, see [Specifying a Callback Synchronization Mode](specifying-a-callback-synchronization-mode.md).

 

 





