---
title: GPU paravirtualization
description: Describes GPU para-virtualization and the related DDI changes.
keywords:
- WDDM , GPU , paravirtualization
- WDDM , GPUP , GPU-PV
ms.date: 01/21/2025
---

# GPU paravirtualization

This article describes GPU paravirtualization in WDDM. This feature is available starting in Windows 10, version 1803 (WDDM 2.4).

## About GPU virtualization

GPU virtualization has become a very important feature for both Windows Client and Windows Server. There are many scenarios that require effective usage of GPU resources in a virtual machine.

Server scenarios (where the host OS doesn't run user applications) include:

* Desktop virtualization
* Compute (AI, ML, etc.)

Client scenarios (where the host OS shares the GPU between VMs and user applications) include:

* Developing graphics applications using Visual Studio where testing is run in a VM.
* Developing applications for IoT, phones, etc.
* Running applications in a VM for security purposes.
* Running Linux or Android OS in a VM with GPU acceleration.

## GPU paravirtualization in WDDM

Paravirtualization (PV) provides an interface to virtual machines (VMs) that are similar to their underlying hardware. In PV, the guest OS is explicitly ported before installing a VM because a non-tailored guest OS can't run on top of a virtual machine monitor (VMM).

Advantages:

* Multiple VMs share the hardware resources.
* Few changes need to be made in the driver code.

The following figure depicts various components, involved in WDDM's paravirtualized design.

:::image type="content" source="images/GpuParavirtualization-DDI.Image01.jpg" alt-text="Diagram that shows the components involved in the paravirtualized design.":::

The D3D runtimes in the guest VM aren't changed. The interfaces with the user-mode runtime and with *KMT* kernel thunks remain the same.

The driver components don't require many changes:

* The UMD in the guest VM needs to:

  * Be aware that the communications with the host kernel-mode driver (KMD) happen across the VM boundary.
  * Use the added *Dxgkrnl* services to access registry settings.

* There isn't a KMD in the guest, only UMD. The KMD is replaced by the Virtual Render Device (VRD) KMD. VRD's purpose is to facilitate the loading of *Dxgkrnl*.

* There isn't a video memory manager (*VidMm*) and scheduler (*VidSch*) in the guest.

* *Dxgkrnl* in a VM gets thunks calls and marshalls them to the host partition via VM bus channels. *Dxgkrnl* in the guest also creates local objects for allocations, processes, devices, etc., which reduces traffic with the host.

## Virtual render device (VRD)

When a paravirtualized GPU is not present in a VM, the VM's Device Manager shows “Microsoft Hyper-V Video” adapter. This is a display-only adapter, which is paired by default with the BasicRender adapter for rendering.

When a paravirtualized GPU is added to a VM, its Device Manager will show two adapters:

* Microsoft Hyper-V Video Adapter or Microsoft Remote Display Adapter
* Microsoft Virtual Render Driver (The actual name is the name of the GPU adapter on the host)

By default, the VRD is paired with the Hyper-V Video adapter, so all UI rendering is done using the VRD adapter.

If there are rendering issues, you can disable this pairing. See the registry settings for GpuVirtualizationFlags. The VRD in this case will be the render-only adapter, which could be used if an application specifically picks it. For example, some DX samples allow the rendering device to be changed. The D3D runtimes would add a logical display output to the VRD when an application decides to use it.

There could be multiple VRD adapters in the guest when multiple virtual GPUs are added to the VM. Only one of them can be paired with the Hyper-V Video adapter. There is no way to specify which one; the OS chooses.

## Containers and VMs

GPU virtualization is supported for VMs and containers. Containers are light weight VMs, where the host OS binaries are mapped to the container VM.

For more information about containers, see [Windows and containers](/virtualization/windowscontainers/about/).


Virtual machines could be of 2 types:
- VMMS (Virtual Machine Management Services) virtual machine
- HCS virtual machine

VMMS virtual machines are created by the VMMS process using the Hyper-V manager
or a powershell Create-VM command. GPU-PV is not officially supported in this case. The drivers are not mapped to the VM and need to be copied manually.

HCS virtual machines are created using the HCS API. A HCS virtual machine can
have arbitrary OS binaries in the VM. Hololense device emulator is an example.

## SECURE VIRTUAL MACHINE

Some virtual machines are created as “secure”. This currently includes
-	MDAG
-	Windows Sandbox
-	WSA
The following limitations exist for a secure virtual machine:
-	Driver Escape calls are not allowed (except known escapes, used with the DriverKnownEscape flag)
-	IoMmu isolation is enabled. VM creation will fail if the driver does not support IoMmu isolation

When the secure mode is enabled:
-	DxgkDdiSetVirtualMachineData will have the SecureVirtualMachine flag set
-	DxgkDdiQueryAdapterInfo will have the SecureVirtualMachine flag set
There are registry setting to force secure mode or disable IoMmu isolation during development. See the “Registry settings” section.

## Remoting of the VM/container desktop

The content of a desktop in a VM is remoted to the host using two methods:

* Using the Hyper-Video (Hyper-V) display only adapter
* Using terminal session remoting

When RDP (remote desktop) is used to connect to a VM, terminal session remoting is used.
Connecting to a Madrid or WDAG containers is done using RDP (terminal session remoting).
WDAG uses application remoting when only the top level windows of an application is remoted to the host.

Hyper-V manager uses the VMConnect application to display a VM desktop. VMConnect works in two modes: Enhanced and Basic. The Enhanced mode uses terminal session remoting. The Basic mode uses the Hyper-Video remoting.

VMConnect can be configured to use the either mode. To enable the “enhanced” mode, open Hyper-V manager, right click on the server, got to “Hyper-V settings” and enable the “enhanced” mode in the “Enhanced session mode policy”.

When the VM starts and the resolution dialog is shown
-	Press “ESC” to use the “Basic” mode
-	Pick a resolution and press “OK” to enter the enhanced mode.

## VM worker process and VM memory

When a VM/container is launched, the operating system creates the following processes on the host:

* VM worker process (*VMWP.EXE*)
* VM memory process (*VMMEM*)

*VMWP.EXE* holds various virtual device drivers, including *VRDUMED.DLL*, which is the driver for paravirtualized graphics adapters.

The *VMMEM* process virtual address space serves as backing for the IO space of the vGPU in the guest. When the IO space is accessed in the guest, the resulting physical address is the entry to the second level translation, which uses the page tables of the *VMMEM* process.

In a virtualized environment, various KMD DDI calls that would typically be executed within the context of a user process on the host are instead executed within the context of the VmMem process when a virtual machine is running.

*Dxgkrnl* creates a single DXGPROCESS (and the corresponding KMD process object) for these processes, which is called “VM worker process” in this article. The EPROCESS, associated with the DXG VM worker process is the VMMEM process.

## VM processes

When a DXGPROCESS is created in the guest VM, *Dxgkrnl* creates a corresponding DXGPROCESS object on the host. This process is called “VM process” in this article. The EPROCESS associated with the DXGPROCESS is the VMMEM process.

All rendering operations from a VM or VM allocation creation are done in the context of the VM DXGPROCESS.

For debugging purposes, the KMD is notified, which process is VM worker process or VM process in DxgkDdiCreateProcess. Using this information, the driver can link a VM process to the VM worker process. This helps debugging in scenarios, when there are more than one VMs running.

## Driver requirements

A KMD that supports GPU paravirtualization needs to set the [**DXGK_VIDMMCAPS::ParavirtualizationSupported**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) cap.

The user-mode driver (UMD) shouldn't use any process context-related data in the private driver data (pointers, handle, etc.). Instead, the KMD gets the private data in the host in a different process context.

UMD in the guest can't share memory with the KMD in the host.

The guest UMD must go through the functions described in [Registry access from UMD](#registry-access-from-umd) to access the registry.

The current paravirtualization implementation uses the VM bus to communicate between the guest and the host. The maximum message size is 128KB. Currently *Dxgkrnl* doesn't break messages to send them in chunks. The driver needs to limit the size of private data passed with object creation. For example, when [**Pfnd3dddiAllocatecb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_allocatecb) is used to create a number of allocations, the total message size includes a header, global private data, plus the size of per allocation private data multiplied by the number of allocations. This information all needs to fit in a single message.

## Running applications in fullscreen emulated mode

The Indirect Display adapter should be enabled for remoting (it is enabled by default). To disable it do the following.

* Start Edit Group Policy
* Navigate to Computer Configuration->Adminstyrative Templates->Windows Components->Remote Desktop Services->Remote Desktop Session Host->Remote Session Environment
* Open the “Use WDDM graphics display driver for Remote Desktop Connection” item
* Select Disable and click OK
* Reboot

DXGI support for fullscreen application in VMs is enabled by default. To disable it, use:
```StagingTool.exe /disable 19316777

Fullscreen applications must be running in the emulated fullscreen mode.

Enable eFSE for all DXGI applications and setting the minimum WDDM version for swap effect transition to be WDDM 2.0.
- D3DEnableFeature.exe /enable DXGI_eFSE_Enablement_Policy
- D3DEnableFeature.exe /setvariant DXGI_eFSE_Enablement_Policy 7

eFSE is enabled by default for D3D9 applications.

## DriverStore in the VM

Driver binaries on the host are located in a driver store *%windir%\system32\drivers\DriverStore\FileRepository\<DriverDirectory>*.

For paravirtualization, UMD's binaries in a VM are expected to be in *%windir%\system32\drivers\HostDriverStore\FileRepository\<DriverDirectory>*.

The host KMD reports UMD DLL's names that have the full path to the driver store. For example, *c:\windows\system32\DriverStore\FileRepository\DriverSpecificDirectory\d3dumd.dll*.

When the VM asks for a UMD name, the name is translated to *<VmSystemDrive>:\windows\system32\HostDriverStore\FileRepository\DriverSpecificDirectory\d3dumd.dll*.

### Host DriverStore for containers

For containers, Hyper-V maps the full host driver store directory in the host to *<%windir%\HostDriverStore* in the container.

### Host DriverStore for full VMs

The driver store files are copied to the VM when the virtual GPU adapter starts in the VM. This feature is disabled in the released version of the OS.

The following registry key and possible values are added to control the copy operation. The key doesn't exist by default.

``` registry
DWORD RTL_REGISTRY_CONTROL\GraphicsDrivers\DriverStoreCopyMode
```

| Value | Description |
| ----- | ----------- |
|  0    | Disable copying of the driver store |
|  1    | Normal operation (enable copying of the driver store files and don't overwrite existing files). |
|  2    | Enable copying of the driver store and overwrite existing files. |

## Registry access from UMD

This section describes DDI additions and updates that can be used to support registry access from the UMD. The driver registry keys exist on the host and aren't reflected to the VM. Therefore the UMD can't read driver registry keys directly.

The [**pfnQueryAdapterInfoCb2**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_queryadapterinfocb2) callback is added to the D3D runtime's [**D3DDDI_ADAPTERCALLBACKS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_adaptercallbacks) structure. (The runtime passes its **D3DDDI_ADAPTERCALLBACKS** when it calls UMD's [**OpenAdapter**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_openadapter).)

* When UMD calls [**pfnQueryAdapterInfoCb2**]((/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_queryadapterinfocb2)) with [**D3DDDICB_QUERYADAPTERINFO2**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddicb_queryadapterinfo2)'s **QueryType** member set to [**D3DDDI_QUERYADAPTERTYPE_QUERYREGISTRY**](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-_d3dddi_queryadaptertype), the **pPrivateDriverData** member points to a [**D3DKMT_ADAPTERREGISTRYINFO**](ns-d3dkmthk-_d3dkmt_adapterregistryinfoto read certain registry keys.

UMD can also use [**D3DKMTQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_queryadapterinfo) directly. This call is useful for UMD in the guest because it's marshalled to the host and provides a way to translate certain names to the guest name space.

* When **D3DKMTQueryAdapterInfo** is called with [**D3DKMT_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_queryadapterinfo)'s **Type** member set to [**KMTQAITYPE_QUERYREGISTRY**](/windows-hardware/drivers/ddi/d3dkmthk/ne-d3dkmthk-_kmtqueryadapterinfotype), the **pPrivateDriverData** member points to a [**D3DKMT_ADAPTERREGISTRYINFO**](ns-d3dkmthk-_d3dkmt_adapterregistryinfo.md)


[**D3DDDI_QUERYREGISTRY_INFO**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_queryregistry_info) structure with input fields that describe the registry information to query and an output field in which the registry information is returned.

The following DDI updates are also made to support registry access from the UMD:

{
    D3DDDI_QUERYADAPTERTYPE QueryType;
    VOID*  pPrivateDriverData;
    UINT   PrivateDriverDataSize;
} D3DDDICB_QUERYADAPTERINFO2;

typedef enum _D3DDDI_QUERYREGISTRY_TYPE
{
   D3DDDI_QUERYREGISTRY_SERVICEKEY      = 0,
   D3DDDI_QUERYREGISTRY_ADAPTERKEY      = 1,
   D3DDDI_QUERYREGISTRY_DRIVERSTOREPATH = 2,
   D3DDDI_QUERYREGISTRY_MAX,
} D3DDDI_QUERYREGISTRY_TYPE;

typedef enum _D3DDDI_QUERYREGISTRY_STATUS
{
   D3DDDI_QUERYREGISTRY_STATUS_SUCCESS              = 0,
   D3DDDI_QUERYREGISTRY_STATUS_BUFFER_OVERFLOW      = 1,
   D3DDDI_QUERYREGISTRY_STATUS_INVALID_PARAMETER    = 2,
   D3DDDI_QUERYREGISTRY_STATUS_FAIL                 = 3,
   D3DDDI_QUERYREGISTRY_STATUS_MAX,
} D3DDDI_QUERYREGISTRY_STATUS;

typedef struct _D3DDDI_QUERYREGISTRY_FLAGS
{
    union
    {
        struct
        {
            UINT   TranslatePath    :  1;
            UINT   MutableValue     :  1;
            UINT   Reserved         : 30;
        };
        UINT Value;
    };
} D3DDDI_QUERYREGISTRY_FLAGS;

typedef struct _D3DDDI_QUERYREGISTRY_INFO
{
   D3DDDI_QUERYREGISTRY_TYPE   QueryType;               // In
   D3DDDI_QUERYREGISTRY_FLAGS  QueryFlags;              // In
   WCHAR                       ValueName[MAX_PATH];     // In
   ULONG                       ValueType;               // In
   ULONG                       PhysicalAdapterIndex;    // In
   ULONG                       OutputValueSize;         // Out
   D3DDDI_QUERYREGISTRY_STATUS Status;                  // Out
   union {
        DWORD   OutputDword;                            // Out
        UINT64  OutputQword;                            // Out
        WCHAR   OutputString[1];                        // Out. Dynamic array
        BYTE    OutputBinary[1];                        // Out. Dynamic array
   };
} D3DDDI_QUERYREGISTRY_INFO;



**D3DDDI_QUERYADAPTERINFO::Type** is KMTQAITYPE_QUERYREGISTRY.

**D3DDDI_QUERYADAPTERINFO::pPrivateDriverData** points to buffer, which is D3DDDI_QUERYREGISTRY_INFO plus dynamically sized buffer.

**D3DDDI_QUERYREGISTRY_INFO::PrivateDriverDataSize** is sizeof(D3DDDI_QUERYREGISTRY_INFO) plus a buffer for the dynamically sized output value.

**QueryType** defines the type of registry access.

When QueryType is D3DDDI_QUERYREGISTRY_SERVICEKEY, the registry path is 	"\REGISTRY\MACHINE\SYSTEM\CurrentControlSet\Services\<ServiceName>”.

When QueryType is D3DDDI_QUERYREGISTRY_ADAPTERKEY, the registry path is "\REGISTRY\MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\<Number>”.

When QueryType is D3DDDI_QUERYREGISTRY_DRIVERSTOREPATH, the full driver store path is returned in the called in OutputString. The path is returned in the form of “<SystemDrive>:\system32\DriverStore\FileRepository\<DriverString>”. ValueType is ignored in this case.

**QueryFlags.TranslatePath** is meant to be used by the caller from a virtual machine. When set, the ValueType must be REG_SZ, REG_MULTI_SZ or REG_EXPAND_SZ and the value string will be processed to translate the path to the virtual machine space. The translation only happens when the OutputString is an absolute path to a file in the DriverStore folder. The path is translated to <SystemDrive>:\windows\system32\HostDriverStore\...

The flag should be set only when QueryType is D3DDDI_QUERYREGISTRY_SERVICEKEY or    D3DDDI_QUERYREGISTRY_ADAPTERKEY.

This flag is ignored if a call is made from a non-virtualized environment.

**QueryFlags.MutableValue** specifies that the registry value should be read from mutable adapter/service key. The OS is going to have separate adapter/software keys for mutable and non-mutable registry values.

**ValueType** must be REG_SZ, REG_MULTI_SZ, REG_EXPAND_SZ, REG_BINARY, REG_QWORD or REG_DWORD. ValueType must be zero for the D3DDDI_QUERYREGISTRY_DRIVERSTOREPATH query.

**ValueName** is a zero terminated UNICODE string. The string can contain a sub-key name, which is separated from the actual value name by backslash. For example, the value name could be  “SubKey1\ SubKey2\NameOfTheValue”. In this case “SubKey1\ SubKey2” is the subkeys of the service or software keys.

**ValueName** is ignored for the D3DDDI_QUERYREGISTRY_DRIVERSTOREPATH query.

**D3DDDI_QUERYREGISTRY_INFO::Status** - status of the operation when pfnQueryAdapterInfo2 succeeds.

**OutputValueSize** contains the size of the written output value in bytes, if pfnQueryAdapterInfoCb2 succeeds (Status is D3DDDI_QUERYREGISTRY_STATUS_SUCCESS). When Status is D3DDDI_QUERYREGISTRY_STATUS_BUFFER_OVERFLOW, OutputValueSize will be set to the number of bytes, required to hold the output value.

**Status** - status (NTSTATUS) of the operation when DxgkQueryAdapterInfo returned STATUS_SUCCESS. The status is STATUS_BUFFER_OVERFLOW when there is not enough space in the private data to hold the registry value. In this case OutputValueSize will be the number of bytes required to hold the value.

**OutputString, OutputBinary, OutputDword and OutputQword* is a union, which will hold the output value. For dynamically sized output value (for strings and binary data), the PrivateDriverData buffer should be large enough to hold the output value.

### Example 1: Reading a value from the service key

``` cpp
    WCHAR ValueName = L”EnableDebug”;
    D3DDDI_QUERYREGISTRY_INFO Args = {};
    Args.QueryType = D3DDDI_QUERYREGISTRY_SERVICEKEY;
    Args.QueryFlags.TranslatePath = FALSE or TRUE;
    Args.ValueType = Supported registry value type;
    wcscpy_s(Args.ValueName, ARRAYSIZE(Args.ValueName), ValueName);

    D3DKMT_QUERYADAPTERINFO Args1 = {};
    Args1.hAdapter = hAdapter;
    Args1.Type = KMTQAITYPE_QUERYREGISTRY;
    Args1.pPrivateDriverData = &Args;
    Args1.PrivateDriverDataSize = sizeof(Args);
    NTSTATUS Status = D3DKMTQueryAdapterInfo(&Args1);
    if (NT_SUCCESS(Status) &&
        Args.Status == D3DDDI_QUERYREGISTRY_STATUS_SUCCESS)
    {
       if (ValueType == REG_SZ || ValueType == REG_EXPAND_SZ) {
          wprintf(L"Value: \"%s\"\n", Args.OutputString);
       } else
       if (ValueType == REG_MULTI_SZ) {
          wprintf(L"Value: ");
          for (UINT i = 0; i < Args.OutputValueSize; i++) {
             if (Args.OutputString[i] == 0) {
                wprintf(L" ");
             } else {
                wprintf(L"%c", Args.OutputString[i]);
             }
          }
          wprintf(L"\n");
       } else
       if (ValueType == REG_DWORD) {
          wprintf(L"Value: %d\n", Args.OutputDword);
       } else
       if (ValueType == REG_QWORD) {
          wprintf(L"Value: 0x%I64x\n", Args.OutputQword);
       } else
       if (ValueType == REG_BINARY) {
          wprintf(L"Num bytes: %d\n", Args.OutputValueSize);
          for (UINT i = 0; i < Args.OutputValueSize; i++) {
             wprintf(L"%d ", Args.OutputBinary[i]);
          }
          wprintf(L"\n");
       }
    }
```

### Example 2: Reading the driver store path

``` cpp
    D3DDDI_QUERYREGISTRY_INFO Args = {};
    Args.QueryType = D3DDDI_QUERYREGISTRY_DRIVERSTOREPATH;

    D3DKMT_QUERYADAPTERINFO Args1 = {};
    Args1.hAdapter = hAdapter;
    Args1.Type = KMTQAITYPE_QUERYREGISTRY;
    Args1.pPrivateDriverData = &Args;
    Args1.PrivateDriverDataSize = sizeof(Args);
    NTSTATUS Status = D3DKMTQueryAdapterInfo(&Args1);
    if (NT_SUCCESS(Status) &&
        Args.Status == D3DDDI_QUERYREGISTRY_STATUS_SUCCESS)
    {
        Args.OutputString holds the output NULL terminated string.
        Args.OutputValueSize holds the number of characters in the string
    }
```

## Copying files to *%windir%\system32* and *%windir%\syswow64* in the VM

In some cases the driver user mode DLLs need to be present in the *%windir%\system32* and *%windir%\syswow64* directories.

The OS provides a way for the driver to specify files that should be copied from the driver store in the host to *%windir%\system32* or *%windir%\syswow64* in the guest.

In the installation INF, the driver can define multiple values in the following subkeys in the graphics adapter registry key:

1. **CopyToVmOverwrite**
2. **CopyToVmWhenNewer**
3. **CopyToVmOverwriteWow64**
4. **CopyToVmWhenNewerWow64**

The **CopyToVmOverwrite** and **CopyToVmWhenNewer** subkeys are used to copy files to the *%windir%\system32* directory.

The **CopyToVmOverwriteWow64** and **CopyToVmWhenNewerWow64** subkeys are used to copy files to the *%windir%\syswow64* directory.

The files under **CopyToVmOverwrite** and **CopyToVmOverwriteWow64** will always overwrite the files in the destination.

The files under **CopyToVmWhenNewer** and **CopyToVmWhenNewerWow64** will overwrite the files in the destination only if the file change date is newer. The "newer" criteria compares two pieces of information:

* FileVersion
* LastWriteTime

When the destination file ends with the *.dll* or *.exe* suffix, the FileVersion is used as the most-significant comparison value where the greatest version is deemed "newer". When the destination file doesn't end with the *.dll* nor *.exe* suffix or the two FileVersion are equal, then LastWriteTime is used as the least-significant comparison values where the later date/ time is deemed "newer".

Each value type under a subkey must be REG_MULTI_SZ or REG_SZ. If the value type is REG_MULTI_SZ, there should be maximum 2 strings in the value. This implies that each value defines a single string or a pair of strings, where the second string could be empty.

The first name in a pair is a path to a file in the driver store. The path is relative to the root of the driver store and can contain sub-directories.

The second name in a pair is the name of the file how it should appear in %windir%\system32 or %windir%\syswow64 directory. The second name should be just the file name, not including path.
If the second name is empty, the file name is the same as in the driver store (excluding subdirectories).

This allows the driver to have different names in the host driver store and in the guest.

**Example 1:**
```
INF [DDInstall] section
HKR,"softgpukmd\CopyToVmOverwrite",SoftGpuFiles,%REG_MULTI_SZ%,"CopyToVm\softgpu1.dll”, “softgpu2.dll”
The directive will create the registry key in the software (adapter) key:
"HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\<number>\CopyToVmOverwrite”, SoftGpuFiles = REG_MULTI_SZ, “CopyToVm\softgpu1.dll”, “softgpu2.dll”
```
The OS will copy <DriverStorePath>\CopyToVm\softgpu1.dll to %windir%\system32\softgpu2.dll

**Example 2:**
```
INF [DDInstall] section:
HKR,"CopyToVmOverwrite",SoftGpuFiles1,%REG_MULTI_SZ%,"softgpu1.dll”,”softgpu.dll”
HKR,"CopyToVmOverwrite",SoftGpuFiles2,%REG_SZ%, “softgpu2.dll”
The directive will create the registry key in the software (adapter) key:
“HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\<number>\CopyToVmOverwrite”,  SoftGpuFiles1 = REG_MULTI_SZ, “softgpu1.dll”, “softgpu.dll”
“HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\<number>\CopyToVmOverwrite”,  SoftGpuFiles2 = REG_SZ, “softgpu2.dll””
```
The OS will copy <DriverStorePath>\softgpu1.dll to %windir%\system32\softgpu.dll and <DriverStorePath>\softgpu2.dll to %windir%\system32\softgpu2.dll.

**Example 3:**
```
INF [DDInstall] section:
HKR,"CopyToVmOverwriteWow64",SoftGpuFiles,%REG_MULTI_SZ%,“Subdir1\Subdir2\softgpu2wow64.dll”,”softgpu.dll”.
The directive will create the registry key in the software (adapter) key:
“HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\<number>\CopyToVmOverwriteWow64”,  SoftGpuFiles = REG_MULTI_SZ, “Subdir1\Subdir2\softgpu2wow64.dll”,”softgpu.dll
```
The OS will copy <DriverStorePath>\Subdir1\Subdir2\softgpu2wow64.dll to %windir%\syswow64\softgpu.dll.

## CHANGES IN DDICREATEPROCESS
```
typedef struct _DXGK_CREATEPROCESSFLAGS
{
    union
    {
        struct
        {
            UINT    SystemProcess               : 1;
            UINT    GdiProcess                  : 1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
            UINT    VirtualMachineProcess       : 1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_4)
            UINT    VirtualMachineWorkerProcess : 1;
            UINT    Reserved                    : 28;
#else
            UINT    Reserved                    : 29;
#endif // (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_4)
#else
            UINT    Reserved                    : 30;
#endif // (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
        };
        UINT Value;
    };
} DXGK_CREATEPROCESSFLAGS;

typedef struct _DXGKARG_CREATEPROCESS
{
    HANDLE                  hDxgkProcess;       // in
    HANDLE                  hKmdProcess;        // out
    DXGK_CREATEPROCESSFLAGS Flags;              // in
    UINT                    NumPasid;           // in
    _Field_size_(NumPasid)
    ULONG*                  pPasid;             // in
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_4)
    HANDLE                  hVmWorkerProcess;   // in
    UINT                    ProcessNameLength;  // in
    _Field_size_(ProcessNameLength)
    WCHAR*                  pProcessName;       // in
#endif // (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_4)
} DXGKARG_CREATEPROCESS;
```

When **CREATEPROCESSFLAGS::VirtualMachineWorkerProcess** is set, the process belongs to the worker process of a virtual machine.

**hVmWorkerProcess** – the driver handle, which was returned when a process with VirtualMachineWorkerProcess, was created. This value is valid only when VirtualMachineProcess is set.

**pProcessName** - pointer to a NULL terminated UNICODE string, with the name of the process. When VirtualMachineProcess is set, this is the name of the process inside a virtual machine.
ProcessNameLength - the number of UNICODE characters in the ProcessName array, not including the terminating NULL.

## DXGKDDISETVIRTUALMACHINEDATA

DxgkDdiSetVirtualMachineData is added to pass information about a virtual machine to the KMD.
```
typedef struct _DXGK_VIRTUALMACHINEDATAFLAGS
{
    union
    {
        struct
        {
            UINT    SecureVirtualMachine    : 1;
        };
        UINT Value;
    };
} DXGK_VIRTUALMACHINEDATAFLAGS;

