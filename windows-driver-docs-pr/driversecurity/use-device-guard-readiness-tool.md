---
title: Evaluate HVCI driver compatibility
description: Follow these steps to use to evaluate HVCI driver compatibility of your driver code.
ms.date: 05/26/2020
ms.localizationpriority: medium
---

# Evaluate HVCI driver compatibility

## Overview

The DGReadiness tool is designed to check a number of requirements for creating a PC that supports a variety of security enhancement features. This section describes how to use the tool to evaluate the ability of a driver to run in a Hypervisor-protected Code Integrity (HVCI) environment.

OS and Hardware requirements for testing HVCI driver compatibility:

1. Windows: Available on all versions of Windows, such as Windows Pro, Windows 10 Enterprise, Windows Server, and Windows 10 IoT Enterprise (Not supported in S Mode).

2. Hardware: Recent hardware that supports virtualization extension with SLAT.

To use the readiness tool to evaluate the additional requirements, such as secure boot, refer to the readme.txt file included in the readiness tool download.

For more information about the related device fundamentals test, see [Device.DevFund tests](/windows-hardware/test/hlk/testref/device-devfund-tests).

## Implement HVCI compatible code

To implement HVCI compatible code, make sure your driver code does the following:

- Opts in to NX by default
- Uses NX APIs/flags for memory allocation (NonPagedPoolNx)
- Does not use sections that are both writable and executable
- Does not attempt to directly modify executable system memory
- Does not use dynamic code in kernel
- Does not load data files as executable
- Section alignment is a multiple of 0x1000 (PAGE\_SIZE). E.g. DRIVER\_ALIGNMENT=0x1000

The following list of DDIs that are not reserved for system use may be impacted:

|       DDI name                                                                                                  |
|------------------------------------------------------------------------------------------------------|
| [**ExAllocatePool**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool)                                                          |
| [**ExAllocatePoolWithQuota**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithquota)                                        |
| [**ExAllocatePoolWithQuotaTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithquotatag)                                  |
| [**ExAllocatePoolWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag)                                            |
| [**ExAllocatePoolWithTagPriority**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtagpriority)                            |
| [**ExInitializeNPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializenpagedlookasidelist)                        |
| [**ExInitializeLookasideListEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializelookasidelistex)                                |
| [**MmAllocateContiguousMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousmemory)                                  |
| [**MmAllocateContiguousMemorySpecifyCache**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousmemoryspecifycache)          |
| [**MmAllocateContiguousMemorySpecifyCacheNode**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousmemoryspecifycachenode)  |
| [**MmAllocateContiguousNodeMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousnodememory)                          |
| [**MmCopyMemory**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmcopymemory)                                                              |
| [**MmMapIoSpace**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmapiospace)                                                              |
| [**MmMapLockedPages**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmaplockedpages)                                                      |
| [**MmMapLockedPagesSpecifyCache**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmaplockedpagesspecifycache)                              |
| [**MmProtectMdlSystemAddress**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmprotectmdlsystemaddress)                                    |
| [**ZwAllocateVirtualMemory**](/previous-versions/ff566416(v=vs.85))                                        |
| [**ZwCreateSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatesection)                                                        |
| [**ZwMapViewOfSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmapviewofsection)                                                  |
| [**NtCreateSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatesection)                                                        |
| [**NtMapViewOfSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmapviewofsection)                                                  |
| [**ClfsCreateMarshallingArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatemarshallingarea)                                    |
| NDIS                                                                                                 |
| [**NdisAllocateMemoryWithTagPriority**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatememorywithtagpriority)                  |
| Storage                                                                                              |
| [**StorPortGetDataInBufferSystemAddress**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetdatainbuffersystemaddress)             |
| [**StorPortGetSystemAddress**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetsystemaddress)                                     |
| [**ChangerClassAllocatePool**](/windows-hardware/drivers/ddi/mcd/nf-mcd-changerclassallocatepool)                                     |
| Display                                                                                              |
| [*DxgkCbMapMemory*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_map_memory)                                                         |
| [**VideoPortAllocatePool**](/windows-hardware/drivers/ddi/video/nf-video-videoportallocatepool)                                           |
| Audio Miniport                                                                                       |
| [**IMiniportDMus::NewStream**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iminiportdmus-newstream)                                        |
| [**IMiniportMidi::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidi-newstream)                                        |
| [**IMiniportWaveCyclic::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavecyclic-newstream)                            |
| [**IPortWavePci::NewMasterDmaChannel**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportwavepci-newmasterdmachannel)                      |
| [**IMiniportWavePci::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepci-newstream)                                  |
| Audio Port Class                                                                                     |
| [**PcNewDmaChannel**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewdmachannel)                                                         |
| [**PcNewResourceList**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewresourcelist)                                                     |
| [**PcNewResourceSublist**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewresourcesublist)                                               |
| IFS                                                                                                  |
| [**FltAllocatePoolAlignedWithTag**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatepoolalignedwithtag)                              |
| [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext)                                                    |
| WDF                                                                                                  |
| [**WdfLookasideListCreate**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdflookasidelistcreate)                                             |
| [**WdfMemoryCreate**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorycreate)                                                           |
| [**WdfDeviceAllocAndQueryProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandqueryproperty)                             |
| [**WdfDeviceAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandquerypropertyex)                         |
| [**WdfFdoInitAllocAndQueryProperty**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandqueryproperty)                           |
| [**WdfFdoInitAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandquerypropertyex)                       |
| [**WdfIoTargetAllocAndQueryTargetProperty**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetallocandquerytargetproperty)             |
| [**WdfRegistryQueryMemory**](/windows-hardware/drivers/ddi/wdfregistry/nf-wdfregistry-wdfregistryquerymemory)                                             |


