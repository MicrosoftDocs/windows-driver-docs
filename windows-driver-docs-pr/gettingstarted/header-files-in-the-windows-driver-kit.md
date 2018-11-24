---
title: Header files in the Windows Driver Kit
description: Header files in the Windows Driver Kit
ms.assetid: 7d02148d-502d-4b49-9c56-9fff498dd2af
keywords:
- driver design decisions WDK , header file changes
- designing drivers WDK , header file changes
- header files WDK
- header files WDK , changes
- .h files
- user-mode header files WDK
- kernel-mode header files WDK
- files WDK header files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Header files in the Windows Driver Kit


The [Windows Driver Kit (WDK)](https://msdn.microsoft.com/library/windows/hardware/ff557573) contains all the header files (.h files) that you need to build kernel-mode and user-mode drivers. Header files are in the Include folder in your WDK installation folder. Example: C:\\Program Files (x86)\\Windows Kits\\10\\Include.

The header files contain version information so that you can use the same set of header files regardless of which version of Windows your driver will run on.

## <span id="Constants_that_represent_Windows_versions"></span><span id="constants_that_represent_windows_versions"></span><span id="CONSTANTS_THAT_REPRESENT_WINDOWS_VERSIONS"></span>Constants that represent Windows versions


Header files in the WDK contain conditional statements that specify programming elements that are available only in certain versions of the Windows operating system. The versioned elements include functions, enumerations, structures, and structure members.

To specify the programming elements that are available in each operating system version, the header files contain preprocessor conditionals that compare the value of NTDDI\_VERSION with a set of predefined constant values that are defined in Sdkddkver.h.

Here are the predefined constant values that represent versions of the Microsoft Windows operating system.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Constant</th>
<th align="left">Operating system version</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>NTDDI_WIN10</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>NTDDI_WINBLUE</p></td>
<td align="left"><p>Windows 8.1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NTDDI_WIN8</p></td>
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>NTDDI_WIN7</p></td>
<td align="left"><p>Windows 7</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NTDDI_WS08SP4</p></td>
<td align="left"><p>Windows Server 2008 with SP4</p></td>
</tr>
<tr class="even">
<td align="left"><p>NTDDI_WS08SP3</p></td>
<td align="left"><p>Windows Server 2008 with SP3</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NTDDI_WS08SP2</p></td>
<td align="left"><p>Windows Server 2008 with SP2</p></td>
</tr>
<tr class="even">
<td align="left"><p>NTDDI_WS08</p></td>
<td align="left"><p>Windows Server 2008</p></td>
</tr>
</tbody>
</table>

 

You can see many examples of version-specific DDI elements in the WDK header files. This conditional declaration appears in Wdm.h, which is a header file that might be included by a kernel-mode driver.

```cpp
#if (NTDDI_VERSION >= NTDDI_WIN7)
_Must_inspect_result_
NTKERNELAPI
NTSTATUS
KeSetTargetProcessorDpcEx (
    _Inout_ PKDPC Dpc,
    _In_ PPROCESSOR_NUMBER ProcNumber
    );
#endif
```

In the example you can see that the [**KeSetTargetProcessorDpcEx**](https://msdn.microsoft.com/library/windows/hardware/ff553279) function is available only in Windows 7 and later versions of Windows.

This conditional declaration appears in Winspool.h, which is a header file that might be included by a user-mode driver.

```ManagedCPlusPlus
#if (NTDDI_VERSION >= NTDDI_WIN7)
...
BOOL
WINAPI
GetPrintExecutionData(
    _Out_ PRINT_EXECUTION_DATA *pData
    );

#endif // (NTDDI_VERSION >= NTDDI_WIN7)
```

In the example can see that the [**GetPrintExecutionData**](https://msdn.microsoft.com/library/windows/desktop/ee264322) function is available only in Windows 7 and later versions of Windows.

## <span id="Header_files_for_the_Kernel_Mode_Driver_Framework"></span><span id="header_files_for_the_kernel_mode_driver_framework"></span><span id="HEADER_FILES_FOR_THE_KERNEL_MODE_DRIVER_FRAMEWORK"></span>Header files for the Kernel Mode Driver Framework


The WDK supports several versions of Windows, and it also supports several versions of the Kernel Mode Driver Framework (KMDF) and User Mode Driver Framework (UMDF). The versioning information in the WDK header files pertains to Windows versions, but not to KMDF or UMDF versions. Header files for different versions of KMDF and UMDF are placed in separate directories.

 

 





