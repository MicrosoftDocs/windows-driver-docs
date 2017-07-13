---
title: Handling Stop IRPs (Windows 98/Me)
author: windows-driver-content
description: Handling Stop IRPs (Windows 98/Me)
ms.assetid: 98eefb69-e321-4cc5-8b4d-79335cd8b06e
keywords: ["stop IRPs WDK PnP", "IRPs WDK PnP", "I/O request packets WDK PnP"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Stop IRPs (Windows 98/Me)


## <a href="" id="ddk-handling-stop-irps-windows-98-me-kg"></a>


On Windows 98/Me, the PnP manager can send stop IRPs for the following reasons:

-   To pause the device while rebalancing resources

-   To stop the device when Device Manager disables it

-   To stop the device after a failed [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request

A driver cannot determine from the IRP why it was sent. Consequently, WDM drivers that run on Windows 98/Me must handle all stop IRPs as if the device were being disabled. In short, this means that such drivers fail incoming I/O requests rather than queuing them (as on Windows 2000 and later).

The following topics provide step-by-step details on handling each of the stop IRPs:

[Handling an IRP\_MN\_QUERY\_STOP\_DEVICE Request (Windows 98/Me)](handling-an-irp-mn-query-stop-device-request--windows-98-me-.md)

[Handling an IRP\_MN\_STOP\_DEVICE Request (Windows 98/Me)](handling-an-irp-mn-stop-device-request--windows-98-me-.md)

[Handling an IRP\_MN\_CANCEL\_STOP\_DEVICE Request (Windows 98/Me)](handling-an-irp-mn-cancel-stop-device-request--windows-98-me-.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20Stop%20IRPs%20%28Windows%2098/Me%29%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


