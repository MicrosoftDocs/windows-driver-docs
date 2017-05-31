---
title: wdfkd.wdfsearchpath
description: The wdfkd.wdfsearchpath extension sets the search path to formatting files for Kernel-Mode Driver Framework (KMDF) error log records.
ms.assetid: cb52dc07-00b3-47d3-8636-4a6cd5ff3e29
keywords: ["wdfkd.wdfsearchpath Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wdfkd.wdfsearchpath
api_location:
- Wdfkd.dll
api_type:
- DllExport
---

# !wdfkd.wdfsearchpath


The **!wdfkd.wdfsearchpath** extension sets the search path to formatting files for Kernel-Mode Driver Framework (KMDF) error log records.

```
!wdfkd.wdfsearchpath Path
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Path______"></span><span id="_______path______"></span><span id="_______PATH______"></span> *Path*   
The path of a directory that contains KMDF formatting files.

## <span id="DLL"></span><span id="dll"></span>DLL


Wdfkd.dll

## <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks


KMDF 1, UMDF 2

## <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information


For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

The KMDF formatting files are included in the Windows Driver Kit (WDK). The path to the formatting files depends on the installation directory of your WDK and on the version of the WDK that you have installed. The KMDF formatting files have extension tmf (trace message formatting). To determine the search path, browse or search your WDK installation for file names of the form Wdf*VersionNumber*.tmf. The following example shows how to use the **!wdfkd.wdfsearchpath** extension.

```
kd> !wdfsearchpath C:\WinDDK\7600\tools\tracing\amd64
```

The TRACE\_FORMAT\_SEARCH\_PATH environment variable also controls the search path, but the **!wdfkd.wdfsearchpath** extension takes precedence over the search path that TRACE\_FORMAT\_SEARCH\_PATH specifies.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>DLL</p></td>
<td align="left">Wdfkd.dll</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdfsearchpath%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