## Using the DGReadiness tool

To use DGReadiness Tool, complete the following steps:

-   **Prepare the test PC**

    *Enable Virtualization Based Protection of Code Integrity* - Run the System Information app (msinfo32). Look for the following item: “Virtualization based security”. It should show: “Running”.

    Alternatively, there is also a WMI interface for checking using management tools that can be used to display information in PowerShell.

    ```console
    Get-CimInstance –ClassName Win32_DeviceGuard –Namespace root\Microsoft\Windows\DeviceGuard
    ```

    *Disable "Device Guard"* - Note that while running the Readiness Tool, "Device Guard" must be disabled on the PC under test, as it might prevent the driver from loading, and the driver won’t be available for the Readiness Tool to test.

    *Optionally Enable Test Signing* - To allow for the installation of unsigned development drivers, you may want to enable test signing using BCDEdit.

    ```console
    bcdedit /set TESTSIGNING ON
    ```

-   **Install test drivers**

    Install the desired test driver(s) on the target test PC.

    **Important**  After you have tested the development driver and worked through any code issues, retest the final production driver. In addition, use the HLK to test the driver. For more information, see [HyperVisor Code Integrity Readiness Test](/windows-hardware/test/hlk/testref/b972fc52-2468-4462-9799-6a1898808c86).



-   **Install the DGReadiness Tool**

    **Warning**  
    As the DGReadiness Tool changes registry values and may impact features such as secure boot, use a test PC that doesn't contain any data or applications. After the tests have been run, you may want to re-install Windows to re-establish your desired security configuration.

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

    |       Category    |  Description                                                                                      |
    |-------------------|---------------------------------------------------------------------------------------------------|
    | Red - Errors      | Elements are missing or not configured that will prevent enabling and using DG/CG.                |
    | Yellow - Warnings | This device can be used to enable and use DG/CG, but additional security benefits will be absent. |
    | Green - Messages  | This device is fully compliant with DG/CG requirements.                                           |

    In addition to the output to the screen, by default, the log file with detailed output is located at C:\\DGLogs

    There are five steps (or sections) in the output of the tool. Step 1 contains the is the driver compatibility information.

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

    The statistics for the seven types of device driver incompatibilities are also available using the !verifier debugger extension. For more information on the !verifier extension, see [**!verifier**](../debugger/-verifier.md).

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
<p>Specify a "no execute" page protection mask.</p>
</td>
</tr>

<tr class="even">
<td align="left"><p>Execute Page Mapping</p></td>
<td align="left"><p>The caller specified an executable memory descriptor list (MDL) mapping.</p>
<p> Make sure that the mask that is used contains MdlMappingNoExecute. For more information, see <a href="/windows-hardware/drivers/kernel/mm-bad-pointer" data-raw-source="[MmGetSystemAddressForMdlSafe](../kernel/mm-bad-pointer.md)">MmGetSystemAddressForMdlSafe</a></p>
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
<p> One way that this can occur is when using the <a href="/cpp/build/reference/merge-combine-sections" data-raw-source="[/MERGE (Combine Sections)](/cpp/build/reference/merge-combine-sections)">/MERGE (Combine Sections)</a> option in code linking. For example if .rdata (Read-only initialized data) is merged with .text data (Executable code), it is possible that the IAT may end up in an executable section of memory.  </p>
</td>
</tr>

</tbody>
</table>

---------

Unsupported Relocs

<p>In Windows 10, version 1507 through Windows 10, version 1607, because of the use of Address Space Layout Randomization (ASLR) an issue can arise with address alignment and memory relocation.  The operating system needs to relocate the address from where the linker set its default base address to the actual location that ASLR assigned. This relocation cannot straddle a page boundary.  For example, consider a 64-bit address value that starts at offset 0x3FFC in a page. It’s address value overlaps over to the next page at offset 0x0003. This type of overlapping relocs is not supported prior to Windows 10, version 1703.</p>

<p>This situation can occur when a global struct type variable initializer has a misaligned pointer to another global, laid out in such a way that the linker cannot move the variable to avoid the straddling relocation. The linker will attempt to move the variable, but there are situations where it may not be able to do so (for example with large misaligned structs or large arrays of misaligned structs). Where appropriate, modules should be assembled using the <a href="/cpp/build/reference/gy-enable-function-level-linking" data-raw-source="[/Gy (COMDAT)](/cpp/build/reference/gy-enable-function-level-linking)">/Gy (COMDAT)</a> option to allow the linker to align module code as much as possible.</p>

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

Below is the list of Regkeys and their values for customization of the script to HVCI and Credential Guard without UEFI Lock.

To enable HVCI and CG without UEFI Lock:

```reg
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard" /v "EnableVirtualizationBasedSecurity" /t REG_DWORD /d 1 /f' 
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard" /v "RequirePlatformSecurityFeatures" /t REG_DWORD /d 1 /f' 
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
