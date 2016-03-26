---
title: Operation Flow with Double Device Stack
description: Operation Flow with Double Device Stack
ms.assetid: a717b9c0-b24a-4347-8b0a-254a17238b5f
keywords: ["operation flow WDK UMDF", "I/O requests WDK UMDF , operation flow", "request processing WDK UMDF , operation flow", "double device stack flow WDK UMDF"]
---

# Operation Flow with Double Device Stack


\[This topic applies to UMDF 1.*x*.\]

The following figure shows the flow of operations that occur to and from UMDF filter and functional drivers in a double device stack.

![umdf i/o call sequence for umdf filter driver and umdf function driver](images/umdfflow2.gif)

**Note**   All I/O that is initiated by applications is routed through kernel mode as shown in the figures in the [Architecture of the UMDF](https://msdn.microsoft.com/library/windows/hardware/ff554461) section, even though the preceding figure does not show this situation.

 

The UMDF filter and function drivers might also call the [**IWDFIoRequest::GetCreateParameters**](https://msdn.microsoft.com/library/windows/hardware/ff559088) method if they require information about the file that is associated with the read request. The UMDF filter and function drivers might also call the [**IWDFIoRequest::GetReadParameters**](https://msdn.microsoft.com/library/windows/hardware/ff559113) method if they require more information about the read request.

The UMDF functional driver calls the [**IWDFIoRequest::Complete**](https://msdn.microsoft.com/library/windows/hardware/ff559070) or [**IWDFIoRequest::CompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559074) method to signal to the filter driver that it is done with the read operation. The UMDF filter driver might also call methods of the [IWDFIoRequestCompletionParams](https://msdn.microsoft.com/library/windows/hardware/ff559055) interface if it requires more information to complete the read request. The UMDF filter driver calls **Complete** or **CompleteWithInformation** to signal that the read operation is complete; the application can then access the read data.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Operation%20Flow%20with%20Double%20Device%20Stack%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




