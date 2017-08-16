---
title: WMI Minor IRPs
author: windows-driver-content
description: WMI Minor IRPs
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: 5788294f-2145-4381-9b06-3b138b2d26df
---

# WMI Minor IRPs


## <a href="" id="ddk-wmi-minor-irps-kr"></a>


This section describes the [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) IRPs that are part of the WMI extensions to WDM. All WMI IRPs use the major code [**IRP\_MJ\_SYSTEM\_CONTROL**](irp-mj-system-control.md) and a minor code that indicates the specific WMI request. The WMI kernel-mode component can send WMI IRPs any time following a driver's successful registration as a supplier of WMI data. WMI IRPs typically get sent when a user-mode data consumer has requested WMI data.

All drivers must set a dispatch table entry point for a [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine to handle WMI requests.

If a driver registers as a WMI data provider by calling [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480), it must handle WMI IRPs using one of the techniques described in [Handling WMI Requests](https://msdn.microsoft.com/library/windows/hardware/ff546968).

Drivers that do not register as WMI data providers must forward all WMI requests to the next-lower driver.

This section describes the following system-defined WMI minor function codes:

[**IRP\_MN\_CHANGE\_SINGLE\_INSTANCE**](irp-mn-change-single-instance.md)

[**IRP\_MN\_CHANGE\_SINGLE\_ITEM**](irp-mn-change-single-item.md)

[**IRP\_MN\_DISABLE\_COLLECTION**](irp-mn-disable-collection.md)

[**IRP\_MN\_DISABLE\_EVENTS**](irp-mn-disable-events.md)

[**IRP\_MN\_ENABLE\_COLLECTION**](irp-mn-enable-collection.md)

[**IRP\_MN\_ENABLE\_EVENTS**](irp-mn-enable-events.md)

[**IRP\_MN\_EXECUTE\_METHOD**](irp-mn-execute-method.md)

[**IRP\_MN\_QUERY\_ALL\_DATA**](irp-mn-query-all-data.md)

[**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](irp-mn-query-single-instance.md)

[**IRP\_MN\_REGINFO**](irp-mn-reginfo.md)

[**IRP\_MN\_REGINFO\_EX**](irp-mn-reginfo-ex.md)

If the driver receives an IRP containing any other IRP minor function code, it should forward the IRP to the next-lower driver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20WMI%20Minor%20IRPs%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


