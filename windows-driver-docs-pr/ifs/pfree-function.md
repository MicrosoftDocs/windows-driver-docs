---
title: PFREE_FUNCTION function pointer
description: A PFREE_FUNCTION typed routine can be registered by a file system legacy filter driver as the filter's FreeCallback callback routine.
keywords: ["PFREE_FUNCTION function pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FreeCallback
api_location:
- wdm.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PFREE_FUNCTION function pointer

A **PFREE_FUNCTION** typed routine can be registered by a file system legacy filter driver as the filter's *FreeCallback* callback routine. The file system calls *FreeCallback* when the file system removes a file context object by using [**FsRtlTeardownPerFileContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperfilecontexts) or removes a stream context object by using [**FsRtlTeardownPerStreamContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperstreamcontexts).

You must declare the callback routine by using the **FREE_FUNCTION** type. For more information, see the example in the Remarks section.

## Syntax

```ManagedCPlusPlus
typedef VOID ( *FreeCallback)(
  _In_ PVOID Buffer
);
```

## Parameters

*Buffer* \[in\]  
A pointer to the [**FSRTL_PER_FILE_CONTEXT**](/previous-versions/ff547352(v=vs.85)) or the [**FSRTL_PER_STREAM_CONTEXT**](/previous-versions/ff547357(v=vs.85)) structure to be freed.

## ## Return value

None

## Remarks

When a file system tears down the per file context object for a file, it must call [**FsRtlTeardownPerFileContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperfilecontexts). This routine calls the *FreeCallback* routines of all per-file context structures associated with the file. This callback routine must free any memory used for the [**FSRTL_PER_FILE_CONTEXT**](/previous-versions/ff547352(v=vs.85)) object and any associated context information. This is also the case for per stream contexts when [**FsRtlTeardownPerStreamContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperstreamcontexts) is called and *FreeCallback* will free memory used for [**FSRTL_PER_STREAM_CONTEXT**](/previous-versions/ff547357(v=vs.85)) objects.

For remarks about synchronizing access to per file context objects or to per stream context objects during a call to *FreeCallback*, see [**FsRtlTeardownPerFileContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperfilecontexts) and [**FsRtlTeardownPerStreamContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperstreamcontexts).

> [!NOTE]
> The *FreeCallback* routine cannot recursively call down into the file system or acquire any file system resources.

To define a *FreeCallback* callback function that is named *MyFreeFunction*, you must first provide a function declaration that the [Static Driver Verifier](../devtest/static-driver-verifier.md) (SDV) and other verification tools require, as follows:

```cpp
FREE_FUNCTION MyFreeFunction;
```

And then implement your callback function as follows:

```cpp
VOID
 MyFreeFunction (
 __in PVOID Buffer
    )
  {...}
```

## Requirements

**Target platform**: Desktop

**Version**: Available starting withWindows Vista.

**Header**: Wdm.h (include Wdm.h or Ntddk.h)

**IRQL**: <= APC_LEVEL


## See also

[**FsRtlTeardownPerFileContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperfilecontexts)

[**FsRtlTeardownPerStreamContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperstreamcontexts)

[**FSRTL_PER_FILE_CONTEXT**](/previous-versions/ff547352(v=vs.85))

[**FSRTL_PER_STREAM_CONTEXT**](/previous-versions/ff547357(v=vs.85))

[Tracking Per-File Context in a Legacy File System Filter Driver](./tracking-per-file-context-in-a-legacy-file-system-filter-driver.md)

[Tracking Per-Stream Context in a Legacy File System Filter Driver](./file-streams--stream-contexts--and-per-stream-contexts.md
)
