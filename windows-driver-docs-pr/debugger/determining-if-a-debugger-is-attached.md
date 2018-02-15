---
title: Determining if a Debugger is Attached
description: Determining if a Debugger is Attached
ms.assetid: 78f7d90a-459c-4967-a980-3f8d6339eb77
keywords: ["determining if a debugger is attached", "KdRefreshDebuggerNotPresent function", "KD_DEBUGGER_ENABLED global variable", "KD_DEBUGGER_NOT_PRESENT global variable"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Determining if a Debugger is Attached


## <span id="ddk_determining_if_a_debugger_is_attached_dbg"></span><span id="DDK_DETERMINING_IF_A_DEBUGGER_IS_ATTACHED_DBG"></span>


Kernel-mode code can determine the status of kernel debugging by using the following variables and routines:

-   (Windows XP and later) The KD\_DEBUGGER\_ENABLED global kernel variable indicates whether kernel debugging is enabled.

-   (Windows XP and later) The KD\_DEBUGGER\_NOT\_PRESENT global kernel variable indicates whether a kernel debugger is currently attached.

-   (Windows Server 2003 and later) The **KdRefreshDebuggerNotPresent** routine refreshes the value of KD\_DEBUGGER\_NOT\_PRESENT.

For complete documentation, see the Windows Driver Kit.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Determining%20if%20a%20Debugger%20is%20Attached%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




