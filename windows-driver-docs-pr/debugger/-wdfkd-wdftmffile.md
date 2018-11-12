---
title: wdfkd.wdftmffile
description: The wdfkd.wdftmffile extension sets the trace message format (.tmf) file to use when the debugger is formatting KMDF error logs for the wdfkd.wdflogdump or wdfkd.wdfcrashdump.
ms.assetid: 7099440c-bfea-472f-b9ee-943026afdb81
keywords: ["wdfkd.wdftmffile Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdftmffile
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdftmffile


The **!wdfkd.wdftmffile** extension sets the trace message format (.tmf) file to use when the debugger is formatting Kernel-Mode Driver Framework (KMDF) error log records for the [**!wdfkd.wdflogdump**](-wdfkd-wdflogdump.md) or [**!wdfkd.wdfcrashdump**](-wdfkd-wdfcrashdump.md) extensions.

```dbgcmd
!wdfkd.wdftmffile TMFpath
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______TMFpath______"></span><span id="_______tmfpath______"></span><span id="_______TMFPATH______"></span> *TMFpath*   
A path that contains the .tmf file.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

If your driver uses a KMDF version earlier than 1.11, you must use the **!wdfkd.wdftmffile** extension before you can use the [**!wdfkd.wdflogdump**](-wdfkd-wdflogdump.md) or [**!wdfkd.wdfcrashdump**](-wdfkd-wdfcrashdump.md) extensions.

Starting in KMDF version 1.11, the framework library's symbol file (for example wdf01000.pdb) contains the trace message format (TMF) entries. Starting in the Windows 8 version of the kernel debugger, the [Kernel-Mode Driver Framework Extensions (Wdfkd.dll)](kernel-mode-driver-framework-extensions--wdfkd-dll-.md) read the entries from the .pdb file. As a result, if your driver uses KMDF version 1.11 or later, and you are using the kernel debugger from Windows 8 or later, you do not need to use **!wdfkd.wdftmffile**. You do need to include the directory that contains the symbol file in the debugger's [symbol path](symbol-path.md). The debugging target machine can be running any operating system that supports KMDF.

The following example shows how to use the **!wdfkd.wdftmffile** extension from the root WDK directory, for KMDF version 1.5.

```dbgcmd
kd> !wdftmffile tools\tracing\<platform>\wdf1005.tmf
```

Note that the path might be different for the version of the Windows Driver Kit (WDK) that you are using. Also note that the .tmf file's name represents the version of KMDF that you are using. For example, Wdf1005.tmf is the .tmf file for KMDF version 1.5.

For information about how to view the KMDF log during a debugging session, see [Using the Framework's Event Logger](https://msdn.microsoft.com/library/windows/hardware/ff545531).

 

 





