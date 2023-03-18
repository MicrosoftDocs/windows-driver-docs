---
title: File System Filter Verification
description: Details on the Filter Verifier
keywords:
- File System Filter Verification feature WDK Driver Verifier
- Minifilter verification WDK Driver Verifier
- Filter Verifier WDK Driver Verifier
ms.date: 03/17/2023
---

# File System Filter Verification

## Usage Validation

Filter Verifier validates the following usage in a minifilter driver:

* Correct use of parameters and calling context
* Correct return values from preoperation and postoperation callback routines
* Consistent and coherent changes to parameters in callback data

## Filter Manager Object Tracking

Filter Verifier tracks the following filter manager objects:

* Filter Contexts (stream contexts, file contexts, etc.)
* Callback Data structures
* Queued Work Items
* NameInformation structures
* File Objects
* Filter Objects
* Instance Objects
* Volume Objects

For reference-counted structures, such as filter contexts and name information structures, Filter Verifier will break into the debugger upon unloading the filter driver if any reference counts appear to have been leaked. It will print instructions on how you can use the [!fltkd debugger extension](/windows-hardware/drivers/ifs/development-and-testing-tools#fltkd-debugger-extension) to find the leaked structures.

## Filter Verifier Violations

When Filter Verifier detects a violation, it prints a message in the debugger describing the violation. For most violations it also halts execution and prompts the user to take some action. For example:

```
FILTER VERIFIER ERROR: A filter returned an unknown pre-operation callback status.
(Filter = FFFFAC04A21CD8A0 (MyFilter), Status = 0xbaadf00d)
Break, ignore, zap or remove ?
```

To proceed, type one of four one-letter commands:
* `B` or `b` for **Break**: This breaks into the debugger where you may perform further investigation.
* `I` or `i` for **Ignore**: Resumes execution. If this violation is encountered again, Filter Verifier will print the violation message to the debugger, halt execution, and display the prompt.
* `Z` or `z` for **Zap**: Resumes execution. If this violation is encountered again, Filter Verifier will print the violation message to the debugger, but will NOT halt execution.
* `R` or `r` for **Remove**: Resumes execution. If this violation is encountered again, Filter Verifier will NOT print the violation message and will NOT halt execution.

> [!NOTE]
> When using Filter Verifier on a driver that has been built with compiler optimizations enabled, you may occasionally encounter a Filter Verifier error consistently claiming that your filter leaked references to one or more resources even when you cannot find a cause for a leak in your code. The message will begin with text similar to the following:
>
> ```
>FILTER VERIFIER ERROR: A filter (Filter = FFFFAC04A21CD8A0 (MyFilter)) leaked references to the following resources:
> ```
>
> You may also see a message indicating that object tracking is out of sync, such as:
>
> ```
> FILTER VERIFIER WARNING: Filter manager verifier object tracking may be out of sync for the system
> ```
>
> The most common cause of this condition is that Filter Verifier was unable to identify the true caller of a Filter Manager API due to a tail call optimization. This may occur when a routine in your driver calls a Filter Manager API as its last line. For example:
>
> ```c
> void MyWorkItemCallback(PFLT_GENERIC_WORKITEM WorkItem,
>                         PVOID Filter,
>                         PVOID Context)
>{
>    // Do some stuff
>    ...
>    FltFreeGenericWorkItem(WorkItem);
>}
> ```
>
> There are a couple of ways to verify that this has happened:
> 1. Disable optimization of the suspect routine by wrapping it in `#pragma optimize("", off) ... #pragma optimize("", on)`.
> 2. Reorder your code such that the Filter Manager API call is not the last thing happening in your routine.
>
> If the error no longer reproduces after trying one of those options, it is likely a false positive.

## Activating This Option

You can activate the File System Filter Verification feature for one or more drivers by using the `verifier.exe` command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

The recommended way to start Filter Verifier is with the **/standard** option of `verifier.exe`, since it provides additional useful features such as [special pool](special-pool.md) and [pool tracking](pool-tracking.md):

```
verifier.exe /standard /driver MyFilter.sys
```

Verification starts when the minifilter driver registers with the filter manager.

- **Enabling Only Filter Verifier in Windows 11 and Later Versions of Windows**
    To enable the minimal set of Filter Verifier checks, enable the [I/O Verification](../devtest/i-o-verification.md) and [File System Filter Verification](../devtest/file-system-filter-verification.md) options in Driver Verifier (*verifier.exe*). For example:

    ```
    verifier.exe /ruleclasses 5 37 /driver MyFilter.sys
    ```

- **Enabling Only Filter Verifier in Windows 10 and Prior Versions of Windows**
    To enable the minimal set of Filter Verifier checks, specify the minifilter driver's name and enable the [I/O Verification](../devtest/i-o-verification.md) option in Driver Verifier (*verifier.exe*). For example:

    ```
    verifier.exe /flags 0x10 /driver MyFilter.sys
    ```
