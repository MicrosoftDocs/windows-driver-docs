---
title: "!wmitrace.dumpminievent"
description: "The !wmitrace.dumpminievent extension displays the system event log trace fragment, which is stored in a dump file."
keywords: ["!wmitrace.dumpminievent Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wmitrace.dumpminievent
api_type:
- NA
---

# !wmitrace.dumpminievent


The **!wmitrace.dumpminievent** extension displays the system event log trace fragment, which is stored in a dump file.

```dbgcmd
!wmitrace.dumpminievent
```

## DLL

Wmitrace.dll

This extension is available in Windows Vista Service Pack 1 (SP1) and later versions of Windows.

This extension is useful only when debugging a minidump file or a full dump file.

## Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about tracing tools, see the Windows Driver Kit (WDK).

## Remarks

The *system event log trace fragment* is a copy of the contents of the last buffer of the System Event Log. The **!wmitrace.dumpminievent** extension displays its contents in event log format.

