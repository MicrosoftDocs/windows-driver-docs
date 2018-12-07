---
title: Use the Device Guard Readiness Tool to evaluate HVCI driver compatibility
description: Follow these steps to use Device Guard Readiness Tool to evaluate HVCI driver compatibility of your driver code.
ms.assetid: 
ms.date: 02/22/2017
ms.localizationpriority: medium
---

# Use the Device Guard Readiness Tool to evaluate HVCI driver compatibility

## Overview

The Device Guard Readiness tool is designed to check a number of requirements for creating a PC that supports a variety of security enhancement features. This section describes how to use the tool to evaluate the ability of a driver to run in a Hypervisor-protected Code Integrity (HVCI) environment. 

OS and Hardware requirements for testing HVCI driver Device Guard compatibility:

1. Windows: Available on all versions of Windows, such as Windows Pro, Windows 10 Enterprise, Windows Server, and Windows 10 IoT Enterprise (Not supported in S Mode).

2. Hardware: Recent hardware that supports virtualization extension with SLAT.

To use the readiness tool to evaluate the additional requirements, such as secure boot, refer to the readme.txt file included in the readiness tool download.

For more information about the related device fundamentals test, see [Device.DevFund.DeviceGuard](https://msdn.microsoft.com/windows/hardware/commercialize/design/compatibility/device-devfund#devicedevfunddeviceguard).

## Implement Device Guard compatible code

To implement Device Guard compatible code, make sure your driver code does the following:

- Opts in to NX by default
- Uses NX APIs/flags for memory allocation (NonPagedPoolNx)
- Does not use sections that are both writable and executable
- Does not attempt to directly modify executable system memory
- Does not use dynamic code in kernel
- Does not load data files as executable
- Section alignment is a multiple of 0x1000 (PAGE\_SIZE). E.g. DRIVER\_ALIGNMENT=0x1000

The following list of DDIs that are not reserved for system use may be impacted:

|                                                                                                      |
|------------------------------------------------------------------------------------------------------|
| DDI name                                                                                             |
| [**ExAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff544501)                                                          |
| [**ExAllocatePoolWithQuota**](https://msdn.microsoft.com/library/windows/hardware/ff544506)                                        |
| [**ExAllocatePoolWithQuotaTag**](https://msdn.microsoft.com/library/windows/hardware/ff544513)                                  |
| [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520)                                            |
| [**ExAllocatePoolWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff544523)                            |
| [**ExInitializeNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545301)                        |
| [**ExInitializeLookasideListEx**](https://msdn.microsoft.com/library/windows/hardware/ff545298)                                |
| [**MmAllocateContiguousMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554460)                                  |
| [**MmAllocateContiguousMemorySpecifyCache**](https://msdn.microsoft.com/library/windows/hardware/ff554464)          |
| [**MmAllocateContiguousMemorySpecifyCacheNode**](https://msdn.microsoft.com/library/windows/hardware/ff554469)  |
| [**MmAllocateContiguousNodeMemory**](https://msdn.microsoft.com/library/windows/hardware/jj602795)                          |
| [**MmCopyMemory**](https://msdn.microsoft.com/library/windows/hardware/dn342884)                                                              |
| [**MmMapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff554618)                                                              |
| [**MmMapLockedPages**](https://msdn.microsoft.com/library/windows/hardware/ff554622)                                                      |
| [**MmMapLockedPagesSpecifyCache**](https://msdn.microsoft.com/library/windows/hardware/ff554629)                              |
| [**MmProtectMdlSystemAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554670)                                    |
| [**ZwAllocateVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566416)                                        |
| [**ZwCreateSection**](https://msdn.microsoft.com/library/windows/hardware/ff566428)                                                        |
| [**ZwMapViewOfSection**](https://msdn.microsoft.com/library/windows/hardware/ff566481)                                                  |
| [**NtCreateSection**](https://msdn.microsoft.com/library/windows/hardware/ff556473)                                                        |
| [**NtMapViewOfSection**](https://msdn.microsoft.com/library/windows/hardware/ff556551)                                                  |
| [**ClfsCreateMarshallingArea**](https://msdn.microsoft.com/library/windows/hardware/ff541520)                                    |
| NDIS                                                                                                 |
| [**NdisAllocateMemoryWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff561606)                  |
| Storage                                                                                              |
| [**StorPortGetDataInBufferSystemAddress**](https://msdn.microsoft.com/library/windows/hardware/jj553720)             |
| [**StorPortGetSystemAddress**](https://msdn.microsoft.com/library/windows/hardware/ff567100)                                     |
| [**ChangerClassAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff551402)                                     |
| Display                                                                                              |
| [*DxgkCbMapMemory*](https://msdn.microsoft.com/library/windows/hardware/ff559533)                                                         |
| [**VideoPortAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff570180)                                           |
| Audio Miniport                                                                                       |
| [**IMiniportDMus::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536701)                                        |
| [**IMiniportMidi::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536710)                                        |
| [**IMiniportWaveCyclic::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536723)                            |
| [**IPortWavePci::NewMasterDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff536916)                      |
| [**IMiniportWavePci::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536735)                                  |
| Audio Port Class                                                                                     |
| [**PcNewDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff537712)                                                         |
| [**PcNewResourceList**](https://msdn.microsoft.com/library/windows/hardware/ff537717)                                                     |
| [**PcNewResourceSublist**](https://msdn.microsoft.com/library/windows/hardware/ff537718)                                               |
| IFS                                                                                                  |
| [**FltAllocatePoolAlignedWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff541762)                              |
| [**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710)                                                    |
| WDF                                                                                                  |
| [**WdfLookasideListCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548694)                                             |
| [**WdfMemoryCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548706)                                                           |
| [**WdfDeviceAllocAndQueryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff545882)                             |
| [**WdfDeviceAllocAndQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265599)                         |
| [**WdfFdoInitAllocAndQueryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff547239)                           |
| [**WdfFdoInitAllocAndQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265612)                       |
| [**WdfIoTargetAllocAndQueryTargetProperty**](https://msdn.microsoft.com/library/windows/hardware/ff548585)             |
| [**WdfRegistryQueryMemory**](https://msdn.microsoft.com/library/windows/hardware/ff549920)                                             |


## Using the DGR tool

To use Device Guard Readiness Tool, complete the following steps:

-   **Prepare the test PC**

    *Enable Virtualization Based Protection of Code Integrity* - Run the System Information app (msinfo32). Look for the following item: “Device Guard Virtualization based security”. It should show: “Running”.

    Alternatively, there is also a WMI interface for checking using management tools that can be used to display information in PowerShell.

    ```console
    Get-CimInstance –ClassName Win32_DeviceGuard –Namespace root\Microsoft\Windows\DeviceGuard
    ```

    For information on how to interrupt the output displayed, see [Enable virtualization-based protection of code integrity](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-exploit-guard/enable-virtualization-based-protection-of-code-integrity).

    *Disable Device Guard* - Note that while running the Readiness Tool, Device Guard must be disabled on the PC under test, as Device Guard might prevent the driver from loading, and the driver won’t be available for the Readiness Tool to test.

    *Optionaly Enable Test Signing* - To allow for the installation of unsigned development drivers, you may want to enable test signing using BCDEdit.

    ```console
    bcdedit /set TESTSIGNING ON 
    ```

-   **Install test drivers**

    Install the desired test driver(s) on the target test PC.

    **Important**  After you have tested the development driver and worked through any code issues, retest the final production driver. In addition, use the HLK to test the driver. For more information, see [HyperVisor Code Integrity Readiness Test](https://msdn.microsoft.com/library/windows/hardware/dn955152).



-   **Install the Device Guard Readiness Tool**

    **Warning**  
    As the Device Guard Readiness Tool changes registry values and may impact features such as secure boot, use a test PC that doesn't contain any data or applications. After the tests have been run, you may want to re-install Windows to re-establish your desired security configuration.

    1. Download the tool from here: [Device Guard and Credential Guard hardware readiness tool](https://www.microsoft.com/download/details.aspx?id=53337).

    2. Unzip the tool on the target test machine.

-   **Configure PowerShell to allow for the execution of unsigned scripts.**

    The Readiness Tool is a PowerShell script. To work with the Readiness Tool script, open an Administrator PowerShell script.

    If Execution-Policy is not already set to allow running script, then you should manually set it as shown here.

    ```powershell
    Set-ExecutionPolicy Unrestricted
    ```

-   **Run the readiness tool to enable HVCI**

    1. In Powershell, locate the directory into which you unzipped the Readiness Tool.

    2. Run the Readiness Tool to enable HVCI.

    ```powershell
    DG_Readiness_Tool.ps1 -Enable HVCI
    ```

    3. When directed, reboot the PC.

-   **Run the script to evaluate HVCI capability**

    1. Run the Readiness Tool to evaluate the ability of the drivers to support HVCI.

    ```powershell
    DG_Readiness_Tool.ps1 -Capable HVCI
    ```

-   **Evaluate the output**

    The output to the screen is color coded.

    |                   |                                                                                                   |
    |-------------------|---------------------------------------------------------------------------------------------------|
    | Red - Errors      | Elements are missing or not configured that will prevent enabling and using DG/CG.                |
    | Yellow - Warnings | This device can be used to enable and use DG/CG, but additional security benefits will be absent. |
    | Green - Messages  | This device is fully compliant with DG/CG requirements.                                           |

    In addition to the output to the screen, by default, the log file with detailed output is located at C:\\DGLogs

    There are five steps (or sections) in the output of the Device Guard Readiness Tool. Step 1 contains the is the driver compatibility information.

    ```text
     ====================== Step 1 Driver Compat ====================== 
    ```

    Drivers displayed in green have no identified HVCI compatibility issues. If you are interested in evaluating a specific driver, if the driver name is displayed in green and is active and loaded, it has passed the HVCI compatibility test.

    Locate the "InCompatible HVCI Kernel Driver Modules" section shown below, towards the end of the log.

    ```text
    InCompatible HVCI Kernel Driver Modules found

    Module: TestDriver1.sys
        Reason: section alignment failures:             9
    Module: TestDriver2.sys
        Reason: execute pool type count:                3
    ```

    In the sample shown above, two drivers are identified as incompatible. TestDriver1.sys has a memory section alignment failure and TestDriver2.sys has a pool that is configured to use executable memory area.

    The statistics for the seven types of device driver incompatibilities are also available using the !verifier debugger extension. For more information on the !verifier extension, see [**!verifier**](https://msdn.microsoft.com/library/windows/hardware/ff565591).

    ```text
            Execute Pool Type Count:                3
            Execute Page Protection Count:          0
            Execute Page Mapping Count:             0
            Execute-Write Section Count:            0
            Section Alignment Failures:             0
            Unsupported Relocs Count:               0
            IAT in Executable Section Count:        0
    ```



Use the following table to interpret the output and determine what driver code changes are needed to fix the different types of HVCI incompatibilities.



<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>

<tr class="odd">
<td align="left"><strong>Warning</strong></td>
<td align="left"><strong>Redemption</strong></td>
</tr>

<tr class="even">
<td align="left"><p>Execute Pool Type</p></td>
<td align="left"><p>The caller specified an executable pool type. Calling a memory allocating function that requests executable memory.</p>
<p>Be sure that all pool types contain a non executable NX flag.</p>
</td>
</tr>

<tr class="odd">
<td align="left"><p>Execute Page Protection</p></td>
<td align="left"><p>The caller specified an executable page protection.</p>
<p>Specify a &quot;no execute&quot; page protection mask.</p>
</td>
</tr>

<tr class="even">
<td align="left"><p>Execute Page Mapping</p></td>
<td align="left"><p>The caller specified an executable memory descriptor list (MDL) mapping.</p>
<p> Make sure that the mask that is used contains MdlMappingNoExecute. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554559.aspx" data-raw-source="[MmGetSystemAddressForMdlSafe](https://msdn.microsoft.com/library/windows/hardware/ff554559.aspx)">MmGetSystemAddressForMdlSafe</a></p>
</td>
</tr>

<tr class="odd">
<td align="left"><p>Execute-Write Section</p></td>
<td align="left"><p>The image contains an executable and writable section.</p>
</td>
</tr>

<tr class="even">
<td align="left"><p>Section Alignment Failures</p>
</td>
<td align="left"><p>The image contains a section that is not page aligned.</p>
<p>Section Alignment must be a multiple of 0x1000 (PAGE_SIZE). E.g. DRIVER_ALIGNMENT=0x1000</p></td>
</tr>


<tr class="even">
<td align="left"><p>IAT in Executable Section</p></td>
<td align="left"><p>The import address table (IAT), should not be an executable section of memory.</p>
<p>This issue occurs when the IAT, is located in a Read and Execute (RX) only section of memory. This means that the OS will not be able to write to the IAT to set the correct addresses for where the referenced DLL. </p>
<p> One way that this can occur is when using the <a href="https://docs.microsoft.com/cpp/build/reference/merge-combine-sections" data-raw-source="[/MERGE (Combine Sections)](https://docs.microsoft.com/cpp/build/reference/merge-combine-sections)">/MERGE (Combine Sections)</a> option in code linking. For example if .rdata (Read-only initialized data) is merged with .text data (Executable code), it is possible that the IAT may end up in an executable section of memory.  </p>
</td>
</tr>

</tbody>
</table>


---------

Unsupported Relocs

<p>In Windows 10, version 1507 through Windows 10, version 1607, because of the use of Address Space Layout Randomization (ASLR) an issue can arise with address alignment and memory relocation.  The operating system needs to relocate the address from where the linker set its default base address to the actual location that ASLR assigned. This relocation cannot straddle a page boundary.  For example, consider a 64-bit address value that starts at offset 0x3FFC in a page. It’s address value overlaps over to the next page at offset 0x0003. This type of overlapping relocs is not supported prior to Windows 10, version 1703.</p>

<p>This situation can occur when a global struct type variable initializer has a misaligned pointer to another global, laid out in such a way that the linker cannot move the variable to avoid the straddling relocation. The linker will attempt to move the variable, but there are situations where it may not be able to do so (for example with large misaligned structs or large arrays of misaligned structs). Where appropriate, modules should be assembled using the <a href="https://docs.microsoft.com/cpp/build/reference/gy-enable-function-level-linking" data-raw-source="[/Gy (COMDAT)](https://docs.microsoft.com/cpp/build/reference/gy-enable-function-level-linking)">/Gy (COMDAT)</a> option to allow the linker to align module code as much as possible.</p>



```cpp
#include <pshpack1.h>

typedef struct _BAD_STRUCT {
      USHORT Value;
      CONST CHAR *String;
} BAD_STRUCT, * PBAD_STRUCT;

#include <poppack.h>

#define BAD_INITIALIZER0 { 0, "BAD_STRING" },
#define BAD_INITIALIZER1 \
      BAD_INITIALIZER0      \
      BAD_INITIALIZER0      \
      BAD_INITIALIZER0      \
      BAD_INITIALIZER0      \
      BAD_INITIALIZER0      \
      BAD_INITIALIZER0      \
      BAD_INITIALIZER0      \
      BAD_INITIALIZER0      

#define BAD_INITIALIZER2 \
      BAD_INITIALIZER1      \
      BAD_INITIALIZER1      \
      BAD_INITIALIZER1      \
      BAD_INITIALIZER1      \
      BAD_INITIALIZER1      \
      BAD_INITIALIZER1      \
      BAD_INITIALIZER1      \
      BAD_INITIALIZER1      

#define BAD_INITIALIZER3 \
      BAD_INITIALIZER2      \
      BAD_INITIALIZER2      \
      BAD_INITIALIZER2      \
      BAD_INITIALIZER2      \
      BAD_INITIALIZER2      \
      BAD_INITIALIZER2      \
      BAD_INITIALIZER2      \
      BAD_INITIALIZER2      

#define BAD_INITIALIZER4 \
      BAD_INITIALIZER3      \
      BAD_INITIALIZER3      \
      BAD_INITIALIZER3      \
      BAD_INITIALIZER3      \
      BAD_INITIALIZER3      \
      BAD_INITIALIZER3      \
      BAD_INITIALIZER3      \
      BAD_INITIALIZER3      

BAD_STRUCT MayHaveStraddleRelocations[4096] = { // as a global variable
      BAD_INITIALIZER4
};
```

There are other situations involving the use of assembler code, where this issue can also occur.

---------


## Script customization

Below is the list of Regkeys and their values for customization of the script to Device Guard and Credential Guard without UEFI Lock.

To enable HVCI and CG without UEFI Lock:

```reg
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard" /v "EnableVirtualizationBasedSecurity" /t REG_DWORD /d 1 /f&#39; 
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard" /v "RequirePlatformSecurityFeatures" /t REG_DWORD /d 1 /f&#39; 
```

## Driver Verifier code integrity

Use the Driver Verifier code integrity option flag (0x02000000) to enable extra checks that validate compliance with this feature. To enable this from the command line, use the following command.

```console
verifier.exe /flags 0x02000000 /driver <driver.sys>
```
To choose this option if using the verifier GUI, select *Create custom settings* (for code developers), select *Next*, and then select _Code integrity checks_.

You can use the verifier command line /query option to display the current driver verifier information.

```console
verifier /query 
```







