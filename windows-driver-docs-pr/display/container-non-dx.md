---
title: Container support for non-DX APIs
description: Non-DX APIs must interact with drivers and kernel more directly, so they are exposed to more complications
ms.date: 05/07/2019
ms.localizationpriority: medium
---

# Container support for non-DX APIs

Windows 10 added features that significantly impact non-DX APIs and the lower-level WDDM architectural details they rely on:

1. Paravirtualized WDDM adapters
2. Users now have control over the adapter used by applications that don't discriminate themselves
3. [Universal drivers](../develop/getting-started-with-windows-drivers.md) introduces a new set of design principals

Maintaining compatibility with the latest Windows 10 features requires the modifications described in the sections below.

## Driver INF modifications

The driver must register non-DX runtimes into the appropriate registry locations to install their binaries
into the system32 and syswow64 subdirectories of the Windows installation.
In the installation INF, the driver can define multiple values in the following sub-keys of the graphics adapter registry key:

- CopyToVmOverwrite
- CopyToVmWhenNewer
- CopyToVmOverwriteWow64
- CopyToVmWhenNewerWow64

The former sub-keys modify the system32 directory, while the latter sub-keys modify the syswow64 directory.
Each value type under a subkey must be REG_MULTI_SZ or REG_SZ.
If the value type is REG_MULTI_SZ, there must be maximum 2 strings in the value.
This implies that each value defines a pair of stings, where the second string could be empty.
The first name in a pair is a path to a file in the driver store.
The path is relative to the root of the driver store and can contain sub-directories.
The second name in a pair is the name of the file how it will appear in the system32 or syswow64 directory.
The second name must be just the file name, not including path.
If the second name is empty, the file name is the same as in the driver store (excluding subdirectories).
This allows the driver to have different names in the host driver store and in the guest.

Files listed under the **CopyToVmWhenNewer** and **CopyToVmWhenNewerWow64** graphics adapter registry sub-keys
only overwrite the destination files when they satisfy the "newer" criteria.

In Windows 10 version 2004, the "newer" criteria compares two pieces of information:

- [FileVersion](/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo)
- [LastWriteTime](/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_file_basic_information)

When the destination file ends with the .dll or .exe suffix,
the **FileVersion** is used as the most-significant comparison value
where the greatest version is deemed "newer".

When the destination file doesn't end with the .dll nor .exe suffix OR the two **FileVersion** are equal,
then **LastWriteTime** is used as the least-significant comparison values
where the later date/ time is deemed "newer".

In Windows 10 versions earlier than 2004, the "newer" criteria only compared the files'
[ChangeTime](/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_file_basic_information).

### Example 1

INF [DDInstall] section  
HKR, "softgpukmd\CopyToVmOverwrite", SoftGpuFiles, %REG_MULTI_SZ%, "CopyToVm\softgpu1.dll", "softgpu2.dll"  

The directive will create the registry key in the software (adapter) key:
"HKLM\SYSTEM\CurrentControlSet\Control\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\<number>\CopyToVmOverwrite", SoftGpuFiles = REG_MULTI_SZ, "CopyToVm\softgpu1.dll", "softgpu2.dll"

The OS will copy \<DriverStorePath>\CopyToVm\softgpu1.dll to %windir%\system32\softgpu2.dll

### Example 2

INF [DDInstall] section:  
HKR, "CopyToVmOverwrite", SoftGpuFiles1, %REG_MULTI_SZ%, "softgpu1.dll", "softgpu.dll"  
HKR, "CopyToVmOverwrite", SoftGpuFiles2, %REG_SZ%, "softgpu2.dll"  

The directive will create the registry key in the software (adapter) key:  
"HKLM\SYSTEM\CurrentControlSet\Control\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\<number>\CopyToVmOverwrite", SoftGpuFiles1 = REG_MULTI_SZ, "softgpu1.dll", "softgpu.dll"  
"HKLM\SYSTEM\CurrentControlSet\Control\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\<number>\CopyToVmOverwrite", SoftGpuFiles = REG_SZ, "softgpu2.dll"  

The OS will copy \<DriverStorePath>\softgpu1.dll to %windir%\system32\softgpu.dll and \<DriverStorePath>\softgpu2.dll to %windir%\system32\softgpu2.dll

### Example 3

INF [DDInstall] section:  
HKR, "CopyToVmOverwriteWow64", SoftGpuFiles, %REG_MULTI_SZ%, "Subdir1\Subdir2\softgpu2wow64.dll", "softgpu.dll"  

The directive will create the registry key in the software (adapter) key:  
"HKLM\SYSTEM\CurrentControlSet\Control\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\<number>\CopyToVmOverwriteWow64", SoftGpuFiles = REG_MULTI_SZ, "Subdir1\Subdir2\softgpu2wow64.dll", "softgpu.dll"  

The OS will copy \<DriverStorePath>\Subdir1\Subdir2\softgpu2wow64.dll to %windir%\syswow64\softgpu.dll

## Driver modifications to Registry and file paths

Inside containers, the driver store is not consistently located at the same canonical path as it normally is.
To consistently use the correctly adjusted path, the registry and driver store must be accessed indirectly through
[D3DKMTQueryAdapterInfo](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtqueryadapterinfo)
with [KMTQAITYPE_QUERYREGISTRY](/windows-hardware/drivers/ddi/d3dkmthk/ne-d3dkmthk-_kmtqueryadapterinfotype),
and [D3DDDI_QUERYREGISTRY_INFO](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_queryregistry_info).

## Honor OS default adapter setting

The default adapter must honor the user's choice that is stored in the OS, which requires:

1. Enumerating adapters through DXGI's [IDXGIFactory::EnumAdapters](/windows/win32/api/dxgi/nf-dxgi-idxgifactory-enumadapters),
as DXGI honors the user's choice.
Adapter 0 changes based on the [user's settings](https://blogs.windows.com/windowsexperience/2018/02/07/announcing-windows-10-insider-preview-build-17093-pc/).
2. Match the adapter order gotten through [D3DKMTEnumAdapters2](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtenumadapters2) to DXGI's.
Adapter identities can be matched up by correlating the LUID between both enumeration techniques.
DXGI returns its LUID through [IDXGIAdapter::GetDesc](/windows/win32/api/dxgi/nf-dxgi-idxgiadapter-getdesc).

## DCHU design modifications

Honor as many [universal driver](../develop/getting-started-with-windows-drivers.md) design principals as possible,
which may vary based on the exact device being supported.

## D3DKMT headers

The headers that include the previously mentioned methods and types are available in the Windows SDK for Windows 10 version 2004 and beyond,
instead of being exclusively available in the WDK.

One option to cleanly include the necessary headers is as follows.
Other options may also exist.

```cpp
// Turn off NTSTATUS codes within windows.h, so that the more exhaustive ntstatus.h can be used.
#define UMDF_USING_NTSTATUS
#include <windows.h> // For the vast majority of Windows functionality
#include <winternl.h> // For NT_SUCCESS
#include <ntstatus.h> // For the most exhaustive list of NTSTATUS codes
#include <d3dkmthk.h> // For D3DKMT support
```
