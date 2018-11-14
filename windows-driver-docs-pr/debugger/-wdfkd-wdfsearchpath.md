---
title: wdfkd.wdfsearchpath
description: The wdfkd.wdfsearchpath extension sets the search path to formatting files for Kernel-Mode Driver Framework (KMDF) error log records.
ms.assetid: cb52dc07-00b3-47d3-8636-4a6cd5ff3e29
keywords: ["wdfkd.wdfsearchpath Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfsearchpath
api_location:
- Wdfkd.dll
api_type:
- DllExport
ms.localizationpriority: medium
---

# !wdfkd.wdfsearchpath


The **!wdfkd.wdfsearchpath** extension sets the search path to formatting files for Kernel-Mode Driver Framework (KMDF) error log records.

```dbgcmd
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

```dbgcmd
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

 

 





