---
title: Process and Thread Termination Issues
author: windows-driver-content
description: Process and Thread Termination Issues
ms.assetid: 11b38c60-1bd8-4f1b-a80e-14a93e4ac474
keywords: ["security WDK file systems , adding security checks", "security checks WDK file systems , process and thread terminations", "process terminations WDK file systems", "thread terminations WDK file systems", "terminated processes or threads WDK file systems"]
---

# Process and Thread Termination Issues


## <span id="ddk_process_and_thread_termination_issues_if"></span><span id="DDK_PROCESS_AND_THREAD_TERMINATION_ISSUES_IF"></span>


File systems that store state information related to specific users might need to watch for process and thread termination conditions. For example, encryption keys associated with a particular user might need to be discarded on the termination (whether planned or premature) of a specialized control application. For more information about the routines used to handle these conditions, see [**PsSetCreateProcessNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559951) and [**PsSetCreateThreadNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559954).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Process%20and%20Thread%20Termination%20Issues%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


