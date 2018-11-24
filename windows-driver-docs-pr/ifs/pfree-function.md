---
title: PFREE\_FUNCTION function pointer
description: A PFREE\_FUNCTION typed routine can be registered by a file system legacy filter driver as the filter's FreeCallback callback routine.
ms.assetid: 291b57d9-3bef-4acb-a571-86b67a03cd08
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

# PFREE\_FUNCTION function pointer


A **PFREE\_FUNCTION** typed routine can be registered by a file system legacy filter driver as the filter's *FreeCallback* callback routine. The file system calls *FreeCallback* when the file system removes a file context object by using [**FsRtlTeardownPerFileContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547290) or removes a stream context object by using [**FsRtlTeardownPerStreamContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547295).

You must declare the callback routine by using the **FREE\_FUNCTION** type. For more information, see the example in the Remarks section.

Syntax
------

```ManagedCPlusPlus
typedef VOID ( *FreeCallback)(
  _In_ PVOID Buffer
);
```

Parameters
----------

*Buffer* \[in\]  
A pointer to the [**FSRTL\_PER\_FILE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff547352) or the [**FSRTL\_PER\_STREAM\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff547357) structure to be freed.

Return value
------------

None

Remarks
-------

When a file system tears down the per file context object for a file, it must call [**FsRtlTeardownPerFileContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547290). This routine calls the *FreeCallback* routines of all per-file context structures associated with the file. This callback routine must free any memory used for the [**FSRTL\_PER\_FILE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff547352) object and any associated context information. This is also the case for per stream contexts when [**FsRtlTeardownPerStreamContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547295) is called and *FreeCallback* will free memory used for [**FSRTL\_PER\_STREAM\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff547357) objects.

For remarks about synchronizing access to per file context objects or to per stream context objects during a call to *FreeCallback*, see [**FsRtlTeardownPerFileContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547290) and [**FsRtlTeardownPerStreamContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547295).

&gt; \[!Note\]
&gt;   The *FreeCallback* routine cannot recursively call down into the file system or acquire any file system resources.

 

To define a *FreeCallback* callback function that is named *MyFreeFunction*, you must first provide a function declaration that the [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) (SDV) and other verification tools require, as follows:

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

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available starting withWindows Vista.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Wdm.h (include Wdm.h or Ntddk.h)</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;= APC_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**FsRtlTeardownPerFileContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547290)

[**FsRtlTeardownPerStreamContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547295)

[**FSRTL\_PER\_FILE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff547352)

[**FSRTL\_PER\_STREAM\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff547357)

[Tracking Per-File Context in a Legacy File System Filter Driver](https://msdn.microsoft.com/library/windows/hardware/ff556856)

[Tracking Per-Stream Context in a Legacy File System Filter Driver](https://msdn.microsoft.com/library/windows/hardware/ff556859)

 

 






