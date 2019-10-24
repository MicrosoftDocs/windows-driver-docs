---
title: Obtaining Parameters for I/O Requests
description: Obtaining Parameters for I/O Requests
ms.assetid: 1ba1fdcf-99bd-44e3-adbf-5dc93a790900
keywords:
- I/O requests WDK UMDF , obtaining parameters
- request processing WDK UMDF , obtaining parameters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining Parameters for I/O Requests


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

When a driver receives an I/O request, the driver can use the following methods of the [IWDFIoRequest](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiorequest) interface to obtain parameters related to the request:

-   [**IWDFIoRequest::GetCreateParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-getcreateparameters) or [**IWDFIoRequest2::GetCreateParametersEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest2-getcreateparametersex)

-   [**IWDFIoRequest::GetDeviceIoControlParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-getdeviceiocontrolparameters)

-   [**IWDFIoRequest::GetReadParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-getreadparameters)

-   [**IWDFIoRequest::GetWriteParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-getwriteparameters)

 

 





