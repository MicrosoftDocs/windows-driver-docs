---
title: Using the IStiUSD Escape Method
description: Using the IStiUSD Escape Method
ms.assetid: f9b1ede6-8311-4cc9-8bf7-20018cb35a3d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the IStiUSD Escape Method





The [**IStiUSD::Escape**](https://msdn.microsoft.com/library/windows/hardware/ff543815) method is called to pass information directly to the hardware. This method is supported only on Windows XP and later operating systems.

All communication between a TWAIN-compatible application and the WIA driver goes first to the data source manager (*twain\_32.dll*), which in turn calls into the TWAIN compatibility layer (*wiadss.dll*). The TWAIN compatibility layer then calls the WIA driver's [**IStiUSD::Escape**](https://msdn.microsoft.com/library/windows/hardware/ff543815) method, and passes one of the following two escape codes to the method:

[ESC\_TWAIN\_CAPABILITY Escape Code](esc-twain-capability-escape-code.md)

[ESC\_TWAIN\_PRIVATE\_SUPPORTED\_CAPS Escape Code](esc-twain-private-supported-caps-escape-code.md)

When the TWAIN application requests the WIA driver's private capability list, the TWAIN compatibility layer calls the driver's **IStiUSD::Escape** method, passing ESC\_TWAIN\_PRIVATE\_SUPPORTED\_CAPS in the call. If the driver does not support pass-through functionality, it returns the TWAIN compatibility layer's static (default) capability list. Otherwise, the driver returns a list of supported private capabilities to the TWAIN compatibility layer.

When the TWAIN application sends a capability operation that is not already in the TWAIN compatibility layer's default list, the TWAIN compatibility layer calls the driver's **IStiUSD::Escape** method, this time passing ESC\_TWAIN\_CAPABILITY in the call.

However, the foregoing explanation is somewhat oversimplified. When the TWAIN application asks for the driver's private capabilities list, the TWAIN compatibility layer actually makes two calls to the driver's **IStiUSD::Escape** method. In the first call, the TWAIN compatibility layer asks the WIA driver how much memory is needed to store the capability list. The TWAIN compatibility layer then allocates that amount of memory for the WIA driver to use. In the second call, the TWAIN compatibility layer asks the WIA driver for the capability list, which the WIA driver copies into the previously mentioned memory. The TWAIN compatibility layer is responsible for allocating and freeing all memory used in TWAIN-WIA transactions. This arrangement prevents the WIA driver from freeing memory the TWAIN compatibility layer is using.

The TWAIN compatibility layer also calls the driver's **IStiUSD::Escape** method twice when ESC\_TWAIN\_CAPABILITY is passed and for which the intent is to get a capability. The first call asks the WIA driver how much memory it needs in order to store the capability, and the second call returns the capability. Note that SET capability operations require only a single call to **IStiUSD::Escape**, because no memory needs to be allocated.

All calls to the **IStiUSD::Escape** method should be validated in this order:

1.  Validate the *EscapeFunction* function code. If it is not valid, fail immediately. This prevents incorrect codes from being processed in the driver.

2.  Validate the incoming buffer, *lpInData*. If it is not valid, fail immediately. Invalid incoming buffers can cause the WIA driver to crash.

3.  Validate the outgoing buffer, *pOutData*. If it is not valid, fail immediately. If the driver cannot complete the request by writing the necessary data, it does not need to process that data.

4.  Validate the size of the outgoing buffer. If the driver cannot write the correct amount of data to the outgoing buffer, then the caller cannot properly process that data.

The code samples in the following sections illustrate the use of pass-though functionality, supporting TWAIN applications with private capabilities. The code samples use two escape codes that are defined in header file *wiatwcmp.h*, ESC\_TWAIN\_PRIVATE\_SUPPORTED\_CAPS and ESC\_TWAIN\_CAPABILITY.

[ESC\_TWAIN\_PRIVATE\_SUPPORTED\_CAPS Escape Code](esc-twain-private-supported-caps-escape-code.md)

[ESC\_TWAIN\_CAPABILITY Escape Code](esc-twain-capability-escape-code.md)

 

 




