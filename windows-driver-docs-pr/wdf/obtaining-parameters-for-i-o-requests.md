---
title: Obtaining Parameters for I/O Requests
author: windows-driver-content
description: Obtaining Parameters for I/O Requests
ms.assetid: 1ba1fdcf-99bd-44e3-adbf-5dc93a790900
keywords:
- I/O requests WDK UMDF , obtaining parameters
- request processing WDK UMDF , obtaining parameters
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Obtaining Parameters for I/O Requests


\[This topic applies to UMDF 1.*x*.\]

When a driver receives an I/O request, the driver can use the following methods of the [IWDFIoRequest](https://msdn.microsoft.com/library/windows/hardware/ff558985) interface to obtain parameters related to the request:

-   [**IWDFIoRequest::GetCreateParameters**](https://msdn.microsoft.com/library/windows/hardware/ff559088) or [**IWDFIoRequest2::GetCreateParametersEx**](https://msdn.microsoft.com/library/windows/hardware/ff558989)

-   [**IWDFIoRequest::GetDeviceIoControlParameters**](https://msdn.microsoft.com/library/windows/hardware/ff559095)

-   [**IWDFIoRequest::GetReadParameters**](https://msdn.microsoft.com/library/windows/hardware/ff559113)

-   [**IWDFIoRequest::GetWriteParameters**](https://msdn.microsoft.com/library/windows/hardware/ff559130)

 

 





