---
title: Calling WmiSystemControl to Handle WMI IRPs
description: Calling WmiSystemControl to Handle WMI IRPs
ms.assetid: a2fa53e2-6468-4c3c-8b41-9a97305abc43
keywords: ["WMI WDK kernel , requests", "requests WDK WMI", "IRPs WDK WMI", "WmiSystemControl"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Calling WmiSystemControl to Handle WMI IRPs





WMI library routines simplify handling of WMI requests because instead of processing each such request, a driver calls [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834). In the **WmiSystemControl** call, the driver passes an initialized [**WMILIB\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff565813) structure that contains entry points to the driver's [WMI library callback routines](https://msdn.microsoft.com/library/windows/hardware/ff566357) (*DpWmiXxx* routines) and information about the driver's data blocks and event blocks.

Because the WMI library provides no mechanism for passing dynamic instance names or a static instance name list, a driver can use the WMI library to handle requests involving only data blocks with static instance names based on a PDO or a single base name string. For more information about static and dynamic instance names, see [Defining WMI Instance Names](defining-wmi-instance-names.md). Nothing prevents a driver from using the WMI library to handle requests for such blocks and processing requests for other blocks in its [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine. For more information, see [Processing WMI IRPs in a DispatchSystemControl Routine](processing-wmi-irps-in-a-dispatchsystemcontrol-routine.md).

To handle WMI IRPs by calling **WmiSystemControl**, a driver must implement certain required *DpWmiXxx* callback routines, and might implement additional optional *DpWmiXxx* callback routines:

-   [*DpWmiQueryReginfo*](https://msdn.microsoft.com/library/windows/hardware/ff544097)—(Required) Provides information about the data and event blocks being registered by the driver. WMI calls a driver's *DpWmiQueryReginfo* routine to process an [**IRP\_MN\_REGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551731) or [**IRP\_MN\_REGINFO\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff551734) request. For more information, see [Using the WMI Library to Register Blocks](using-the-wmi-library-to-register-blocks.md).

-   [*DpWmiQueryDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544096)—(Required) Returns either a single instance or all instances of a data block. WMI calls a driver's *DpWmiQueryDataBlock* routine to process an [**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff551718) or [**IRP\_MN\_QUERY\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff551650) request.

-   [*DpWmiSetDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544104)—(Optional) Changes all data items in a single instance of a data block. WMI calls a driver's *DpWmiSetDataBlock* routine to process an [**IRP\_MN\_CHANGE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff550831) request.

-   [*DpWmiSetDataItem*](https://msdn.microsoft.com/library/windows/hardware/ff544108)—(Optional) Changes a single data item in an instance of a data block. WMI calls a driver's *DpWmiSetDataItem* routine to process an [**IRP\_MN\_CHANGE\_SINGLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff550836) request.

-   [*DpWmiFunctionControl*](https://msdn.microsoft.com/library/windows/hardware/ff544094)—(Optional) Enables and disables event notification and data collection for blocks registered as expensive to collect. WMI calls a driver's *DpWmiFunctionControl* routine to process an [**IRP\_MN\_ENABLE\_COLLECTION**](https://msdn.microsoft.com/library/windows/hardware/ff550857), [**IRP\_MN\_DISABLE\_COLLECTION**](https://msdn.microsoft.com/library/windows/hardware/ff550848), [**IRP\_MN\_ENABLE\_EVENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550859), or [**IRP\_MN\_DISABLE\_EVENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550851) request.

-   [*DpWmiExecuteMethod*](https://msdn.microsoft.com/library/windows/hardware/ff544090)—(Optional) Executes a method associated with a data block. WMI calls a driver's *DpWmiExecuteMethod* routine to process an [**IRP\_MN\_EXECUTE\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff550868) request.

A driver's *DpWmiXxx* routines can have any names chosen by the driver writer.

Before calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), the driver must initialize a [**WMILIB\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff565813) structure with entry points to its *DpWmiXxx* routines and information about its data blocks and event blocks.

When the driver receives a WMI request:

1. The driver calls **WmiSystemControl** with a pointer to its initialized **WMILIB\_CONTEXT** structure, a pointer to its device object, and a pointer to the IRP.

2. WMI validates the IRP parameters and calls the driver's *DpWmiXxx* routine that processes the request. If the driver set no entry point in its **WMILIB\_CONTEXT** for an optional *DpWmiXxx* routine, WMI completes the IRP with default values and status.

3. In its *DpWmiXxx* routine, the driver processes the request and writes any output to the caller-supplied buffer. For example, a driver's [*DpWmiQueryDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine would write the requested instance(s) of the specified block to the buffer.

4. In all *DpWmiXxx* routines except [*DpWmiQueryReginfo*](https://msdn.microsoft.com/library/windows/hardware/ff544097), the driver calls [**WmiCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff565798) to complete the request, or returns STATUS\_PENDING to postpone completion, as for any IRP.

5. WMI performs any necessary postprocessing, packages any output in an appropriate **WNODE\_*XXX*** structure, and passes the output and status to the data consumer.

 

 




