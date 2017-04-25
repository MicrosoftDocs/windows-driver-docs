---
title: Error Reporting
author: windows-driver-content
description: Error Reporting
ms.assetid: 6f8c08f4-2809-4f49-9332-bbee85399404
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Error Reporting


## <a href="" id="ddk-error-reporting-si"></a>


All methods in the [IWiaMiniDrv interface](https://msdn.microsoft.com/library/windows/hardware/ff545027) return a COM HRESULT value. If the method succeeds, the minidriver returns S\_OK and clears the device error value that the *plDevErrVal* parameter points to. If the method fails, the minidriver returns a standard COM error code and sets \**plDevErrVal* with a device-specific error code. The WIA service can call the [**IWiaMiniDrv::drvGetDeviceErrorStr**](https://msdn.microsoft.com/library/windows/hardware/ff543982) method to obtain the error message string associated with the value pointed to by *plDevErrVal*. For more information about COM error values, see the Microsoft Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Error%20Reporting%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


