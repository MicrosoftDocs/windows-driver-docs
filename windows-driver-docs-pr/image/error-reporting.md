---
title: Error Reporting
description: Error Reporting
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Error Reporting





All methods in the [IWiaMiniDrv interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv) return a COM HRESULT value. If the method succeeds, the minidriver returns S\_OK and clears the device error value that the *plDevErrVal* parameter points to. If the method fails, the minidriver returns a standard COM error code and sets \**plDevErrVal* with a device-specific error code. The WIA service can call the [**IWiaMiniDrv::drvGetDeviceErrorStr**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetdeviceerrorstr) method to obtain the error message string associated with the value pointed to by *plDevErrVal*. For more information about COM error values, see the Microsoft Windows SDK documentation.

 

