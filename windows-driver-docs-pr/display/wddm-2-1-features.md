---
title: WDDM 2.1 Features
description: This section provides details about features and enhancements in Windows Display Driver Model (WDDM) version 2.1.
ms.date: 08/10/2021
---

# WDDM 2.1 Features

This topic provides details about features and enhancements in Windows Display Driver Model (WDDM) version 2.1, which is available starting with the Windows 10 Anniversary Edition (Windows 10, version 1607).

WDDM 2.1 itself is optional. If implemented, it is a collection of mandatory and optional driver capabilities. A driver that supports any of these capabilities must support all of the mandatory ones. Support can be validated by Windows Hardware Lab Kit (HLK) tests, but *Dxgkrnl* checks for consistency in the capabilities and DDIs.

## WDDM 2.1 Requirements Table

| Feature | Applicability |
| ------- | ------------- |
| Offer and reclaim improvements                              | Mandatory |
| Video memory management                                     | Optional |
| HW protected content reliability improvements               | Select Hardware |
| Application support with Windows GameDVR                    | Mandatory |
| Indirect display                                            | Select Hardware |
| Driver store and side-by-side installation                  | Mandatory |
| DirectX memory surface sharing for camera/capture scenarios | Mandatory|

WDDM 2.1 supports the following D3D versions: D3D9, D3D10, D3D10.1, D3D11, D3D11.x, D3D12

## Offer and reclaim improvements

The [PFND3DDDI_RECLAIMALLOCATIONS3CB](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_reclaimallocations3cb) callback function was added to reduce memory footprint of applications running in background mode. This interface enables applications to offer resources that are acceptable to fully de-commit, when going into the background. As a result, the Process Lifetime Manager is able to reclaim more memory from background apps that use DirectX, which leads to less background application terminations when under memory pressure.

Other DDI changes:

* [PFND3DDDI_UPDATEALLOCATIONPROPERTYCB callback](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_updateallocationpropertycb)
* [PFND3DDDI_OFFERALLOCATIONS2CB callback](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_offerallocations2cb)
* [D3DDDICB_OFFERALLOCATIONS2 structure](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-d3dddicb_offerallocations2)
* [D3DDDICB_RECLAIMALLOCATIONS3 structure](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddicb_reclaimallocations3)

For more information about offer and reclaim resources, see [Offer and reclaim changes](offer-and-reclaim-changes.md).

## Application support with Windows GameDVR

Windows 10 Anniversary edition includes improved ability to use the Windows game bar and GameDVR with full screen games.

WDDM 2.1 drivers are required to support a performance feature called *present batching*, which adds multi-threading support for flip model swapchains. This is an essential feature that ensures that full screen games with game bar run at the same level of performance as on earlier versions of Windows.

The following DDIs were added to enable this feature:

* [PFND3DDDI_SYNCTOKENCB callback](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_synctokencb)
* [D3DDDIARG_SYNCTOKEN structure](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_synctoken)
* [PFND3DDDI_SYNCTOKEN callback](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_synctoken)

## Indirect Display

In WDDM 2.1, Indirect Display enables USB-connected displays to participate in all the same user experiences as any other monitor. In addition, an Indirect Display driver (IDD) is a user-mode driver, which is simpler to develop than a kernel mode driver, and as a result contributes to increased overall system reliability.

In WDDM 2.1, the following USB display features/experiences are enabled:

* When connecting a USB display to a Windows platform or upgrading operating systems, the proper drivers will be downloaded and installed from Windows update.

* Connecting monitors to USB display hardware will detect and set the correct monitor topology, resolution and DPI.

* Users can change monitor resolution and scaling on the monitor.

* Users can disconnect USB displays and reconnect displays without unexpected side effects.

* Monitor topology is retained through disconnect and reconnect to the same monitor.

* USB displays functions properly in various power states including sleep and hibernation.

For more information about indirect display, see [Indirect Display Driver Model Overview](indirect-display-driver-model-overview.md)

## Driver Store and Side-by-Side driver installation

WDDM 2.1 introduces installation of graphics drivers through the *driver store*. This mechanism of installing graphics drivers improves the resiliency of driver updates from Windows Update, eliminating driver file version mismatches resulting in system instabilities and user initiated reboots. Each subsequent driver update will be run directly from its unique location in the driver store (i.e. `System32\DriverStore\FileRepository\[…]`), thus avoiding driver file overwrites and mismatches.

