---
title: Using the State-Refresh Callback Functions
description: Using the State-Refresh Callback Functions
ms.assetid: fadd2edb-776b-4ef1-b663-cc004522f8ae
---

# Using the State-Refresh Callback Functions


The user-mode display driver can use the [Direct3D Runtime Version 10 State-Refresh Callback Functions](https://msdn.microsoft.com/library/windows/hardware/ff552879) to achieve a stateless driver or to build up command buffer preamble data.

The Direct3D runtime supplies pointers to its state-refresh callback functions in the [**D3D10DDI\_CORELAYER\_DEVICECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff541820) structure that the **pUMCallbacks** member of the [**D3D10DDIARG\_CREATEDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff541664) structure points to in a call to the [**CreateDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540635) function.

The user-mode display driver might call, for example, the [**pfnStateIaIndexBufCb**](https://msdn.microsoft.com/library/windows/hardware/ff568970) state-refresh callback function, while the driver is within a call to the driver's [**IaSetIndexBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff567387) function. This call is quite possible, especially because the user-mode display driver might use the **pfnStateIaIndexBufCb** callback function to build a preamble, and the call to *IaSetIndexBuffer* might exhaust the size of the command buffer and cause a flush. For such a situation, the call to **pfnStateIaIndexBufCb** passes the same "new" binding information as the original call to *IaSetIndexBuffer*. This situation results in a more optimal preamble.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20the%20State-Refresh%20Callback%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




