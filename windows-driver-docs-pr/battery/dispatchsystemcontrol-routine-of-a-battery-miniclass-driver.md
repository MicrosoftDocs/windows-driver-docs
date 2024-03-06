---
title: Battery Miniclass Driver's DispatchSystemControl Routine
description: Discover the DispatchSystemControl routine in battery miniclass drivers and its role in supporting Windows Management Instrumentation (WMI).
keywords:
- battery miniclass drivers WDK, routines
- DispatchSystemControl routine
- WMI WDK battery
ms.date: 10/04/2023
---

# DispatchSystemControl Routine of a Battery Miniclass Driver

Battery miniclass drivers must support [Windows Management Instrumentation (WMI)](../kernel/implementing-wmi.md) by providing a [*DispatchSystemControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine to handle the [**IRP_MJ_SYSTEM_CONTROL**](../kernel/irp-mj-system-control.md) IRP. WMI offers a consistent way for drivers to expose measurement and instrumentation data.

To perform initial processing, battery miniclass drivers use the [**BatteryClassSystemControl**](/windows/win32/api/batclass/nf-batclass-batteryclasssystemcontrol) routine, which takes a *WmiLibContext* parameter specifying a dispatch table of functions. The routine uses the **MinorFunction** member of IRP_MJ_SYSTEM_CONTROL to determine the dispatch function it calls.

All drivers for battery devices must handle certain WMI queries. Battery miniclass drivers forward these WMI queries to the battery class driver instead of directly supporting them. To handle WMI queries, the miniclass driver provides a pointer to a [**DpWmiQueryDataBlock**](/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_query_datablock_callback) routine in the **QueryWmiDataBlock** member of [**WMILIB_CONTEXT**](/windows-hardware/drivers/ddi/wmilib/ns-wmilib-_wmilib_context). The miniclass driver is not required to handle any other type of WMI request and can set the other members of WMILIB_CONTEXT to zero if it doesn't.

In its [**DpWmiQueryDataBlock**](/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_query_datablock_callback) routine, the miniclass driver calls the [**BatteryClassQueryWmiDataBlock**](/windows/win32/api/batclass/nf-batclass-batteryclassquerywmidatablock) routine, allowing the battery class driver to handle the WMI query request if possible. If the battery class driver handles the WMI class GUID, it completes the IRP. Otherwise, **BatteryClassQueryWmiDataBlock** returns a value of STATUS_WMI_GUID_NOT_FOUND. The miniclass driver can then perform driver-specific processing and use [**WmiCompleteRequest**](/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmicompleterequest) to complete the request.

Battery miniclass drivers only need to call **BatteryClassQueryWmiDataBlock** for WMI IRP processing. In a minimal WMI handling implementation for a battery miniclass driver, if **BatteryClassQueryWmiDataBlock** returns STATUS_WMI_GUID_NOT_FOUND, the miniclass driver simply calls [**WmiCompleteRequest**](/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmicompleterequest) with a status value of STATUS_WMI_GUID_NOT_FOUND.
