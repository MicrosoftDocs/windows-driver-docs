---
title: Debugging an Application Failure
description: Debugging an Application Failure
ms.assetid: c4118acb-2566-441a-8481-dee4bfdb03ba
keywords: ["application failures"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging an Application Failure


## <span id="ddk_debugging_an_application_failure_dbg"></span><span id="DDK_DEBUGGING_AN_APPLICATION_FAILURE_DBG"></span>


There are a variety of errors possible in user-mode applications.

The most common kinds of failures include access violations, alignment faults, exceptions, critical section time-outs (deadlocks), and in-page I/O errors.

Access violations and data type misalignments are among the most common. They usually occur when an invalid pointer is dereferenced. The blame could lie with the function that caused the fault, or with an earlier function that passed an invalid parameter to the faulting function.

User-mode exceptions have many possible causes. If an unknown exception occurs, locate it in ntstatus.h or winerror.h if possible.

Critical section timeouts (or possible deadlocks) occur when one thread is waiting for a critical section for a long time. These are difficult to debug and require an in-depth analysis of the stack trace.

In-page I/O errors are almost always hardware failures. You can double-check the status code in ntstatus.h to verify.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20an%20Application%20Failure%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




