---
title: Calling WmiSystemControl to Handle WMI IRPs
author: windows-driver-content
description: Calling WmiSystemControl to Handle WMI IRPs
ms.assetid: a2fa53e2-6468-4c3c-8b41-9a97305abc43
keywords: ["WMI WDK kernel , requests", "requests WDK WMI", "IRPs WDK WMI", "WmiSystemControl"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Calling WmiSystemControl to Handle WMI IRPs


## <a href="" id="ddk-calling-wmisystemcontrol-to-handle-wmi-irps-kg"></a>


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

1.  The driver calls **WmiSystemControl** with a pointer to its initialized **WMILIB\_CONTEXT** structure, a pointer to its device object, and a pointer to the IRP.

2.  WMI validates the IRP parameters and calls the driver's *DpWmiXxx* routine that processes the request. If the driver set no entry point in its **WMILIB\_CONTEXT** for an optional *DpWmiXxx* routine, WMI completes the IRP with default values and status.

3.  In its *DpWmiXxx* routine, the driver processes the request and writes any output to the caller-supplied buffer. For example, a driver's [*DpWmiQueryDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine would write the requested instance(s) of the specified block to the buffer.

4.  In all *DpWmiXxx* routines except [*DpWmiQueryReginfo*](https://msdn.microsoft.com/library/windows/hardware/ff544097), the driver calls [**WmiCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff565798) to complete the request, or returns STATUS\_PENDING to postpone completion, as for any IRP.

5.  WMI performs any necessary postprocessing, packages any output in an appropriate **WNODE\_*XXX*** structure, and passes the output and status to the data consumer.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Calling%20WmiSystemControl%20to%20Handle%20WMI%20IRPs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


