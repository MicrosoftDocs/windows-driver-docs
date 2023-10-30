---
title: errlog (WinDbg)
description: The errlog extension displays the contents of any pending entries in the I/O system's error log.
keywords: ["errlog Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- errlog
api_type:
- NA
---

# !errlog


The **!errlog** extension displays the contents of any pending entries in the I/O system's error log.

```dbgcmd
!errlog 
```

## <span id="ddk__errlog_dbg"></span><span id="DDK__ERRLOG_DBG"></span>


### DLL

Kdexts.dll

 

### Additional Information

For information about [**IoWriteErrorLogEntry**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iowriteerrorlogentry), see the Windows Driver Kit (WDK) documentation.

## Remarks

This command displays information about any pending events in the I/O system's error log. These are events queued by calls to the [**IoWriteErrorLogEntry**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iowriteerrorlogentry) function, to be written to the system's event log for subsequent viewing by the **Event Viewer**.

Only entries that were queued by [**IoWriteErrorLogEntry**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iowriteerrorlogentry) but have not been committed to the error log will be displayed.

This command can be used as a diagnostic aid after a system crash because it reveals pending error information that was unable to be committed to the error log before the system halted.

 

