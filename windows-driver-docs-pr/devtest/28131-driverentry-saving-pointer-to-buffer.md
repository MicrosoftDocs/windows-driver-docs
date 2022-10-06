---
title: C28131 warning
description: Warning C28131 The DriverEntry routine should save a copy of the argument, not the pointer, because the I/O Manager frees the buffer.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 09/27/2022
f1_keywords: ["C28131", "NOT_COPYING_NAME", "__WARNING_NOT_COPYING_NAME"]
---
# Warning C28131

> The DriverEntry routine should save a copy of the argument, not the pointer, because the I/O Manager frees the buffer

## Remarks

The driver's `DriverEntry` routine is saving a copy of the pointer to the buffer instead of saving a copy of the buffer. Because the buffer is freed when the `DriverEntry` routine returns, the pointer to the buffer will soon be invalid.

Code analysis name: NOT_COPYING_NAME

 ## Example

The following code generates this warning. `g_RP` is of type `PUNICODE_STRING`, which is a pointer to the data type `UNICODE_STRING`. By saving `PUNICODE_STRING RegistryPath`, we are only saving the pointer to the `UNICODE_STRING` where the data exists. This will be lost at the end of `DriverEntry`.

```cpp
PUNICODE_STRING g_RP;

NTSTATUS
DriverEntry(
    PDRIVER_OBJECT DriverObject,
    PUNICODE_STRING RegistryPath
    )
{
    g_RP = RegistryPath;
    return 0;
}
```

The following code remediates this issue. `g_RP` is now a `UNICODE_STRING`, with its own buffer. When the data is copied over, it will persist beyond the return of `DriverEntry`

```cpp
UNICODE_STRING g_RP;

NTSTATUS
DriverEntry(
    PDRIVER_OBJECT DriverObject,
    PUNICODE_STRING RegistryPath
    )
{
    g_RP = CloneRegistryPath(RegistryPath);  // CloneRegistryPath is an example helper function that copies over the data.
    return 0;
}
```
