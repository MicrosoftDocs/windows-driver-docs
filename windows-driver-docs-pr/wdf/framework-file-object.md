---
title: Framework File Object
description: Framework File Object
ms.assetid: dd8215ee-2c10-4e49-9d7f-d2295bf219da
keywords:
- UMDF objects WDK , file objects
- framework objects WDK UMDF , file objects
- file objects WDK UMDF
- IWDFFile
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework File Object


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The framework file object is exposed to drivers by the [IWDFFile](https://msdn.microsoft.com/library/windows/hardware/ff558912) interface. It is the framework representation of the opened device. When an application opens the device through the Microsoft Win32 [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function, the framework creates a file object to represent the opened device instance. Therefore, the framework file object is conceptually equivalent to the Win32 handle that is returned from the application's call to **CreateFile**. The framework can create multiple file objects associated with a single device. Each file object is created for each successful call to **CreateFile**. All I/O operations, like reads and writes, are targeted to a specific file-object instance.

**Note**   All requests passed to UMDF drivers are associated with file objects. However, requests that are passed to [WDM](https://msdn.microsoft.com/library/windows/hardware/ff565698) and [KMDF](https://msdn.microsoft.com/library/windows/hardware/ff544296) drivers are sometimes not associated with file objects.

 

A UMDF driver can call the [**IWDFIoRequest::GetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff559099) method to obtain the file object associated with a request.

When your driver calls [**GetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff559099), the framework increments the reference count on the interface. Your driver is responsible for releasing the reference when finished with the interface pointer. To do so, either use a smart pointer that automatically decrements the reference count when the object goes out of context, or call [**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) on the interface when finished with it. For a code example that shows how to use a smart pointer, see **GetFileObject**.

 

 