typedef struct _DXGKARG_SETVIRTUALMACHINEDATA
{
    HANDLE                          hKmdVmWorkerProcess;    // in
    GUID*                           pVmGuid;                // in
    DXGK_VIRTUALMACHINEDATAFLAGS    Flags;                  // in
} DXGKARG_SETVIRTUALMACHINEDATA;
typedef _In_ CONST DXGKARG_SETVIRTUALMACHINEDATA*   IN_CONST_PDXGKARG_SETVIRTUALMACHINEDATA;

typedef
    _Check_return_
    _Function_class_DXGK_(DXGKDDI_SETVIRTUALMACHINEDATA)
    _IRQL_requires_(PASSIVE_LEVEL)
NTSTATUS
APIENTRY
DXGKDDI_SETVIRTUALMACHINEDATA(
    IN_CONST_HANDLE                         hAdapter,
    IN_CONST_PDXGKARG_SETVIRTUALMACHINEDATA Args
    );
```
**hKmdVmWorkerProcess** – the driver handle, which was returned when a process with
VirtualMachineWorkerProcess, was created.

**pVmGuid** – identifies a virtual machine. This is provided for debugging purposes, so developers can attribute rendering to a specific virtual machine when multiple VMs are running.

**Flags.SecureVirtualMachine** - specifies that the virtual machine runs in the secure mode.
See the section Secure Virtual Machine.

## ASYNCHRONOUS VM BUS MESSAGES TO THE HOST

Starting from the Iron release (10/20/2020) some messages from Dxgkrnl in the guest OS to the host are asynchronous. This is done to improve performance of high frequency Dxgkrnl API calls in the guest. Overhead of each synchronous VM bus message to the host could be high.

The async messages include:
- D3DKMTSubmitCommand
- D3DKMTSubmitCommandToHardwareQueue
- D3DKMTSignalSynchronizationObjectFromGpu
- D3DKMTWaitForSignalSynchronizationObjectFromGpu

## LDA support in GPU-PV

LDA is supported in GPU-PV since SV2 (Windows 2022) for all scenarios and partially supported in pre-SV2 releases.

To have a consistent implementation and to support possible future porting of the LDA support to older Windows releases, the KMD needs to check the LDA support in GPU-PV by calling DxgkCbIsFeatureEnabled(DXGK_FEATURE_LDA_GPUPV). The support is enabled if the function succeeds and returns "Enabled". If the KMD does not call this callback Dxgkrnl assumes that the KMD doesn't support LDA in GPU-PV.

```cpp
typedef enum _DXGK_FEATURE_ID
{
    // Support for LDA in GPU-PV
    DXGK_FEATURE_LDA_GPUPV = 2,
} DXGK_FEATURE_ID;
```

If the OS supports the feature, it is up to the driver to enable or not LDA in user mode.

### Pre-SV2

Currently DxgkCbIsFeatureEnabled(DXGK_FEATURE_LDA_GPUPV) will fail in the pre-SV2 OS release.
But LDA still could be enabled in Linux user mode runtimes.

The LDA state in user mode should be set as follow:

Runtime                          |  LDA state
---------------------------------| -----------
pre-d3d12 runtime                | Must be disabled
non-DX runtimes (Windows)        | Must be disabled
d3d12 runtime (Windows)          | Must be disabled
Linux (d3d12 and non-DX runtime) | Can be enabled

### SV2+

The LDA state in user mode should be set as follow:

Runtime                          |  LDA state
---------------------------------| -----------
pre-d3d12 runtime                | Can be enabled if DXGK_FEATURE_LDA_GPUPV is supported and the guest OS is SV2+
non-DX runtimes (Windows)        | Can be enabled if DXGK_FEATURE_LDA_GPUPV is supported and the guest OS is SV2+. Instead of checking the OS version, the UMD could call D3DKMTQueryAdapterInfo(KMTQAITYPE_PHYSICALADAPTERCOUNT) and enable LDA when it returns number of physical adapters greater than 1
d3d12 runtime (Windows)          | Can be enabled. See the section about d3d12 LDA interface
Linux (d3d12 and non-DX runtime) | Can be enabled if DXGK_FEATURE_LDA_GPUPV is supported

Drivers, compiled with the interface version less than DXGKDDI_INTERFACE_VERSION_WDDM3_0, do not check DXGK_FEATURE_LDA_GPUPV. These drivers can still enable LDA for Linux runtimes.

### Setting the LDA state for the d3d12 runtime

When enabling/disabling LDA for the d3d12 runtime, the UMD needs to return the correct tier and the node map information to the runtime. The code flow is as following:

- d3d12 gets the D3D12_CROSS_NODE_SHARING_TIER cap from UMD
- d3d12 gets the physical adapter count from Dxgkrnl by calling D3DKMTQueryAdapterInfo(KMTQAITYPE_PHYSICALADAPTERCOUNT)
- d3d12 calls pfnQueryNodeMap(PhysicalAdapterCount, &map) to get mapping of logical node indices to physical nodes. "Node" in this case means "physical adapter". The UMD needs to set the actual physical adapter index in the map or D3D12DDI_NODE_MAP_HIDE_NODE to disable a node.
- Based on the pfnQueryNodeMap results d3d12 computes the effective physical adapter count by not counting the hidden nodes.
- If the state of the tier and the effective physical adapter count do not match, d3d12 fails device creation. Mismatch happens when
    -	the tier is D3D12DDI_CROSS_NODE_SHARING_TIER_NOT_SUPPORTED and adapter count is > 1
    -	the tier is not D3D12DDI_CROSS_NODE_SHARING_TIER_NOT_SUPPORTED and adapter count is 1

To disable LDA the UMD needs to return the D3D12DDI_CROSS_NODE_SHARING_TIER_NOT_SUPPORTED tier and keep only one physical adapter enabled in tha node map.

### D3DKMTQueryAdapterInfo(KMTQAITYPE_PHYSICALADAPTERCOUNT)

A query for the physical adapter count (KMTQAITYPE_PHYSICALADAPTERCOUNT) always returns correct physical adapter count to the guest:
-	On pre-SV2 guests it returns 1. This is hard coded in the guest code. Note that could be changed in the future if LDA support is ported to older OS releases
-	On SV2+ it returns:
    -	the actual number of physical adapters when DXGK_FEATURE_LDA_GPUPV is enabled (driver needs to call the DxgkCbIsFeatureEnabled callback).
    - 1 otherwise.

# Paravirtualization bring up

Virtualization support needs to be enabled in the BIOS (VT-d or similar).

GPU-PV setup is different for VMMS virtual machines and the containers.

In PowerShell (running as Administrator), enable script execution on the server:

``` PowerShell
set-executionpolicy unrestricted
```

## VMMS	virtual machine setup

### Setting up the host and the VM

The OS build in the VM can be older or newer than the OS build in the host.
1.	Enable the Hyper-V feature in the server roles or the Hyper-V feature on the client. When enabling this feature on the server, select the option to use network adapter as the External switch.
2.	(optional) Enable test signing (bcdedit -set TESTSIGNING ON)
3.	Reboot.
4.	Install a GPU driver, which supports para-virtualization
5.	(optional) Some drivers do not set the ParavirtualizationSupported cap. In this case add the following registry before installing the driver or disable/enable the device after the flag is set.
DWORD HKLM\System\CurrentControlSet\Control\GraphicsDrivers\GpuVirtualizationFlags = 1
6.	To check if the paravirtualized GPU is recognized by the OS, execute the following PowerShell command:
```
Get-VMPartitionableGpu
```
The output should be similar to this:
```
Name                    : \\?\PCI#VEN_10DE&DEV_1C02&SUBSYS_11C210DE&REV_A1#4&275d7527&0&0010#{064092b3-625e-43bf-9eb5-d
                          c845897dd59}\GPUPARAV
