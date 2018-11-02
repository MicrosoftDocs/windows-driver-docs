---
title: errlog
description: The errlog extension displays the contents of any pending entries in the I/O system's error log.
ms.assetid: 2ef6331e-fa83-4515-8d70-5094e40b8497
keywords: ["errlog Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- errlog
api_type:
- NA
ms.localizationpriority: medium
---

# !errlog


The **!errlog** extension displays the contents of any pending entries in the I/O system's error log.

```dbgcmd
!errlog 
```

## <span id="ddk__errlog_dbg"></span><span id="DDK__ERRLOG_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about [**IoWriteErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff550527), see the Windows Driver Kit (WDK) documentation.

Remarks
-------

This command displays information about any pending events in the I/O system's error log. These are events queued by calls to the [**IoWriteErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff550527) function, to be written to the system's event log for subsequent viewing by the **Event Viewer**.

Only entries that were queued by [**IoWriteErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff550527) but have not been committed to the error log will be displayed.

This command can be used as a diagnostic aid after a system crash because it reveals pending error information that was unable to be committed to the error log before the system halted.

 

 





