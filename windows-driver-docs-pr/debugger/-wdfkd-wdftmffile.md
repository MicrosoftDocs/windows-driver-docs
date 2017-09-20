---
title: wdfkd.wdftmffile
description: The wdfkd.wdftmffile extension sets the trace message format (.tmf) file to use when the debugger is formatting KMDF error logs for the wdfkd.wdflogdump or wdfkd.wdfcrashdump.
ms.assetid: 7099440c-bfea-472f-b9ee-943026afdb81
keywords: ["wdfkd.wdftmffile Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wdfkd.wdftmffile
api_type:
- NA
---

# !wdfkd.wdftmffile


The **!wdfkd.wdftmffile** extension sets the trace message format (.tmf) file to use when the debugger is formatting Kernel-Mode Driver Framework (KMDF) error log records for the [**!wdfkd.wdflogdump**](-wdfkd-wdflogdump.md) or [**!wdfkd.wdfcrashdump**](-wdfkd-wdfcrashdump.md) extensions.

```
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

```
kd> !wdftmffile tools\tracing\<platform>\wdf1005.tmf
```

Note that the path might be different for the version of the Windows Driver Kit (WDK) that you are using. Also note that the .tmf file's name represents the version of KMDF that you are using. For example, Wdf1005.tmf is the .tmf file for KMDF version 1.5.

For information about how to view the KMDF log during a debugging session, see [Using the Framework's Event Logger](https://msdn.microsoft.com/library/windows/hardware/ff545531).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdftmffile%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