ValidPartitionCounts    : {32}
PartitionCount          : 32
TotalVRAM               : 1000000000
AvailableVRAM           : 1000000000
MinPartitionVRAM        : 0
MaxPartitionVRAM        : 1000000000
OptimalPartitionVRAM    : 1000000000
TotalEncode             : 18446744073709551615
AvailableEncode         : 18446744073709551615
MinPartitionEncode      : 0
MaxPartitionEncode      : 18446744073709551615
OptimalPartitionEncode  : 18446744073709551615
TotalDecode             : 1000000000
AvailableDecode         : 1000000000
MinPartitionDecode      : 0
MaxPartitionDecode      : 1000000000
OptimalPartitionDecode  : 1000000000
TotalCompute            : 1000000000
AvailableCompute        : 1000000000
MinPartitionCompute     : 0
MaxPartitionCompute     : 1000000000
OptimalPartitionCompute : 1000000000
CimSession              : CimSession: .
ComputerName            : IOURIT-TEST2
IsDeleted               : False
```
7.	Run the following commands in PowerShell to create a VM with GPU)
```
$vm = “TEST“
New-VM –VMName $vm -Generation 2
Set-VM -GuestControlledCacheTypes $true -VMName $vm
```
A VM, named TEST, will be created

8.	Set IO space for the VM. IO space is used by GPU-PV to handle CPU visible allocations. At least 8GB of IO space is needed.
```
Set-VM -LowMemoryMappedIoSpace 1GB -VMName $vm
Set-VM –HighMemoryMappedIoSpace 16GB –VMName $vm
```

9.	[optional] By default, the base address for the high memory IO space is set to (64GB – 512MB). On Haswell chipsets with 36 bits physical memory addressing, the end address of the IO space region needs to be below 64GB, so the start address needs to be set accordingly. The following script set the start address to 47GB.

SetHighMmioBase.ps1:
```
param( [string]$VmName, $BaseInMB)

