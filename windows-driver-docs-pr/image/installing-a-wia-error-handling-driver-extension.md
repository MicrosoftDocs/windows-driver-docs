---
title: Installing a WIA Error Handling Driver Extension
description: Installing a WIA Error Handling Driver Extension
ms.assetid: 8a16b0db-25ed-4512-8b45-0256fed6b83e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a WIA Error Handling Driver Extension


The error handling extension should be installed together with the WIA driver. In order to install the driver's error handler together with the driver, a small number of additions must be done to the driver's INF file.

The following example shows how an existing driver INF file can be modified to include the error handler.

```INF
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

 

 




