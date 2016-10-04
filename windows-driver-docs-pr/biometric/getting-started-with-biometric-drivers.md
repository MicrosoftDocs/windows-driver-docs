---
title: Getting Started with Biometric Drivers
description: Getting Started with Biometric Drivers
ms.assetid: 7f5dcac2-db0d-4ddd-9e57-886db324e38b
keywords: ["biometric drivers WDK , about biometric drivers"]
---

# Getting Started with Biometric Drivers


The Windows Biometric Framework (WBF) is a generic biometric architecture in Windows 7 and later versions of Windows.

WBF includes an IOCTL-based driver interface known as the Windows Biometric Driver Interface (WBDI) as well as a Windows service called the Windows Biometric Service (WBS). WBS is also referred to as the WinBio service. WBDI drivers respond to requests from the WinBio service. WBF also includes Windows log-in support.

This documentation describes the WBDI. WBS is documented separately in the Windows SDK.

### <span id="choosing_a_driver_model"></span><span id="CHOOSING_A_DRIVER_MODEL"></span>Choosing a Driver Model

The first choice you must make when you develop a driver to work with the Windows Biometric Driver Interface (WBDI) is which driver model to use.

Microsoft recommends that IHVs develop biometric device drivers by using the Windows User-mode Driver Framework (WUDF, also referred to as [UMDF](https://msdn.microsoft.com/library/windows/hardware/ff554928)) and the WinUSB I/O target.

The following diagram shows how a UMDF-based Windows Biometric Driver Interface (WBDI) driver fits into the Windows Biometric Framework (WBF) biometric support in Windows 7. All biometric operations are driven by client applications to the Windows Biometric Service (WBS). The WBS sends requests to biometric device drivers that expose the WBDI interface.

![diagram illustrating biometric internal driver architecture](images/bioarch.png)

In the previous diagram, the vendor supplies the biometric device driver DLL.

If you do not want to use UMDF to develop your driver, you can also choose to implement the WBDI by using a KMDF or WDM driver, but this is not the preferred driver development environment.

The following list shows the different ways that you can develop a driver for WBDI, with the most preferred method on top and the least preferred at the bottom:

1.  UMDF with a WinUsb I/O target

2.  UMDF with a custom KMDF filter on WinUsb or custom KMDF I/O target

3.  KMDF

4.  WDM (only when absolutely necessary)

This documentation describes how to use UMDF to write a WBDI-based user-mode USB biometric driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[biometric\biometric]:%20Getting%20Started%20with%20Biometric%20Drivers%20%20RELEASE:%20%288/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




