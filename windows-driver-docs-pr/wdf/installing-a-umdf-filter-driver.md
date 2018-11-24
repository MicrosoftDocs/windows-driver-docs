---
title: Installing a UMDF Filter Driver
description: A filter driver can support a specific device or all devices in a setup class.
ms.assetid: AE6D4E36-B758-451A-983E-6F0D7ADFD7A7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a UMDF Filter Driver


A filter driver can support a specific device or all devices in a setup class. A lower filter driver attaches below a device's function driver, while an upper filter attaches above a device's function driver.

This topic describes how to install and configure a User-Mode Driver Framework (UMDF) device-specific (upper or lower) filter driver. You cannot use UMDF to write a class filter driver. This topic applies to both UMDF versions 1 and 2.

As you structure your device stack, keep in mind that the framework currently supports only one contiguous block of UMDF drivers per stack. Also, you cannot install UMDF version 1 and version 2 drivers in the same device stack.

**How to install and configure your driver**

1.  A UMDF 1 filter driver should call [**IWDFDeviceInitialize::SetFilter**](https://msdn.microsoft.com/library/windows/hardware/ff556985) from the its [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) callback function. Starting in UMDF version 2, your driver instead calls [**WdfFdoInitSetFilter**](https://msdn.microsoft.com/library/windows/hardware/ff547273).

2.  In addition to any UMDF-specific directives your driver may specify, you must specify the **UmdfService** and **UmdfServiceOrder** directives. In this topic, we'll specify an upper filter driver:

    ```cpp
    [<mydriver>_Install.NT.Wdf]
    UmdfService=UMDFFunction,WUDFFuncDriver_Install
    UmdfService=UMDFFilter,UMDFFilter_Install
    UmdfServiceOrder=UMDFFunction,UMDFFilter
    ```

    The drivers are added to the device stack in the order that they are listed in the **UmdfServiceOrder** entry. The first parameter specifies the lowest UMDF driver in the device stack. To install a lower filter driver, simply reverse the arguments for **UmdfServiceOrder**.

    For more info about these and other UMDF-specific INF directives, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

3.  If your driver's device stack contains only UMDF drivers, skip this step.

    If your driver's device stack contains any drivers that are not UMDF, your INF file must include an **AddReg** section that specifies the reflector as an upper filter driver:

    ```cpp
    [<mydriver>_Device_AddReg]
    ; Load the redirector as an upperfilter on this specific device.
    ; 0x00010008 - FLG_ADDREG_TYPE_MULTI_SZ | FLG_ADDREG_APPEND
    HKR,,"UpperFilters",0x00010008,"WUDFRd" 
    ```

4.  After your driver is loaded as an upper filter, it is responsible for forwarding I/O requests to the next driver in the stack. To illustrate, consider a simple pass-through driver (UMDF version 1) that is above a KMDF function driver.

    First, retrieve the interface of the default I/O target (next driver in the stack). Then, format and send the request. The simplest scenario would look like this:

    ```cpp
    IWDFIoTarget * kmdfIoTarget = NULL;
        
        this->GetFxDevice()->GetDefaultIoTarget (&kmdfIoTarget);

        Request->FormatUsingCurrentType();

        hr = Request->Send (
            kmdfIoTarget, 
            0,  // 0 Submits Asynchronous else use WDF_REQUEST_SEND_OPTION_SYNCHRONOUS
            0);
    ```

 

 





