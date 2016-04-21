---
title: Framework File Object
author: windows-driver-content
description: Framework File Object
ms.assetid: dd8215ee-2c10-4e49-9d7f-d2295bf219da
keywords: ["UMDF objects WDK , file objects", "framework objects WDK UMDF , file objects", "file objects WDK UMDF", "IWDFFile"]
---

# Framework File Object


\[This topic applies to UMDF 1.*x*.\]

The framework file object is exposed to drivers by the [IWDFFile](https://msdn.microsoft.com/library/windows/hardware/ff558912) interface. It is the framework representation of the opened device. When an application opens the device through the Microsoft Win32 [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function, the framework creates a file object to represent the opened device instance. Therefore, the framework file object is conceptually equivalent to the Win32 handle that is returned from the application's call to **CreateFile**. The framework can create multiple file objects associated with a single device. Each file object is created for each successful call to **CreateFile**. All I/O operations, like reads and writes, are targeted to a specific file-object instance.

**Note**   All requests passed to UMDF drivers are associated with file objects. However, requests that are passed to [WDM](https://msdn.microsoft.com/library/windows/hardware/ff565698) and [KMDF](https://msdn.microsoft.com/library/windows/hardware/ff544296) drivers are sometimes not associated with file objects.

 

A UMDF driver can call the [**IWDFIoRequest::GetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff559099) method to obtain the file object associated with a request.

When your driver calls [**GetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff559099), the framework increments the reference count on the interface. Your driver is responsible for releasing the reference when finished with the interface pointer. To do so, either use a smart pointer that automatically decrements the reference count when the object goes out of context, or call [**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) on the interface when finished with it. For a code example that shows how to use a smart pointer, see **GetFileObject**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20File%20Object%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




