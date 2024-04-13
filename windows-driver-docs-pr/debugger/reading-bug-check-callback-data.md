---
title: Reading Bug Check Callback Data
description: Reading Bug Check Callback Data
keywords: ["callback data for bug checks", "callback data for bug checks, displaying callback data", "callback data for bug checks, displaying secondary data", "secondary bug check callback data", "bug check, callback routines", "dbgeng.h header file, IDebugDataSpaces3", "dbgeng.h header file, ReadTagged", "dbgeng.h header file, StartEnumTagged", "dbgeng.h header file, GetNextTagged"]
ms.date: 06/05/2020
---

# Reading Bug Check Callback Data

Many drivers supply *bug check callback routines*. When Windows issues a bug check, it calls these routines before shutting down the system. These routines can specify and write to areas of memory known as *callback data* and *secondary callback data*.

**BugCheckCallback** use [KBUGCHECK_CALLBACK_ROUTINE](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_callback_routine)  
Data written by this routine becomes part of *callback data*. The data is not included in the crash dump file.

**BugCheckSecondaryDumpDataCallback** use [KBUGCHECK_REASON_CALLBACK_ROUTINE](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_reason_callback_routine)  
Data written by this routine becomes part of *secondary callback data*. The data is included in the crash dump file.

**BugCheckAddPagesCallback** use [KBUGCHECK_REASON_CALLBACK_ROUTINE](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_reason_callback_routine)  
Pages specified by this routine become part of *callback data*. The data in those pages is included in the crash dump file.

The amount of callback and secondary callback data that is available to the debugger depends on several factors:

- If you are performing live debugging of a crashed system, callback data that has already been written by [BugCheckCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_callback_routine) or specified by [BugCheckAddPagesCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_reason_callback_routine) will be available. Secondary callback data will not be available, because it is not stored in any fixed memory location.

- If you are debugging a Complete Memory Dump or Kernel Memory Dump, callback data specified by [BugCheckAddPagesCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_reason_callback_routine) and secondary callback data written by [BugCheckSecondaryDumpDataCallback](/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kbugcheck_reason_callback_routine) will be available. Callback data written by [BugCheckCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_callback_routine) will not be available.

- If you are debugging a Small Memory Dump, callback data will not be available. Secondary callback data will be available.

See [Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md) for more details on these different dump file sizes.

## Displaying Callback Data

To display bug check callback data, you can use the [**!bugdump**](../debuggercmds/-bugdump.md) extension.

Without any parameters, [**!bugdump**](../debuggercmds/-bugdump.md) will display data for all callbacks.

To view data for one specific callback routine, use [**!bugdump**](../debuggercmds/-bugdump.md)*Component*, where *Component* is the same parameter that was passed to **KeRegisterBugCheckCallback** when that routine was registered.

### Displaying Secondary Callback Data

There are two methods for displaying secondary callback data. You can use the **.enumtag** command or you can write your own debugger extension.

Each block of secondary callback data is identified by a GUID tag. This tag is specified by the **Guid** field of the **(KBUGCHECK\_SECONDARY\_DUMP\_DATA)ReasonSpecificData** parameter passed to [BugCheckSecondaryDumpDataCallback](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_reason_callback_routine).

The [**.enumtag (Enumerate Secondary Callback Data)**](../debuggercmds/-enumtag--enumerate-secondary-callback-data-.md) command is not a very precise instrument. It displays every secondary data block, showing the tag and then showing the data in hexadecimal and ASCII format. It is generally useful only to determine what tags are actually being used for secondary data blocks.

To use this data in a more practical way, it is recommended that you write your own debugger extension. This extension must call methods in the dbgeng.h header file. For details, see [Writing New Debugger Extensions](../debuggercmds/writing-new-debugger-extensions.md).

If you know the GUID tag of the secondary data block, your extension should use the method **IDebugDataSpaces3::ReadTagged** to access the data. Its prototype is as follows:

```cpp
STDMETHOD(ReadTagged)(
    THIS_
    IN LPGUID Tag,
    IN ULONG Offset,
    OUT OPTIONAL PVOID Buffer,
    IN ULONG BufferSize,
    OUT OPTIONAL PULONG TotalSize
    ) PURE; 
```

Here is an example of how to use this method:

```cpp
UCHAR RawData[MY_DATA_SIZE];
GUID MyGuid = .... ;

Success = DataSpaces->ReadTagged(  &MyGuid,  0,  RawData,
                                   sizeof(RawData),  NULL); 
```

If you supply a *BufferSize* that is too small, **ReadTagged** will succeed but will write only the requested number of bytes to *Buffer*. If you specify a *BufferSize* that is too large, **ReadTagged** will succeed but will write only the actual block size to *Buffer*. If you supply a pointer for *TotalSize*, **ReadTagged** will use it to return the size of the actual block. If the block cannot be accessed, **ReadTagged** will return a failure status code.

If two blocks have identical GUID tags, the first matching block will be returned, and the second block will be inaccessible.

If you are not sure of the GUID tag of your block, you can use the **IDebugDataSpaces3::StartEnumTagged**, **IDebugDataSpaces3::GetNextTagged**, and **IDebugDataSpaces3::EndEnumTagged** methods to enumerate the tagged blocks. Their prototypes are as follows:

```cpp
STDMETHOD(StartEnumTagged)(
    THIS_
    OUT PULONG64 Handle
    ) PURE;

STDMETHOD(GetNextTagged)(
    THIS_
    IN ULONG64 Handle,
    OUT LPGUID Tag,
    OUT PULONG Size
    ) PURE;

STDMETHOD(EndEnumTagged)(
    THIS_
    IN ULONG64 Handle
    ) PURE;
```

### Debugging Callback Routines

It is also possible to debug the callback routine itself. Breakpoints within callback routines work just like any other breakpoint.

If the callback routine causes a second bug check, this new bug check will be processed first. However, Windows will not repeat certain parts of the Stop process—for example, it will not write a second crash dump file. The Stop code displayed on the blue screen will be the second bug check code. If a kernel debugger is attached, messages about both bug checks will usually appear.
