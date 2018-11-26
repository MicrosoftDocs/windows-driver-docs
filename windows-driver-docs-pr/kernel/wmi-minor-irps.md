---
title: WMI Minor IRPs
description: WMI Minor IRPs
ms.date: 08/12/2017
ms.assetid: 5788294f-2145-4381-9b06-3b138b2d26df
ms.localizationpriority: medium
---

# WMI Minor IRPs





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

 

 




