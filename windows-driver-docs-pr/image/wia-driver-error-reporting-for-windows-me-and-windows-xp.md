---
title: WIA Driver Error Reporting for Windows Me and Windows XP
author: windows-driver-content
description: WIA Driver Error Reporting for Windows Me and Windows XP
ms.assetid: 5f696e16-0c22-4d71-98d2-d642e721ac8c
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Driver Error Reporting for Windows Me and Windows XP


## <a href="" id="ddk-wia-driver-error-reporting-for-windows-me-and-windows-xp-si"></a>


A WIA minidriver has the ability to report extended error information to the WIA application in string form. After receiving an HRESULT error code, a WIA application can call the **IWiaItemExtras::GetExtendedErrorInfo** method (described in the Microsoft Windows SDK documentation) for a user-readable string that describes the details of an error. The string reported by this method should be localized into multiple languages.

A WIA minidriver should implement the following methods to perform error reporting:

[**IStiUSD::GetLastError**](https://msdn.microsoft.com/library/windows/hardware/ff543818) − The WIA service calls this method to retrieve the device-specific error code for the recent failed action.

[**IStiUSD::GetLastErrorInfo**](https://msdn.microsoft.com/library/windows/hardware/ff543820) − The WIA service calls this method to retrieve extended information about the error code returned from the **IStiUSD::GetLastError** method call.

[**IWiaMiniDrv::drvGetDeviceErrorStr**](https://msdn.microsoft.com/library/windows/hardware/ff543982) − The WIA service calls this method to retrieve any displayable strings that describe the error in detail, or instructions to the end user on how to proceed after the error. The **IWiaItemExtras::GetExtendedErrorInfo** method returns the error string this method retrieved.

The WIA service asks for error information if any of the [IWiaMiniDrv COM Interface](iwiaminidrv-com-interface.md) methods fail.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Driver%20Error%20Reporting%20for%20Windows%20Me%20and%20Windows%20XP%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


