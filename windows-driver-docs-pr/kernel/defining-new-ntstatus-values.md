---
title: Defining New NTSTATUS Values
author: windows-driver-content
description: Defining New NTSTATUS Values
ms.assetid: 44211ae4-6bfe-4931-b12c-e590c7aacd97
keywords: ["NTSTATUS values WDK kernel", "custom NTSTATUS values WDK kernel", "IO_ERR_XXX values"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Defining New NTSTATUS Values


## <a href="" id="ddk-defining-new-ntstatus-values-kg"></a>


Drivers can define custom IO\_ERR\_*XXX* constants to use as **ErrorCode** values when logging errors. Pairs of drivers that are written together can also define custom STATUS\_*XXX* values for [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests.

The following diagram shows the bit fields in a 32-bit NTSTATUS value.

![diagram illustrating the bit fields in an ntstatus value](images/16ntstat.png)

The **Sev** field shown in the preceding diagram indicates the severity code, which must be one of the following system-defined values:

<a href="" id="status-severity-success"></a>STATUS\_SEVERITY\_SUCCESS  
Indicates a successful NTSTATUS value, such as STATUS\_SUCCESS, or the value IO\_ERR\_RETRY\_SUCCEEDED in error log packets.

<a href="" id="status-severity-informational"></a>STATUS\_SEVERITY\_INFORMATIONAL  
Indicates an informational NTSTATUS value, such as STATUS\_SERIAL\_MORE\_WRITES.

<a href="" id="status-severity-warning"></a>STATUS\_SEVERITY\_WARNING  
Indicates a warning NTSTATUS value, such as STATUS\_DEVICE\_PAPER\_EMPTY.

<a href="" id="status-severity-error"></a>STATUS\_SEVERITY\_ERROR  
Indicates an error NTSTATUS value, such as STATUS\_INSUFFICIENT\_RESOURCES for a **FinalStatus** value or IO\_ERR\_CONFIGURATION\_ERROR for an **ErrorCode** value in error log packets.

Most public IO\_ERR\_*XXX* constants belong to the STATUS\_SEVERITY\_ERROR category.

The **Facility** code specifies the facility that generated the error. For new IO\_ERR\_*XXX* values, drivers specify the FACILITY\_IO\_ERROR\_CODE value for **Facility**. For custom STATUS\_*XXX* values, the meaning of different values for **Facility** is driver-defined.

The **C** bit specifies if the value is customer-defined or Microsoft-defined. The bit is set for customer-defined values and clear for Microsoft-defined values.

Drivers can define new IO\_ERR\_*XXX* values to identify custom error messages in the system event log. For a description of how to define the NTSTATUS values and the error messages that they identify, see [Defining Custom Error Types](defining-custom-error-types.md).

Pairs of drivers can define driver-specific STATUS\_*XXX* values to communicate information about privately defined [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests from the lower to the higher driver of the pair.

The class driver must map any private STATUS\_*XXX* value to a system-defined NTSTATUS value when it completes an IRP if an existing higher-level driver's [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine might be called for that IRP.

For paired display and video miniport drivers, the video port driver does the mapping between public STATUS\_*XXX* values and the Win32-defined constants returned by video miniport drivers. For more information, see [Video Miniport Drivers in the Windows 2000 Display Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff570509).

Drivers cannot use custom NTSTATUS values for IRPs that can be received in user mode, because only the system-defined values can be translated into Win32 error codes.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Defining%20New%20NTSTATUS%20Values%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


