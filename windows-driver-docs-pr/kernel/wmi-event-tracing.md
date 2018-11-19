---
title: WMI Event Tracing
description: WMI Event Tracing
ms.assetid: 72505a9a-830a-4529-ba73-31af0fedfeec
keywords: ["WMI WDK kernel , event tracking", "events WDK WMI", "tracing WDK WMI", "WMI WDK kernel , WDM drivers", "WDM drivers WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# WMI Event Tracing





This section describes the WMI extensions to WDM (supported by Windows 2000 and later) that kernel-mode drivers, as information providers, can use to provide information to information consumers. Drivers typically provide information that a consumer uses to determine the driver's configuration and resource usage. In addition to the WMI extensions to WDM, a user-mode API supports providers or consumers of WMI event information—see the Windows SDK for more information.

The event tracing logger supports up to 32 instances. One of the instances is reserved for tracing the kernel. The logger supports tracing a high event rate.

Trace events are defined in the same manner as other WMI events. WMI events are described in the MOF file. For more information about WMI event descriptions, see [MOF Syntax for WMI Data and Event Blocks](mof-syntax-for-wmi-data-and-event-blocks.md).

The process by which kernel-mode drivers log information is integrated into the existing WMI infrastructure. To log trace events, a driver does the following:

1.  Register as a WMI provider by calling [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480).

2.  Mark events as traceable by setting WMIREG\_FLAG\_TRACED\_GUID in the **Flags** member of the [**WMIREGGUID**](https://msdn.microsoft.com/library/windows/hardware/ff565827) structure that is passed when the driver registers events with WMI.

3.  Specify one event as the control event for overall enabling/disabling of a set of trace events by setting WMIREG\_FLAG\_TRACE\_CONTROL\_GUID in the **Flags** member of the **WMIREGGUID** structure that is passed when the driver registers events with WMI.

4.  Upon receiving a request from WMI to enable events where the GUID matches the trace control GUID, the driver should store the handle to the logger. The value will be needed when writing an event. For information about how to use this handle, see step 6. The logger handle value is contained in the **HistoricalContext** member of the [**WNODE\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566375) portion of the WMI buffer that is part of the parameters in the enable events request.

5.  Decide whether the trace event will be sent to WMI event consumers or is targeted for the WMI event logger only. This will determine where the memory for the [**EVENT\_TRACE\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff544329) structure should come from. This memory will eventually be passed to [**IoWMIWriteEvent**](https://msdn.microsoft.com/library/windows/hardware/ff550520).

    If the event is a log event only, the memory will not be deleted by WMI. In this case, the driver should pass in a buffer on the stack or should be reusing an allocated buffer for this purpose. For performance reasons, the driver should minimize any unnecessary calls to allocate or free memory. Failure to comply with this recommendation will compromise the integrity of the timing information contained in the log file.

    If the event is to be sent to both the logger and to WMI event consumers, then the memory must be allocated from a nonpaged pool. In this case the event will be sent to the logger and then forwarded to WMI to be sent to WMI event consumers who have requested notification of the event. The memory for the event will then be freed by WMI according to the behavior of **IoWMIWriteEvent**.

6.  After the memory for the [**EVENT\_TRACE\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff544329) and any driver event data, if any, has been secured, the following information should be set:

    Set the **Size** member to the sizeof(**EVENT\_TRACE\_HEADER**) plus the size of any additional driver event data that will be appended on to the end of **EVENT\_TRACE\_HEADER**.

    Set the **Flags** member to WNODE\_FLAG\_TRACED\_GUID to have the event sent to the logger. If the event is to be sent to WMI event consumers as well, set the WNODE\_FLAG\_LOG\_WNODE. Note, it is not necessary to set WNODE\_FLAG\_TRACED\_GUID if setting WNODE\_FLAG\_LOG\_WNODE. If both are set, WNODE\_FLAG\_TRACED\_GUID will take precedence and the event will not be sent to WMI event consumers.

    Set the **Guid** or the **GuidPtr** member. If using **GuidPtr**, set WNODE\_FLAG\_USE\_GUID\_PTR in the **Flags** member.

    Optionally, specify a value for **TimeStamp**. If the driver does not specify a **TimeStamp** value the logger will fill this in. If the driver does not want the logger to set the time stamp then it should set WNODE\_FLAG\_USE\_TIMESTAMP in the **Flags** member.

    Set any of the following **EVENT\_TRACE\_HEADER** members that have meaning to the driver: **Class.Type**, **Class.Level**, and **Class.Version**.

    Finally cast the **EVENT\_TRACE\_HEADER** to a **WNODE\_HEADER** and set the **HistoricalContext** value of the **Wnode** to the logger handle that was saved in step 4 above.

7.  Call [**IoWMIWriteEvent**](https://msdn.microsoft.com/library/windows/hardware/ff550520) with the pointer to the **EVENT\_TRACE\_HEADER** structure.

The driver should continue logging trace events associated with the control GUID until the driver receives notification to disable event logging via an **IRP\_MN\_DISABLE\_EVENTS** request.

 

 




