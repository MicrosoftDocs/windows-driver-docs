---
title: Error Reporting
description: Error Reporting
ms.assetid: 6f8c08f4-2809-4f49-9332-bbee85399404
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Error Reporting





All methods in the [IWiaMiniDrv interface](https://msdn.microsoft.com/library/windows/hardware/ff545027) return a COM HRESULT value. If the method succeeds, the minidriver returns S\_OK and clears the device error value that the *plDevErrVal* parameter points to. If the method fails, the minidriver returns a standard COM error code and sets \**plDevErrVal* with a device-specific error code. The WIA service can call the [**IWiaMiniDrv::drvGetDeviceErrorStr**](https://msdn.microsoft.com/library/windows/hardware/ff543982) method to obtain the error message string associated with the value pointed to by *plDevErrVal*. For more information about COM error values, see the Microsoft Windows SDK documentation.

 

 