function Get-WMIVM
{
    [CmdletBinding()]
    param(
        [parameter(Mandatory=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$VmName = ""
        )

    gwmi -namespace root\virtualization\v2 -query "select * from Msvm_ComputerSystem where ElementName = '$VmName'"
}
function Get-WMIVmSettingData
{
    [CmdletBinding()]
    param(
        [parameter(Mandatory=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$VmName = ""
        )
    $vm = Get-WMIVM $VmName

    return $vm.GetRelated ("Msvm_VirtualSystemSettingData","Msvm_SettingsDefineState",$null,$null, "SettingData", "ManagedElement", $false, $null)
}

Write-Host "Setting HighMmioGapBase to $BaseInMB for VmName $VmName"
$vssd = Get-WMIVmSettingData $VmName
$vmms = Get-WmiObject -Namespace "root\virtualization\v2" -Class Msvm_VirtualSystemManagementService
$vssd.HighMmioGapBase = $BaseInMB
$settingsText = $vssd.PSBase.GetText("CimDtd20")
$ret=$vmms.ModifySystemSettings($settingsText).ReturnValue
if ($ret -eq 0)
{
   Write-Host "Successfully set" $vssd.HighMmioGapBase
} else
{
   Write-Host "Error $ret"
}
```
Example: SetHightMmioBase.ps1 “TEST” 48128

10.	Add a virtual GPU to the VM and disable checkpoints.
```
Add-VMGpuPartitionAdapter –VMName $vm
Set-VM –CheckpointType Disabled -VMName $vm
```
11.	To check that the VM has a paravirtualized GPU, execute the following command:
Get-VMGpuPartitionAdapter –VMName $vm in PowerShell. The output should show the adapter.

Example:
```
MinPartitionVRAM        :
MaxPartitionVRAM        :
OptimalPartitionVRAM    :
MinPartitionEncode      :
MaxPartitionEncode      :
OptimalPartitionEncode  :
MinPartitionDecode      :
MaxPartitionDecode      :
OptimalPartitionDecode  :
MinPartitionCompute     :
MaxPartitionCompute     :
OptimalPartitionCompute :
Name                    : GPU Partition Settings
Id                      : Microsoft:9ABB95E2-D12D-43C3-B840-6F4A9CFB217B\929890BC-BB33-4687-BC1A-F72A4F1B3B3F
VMId                    : 9abb95e2-d12d-43c3-b840-6f4a9cfb217b
VMName                  : TEST
VMSnapshotId            : 00000000-0000-0000-0000-000000000000
VMSnapshotName          :
CimSession              : CimSession: .
ComputerName            : IOURIT-TEST2
IsDeleted               : False
VMCheckpointId          : 00000000-0000-0000-0000-000000000000
VMCheckpointName        :
```
12.	Copy VHDX of the same client build, which will be used in the VM, to a host directory. For example, d:\VM\os.vhdx

13.	Open Hyper-V manager and modify VM parameters (select VM and click Settings):
```
Security – uncheck “Enable Secure Boot”
Memory – Check “Enable Dynamic Memory”. The amount of memory is 1024MB or more.
Processor – Set “Number of virtual processors” to 2 or 4.
Network adapter – Select the network adapter to use with the VM from the drop out box. If network debugging is enabled, make sure to pick Microsoft Debugging NET adapter.
SCSI controller – Hard Drive – Add – Virtual Hard Disk – Browse – Select d:\VM\os.vhdx
```
14.	Copy driver files to the VM [Not needed for GRFX_DEV RS5 builds after 04/20/2018]
This step is required for release builds and builds

Starting from RS5 (04/20/2018) the OS copies the files from the host driver store to the HostDriverStore directory in the guest when the adapter is initialized in the guest. This is done only in the builds from RS_ONECORE_SIGMA_GRFX_DEV.
-	Mount the VM’s VHDX. For example, to the disk f:
-	In the mounted VM create a directory named f:\%windir%\system32\HostDriverStore\FileRepository.

Replicate driver files from %windir%\system32\DriverStore in the host to the VM. There should be f:\%windir%\system32\HostDriverStore\FileRepository\YourDriverDirectory\* in the VM.

15.	If the driver needs to access files from %windir%\system32 or %windir%\syswow64, the files need to be copied manually to the VM.

16.	Enable test signing in the VM if the drivers are not Microsoft signed
From the CMD admin window:
bcdedit /store <VM drive>:\EFI\Microsoft\Boot\BCD -set {bootmgr} testsigning on
Dismount the VM’s VHDX

17. Start the VM

18. Connect to the VM using the Hyper-V manager Connect option

### INSIDE THE VM

Check that there is Virtual Render Device in the VM’s device manager
All rendering inside the VM will go through virtual GPU

### POWER SHELL SCRIPT TO SETUP A VM

Here is an example of a power shell script, which sets up a VM from scratch. Modify it to suit your needs.
```
Param(
   [string]$VMName,
   [string]$VHDPath,
   [string]$SwitchName,
   [switch]$CreateVm,
   [switch]$InitDebug,
   [switch]$CopyRegistry,
   [switch]$CopyDriverStore,
   [switch]$CreateSwitch,
   [switch]$AddGpu,
   [switch]$All
)

if($All)
{
   $CreateVm = $True
   $CreateInitDebug = $True
   $CopyRegistry = $True
   $CopyDriverStore = $True
   $CreateSwitch = $True
   $AddGpu = $True
   $InitDebug = $True
}

   $vm = $VMName

#
# Validate parameters
#
if ($CreateSwitch -or $CreateVM)
{
    if ($SwitchName -eq "")
    {
        write "SwitchName is not set"
        exit
    }
}

if ($AddGpu -or $CreateVM)
{
    if ($VMName -eq "")
    {
        write "VMName is not set"
        exit
    }
}

if ($InitDebug -or $CreateVM -or $CopyDriverStore -or $CopyRegistry)
{
    if ($VHDPath -eq "")
    {
        write "VHDPath is not set"
        exit
    }
}

enable-windowsoptionalfeature -FeatureName Microsoft-Hyper-V-All -online

#
# Create a network switch for the VM
#
if ($CreateSwitch)
{
    New-VMSwitch $SwitchName -NetAdapterName "Ethernet (Kernel Debugger)"
}

#
# Create a VM and assign VHD to it
#
if ($CreateVm)
{
   New-VM –VMName $vm -Generation 2
   Set-VM -GuestControlledCacheTypes $true -VMName $vm
   Set-VM -LowMemoryMappedIoSpace 1Gb -VMName $vm
   Set-VM –HighMemoryMappedIoSpace 32GB –VMName $vm
   Set-VMProcessor -VMname $vm -count 4
   Set-VMMemory -VMName $vm -DynamicMemoryEnabled $true -MinimumBytes 1024MB -MaximumBytes 4096MB -StartupBytes 1024MB -Buffer 20
   Add-VMHardDiskDrive -VMName $vm -Path $VHDPath
   Connect-VMNetworkAdapter -VMName $vm -Name "Network Adapter" -SwitchName $SwitchName
   Set-VMFirmware -VMName $vm -EnableSecureBoot off
   Set-VMFirmware -VMName $vm -FirstBootDevice (Get-VMHardDiskDrive -VMName $vm)
}

#
# Enable debugger and testsiging
#
if ($InitDebug)
{
   Mount-vhd $VHDPath
   Add-PartitionAccessPath  -DiskNumber (Get-DiskImage -ImagePath $VHDPath | Get-Disk).Number -PartitionNumber 1 -AssignDriveLetter
   $efidrive = (Get-DiskImage -ImagePath $VHDPath | Get-Disk | Get-Partition -PartitionNumber 1).DriveLetter
   bcdedit /store ${efidrive}:\EFI\Microsoft\Boot\BCD -set '{bootmgr}' testsigning on
   bcdedit /store ${efidrive}:\EFI\Microsoft\Boot\BCD -set '{default}' debug on
   bcdedit /store ${efidrive}:\EFI\Microsoft\Boot\BCD /dbgsettings net port:50052 key:a.b.c.d hostip:10.131.18.133
   Dismount-VHD $VHDPath
}

#
# Now boot the VM without vGPU to verify that it is initialized correctly
# If everyting is OK, turn off the VM
#
if ($CreateVm)
{
   Write-Output "Boot the VM and turn it OFF after it is initialized"
   pause
}

#
# Add virtual GPU
#
if($AddGpu)
{
   Add-VMGpuPartitionAdapter –VMName $vm
   Get-VMGpuPartitionAdapter –VMName $vm
}

#
# Copy the driver store to the VM
#
if ($CopyDriverStore)
{
   Write "Copying driver store"
   Mount-vhd $VHDPath
   $drive = (Get-DiskImage -ImagePath $VHDPath | Get-Disk | Get-Partition -PartitionNumber 3).DriveLetter
   xcopy /s $Env:windir\system32\driverstore\* ${drive}:\windows\system32\hostdriverstore\
   Dismount-VHD $VHDPath
}

#
# Export driver registry settings
#
if ($CopyRegistry)
{
   Write "Copying registry"
   Mount-vhd $VHDPath
   $drive = (Get-DiskImage -ImagePath $VHDPath | Get-Disk | Get-Partition -PartitionNumber 3).DriveLetter
   reg load HKLM\VMSettings ${drive}:\Windows\System32\config\SYSTEM
   reg copy "HKLM\System\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" "HKLM\VmSettings\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000" /s /f
   reg unload "HKLM\VmSettings"
   Dismount-VHD $VHDPath
}
```

### DEBUGGING THE VM

The VM debugger is configured the same way as network debugging on a regular client machine.

#### IF THE VM DOES NOT START OR YOU SEE BLACK SCREEN
Turn OFF the vm and remove the virtual GPU from the VM using the following commands:
```
$vm = “TEST“
remove-VMGpuPartitionAdapter  -VMName $vm –AdapterId “<Id from Get-VMGpuPartitionAdapter>”
```
For example:
```
remove-VMGpuPartitionAdapter  -VMName $vm –AdapterId “Microsoft:9ABB95E2-D12D-43C3-B840-6F4A9CFB217B\929890BC-BB33-4687-BC1A-F72A4F1B3B3F”
```
Start the VM. If it starts successfully, make sure the driver files are copied correctly to the HostDriverStore in the VM.

Add vGPU to the VM using the Add-VMGpuPartitionAdapter command

Start the VM again.
See the Troubleshooting section for additional information

## CONTAINER SETUP

###	OVERVIEW

The difference between containers (also called HCS VM) and the full VM is that the OS binaries and the driver store files are mapped to the container. So, there is no need to copy the driver files to the container (unless they are needed in the windows\system32 directory).

There are the following container types today:
- WDAG (Windows Defender Application Guard), also called “Barcelona”
- WDAG for the Microsoft’s Chromium (Anaheim) browser
- WDAG for Office
- Windows Sandbox

The difference between them is in
- how the container image is remoted to the host
- if the container is considered “secure”.

Driver escapes are disabled for secure containers. Also, the driver must support IOMMU isolation to be enabled inside a secure container.

WDAG and Windows Sandbox support GPU adapter “hot plug”.
When the driver on the host is updated and host GPU is started/stopped, the changes are reflected in the container.

### WDAG (BARCELONA)
This container type is used to run the Edge browser. Only the Edge window is remoted and shown in the host. Driver escapes are disabled. The Edge swapchain is shared between the container and the host (which is called “graphics VAIL technology” – do not confuse with VAIL container type)

### WDAG FOR THE CHROMIUM (ANAHEIM) BROWSER

The Chromium browser can be installed from https://www.microsoftedgeinsider.com/
Currently, a browser from the DEV or Canary channels can use virtual GPU.
vGPU setup is the same as for the Edge WDAG container. The container type and properties are the same as for Edge WDAG.

Open Settings.

Security - App & Browser control -> Isolated Browsing -> Change Application Guard Settings -> Advanced Graphics – enable hw acceleration.

Reboot

Open gpedit and go to Computer configuration – Administrative Templates – Windows components – Microsoft Defender Application Guard and enable hw acceleration and data persistence.

Do “gpupdate/force after that.

Configure the Group Policy settings for Microsoft Defender Application Guard (Windows 10) - Windows security | Microsoft Docs

Here is the link to the group policy to enable GPU acceleration:
Microsoft Edge Browser Policy Documentation | Microsoft Docs

#### GROUP POLICY (ADMX) INFO

- GP unique name: HardwareAccelerationModeEnabled
- GP name: Use hardware acceleration when available
- GP path (Mandatory): Administrative Templates/Microsoft Edge/
- GP path (Recommended): N/A
- GP ADMX file name: MSEdge.admx

####	WINDOWS REGISTRY SETTINGS
- Path (Mandatory): SOFTWARE\Policies\Microsoft\Edge
- Path (Recommended): N/A
- Value Name: HardwareAccelerationModeEnabled
- Value Type: REG_DWORD

Launch WDAG and go to edge://settings – system. Enable HW acceleration.

Navigate to aka.ms/gpucheck to see if vGPU is enabled.

(Supported mechanism of launching WDAG is: [on host] msedge.exe --ms-application-guard <URL>).

### WINDOWS SANDBOX (ALSO CALLED MADRID)

This container type is used to try risky application inside the container. The full desktop image is remoted to the host. The Indirect Display Driver is used for remoting. Graphics VAIL is not used, so bringing desktop image to the host is slow.

Virtual GPU is disabled by default in Windows Sandbox. To enable it, one needs to create a WSB configuration file (for example, config.wsb) and enable virtual GPU in it. Start Sandbox by clicking on the configuration file.

Configuration file example:
```
<Configuration>
    <VGpu>Enable</VGpu>
</Configuration>
```
The vGPU in the container has driver escapes disabled by default.
Starting with Manganese builds (12/2/2019) a configuration option is added to enable driver escapes. The WSB file example (this will enable vGPU in Sandbox and enable driver escapes):
<Configuration>
    <VGpu>EnableVendorExtensions</VGpu>
</Configuration>

### VAIL CONTAINER

This container type is used to run Win32 applications inside a WCOS (Windows Core Operated System) based host. The image of each application in the container is remoted to the host. Graphics VAIL is enabled to remote each application swapchain. Driver escapes are enabled.

### COMMON CONTAINER REQUIREMENTS

1.	Machine requirements:
- needs to have both Vtx and Vtd enabled in BIOS (or their equivalents: AMD-V, AMD-IOMMU)
- there should be at least 8GB of RAM
- there should be more than 5GB of system disk space

### SETTING UP WDAG (BARCELONA CONTAINER)

The Barcelona container design is switched to so called “V2 schema” by default. In this case the OS makes a snapshot of the container to increase the startup speed. This changes the ways security policy is disabled, debugger is attached to the container etc.
Note! The V2 schema cannot be disabled anymore.

Driver requirements:

- Driver must support the IoMmu feature. It will be enabled when WDAG is running
- Driver is running in the “secure” mode (calls to D3DKMTEscape will fail)
- Install a client OS build from RS_ONECORE_SIGMA_GRFX_DEV or a recent RS4 build
- In “Turn remove Windows Features on or off” enable the Hyper-V, Container and Microsoft Defender Application Guard features

Reboot

Start Microsoft Edge

Click on the “…” button (Settings and more) and click on “New Application Guard Window”

Wait until the window is created. It might take some time. The window has a distinctive border around.

If WDAG window opens, the container is successfully started.

By default, there is no virtual GPU in the container. To enable virtual GPU do one of the following:
- Set the registry key DWORD HKLM\Software\Microsoft\HVSI\EnableVirtualGpu = 1
- Go to Setting – Security – Windows Security – Browser Control – Defender Application Guard Settings – Enable Advanced Graphics

Reboot.

Only the “post” GPU adapter is projected to the container.

By default, the IoMmu isolation feature is enabled for vGPUs in WDAG. If the driver does not support IoMmu isolation, the vGPU will fail to start. To avoid this set the following registry key

DWORD HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\IoMmuFlags = 8

WDAG will not load user mode DLLs, which are not signed with Microsoft signature. For testing purposes, the security policy can be disabled in the WDAG container. Another option is to attach kernel debugger to the container. These options are explained in the next sections.

Reboot

Start WDAG

To verify that vGPU is running in WDAG:

Visit http://gpucheck.azurewebsites.net/

Visit http://madebyevan.com/webgl-water/, try to move the ball and observe that rendering is fast

### DISABLING SECURITY POLICY IN WDAG

Disabling security policy in the WDAG container is needed, if one wants to run an application inside the container or use a driver, which is not signed by Microsoft.

Copy all files from docs\Virtualization and below to a local directory
-	Start WDAG
-	Run containerAUditMode.cmd without parameters to see the current settings
-	Run “containerAUditMode.cmd Enable” to disable security policy.
-	Run “containerAUditMode.cmd Disable” to enable security policy.
-	Restart the container by running in the administrative command shell:
o	sc stop hvsics
o	sc start hvsics
o	Start WDAG windows


### SETTING UP KERNEL DEBUGGER FOR WDAG OR WINDOWS SANDBOX

##### USING CMDIAG (19H1+)

A Container Manager service (cmservice) is used to control Hyper-V isolated containers.
CMDIAG.EXE is an application (available when Hyper-V, WDAG and Containers features are installed), which is used to enabled kernel mode debugging for containers, enable test signing, etc.

Serial and NET debugging is supported by the Container Manager. (At this point NET debugging is not verified by the graphics team).

Run “cmdiag.exe Debug” to see the options.

CMDIAG modifies debugger settings in the container base image. Both Madrid and WDAG containers are using the same base image.  There should be only one instance of a container running (Madrid or WDAG) when kernel debugger is enabled.

HVSICS service needs to be stopped before changing the debugger settings.
Example 1:
```
C:\Windows\system32>sc stop hvsics
SERVICE_NAME: HVSICS
        TYPE               : 30  WIN32
        STATE              : 3  STOP_PENDING
                                (STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x1
        WAIT_HINT          : 0xbb8

C:\Windows\system32>cmdiag debug -on -Serial  -Force
Debugging successfully enabled. Connection string: -k com:pipe,port=\\.\pipe\debugpipe,reconnect -v
```
Example 2:
```
C:\Windows\system32>cmdiag debug -on -net -port 51000 -key a.b.c.d -hostip 10.131.18.34
```
#### RUNNING DEBUGGER ON A DIFFERENT MACHINE

When serial debugger is used, it is often desired to run the debugger on a different machine.
Kdsrv.exe could be used if it is desired to run debugger on a different machine. See Windows debugger information. For example, if the machine where WDAG is running, has IP address 10.131.18.190 and the kernel debugger connection to the container is COM port at =\\.\pipe\debugpipe, do the following:
- Start kdsrv in the machine, where WDAG is running

kdsrv.exe -t tcp:port=50006

- Start the debugger where you want it to be running:

windbg.exe -k kdsrv:server=@{tcp:server=10.131.18.190,port=50006},trans=@{com:pipe,port=\\.\pipe\debugpipe,reconnect}

To disable timeouts during kernel debugging set the following registry keys:
```
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Virtualization\Containers\UtilityVm" /v BridgeTransactionTimeout /t REG_DWORD /d 0xffffffff /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Virtualization\Containers\UtilityVm" /v BridgeServerConnectTimeout /t REG_DWORD /d 0xffffffff /f
reg add "HKLM\SOFTWARE\Microsoft\HVSI" /f /v DisableResetContainer /t REG_DWORD /d 1
reg add "HKLM\SOFTWARE\Microsoft\HVSI" /f /v AppLaunchTimeoutInSeconds /t REG_DWORD /d 0x7fffffff
reg add "HKLM\Software\Microsoft\Terminal Server Client" /f /v ConnectionHealthMonitoringSupported /t REG_DWORD /d 0
reg add "HKLM\Software\Microsoft\Terminal Server Client" /f /v DisableUDPTransport /t REG_DWORD /d 1
reg add "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client" /f /v ConnectionHealthMonitoringSupported /t REG_DWORD /d 0
reg add "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client" /f /v DisableUDPTransport /t REG_DWORD /d 1
```
#### SETTING DEBUGGER FOR VAIL CONTAINER
- Connect to the host using telnet. The IP address of the host could be obtained from Network Settings in the host OS.
- Use cmdiag.exe to configure the debugger

#### RS4 INSTRUCTIONS
Only COM port debugging is available when V2 schema is enabled.
-	Run the KryptonDebug.ps1 script without parameters to setup serial debugger. The script will print the debugger connection options.
-	Start your debugger session connecting with the options showed.
-	Start the WDAG window.
-	If debugger is not connected, try to stop/start the HVSI service:
```
sc stop hvsics
sc start hvsics
Start WDAG
```
### TAKING ETL TRACES INSIDE BARCELONA CONTAINER FOR GPUVIEW

hcsdiag.exe is a tool, which is available in the OS when the “Containers” feature is enabled
“hcsdiag list” is used to get the list of running containers and their IDs.

- Disable security policy for WDAG
- Install XPERF tools in the host. The tools should have the GPUVIEW folder
- Share the XPREF folder on the host with the container by using the “hcsdiag share” command

- Start a console (command shell) application in the container by using “hcsdiag.exe console <container id>”
- Start ETW session on the host by running XPERF\GPUVIEW\log.cmd
- Start ETW session in the container by running XPERF\GPUVIEW\log.cmd
- Repro a scenario
- Stop sessions in the container and the host by executing log.cmd again
- Open merged.etl from the host and from the container by GpuView.exe
- GpuView synchronizes view for both ETL files so events in the container and the host can be correlated.

### CHANGING REGISTRY VALUES IN BARCELONA CONTAINER
TBD

## SETTING UP HYPERVISOR DEBUGGER
```
bcdedit /hypervisorsettings NET port:50000 key:a.b.c.d hostip:1.1.1.1
bcdedit /set {hypervisorsettings} hypervisorbusparams 0.0.0 (if needed)
bcdedit /set hypervisordebug on
reboot host
```
The hypervisor extensions are in \\winbuilds\release\RS1_ONECORE_CONTAINER_HYP\14312.1003.160401-1800\amd64fre\bin\dbg\files\bin\winext\hvexts.dll

# TROUBLESHOOTING

## GET-VMHOSTPARTITIONABLEGPU

Call this command from PowerShell to see if there is a virtualized GPU. If the output is empty, there is an error somewhere (driver did not set the virtualization cap, virtualization is not enabled, etc.).

Example:
```
Name                    : \\?\PCI#VEN_10DE&DEV_1188&SUBSYS_095B10DE&REV_A1#6&cfd27c8&0&00400008#{064092b3-625e-43bf-9eb5-dc845897dd59}\PARAV
ValidPartitionCounts    : {32, 4}
PartitionCount          : 32
TotalVRAM               : 2000000
AvailableVRAM           : 1800000
MinPartitionVRAM        : 100000
MaxPartitionVRAM        : 1000000
OptimalPartitionVRAM    : 1000000
TotalEncode             : 20
AvailableEncode         : 20
MinPartitionEncode      : 1
MaxPartitionEncode      : 5
OptimalPartitionEncode  : 4
TotalDecode             : 40
AvailableDecode         : 30
MinPartitionDecode      : 2
MaxPartitionDecode      : 20
OptimalPartitionDecode  : 15
TotalCompute            : 100
AvailableCompute        : 100
MinPartitionCompute     : 1
MaxPartitionCompute     : 50
OptimalPartitionCompute : 30
CimSession              : CimSession: .
ComputerName            : WIN-T3H0LVHJJ59
IsDeleted               : False
```
## USING ETW EVENTS

- Dxgkrnl has Admin and Operational channels for ETW events. The events are shown in the Windows Event Viewer: Application and Services Log – Microsoft – Windows - Dxgkrnl
- Event Viewer has events from other components, which participate in the creation of a VM with GPU-PV (Hyper-V-Compute, Hyper-V-Worker, Hyper-V-VID, WDAG-Service, etc)

## USING ADD-VMGPUPARTITIONADAPTER
When using Add-VMGpuPartitionAdapter do not specify a capability (for example, decode) if it is not needed. Do not use 0 for this.

## USING REMOVE-VMGPUPARTITIONADAPTER

If VM fails to start or has rendering issues, try to remove the virtual GPU from the VM using the remove-VMGpuPartitionAdapter command in PowerShell. Example:
remove-VMGpuPartitionAdapter  -VMName $vm –AdapterId “Microsoft:9ABB95E2-D12D-43C3-B840-6F4A9CFB217B\929890BC-BB33-4687-BC1A-F72A4F1B3B3F”
6.4	PREVENT VM START DURING BOOT
set-vm -AutomaticStartAction Nothing -VmName TEST
6.5	MICROSOFT HYPER-V VIRTUAL PCI BUS DEVICE FAILS TO START
Take VPCI logs and send them to the Hyper-V team or DX team:
tracelog -start vpci -kd -level 8 -flag 0xfffffff -ls -guid #18d46045-3e20-45c8-9217-ca5aa507e1ec
Start a VM with GPUP assigned
tracelog -stop vpci
LogFile.etl will be produced.
Tracelog.exe is a tool, which comes with WDK.
A trace could also be taken using XPERF:
xperf can be used instead of tracelog.exe. Tracelog is included in Windows 8 DDK.
xperf -start vpci -on 18d46045-3e20-45c8-9217-ca5aa507e1ec:0xfffffff:8 -f vpci.etl
Start a VM with GPUP assigned
xperf -stop vpci
vpci.etl will be produced.

To see the trace output in the debugger, wmi tracing needs to be enabled:
!wmitrace.enable vpci 18d46045-3e20-45c8-9217-ca5aa507e1ec
To decode the trace, the corresponding TMF file needs to be in the WMITRACE search path
!wmitrace.searchpath [+] TMFPath
Or specify the TMF file:
 !wmitrace.tmffile 07306ff0-4926-341a-535c-abbf1f57b1ed.tmf
The TMF file could be produced by running the following command:
tracepdb.exe -i  vpcivsp.sys
tracepdb.exe -f  vpcivsp.pdb
TMF files can be found in the build:
\\winbuilds\release\RS_ONECORE_SIGMA_GRFX_DEV\...\amd64fre\symbols.pri\TraceFormat
6.6	EVENT VIEWER EVENTS
Events are added to the event viewer channel, which help to identify issues with vGPU startup.
The events are located in “Application and Services Logs\Microsoft\Windows\Dxgkrnl”.
The event channels are Admin and Operational.
Events are issued when:
- vGPU is created
- vGPU is destroyed
- The guest opens a virtual adapter
The event files are in
c:\Windows\System32\winevt\Logs\Microsoft-Windows-DxgKrnl-Admin.evtx
c:\Windows\System32\winevt\Logs\Microsoft-Windows-DxgKrnl-Operational.evtx
Check if a vGPU was created and any errors.

# REGISTRY SETTINGS
## GPUVIRTUALIZATIONFLAGS

DWORD HKLM\System\CurrentControlSet\Control\GraphicsDrivers\GpuVirtualizationFlags

This bit-field changes the behavior of paravirtualized GPUs.

### BIT 1 (0X1) FORCE SUPPORT FOR PARAVIRTUALIZED VIRTUAL GPUS

The bit 0x1 is used to force GPU paravirtualization support on drivers, which do not set the ParavirtualizationSupported cap. The bit is used in the host.

### BIT 3 (0X4) FORCE SECURE VIRTUAL MACHINE

The bit 0x4 enables secure virtual machine mode. This bit is used in the host. In this mode there are restriction on the user mode driver. For example, the driver cannot use Escape calls. They will fail.

### BIT 4 (0X8) PAIR VIRTUAL RENDER DEVICE WITH THE DISPLAY ONLY DRIVER

The bit 0x8 enables/disables pairing of the VRD in the guest with the display-only adapter). The bit needs to be set in the guest VM. Pairing is enabled by default.

## SETTING THE SIZE OF THE IO SPACE IN THE GUEST

The guest IO space is currently used to implement CPU visible allocations. A CPU visible allocation backing store in the host is pinned in memory and is mapped to the guest IO space. In the guest the allocation user mode virtual address is rotated to the IO space region. On some Haswell systems CPU has 36 bit physical address. Hyper-V on such system has limited IO space size. Dxgkrnl provides a way to specify the IO space size for a virtual GPU.

DWORD HKLM\System\CurrentControlSet\Control\GraphicsDrivers\Paravirtualization\GuestIoSpaceSizeInMb

Specifies the size of the guest IO space for virtual GPU in megabytes. The default value is 1000MB (1GB).

## DISABLE IOMMU ISOLATION FOR SECURE VIRTUAL MACHINES

If a driver doesn’t support IoMmu isolation, the following registry could be used during development to disable IoMmu isolation.
DWORD HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\IoMmuFlags = 8

## LIMIT THE NUMBER OF VIRTUAL FUNCTIONS

By default, the number of virtual functions, which are exposed by an adapter, which supports GPU paravirtualization, is equal to 32. This means that the adapter could be added to 32 virtual machines (assuming each VM has one adapter). The following registry allows to limit the number of exposed virtual functions. For example, if NumVirtualFunctions is set to 1, the adapter could be added to only one GPU one time. It is useful when a computer has multiple GPU adapters, which support GPU-PV, and the developer wants to assign each adapter to a VM. Note that Add-VMGpuPartitionAdapter does not allow to specify, which adapter to add. So if 2 adapters are added to a VM, both could get the same GPU-PV adapter from the host.

DWORD HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\NumVirtualFunctions

## WDDM 2.4 DDI
There are few changes required for the driver to be ready for GPU paravirtualization. They are described in this section.

## GPUPARAVIRTUALIZATIONSUPPORTED CAP

A new cap is added to DXGK_VIDMMCAPS – ParavirtualizationSupported. The host KMD needs to set the cap if all DDIs, described in this section, are implemented.

```
typedef struct _DXGK_VIDMMCAPS
{
    union
    {
        struct
        {
            UINT    OutOfOrderLock              : 1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN7)
            UINT    DedicatedPagingEngine       : 1; // _ADVSCH_
            UINT    PagingEngineCanSwizzle      : 1; // _ADVSCH_
            UINT    SectionBackedPrimary        : 1; // Create primaries using section without need for IO range
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
            UINT    CrossAdapterResource        : 1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
            UINT    VirtualAddressingSupported  : 1;
            UINT    GpuMmuSupported             : 1;
            UINT    IoMmuSupported              : 1;
            UINT    ReplicateGdiContent         : 1;
            UINT    NonCpuVisiblePrimary        : 1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
            UINT    ParavirtualizationSupported : 1;
            UINT    Reserved                    : 21;
#else
            UINT    Reserved                    : 22;
#endif // DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2
#else  // ! DXGKDDI_INTERFACE_VERSION_WDDM2_0
            UINT    Reserved                    : 27;
#endif // DXGKDDI_INTERFACE_VERSION_WDDM2_0
#else  // ! DXGKDDI_INTERFACE_VERSION_WDDM1_3
            UINT    Reserved                    : 28;
#endif // DXGKDDI_INTERFACE_VERSION_WDDM1_3
#else  // ! DXGKDDI_INTERFACE_VERSION_WIN7
            UINT    Reserved                    : 31;
#endif // DXGKDDI_INTERFACE_VERSION_WIN7
        };
        UINT        Value;
    };
    UINT            PagingNode;
} DXGK_VIDMMCAPS;
```
## DRIVER PRIVATE DATA PASSED THROUGH DDI

Various DDI used by a UMD exchange private information with the corresponding KMD. When the UND runs in the guest VM, the corresponding KMD DDI call will be done in the host partition. So
1.	The UMD cannot pass any pointers in the private data
2.	The UMD cannot pass any handles in the private data
3.	The UMD should not instruct the KMD to make global changes of the GPU state, as this could affect other running VMs.

## VIRTUALMACHINEPROCESS FLAG IN DXGARG_CREATEPROCESS

The operating system creates a worker process for each running virtual machine (called Virtual Machine Worker Process). Dxgkrnl creates the corresponding DXGPROCESS and calls DdiCreateProcess with VirtualMachineWorkerProcess flag set. There will be no rendering or driver resource creation in this process context. So the driver might skip allocating certain resources.

The OS creates a DXG process in the host for every process in a guest virtual machine, which uses GPU. Dxgkrnl calls DdiCreateProcess with the VirtualMachineProcess flag set. Note, that each Virtual Machine DXG process will belong to the same EPROCESS as the Virtual Machine Worker Process.
```
typedef struct _DXGK_CREATEPROCESSFLAGS
{
    union
    {
        struct
        {
            UINT    SystemProcess           : 1;
            UINT    GdiProcess              : 1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
            UINT    VirtualMachineProcess   : 1;
            UINT    VirtualMachineWorkerProcess   : 1;
            UINT    Reserved                : 28;
#else
            UINT    Reserved                : 30;
#endif // (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
        };
        UINT Value;
    };
} DXGK_CREATEPROCESSFLAGS;

1.	Flag that escape is from a containter in Escape.
2.	Change in DdiCreateProcess (process name, etc.)
 
8.4	DXGKDDIQUERYADAPTERINFO
typedef struct _DXGK_QUERYADAPTERINFOFLAGS
{
    union
    {
        struct
        {
            UINT    VirtualMachineData          : 1;    // 0x00000001
            UINT    SecureVirtualMachine        : 1;    // 0x00000002
            UINT    Reserved                    :30;    // 0xFFFFFFFC
        };
        UINT Value;
    };
 } DXGK_QUERYADAPTERINFOFLAGS;
}

typedef struct _DXGKARG_QUERYADAPTERINFO
{
    DXGK_QUERYADAPTERINFOTYPE   Type;
    VOID*                       pInputData;
    UINT                        InputDataSize;
    VOID*                       pOutputData;
    UINT                        OutputDataSize;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_4)
    HANDLE                      hKmdProcessHandle;      // in: driver process handle
#endif // (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_4)
} DXGKARG_QUERYADAPTERINFO;
```
**Flags.SecureVirtualMachine** - specifies that the virtual machine runs in the secure mode.
**Flags.VirtualMachineData** - set when the call comes from a virtual machine
**hKmdProcessHandle** – a handle, return by the KMD from DxgkDdiCreateProcess. The driver must check the value for NULL. Note, that hKmdProcessHandle is created when the first DXG device is created for the adapter and destroyed when the last adapter handle in the process is closed.

## DXGKDDIESCAPE
```
typedef struct _D3DDDI_ESCAPEFLAGS
{
    union
    {
        struct
        {
            UINT    HardwareAccess      : 1;    // 0x00000001
            UINT    DeviceStatusQuery   : 1;    // 0x00000002
            UINT    ChangeFrameLatency  : 1;    // 0x00000004
            UINT    NoAdapterSynchronization    : 1; // 0x00000008
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
            UINT    VirtualMachineData  : 1;    // 0x00000010
            UINT    Reserved            :27;    // 0xFFFFFFE0
#endif //  (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
        };
        UINT        Value;
    };
}

typedef struct _DXGKARG_ESCAPE
{
    HANDLE             hDevice;                // in: driver device handle
    D3DDDI_ESCAPEFLAGS Flags;                  // in: flags
    VOID*              pPrivateDriverData;     // in/out: escape data
    UINT               PrivateDriverDataSize;  // in: size of escape data
    HANDLE             hContext;               // in: driver context handle
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
    HANDLE             hKmdProcessHandle;      // in: driver process handle
#endif // (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
} DXGKARG_ESCAPE;
```
**hKmdProcessHandle** - driver handle, which is returned by the KMD from DxgkDdiCreateProcess. The driver must check the handle for NULL. The handle is create when the first DXG device is created for a process. The handle is destroyed when the last adapter handle is closed for a process.

**VirtualMachineData** - indicates that DxgkDdiEscape is called from a virtual machine.

## PHYSICAL ACCESS TO GPU ALLOCATIONS

Currently physical access to the allocations is not implemented. The driver must support GpuMmu.

## DXGKCBACQUIREHANDLEDATA, DXGKCBRELEASEHANDLEDATA

The calls on the host must be in the context of the same thread as the one, which called a DxgkDdi* function.

For example. Let’s assume that without virtualization the KMD calls DxgkCbAcquireHandleData in the context of the user mode thread, which calls DxgkEscape (which calls DxgkDdiEscape).

In case of paravirtualization, the UMD in the guest will call DxgkEscape and the KMD in the host will get the corresponding DxgkDdiEscape call. The KMD needs to call
DxgkCbAcquireHandleData in the context of this thread.

# WDDM 2.5 DDI

For WDDM 2.5, the following DDI changes are also required for paravirtualization support.

## SIGNALING GUEST EVENTS BY THE HOST KMD

There are scenarios, which already exist without virtualization, when the KMD needs to signal an event, which was created by an UMD. To handle such scenarios in case of paravirtualization, the KMD on the host needs to signal an event, which is created in the guest. A new driver callback (DxgkCbSignalEvent) is added for this purpose. Note, the callback can be used to signal events of the host processes as well.
```
typedef struct _DXGKARGCB_SIGNALEVENT
{
    HANDLE          hDxgkProcess;
    HANDLE          hEvent;
    union
    {
        struct
        {
            UINT Reserved       : 32;
        };
        UINT Flags;
    };
} DXGKARGCB_SIGNALEVENT;

typedef _In_    CONST DXGKARGCB_SIGNALEVENT *  IN_CONST_PDXGKARGCB_SIGNALEVENT;

typedef
    _Check_return_
    _Function_class_DXGK_(DXGKCB_SIGNALEVENT)
    _IRQL_requires_(PASSIVE_LEVEL)
NTSTATUS
(APIENTRY CALLBACK *DXGKCB_SIGNALEVENT)(IN_CONST_PDXGKARGCB_SIGNALEVENT);

typedef struct _DXGKRNL_INTERFACE {
   DXGKCB_SIGNALEVENT  DxgkCbSignalGuestEvent
} DXGKRNL_INTERFACE, *PDXGKRNL_INTERFACE;
```
**hDxgkProcess** Handle to the DXG process object, which is passed to DxgkDdiCreateProcess (DXGKARG_CREATEPROCESS::hDxgkProcess).

The driver must synchronize the callback with DxgkDdiDestroyProcess to ensure that the process is not destroyed during the callback.

**hEvent** User mode event handle, which needs to be signaled. The handle is valid in the context of the DXG process, identified by hDxgkProcess. The UMD in the guest could send the user mode event handle to KMD via Escape or other APIs, which allow private driver data.

**Reserved** Should be zero.

**IRQL**

Builds prior to Vibranium (6/21/2019)
-	< DISPATCH_LEVEL

Builds starting from Vibranium (6/21/2019)
-	<= DISPATCH_LEVEL when signaling events of a process in a virtual machine
-	< DISPATCH_LEVEL when signaling events of a local process

**Remarks**

In case of paravirtualization the callback does not signal the event synchronously, so the event is not signaled when the callback returns. Otherwise, the event is signaled synchronously.

## SUPPORT FOR DXGKACQUIREHANDLEDATACB, ETC.

Certain driver callbacks (DxgkCbAcquireHandleData, DxgkCbReleaseHandleData, DxgkCbGetHandleData, DxgkCbGetHandleParent) accept an Dxgkrnl allocation or resource handle passed by the KMD. The handle is usually passed to the KMD by UMD via D3DKMTEscape. When UMD is running in a virtual machine it knows only the guest allocation handles and cannot pass such handles to the KMD, because it is running in the host.

A new driver escape is added to translate the guest allocation/resource handle to the corresponding host handle. The escape is specified by setting the new flag D3DDDI_ESCAPEFLAGS::DriverKnownEscape.

When the DriverKnownEscape flag is set:
-	D3DKMT_ESCAPE::Type should be D3DKMT_ESCAPE_DRIVERPRIVATE
-	D3DKMT_ESCAPE::pPrivateDriverData should point to a known driver escape structure, defined below. Each structure starts with a D3DDDI_DRIVERESCAPETYPE value.
-	D3DKMT_ESCAPE::PrivateDriverDataSize should be se to the size of the structure, which depends on the particular escape type
-	D3DKMT_ESCAPE::hAdapter must be specified
-	D3DKMT_ESCAPE::Flags.HardwareAccess should be zero

When virtualization is not used, the translated handle is the same as the input handle.
```
typedef struct _D3DDDI_ESCAPEFLAGS
{
    union
    {
        struct
        {
            UINT    DriverKnownEscape : 1;    // 0x00000040   Driver private data is
        };
        UINT        Value;
    };
} D3DDDI_ESCAPEFLAGS;

typedef enum _D3DDDI_DRIVERESCAPETYPE
{
        D3DDDI_DRIVERESCAPETYPE_TRANSLATEALLOCATIONHANDLE = 0,
        D3DDDI_DRIVERESCAPETYPE_TRANSLATERESOURCEHANDLE = 1,
        D3DDDI_DRIVERESCAPETYPE_MAX = 2,
} D3DDDI_DRIVERESCAPETYPE;
```

### KNOWN DRIVER ESCAPES

The following known driver escapes are defined.

#### D3DDDI_DRIVERESCAPE_TRANSLATEALLOCATIONHANDLE
```
struct D3DDDI_DRIVERESCAPE_TRANSLATEALLOCATIONEHANDLE
{
     D3DDDI_DRIVERESCAPETYPE  EscapeType;
     D3DKMT_HANDLE            hAllocation
};
```
**EscapeType** [in] - D3DDDI_DRIVERESCAPETYPE_TRANSLATEALLOCATIONHANDLE

**hAllocation** [in] [out]
- [in]	A handle to DXG allocation, returned from DxgkCreateAllocation
- [out] A handle, which can be sent to the KMD and used in DxgkCbAcquireHandleData, DxgkCbReleaseHandleData, DxgkCbGetHandleData, DxgkCbGetHandleParent

#### D3DDDI_DRIVERESCAPE_TRANSLATERESOURCEHANDLE
```
struct D3DDDI_DRIVERESCAPE_TRANSLATERESOURCEHANDLE
{
     D3DDDI_DRIVERESCAPETYPE  EscapeType;
     D3DKMT_HANDLE            hResource;
};
```
**EscapeType** [in] - D3DDDI_DRIVERESCAPETYPE_TRANSLATERESOURCEHANDLE

**hAllocation** [in] [out]
- [in]	A handle to DXG resource, returned from DxgkCreateAllocation
- [out] A handle, which can be sent to the KMD and used in DxgkCbAcquireHandleData, DxgkCbReleaseHandleData, DxgCbEnumHandleChildren, DxgkCbGetHandleData.

### USAGE EXAMPLE
```
    D3DDDI_DRIVERESCAPE_TRANSLATEALLOCATIONEHANDLE Command = {};
    Command.EscapeType = D3DDDI_DRIVERESCAPETYPE_TRANSLATEALLOCATIONHANDLE;
    Command.hAllocation = hAlloc;
    D3DKMT_ESCAPE Args = {};
    Args.hAdapter = hAdapter;
    Args.Flags.DriverKnownEscape = TRUE;
    Args.Type = D3DKMT_ESCAPE_DRIVERPRIVATE;
    Args.pPrivateDriverData = &Command;
    Args.PrivateDriverDataSize = sizeof(Command);
    Status = D3DKMTEscape(&Args);
```

# 19H1 CHANGES
##	DXGK_ALLOCATIONINFOFLAGS::ACCESSEDPHYSICALLY

Prior to 19H1 the DXGK_ALLOCATIONINFOFLAGS::AccessedPhysically flag was not allowed to be used by the drive in a virtual machine. Allocation creation with this flag would fail.
Starting from 19H1 (DXGKDDI_INTERFACE_VERSION_WDDM2_6) the driver can use the flag in a virtual machine.

## DXGKUPDATEALLOCATIONPROPERTY
Starting from 19H1 (DXGKDDI_INTERFACE_VERSION_WDDM2_6), DxgkUpdateAllocationProperty can be used by UMD in a virtual machine. Prior to this this call would fail.

# VIBRANIUM CHANGES

## IMPROVE THE DEFINITION OF NEWER FOR COPYTOSYSTEM32WHENNEWER

New Non-DX runtimes and loaders have been enlightened to support GPU paravirtualization, and the OS behavior must be changed to better prefer those binaries. Files listed under the CopyToVmWhenNewer and CopyToVmWhenNewerWow64 graphics adapter registry sub-keys only overwrite the destination files when they satisfy the "newer" criteria. Previously, the "newer" criteria only compared the files' ChangeTime.

In Vibranium the "newer" criteria compares two pieces of information:
- FileVersion
- LastWriteTime

When the destination file ends with the .dll or .exe suffix, the FileVersion is used as the most-significant comparison value where the greatest version is deemed "newer". When the destination file doesn't end with the .dll nor .exe suffix OR the two FileVersion are equal, then LastWriteTime is used as the least-significant comparison values where the later date/ time is deemed "newer".

# ENCODER MFT SUPPORT (VIBRANUIM)
## OVERVIEW

Video encode engines on the GPU are fully virtualized and accessible to the vGPU within a GPU para-virtualized environment. However today, there currently is no DirectX API that exposes video encode. Video encode functionality is instead implemented by IHV’s proprietary APIs or through a Media Foundation plugin called Media Foundation Transform. These two components communicate with the IHV’s DirectX11 UMD or with WDDM services to expose the GPU encode engine. See image below for diagram describing this system.

In a container with a vGPU, video encoding is not supported currently. For the Vibranium release, we will support hardware accelerated encoding on a vGPU by leveraging IHV’s MFTs.
To support video encode inside a container, the MFT needs to be registered so that it can be seen by COM and MF. COM needs to have the driver COM objects visible, so that calls to CoCreateInstance succeed. In addition, MF needs some global MF specific registry keys to register the MFT and to determine what functionality the MFT has and what UUID to instantiate for the MFT COM object. These are currently registered in the global space under HKLM\SOFTWARE\ when the driver is installed. These registry keys aren’t available within the container however as there is no PnP or servicing mechanic for creating these keys. Additionally, the current registry key location is read-only as defined by driver package isolation. Registry keys cannot be created globally under HKLM\SOFTWARE\ or HKLM\SYSTEM\ per driver package isolation. However, by defining a new location for these registry keys and by reflecting the keys into the container on vGPU initialization, video encode can be supported within a container.

## COM OBJECT AND MFT REGISTRATION OF HW MFTS

Rather than registering the driver COM object globally, the driver COM object will now be registered under the device key. This allows MFT COM registration from within the container and prevents global registry keys being created, thus preserving driver package isolation. MFTs will now be registered under the device key as well for similar reasons.

### CHANGES TO DRIVER INF
Upon device driver installation, the INF must now make all COM object and MFT registrations under the device key. MFT and COM registrations must change as seen below:

#### MFT REGISTRATIONS:

Before	After
INF AddReg:

HKCR,MediaFoundation\Transforms\{clsid}\...	Per-Instance device software INF AddReg:

HKR,MediaFoundation\Transforms\{clsid}\...
Registry Location:

HKLM\SOFTWARE\Classes\MediaFoundation\Transforms\{clsid}\...	Registry Locations (AdapterKey location is subject to change):

AdapterKey\MediaFoundation\Transforms\{clsid}\...

#### COM REGISTRATIONS:

Before	After
INF AddReg:

HKLM,Software\Classes\CLSID\{clsid}\...
HKCR,CLSID\{clsid}\...
HKCR,Wow6432Node\CLSID\{clsid}\...
HKCR,WowAA32Node\CLSID\{clsid}\...	Per-Instance device software INF AddReg:

HKR,Classes\CLSID\{clsid}\...
HKR,Classes\CLSID\{clsid}\...
HKR,Classes\Wow6432Node\CLSID\{clsid}\...
HKR,Classes\WowAA32Node\CLSID\{clsid}\...

HKLM\SOFTWARE\Classes\CLSID\{clsid}\...
HKLM\SOFTWARE\Classes\Wow6432Node\CLSID\{clsid}\...
HKLM\SOFTWARE\Classes\WowAA32Node\CLSID\{clsid}\...	(AdapterKey location is subject to change)

AdapterKey\Classes\...

The INF syntax for differentiating based on OS version can be found on MSDN here . Starting in Vibranium, the INF must conform to these new registry keys. Older OS versions will still use the traditional registry keys for compatibility. The INF must setup these registry keys in the old location on older OS builds and create the new keys in their new location for newer OS builds. For example, for an MFT registration on an old build the INF will create the key under:
HKLM\SOFTWARE\Classes\MediaFoundation\Transforms\{clsid}\

For an MFT registration on a new WCOS build, the INF will create the key under:
HKLM\DEVICES\CurrentControlSet\Enum\<device instance>\Driver Parameters\MediaFoundation\Transforms\{clsid}\

A syntax example of targeting different OS versions can be seen below:
```
[Manufacturer]
%Msft% = Msft, nt.10.0...18500

; -------------- ;
; Models Section ;
; -------------- ;

; Targets old builds
[Msft]

; INF work for older build here


; Windows 10 build with build number equal to or greater than 18500
[msft.nt.10.0...18500]

; INF work for newer build here
```
More information and other examples can be found at MSDN.

### ONLY IN-PROCESS COM OBJECTS

Only in-process COM objects will be supported for projection into a Container/VM and the driver must limit itself to this type of COM object only. This rule will be enforced through new INFVERIF rules that check that only in-process COM objects are registered.
12.2.3	NEW API FOR IN-PROCESS COM DATABASE ADDITIONS

A new API, consumed by the Media stack, will be provided to add a device COM object registration keys.

#### IN PROCESS COM OBJECT INSTANTIATION

The new API will add the device registry key to the list of registry keys COM searches through when instantiating a new COM object. This will only apply to the current process, thus enabling in process COM object instantiation. Similarly, the API will allow removal of registration entries. The registration and removal is reference counted to allow multiple components to use any particular COM object.

### MEDIA FOUNDATION INITIALIZATION AND CLEANUP
Media Foundation has been updated to enumerate all GPUs exposing MFTs and use the new COM API to register the corresponding COM objects for the current process.

#### INITIALIZATION

On initialization, MF enumerates all the GPUs and registers their COM objects with COM. In addition, when a new GPU is added to the system, MF registers the associated driver with COM before using the new GPU. MF also ensures that the registration is always done within the process hosting the MFT.

#### CLEANUP

When MF is finished or there is no longer a valid GPU, it unregisters the driver from the COM database.

### REGISTRY KEY REFLECTION INTO CONTAINER

In a container, dxgkrnl.sys will now reflect device-specific registry keys from the host into the container for MF and COM registration.

#### VGPU INITIALIZATION

On initialization of a vGPU within a paravirtualized environment, dxgkrnl.sys checks with the host dxgkrnl.sys for any COM object registrations that exist for the device. If there are any registrations present, they will be reflected in the container for the VRD. The filepath to the COM object will be updated as well to reflect the actual location from the container’s point of view.

Following these changes, MF will now be able to discover the MFT registered on the host and load them inside of the guest environment. The MFT needs to be updated to ensure that any communication between the MFT and the KMD through private driver data follow the paravirtualization constraints. Refer to the GPU paravirtualization spec for more information.

#### VGPU DESTRUCTION

When the vGPU is destroyed, the MFT and COM registration registry keys are deleted on the guest as part of cleanup. As a result, MF will no longer be able to discover the MFT registered on the host.

#### STAGING SUPPORT FOR MFT

The changes documented here will appear later in Vibranium, but IHVs are strongly encouraged to begin testing their MFT within a VM environment manually by registering the MFT inside of the VM. This can be done by manually creating the registry keys that would normally be setup by the INF inside of the VM at the old, global, location. MF will be able to properly find the MFT this way.

### VALIDATION OF MFT FUNCTIONALITY

Sigma/GRFX will work with and assist our IHV partners to ensure that their MFT runs within a container. Video encode within a container is a critical deliverable for allowing applications, such as Teams, to run effectively and is an important target for Vibranium.

# WSA (WINDOWS SUBSYSTEM FOR ANDROID)

This document is intended to describe GPU driver changes, required to support GPU-PV
(GPU paravirtualization) in WSA (Windows Subsystem for Android).

## Overview

Driver support for GPU-PV in WSA is similar to WSL2, but there are changes in how
the UMD (User Mode Driver) binaries are packaged and how the UMD names are defined.

In WSL2 (Windows Subsystem for Linux) the full host DriverStore directory is mapped to the virtual machine. This is not possible in WSA for security reasons. The driver user mode WSA binaries need to be packaged in a ext4 image file.

WSA UMDs are compiled using the Android NDK (Native Development Kit), so they are separate
from the WSL2 binaries. The driver INF file needs to define the UMD names for WSA.

The WSA virtual machine is "secure" unless one of the following conditions:

- DWORD HKLM\Software\Microsoft\WSA\DeveloperModeEnabled is 1
- the WSA package is debug and HKLM\Software\Microsoft\WSA\DeveloperModeEnabled is not present

## Building the driver

Similar to [building for WSL](../d3d/Linux.md), building this driver will produce an ELF shared object (.so) file. Differences to building for Linux:

### Cross-compiling using the NDK

This will be a cross-compile. Linux drivers could be built either inside Linux, or as a cross-compile, but you can't build these binaries inside Android. You can use either Windows or Linux as your build machine.

The compiler toolchain should be the version of Clang included in the NDK. If you're building with CMake, we suggest using the instructions from https://developer.android.com/ndk/guides/cmake. If you're not, the instructions from https://developer.android.com/ndk/guides/other_build_systems are also helpful.

Important details to be aware of:
* Please target platform level 30 (at this time).
* Ensure that all driver code is built with `-fPIC`. Building without this will produce `TEXTREL` (text relocations), which is not supported in modern Android, as it involves patching the executable text segment.

#### Building in an AOSP build environment

It is theoretically possible to build inside of an Android 11 AOSP source tree using Android.bp/mk build system. Ensure that the binary produced this way is configured to build as a vendor binary. This is not our expected path, so we are not providing in-depth documentation on how to do it.

### Building for 32-bit

Unlike Linux/WSL, we will need 32-bit binaries. Our latest WDK drops (and https://github.com/microsoft/libdxg) include updated d3dkmthk.h and d3dukmdt.h headers with 32-bit support. Notably, unlike Windows, we do not have a 32->64 bit thunking layer which translates our structures. Instead, the 32-bit userspace is expected to fill out the structure in a way that the 64-bit kernel can read it.

The biggest problem with the i686 (x86) ABI for Linux/Android is that unlike Windows (x86 and x64) and Linux x86_64, the Linux i686 ABI does not have 8-byte alignment. If you're using a `uint64_t` or `double`, these will be 4-byte aligned. If you have these in a structure, when that structure is interpreted in the x64 kernel, there may be padding that is not present in the x86 usermode.

The second problem to be aware of (which your drivers should already handle) is pointers and variable-sized integers like `size_t`.

We've updated our standard structures in our headers to address these cases and produce fixed-size structures. The 8-byte alignment is addressed using C11/C++11 `alignas` declarations. The pointers are addressed by unioning them with a 64-bit value - this is done so that the high bits of the pointer can be written as zero. If you are using brace initialization to fill out a D3DKMT_* structure, you'll need to use `D3DKMT_PTR_INIT` to cast it to `uint64_t`.

Please audit your driver private data for alignment issues for 32-bit usermode drivers.

### Layered drivers

If your driver contains multiple .so files, loading dependent files should be done using paths that are relative to the lib or lib64 directory of the image that contains your driver binaries (see below). The driver will be loaded into the SPHAL namespace which puts the appropriate directory in the search path for loading binaries.

## Preparing a WSA driver package

The WSA driver package is an image file having the ext4 format. There could be arbitrary
directory structure inside the ext4 file system.

The image file could be made by the following steps:
```
# create a 32M initial  file
truncate -s 32M my.img
# format he file as ext4 with 4K block size, which is needed for DAX (direct memory access)
mkfs.ext4 -b 4096 my.img
# create a directory for mounting
mkdir ~/mnt_img
# mount the image as loop device
sudo mount -oloop my.img ~/mnt_img
# make lib and lib64 directories
mkdir ~/mnt_img/lib64
mkdir ~/mnt_img/lib
# copy files to the image
cp <all WSA 64bit user mode driver files> ~/mnt_img/lib64
cp <all WSA 32bit user mode driver files> ~/mnt_img/lib
# add selinux attributes
# for each directory **including the root of the image (~/mnt_img)**:
sudo setfattr -n security.selinux -v u:object_r:vendor_file:s0 ~/mnt_img[/dir_name]
# for each file:
sudo setfattr -n security.selinux -v u:object_r:same_process_hal_file:s0 ~/mnt_imt/[file_name]
# unmount the image
sudo umount ~/mnt_img/

# the following steps to resize the image are optional.
# check the image for errors and fix them
e2fsck -y -f my.img
# resize the image
resize2fs -M my.img
```

The image file will be mounted to the WSA virtual machine at a mount point. For example,
/odm. libdxgcore and libdxg will translate the UMD driver name using the appropriate root.

## Specifying the WSA UMD image file name and UMD names in the INF file

The driver INF file needs to specify names of the
- WSA UMD image file (UserModeDriverWsaImage)
- WSA 32 bit UMD (UserModeDriverNameWsa32)
- WSA 64 bit UMD (UserModeDriverNameWsa64)

The WSA UMD image file must be specified relative to the DriverStore.
The entry type is REG_SZ.

```
HKR,,UserModeDriverWsaImage,%REG_SZ%,"%13%\softgpuwsa.img"
```

WSA UMDs are separate for 32 and 64 bit processes. File paths should be relative to the lib and lib64 subdirectories.
The entry type is REG_MULTI_SZ. Only the first string is currently used.

```
HKR,,UserModeDriverNameWsa32,%REG_MULTI_SZ%,"softgpuumd32.so"
HKR,,UserModeDriverNameWsa64,%REG_MULTI_SZ%,"softgpuumd64.so"
```
