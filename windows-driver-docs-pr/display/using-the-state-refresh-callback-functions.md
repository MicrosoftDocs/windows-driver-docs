---
title: Using the State-Refresh Callback Functions
description: Using the State-Refresh Callback Functions
ms.assetid: fadd2edb-776b-4ef1-b663-cc004522f8ae
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the State-Refresh Callback Functions


The user-mode display driver can use the [Direct3D Runtime Version 10 State-Refresh Callback Functions](https://msdn.microsoft.com/library/windows/hardware/ff552879) to achieve a stateless driver or to build up command buffer preamble data.

The Direct3D runtime supplies pointers to its state-refresh callback functions in the [**D3D10DDI\_CORELAYER\_DEVICECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff541820) structure that the **pUMCallbacks** member of the [**D3D10DDIARG\_CREATEDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff541664) structure points to in a call to the [**CreateDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540635) function.

The user-mode display driver might call, for example, the [**pfnStateIaIndexBufCb**](https://msdn.microsoft.com/library/windows/hardware/ff568970) state-refresh callback function, while the driver is within a call to the driver's [**IaSetIndexBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff567387) function. This call is quite possible, especially because the user-mode display driver might use the **pfnStateIaIndexBufCb** callback function to build a preamble, and the call to *IaSetIndexBuffer* might exhaust the size of the command buffer and cause a flush. For such a situation, the call to **pfnStateIaIndexBufCb** passes the same "new" binding information as the original call to *IaSetIndexBuffer*. This situation results in a more optimal preamble.

 

 