Feature implementation of driver store requires changes to the graphics driver INF file in order to ensure that the driver files get copied to the unique driver repository. The INF changes are explained in more details in [INF Requirements](#graphics-inf-requirements).

## DXIL

WDDM 2.1 introduces the transition of the GPU shader compiler stack from DirectX Byte Code (DXBC) to DirectX Intermediate Language (DXIL), a newer format for transmitting shader instructions to the GPU. Transition to DXIL delivers the following benefits to developers:

* Programmability - Ease-of-development is improved and complexity of the shader creation process is reduced for developers by minimizing differences between GPU programming syntax and CPU languages that developers are familiar with.

* Higher-performance compiler:

  * *Runtime Shader Performance* is enabled to deliver improved performance.
  * DXIL provides a set of intrinsic that enables sharing of data across the lanes of the SIMD processors in GPUs.

* Workflow Flexibility - DXIL enables developers to be in control of their own custom tools and optimization passes and choose which compilation steps are applied at build time versus runtime.

* Advanced Language Features - An evolved language provides key features that eliminate differences between GPU code and CPU code, and flatten the learning curve for GPU programmers.

With these features focusing on providing benefits for developers, end users will see the benefits in improved performance of new or updated games even when run on existing hardware.

## DirectX Memory Surface Sharing for Camera/Capture Scenarios

In WDDM 2.1, a frame server component was introduced to share a camera or capture device across multiple processes concurrently. This enables saving of captured frames to one memory location where multiple applications can read from, as opposed to copying the image data between processes and co-processes multiple times. This feature provides more efficient management of captured pictures across multiple processes, power savings, bandwidth reduction and latency reduction for WDDM 2.1-compliant hardware and drivers which results in performance gains for applications and users.

The frame server allocates a captured image as cross-process shareable memory, and shares this memory out to processes requesting access. Since the frame server broadcasts the texture to multiple client processes, the texture must support concurrent reading. Currently NV12 textures are supported for this purpose.

## Pipeline State Object (PSO) Caching and Library

Introduced in D3D12, Pipeline State Object (PSO) is an interface that represents the graphics pipeline instructions and resources (aka state) as a unified object to reduce mismatch between D3D and driver decompositions of the state. Running graphically demanding applications and games requires creating a vast number of PSOs.

WDDM 2.1 PSO library and caching enables the gaming applications to store a PSO on physical storage after being created during the initial run. This allows the D3D runtime to retrieve the pre-created PSOs from the library in future instances, thus reducing the PSO extraction time. For example, when running a game after the first time or after rebooting the PC, content will be loaded from the physical library as saved PSOs.

## Start of Pipeline GPU Timestamps

In WDDM 2.1, the capability to retrieve start of graphics events’ timestamps in the GPU pipeline was introduced. This feature, used in conjunction with the end of pipeline timestamps, provides developers with a clear and fine-grained visualization of the parallelization, pipelining, and timing of their application’s activities occurring on the GPU. Provided with the execution time of each event, developers can further optimize their code and investigate inefficiencies and other performance issues.

This feature contributes to enabling ‘real-time, low overhead’ GPU performance data gathering and at the same time, provides enough information to visualize and measure workloads on GPUs. The goal of the feature is to provide enough information to reconstruct the exact order and duration of operations executed by the GPU, so that tools can visualize parallelism and pipelining with an engine, measure GPU workloads, and identify potential synchronization issues.

## Viewing GPU Microcode

WDDM 2.1 enables developers to further optimize their shaders by presenting GPU microcode viewing. Developers program the graphics pipeline by creating shaders in high-level shader language (HLSL), which are then compiled to an intermediate language for the GPU driver. The driver runs additional compilations and optimizations to convert this code to GPU-specific instructions which remained opaque to the developers. With this feature, developers are presented readable GPU-specific code to evaluate the extent of their shader optimization and speed.

This feature enables the user-mode driver (UMD) to comment on each programmable stage of the graphics pipeline (shaders) and return actionable information on the programmer’s use or misuse of those shaders. The GPU-specific microcode is disassembled and presented in readable string format along with the UMD comments. Developers can view their HLSL code mapping to readable GPU code side by side which enables them to dynamically modify their code and see the compiler optimization results on the GPU code side.

## Determining WDDM Version

### WDDM 2.1 Caps

Drivers report WDDM 2.1 support through [DXGK_DRIVERCAPS::WDDMVersion](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps) with the version constant:

`DXGK_WDDMVERSION::DXGKDDI_WDDMv2_1 = 0x2100`

*Dxgkrnl* does not use the **WDDMVersion** cap as a way to determine which features are supported; that task is left to other caps or DDI presence. However, if the driver reports WDDM 2.1 support through the **WDDMVersion** cap, *Dxgkrnl* does validate that the caps or DDIs required by WDDM 2.1 are present and fail to create the adapter if they are not. Inconsistent caps result in failure to create adapter or segment.

> [!NOTE]
> Applications, existing or newer, must not have to query the driver model to take advantage of any Windows 10 Anniversary Edition features which are enabled through platform improvements such as the ones outlined here. Any capability changes must be surfaced through the respective runtime.

The following constant was added to match KMT_DRIVERVERSION_WDDM_2_1:

```cpp
typedef enum _DXGIDRIVERMODELVERSION
{
    DXGIDMVERSION_1_0            = 1000,
    DXGIDMVERSION_1_1_PRERELEASE = 1102,
    DXGIDMVERSION_1_1            = 1105, 
    DXGIDMVERSION_1_2            = 1200,
    DXGIDMVERSION_1_3            = 1300,
    DXGIDMVERSION_2_0            = 2000,
    DXGIDMVERSION_2_1            = 2100,

} DXGIDRIVERMODELVERSION;
```

DDI interface versions in the kernel-mode driver (KMD) are as follows:

```cpp
#define DXGKDDI_INTERFACE_VERSION_VISTA      0x1052
#define DXGKDDI_INTERFACE_VERSION_VISTA_SP1  0x1053
#define DXGKDDI_INTERFACE_VERSION_WIN7       0x2005
#define DXGKDDI_INTERFACE_VERSION_WIN8       0x300E
#define DXGKDDI_INTERFACE_VERSION_WDDM1_3    0x4002
#define DXGKDDI_INTERFACE_VERSION_WDDM1_3_PATH_INDEPENDENT_ROTATION  0x4003
#define DXGKDDI_INTERFACE_VERSION_WDDM2_0    0x5023
#define DXGKDDI_INTERFACE_VERSION_WDDM2_1    0x6002
```

## Graphics INF Requirements

WDDM 2.1 graphics drivers have different INF requirements as compared to the WDDM 2.0 or previous drivers. These are:

1. WDDM 2.1 must have an identical Feature Score as that of the WDDM 2.0 graphics driver (D1).

2. WDDM 2.1 graphics drivers must use a different OS INF install section.

3. WDDM 2.1 graphics driver INF changes for “Driver Store" installation.

For more info, see [INF File Sections and Directives](../install/index.md).

Driver files, 32 and 64 bit, will remain in and be loaded from the driver store. WoW64 file system redirection does not apply to the driver store. IHVs can specify subfolders by using standard INF syntax to create, for example, a WoW64 folder under the unique driver store folder if desired.

The following is an example of how an INF supporting run from driver store differs from previous behavior.

```inf
WINDOWS 10 ANNIVERSARY EDITION APPROACH: RUNNING DRIVERS FROM THE DRIVER STORE
[DestinationDirs]
KMDCopyFiles = 13
UMDCopyFiles = 13
UMDWoW64CopyFiles = 13

[DDInstall]
CopyFiles=KMDCopyFiles
CopyFiles=UMDCopyFiles
CopyFiles=UMDWoW64CopyFile

[KMDCopyFiles]
myKMD.sys

[UMDCopyFiles]
myUMD64.dll
myOpenCL64.dll
myOpenGL64.dll

[UMDWow64CopyFiles]
myUMD32.dll
myOpenCL32.dll
myOpenGL32.dll

[DDInstall.Services]
AddService = serviceName, 0x00000002, serviceName_Service_Inst

[serviceName_Service_Inst]
ServiceBinary = %13%\serviceName.sys

[regAdd]
HKR,,UserModeDriverName,%REG_MULTI_SZ%,%13%\myUMD64.dll, %13%\myUMD64.dll, %13%\myUMD64.dll, %13%\myUMD64.dll
HKR,,UserModeDriverNameWoW,%REG_MULTI_SZ%, %13%\myUMD32.dll, %13%\myUMD32.dll, %13%\myUMD32.dll, %13%\myUMD32.dll
HKLM,"Software\Khronos\OpenCL\Vendors",%13%\myOpenCL64.dll,%REG_DWORD%,0x00000000
HKLM,"Software\Wow6432Node\Khronos\OpenCL\Vendors",%13%\ myOpenCL32.dll,%REG_DWORD%,0x00000000
HKR,,OpenGLDriverName,%REG_MULTI_SZ%,%13%\myOpenGL64.dll
HKR,,OpenGLDriverNameWoW,%REG_MULTI_SZ%,%13%\myOpenGL32.dll
```

To specify a subfolder, drivers may use syntax as shown in the following example:

```inf
...
[DestinationDirs]
...
UMDWoW64CopyFiles = 13,WoW64
...
[regAdd]
...
HRK,, UserModeDriverNameWoW,%REG_MULTI_SZ%, %13%\WoW64\myUMD.dll, %13%\WoW64\myUMD.dll, %13%\

The manufacturer install section decoration for Windows 10 Anniversary edition WDDM 2.1 drivers is as follows: 
...
[Manufacturer]
%Grfx_Manf% =  IHVGfx, NTamd64.10.0…14310
...
[IHVGfx.NTamd64.10.0…14310]
; HW ID list
[list of HW IDs]
```

## Driver Versioning

The driver DLL and SYS files for a graphics adapter or chip set must have a properly formatted file version.

The driver information file (.inf), kernel mode driver (.sys), and user mode driver (.dll) file version info must match. In addition, version info for any files identified in the `[SignatureAttributes]` section of the .inf as PETrust binaries must match the .inf. It is recommended that file version info for additional binaries in a driver package match the .inf.

To be consistent with the prevailing file versioning requirements for legacy operating systems, file version formatting must follow an `AA.BB.CCCCC.DDDDD` pattern where:

* AA indicates the driver model version of the most capable device listed in the .inf

* BB (for WDDM 1.2 drivers and higher) indicates the highest available D3D Feature Level of the most capable device listed in the .inf
* BB (for WDDM 1.1 drivers and lower) indicates the highest available DDI version supported by the most capable device listed in the .inf
* CCCCC is a number up to 5 digits from 0 to 65535 chosen by the vendor
* DDDDD is a number up to 5 digits from 0 to 65535 chosen by the vendor

Values for AA field:

|Driver Model | AA value |
| ----------- | -------- |
|WDDM v2.1    |21        |
|WDDM v2.0    |20        |
|WDDM v1.3    |10        |
|WDDM v1.2    |9         |
|WDDM v1.1    |8         |
|WDDM v1.0    |7         |
|XDDM         |6         |

Values for BB field (WDDM 1.2 and later):

|DirectX Feature Level|BB value|
|---------------------|--------|
| 12_x | 21 |
| 12_1 | 20 |
| 12_0 | 19 |
| 11_1 | 18 |
| 11_0 | 17 |
| 10_1 | 16 |
| 10_0 | 15 |
| 9_3  | 14 |
| 9_2  | 14 |
| 9_1  | 14 |

Values for BB field (WDDM 1.1 and earlier):

|DDI version|BB value|
|-----------|--------|
| D3D11-DDI on Feature Level 11_0 | 17 |
| D3D11-DDI on Feature Level 10   | 16 |
| D3D10-DDI                       | 15 |
| D3D9 DDI                        | 14 |

### Examples

> [!NOTE]
> There is no requirement to pad numbers with leading zeros, i.e. 123 does not need to be represented as 00123 for the CCCCC or DDDDD fields. In previous versions of the Windows OS the last two fields were 4 digits, i.e. CCCC.DDDD. Therefore, the examples for driver versions prior to Windows 10 and WDDM 2.0 only have 4 digits.

* Windows Vista WDDM 1.0:

  * D3D9 DDI drivers can use 7.14.0000.0000 to 7.14.9999.9999
  * D3D10 DDI drivers can use 7.15.0000.0000 to 7.15.9999.9999

* Windows 7 WDDM 1.1:

  * D3D9 DDI drivers can use 8.14.0000.0000 to 8.14.9999.9999
  * D3D10 DDI drivers can use 8.15.0000.0000 to 8.15.9999.9999
  * D3D11 DDI with FL_10_0 drivers can use 8.16.0000.0000 to 8.16.9999.9999
  * D3D11 DDI with FL_11_0 drivers can use 8.17.0000.0000 to 8.17.9999.9999

* Windows 8 WDDM 1.2:

  * FL_10_0 HW can use 9.15.0000.0000 to 9.15.9999.9999
  * FL_10_1 HW can use 9.16.0000.0000 to 9.16.9999.9999
  * FL_11_0 HW can use 9.17.0000.0000 to 9.17.9999.9999
  * FL_11_1 HW can use 9.18.0000.0000 to 9.18.9999.9999

* Windows 8.1 WDDM 1.3:

  * FL_10_0 HW can use 10.15.0000.0000 to 10.15.9999.9999
  * FL_10_1 HW can use 10.16.0000.0000 to 10.16.9999.9999
  * FL_11_0 HW can use 10.17.0000.0000 to 10.17.9999.9999
  * FL_11_1 HW can use 10.18.0000.0000 to 10.18.9999.9999

* Windows 10 WDDM 2.0:

  * FL_11_1 HW can use 20.18.0000.0000 to 20.18.65535.65535
  * FL_12_0 HW can use 20.19.0000.0000 to 20.19.65535.65535
  * FL_12_1 HW can use 20.20.0000.0000 to 20.20.65535.65535

* Windows 10 WDDM 2.1:

  * FL_11_1 HW can use 20.18.0000.0000 to 21.18.65535.65535
  * FL_12_0 HW can use 20.19.0000.0000 to 21.19.65535.65535
  * FL_12_1 HW can use 20.20.0000.0000 to 21.20.65535.65535

### Enforcement

A mandatory test in the HLK certification playlist for Windows 10 builds higher than 10586 enforces the rules above. The test is optional for older OS versions. For Windows 10 builds after 10586 the WDDM version has been updated to 2.1. Another way to view this is that the mandatory requirement only applies to drivers that are built for WDDM 2.1 or higher.
