---
title: "!wmitrace.dumpmini"
description: "The !wmitrace.dumpmini extension displays the system trace fragment, which is stored in a dump file."
keywords: ["!wmitrace.dumpmini Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wmitrace.dumpmini
api_type:
- NA
---

# !wmitrace.dumpmini

The **!wmitrace.dumpmini** extension displays the system trace fragment, which is stored in a dump file.

```dbgcmd
!wmitrace.dumpmini
```

## DLL

Wmitrace.dll

This extension is available in Windows Vista and later versions of Windows.

This extension is useful only when debugging a minidump file or a full dump file.

## Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about tracing tools, see the Windows Driver Kit (WDK).

## Remarks

The *system trace fragment* is a copy of the contents of the last buffer of the System Context Log. Under normal conditions, this is the trace session whose logger ID is 2.
