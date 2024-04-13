---
title: Bug Check 0x1A7 SMB_REDIRECTOR_LIVEDUMP
description: The SMB_REDIRECTOR_LIVEDUMP live dump has a value of 0x000001A7. It indicates that the SMB redirector has detected a problem and has captured a kernel dump to collect debug information.
keywords: ["Bug Check 0x1A7 SMB_REDIRECTOR_LIVEDUMP", "SMB_REDIRECTOR_LIVEDUMP"]
ms.date: 01/10/2019
topic_type:
- apiref
ms.topic: reference
api_name:
- SMB_REDIRECTOR_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x1A7: SMB\_REDIRECTOR\_LIVEDUMP

The SMB\_REDIRECTOR\_LIVEDUMP live dump has a value of 0x000001A7. It indicates that the SMB redirector has detected a problem and has captured a kernel dump to collect debug information.

## SMB\_REDIRECTOR\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Reason Code - see values below.|
|2| See values below.|
|3| Reserved.|
|4| Reserved.|

The SMB redirector has detected a problem and has captured a kernel dump to collect debug information.

**Reason Code**

```text
0x1 : An I/O failed to complete in a reasonable amount of time.
    2 - Pointer to the connection object.
    3 - Reserved.
    4 - Reserved.
```

## Cause

The SMB redirector has detected a problem and has captured a kernel dump to collect debug information.

A live dump with this bugcheck code will be generated only if the following registry value is set.

```registry
HKLM\System\CurrentControlSet\Services\Lanmanworkstation\Parameters [DWORD] LiveDumpFilter = 1
```

When this registry key is set and the RDR times out on IO, a livedump will occur.

(This code can never be used for a real bugcheck; it is used to identify live dumps.)

## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)
