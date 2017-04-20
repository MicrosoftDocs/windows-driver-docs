---
title: Installing a WIA Error Handling Driver Extension
author: windows-driver-content
description: Installing a WIA Error Handling Driver Extension
ms.assetid: 8a16b0db-25ed-4512-8b45-0256fed6b83e
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing a WIA Error Handling Driver Extension


The error handling extension should be installed together with the WIA driver. In order to install the driver's error handler together with the driver, a small number of additions must be done to the driver's INF file.

The following example shows how an existing driver INF file can be modified to include the error handler.

```
MyDriver.AddReg]
...
HKCR,CLSID\{UiClassId}\shellex\ErrorHandler\{ErrorHandlerCLSID}
...
HKCR,CLSID\{ErrorHandlerCLSID },,,"My Error Handler"
HKCR,CLSID\{ErrorHandlerCLSID }\InProcServer32,,,%11%\myerrhandler.dll
HKCR,CLSID\{ErrorHandlerCLSID }\InProcServer32,ThreadingModel,,"Both"
...

[MyDriver.CopyFiles]
...
myerrhandler.dll
...

[SourceDisksFiles.x86]
...
myerrhandler.dll=1
...
```

The {UiClassId} class ID is the value that the driver returns for the WIA\_DIP\_UI\_CLSID property and {ErrorHandlerCLSID} is the class ID of the error handler. In this example, *myerrhandler.dll* contains the implementation of the error handler.

The first entry in the **AddReg** section is to register the error handler as a WIA extension for the driver. The following three entries register the error handler as a COM component.

The *ThreadingModel* value for the error handling extension must be **Both**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Installing%20a%20WIA%20Error%20Handling%20Driver%20Extension%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


