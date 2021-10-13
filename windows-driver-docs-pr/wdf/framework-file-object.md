---
title: Framework File Object
description: Framework File Object
keywords:
- UMDF objects WDK , file objects
- framework objects WDK UMDF , file objects
- file objects WDK UMDF
- IWDFFile
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework File Object


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The framework file object is exposed to drivers by the [IWDFFile](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffile) interface. It is the framework representation of the opened device. When an application opens the device through the Microsoft Win32 [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function, the framework creates a file object to represent the opened device instance. Therefore, the framework file object is conceptually equivalent to the Win32 handle that is returned from the application's call to **CreateFile**. The framework can create multiple file objects associated with a single device. Each file object is created for each successful call to **CreateFile**. All I/O operations, like reads and writes, are targeted to a specific file-object instance.

**Note**   All requests passed to UMDF drivers are associated with file objects. However, requests that are passed to [WDM](../kernel/writing-wdm-drivers.md) and [KMDF](./index.md) drivers are sometimes not associated with file objects.

 

A UMDF driver can call the [**IWDFIoRequest::GetFileObject**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-getfileobject) method to obtain the file object associated with a request.

When your driver calls [**GetFileObject**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-getfileobject), the framework increments the reference count on the interface. Your driver is responsible for releasing the reference when finished with the interface pointer. To do so, either use a smart pointer that automatically decrements the reference count when the object goes out of context, or call [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) on the interface when finished with it. For a code example that shows how to use a smart pointer, see **GetFileObject**.

