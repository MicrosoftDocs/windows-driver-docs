---
title: Process and Thread Termination Issues
description: Process and Thread Termination Issues
keywords:
- security WDK file systems , adding security checks
- security checks WDK file systems , process and thread terminations
- process terminations WDK file systems
- thread terminations WDK file systems
- terminated processes or threads WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Process and Thread Termination Issues


## <span id="ddk_process_and_thread_termination_issues_if"></span><span id="DDK_PROCESS_AND_THREAD_TERMINATION_ISSUES_IF"></span>


File systems that store state information related to specific users might need to watch for process and thread termination conditions. For example, encryption keys associated with a particular user might need to be discarded on the termination (whether planned or premature) of a specialized control application. For more information about the routines used to handle these conditions, see [**PsSetCreateProcessNotifyRoutine**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetcreateprocessnotifyroutine) and [**PsSetCreateThreadNotifyRoutine**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetcreatethreadnotifyroutine).

 

