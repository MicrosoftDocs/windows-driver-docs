---
title: UMDF DDI Programming Model
description: UMDF DDI Programming Model
ms.assetid: d4bf0791-d2c4-4504-84ad-020880124363
keywords: ["UMDF objects WDK , DDI", "framework objects WDK UMDF , DDI", "UMDF DDI WDK", "DDI WDK UMDF"]
---

# UMDF DDI Programming Model


\[This topic applies to UMDF 1.*x*.\]

The framework and the UMDF driver communicate through the UMDF DDI. The UMDF DDI is similar to the KMDF DDI except that the UMDF DDI is based on COM. Therefore, driver writers familiar with KMDF will understand UMDF.

For each type of framework object, the UMDF defines an interface through which to manipulate instances of the object. Each interface supports methods and properties. Methods define actions that can be taken on behalf of the object and properties set and retrieve the characteristics of the object. Some interfaces are implemented by the framework and others are implemented by the driver. Interfaces that are exposed by a framework object are of the form IWDF&lt;object&gt;, while the event callback interfaces exposed by a driver are of the form I&lt;object&gt;&lt;action&gt;, where &lt;object&gt; represents a queue, request, and so on, and &lt;action&gt; indicates what the interface does. Methods of the callback interfaces begin with "On".

The UMDF driver communicates with the framework's objects through their methods and properties. The framework communicates with the driver through event notifications, which are callback functions that the framework can call to notify the driver about specific events. To register callback functions, the driver can call, for example, the following framework object methods and can pass a pointer to the **IUnknown** interface associated with all the interfaces for the callback functions that the driver supports.

-   [**IWDFDevice::CreateIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff557020)

-   [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899)

-   [**IWDFDriver::CreateWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff558906)

As an example of driver to framework communication, consider a device's default I/O queue object. A driver can call methods, such as [**IWDFIoQueue::GetState**](https://msdn.microsoft.com/library/windows/hardware/ff558959), to retrieve status information about the I/O queue, or [**IWDFIoQueue::RetrieveNextRequest**](https://msdn.microsoft.com/library/windows/hardware/ff558967) to retrieve a request from the I/O queue. A driver can also request for notifications on the I/O queue by calling the [**IWDFDevice::CreateIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff557020) method to register callback interfaces, such as [IQueueCallbackRead](https://msdn.microsoft.com/library/windows/hardware/ff556872) and [IQueueCallbackWrite](https://msdn.microsoft.com/library/windows/hardware/ff556882). The methods of these interfaces are subsequently called by the framework when an application sends read and write requests.

The framework provides any synchronization required across driver callback methods. By default, the framework synchronizes at device object level; that is, the framework does not concurrently call the event callback methods at or below the device object level. A driver can override this default by requesting no synchronization. For more information, see [Specifying a Callback Synchronization Mode](specifying-a-callback-synchronization-mode.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20UMDF%20DDI%20Programming%20Model%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




