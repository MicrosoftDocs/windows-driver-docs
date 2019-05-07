---
title: Container Support for non-DX APIs
description: Non-DX APIs must interact with drivers and kernel more directly, so they are exposed to more complications
ms.assetid: 6c4a6974-c67b-4710-80c6-48a5b378e088
ms.date: 05/07/2019
ms.localizationpriority: medium
---

# Container Support for non-DX APIs

Windows 10 added several features that significantly impact non-DX APIs,
and the lower-level WDDM architectural details they rely on.
1. Paravirtualized WDDM adapters 
2. Users now have control over the adapter used by applications that don't discriminate themselves
3. [Universal drivers](https://docs.microsoft.com/windows-hardware/drivers/develop/getting-started-with-universal-drivers) introduces a new set of design principals

Maintaining compatibility with the latest Windows 10 features requires the following modifications:

## Driver INF Modifications
The driver must register non-DX runtimes into the appropriate registry locations to install their binaries
into the system32 and syswow64 subdirectories of the Windows installation.
In the installation INF, the driver can define multiple values in the following sub-keys of the graphics adapter registry key:
- CopyToVmOverwrite
- CopyToVmWhenNewer
- CopyToVmOverwriteWow64
- CopyToVmWhenNewerWow64

The former sub-keys modify the system32 directory, while the latter sub-keys modify the syswow64 directory.
__Newer__ is defined by comparing the file's [ChangeTime](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_file_basic_information).
Each value type under a subkey must be REG_MULTI_SZ or REG_SZ. 
If the value type is REG_MULTI_SZ, there must be maximum 2 strings in the value. 
This implies that each value defines a pair of stings, where the second string could be empty.
The first name in a pair is a path to a file in the driver store. 
The path is relative to the root of the driver store and can contain sub-directories.
The second name in a pair is the name of the file how it will appear in the system32 or syswow64 directory.
The second name must be just the file name, not including path. 
If the second name is empty, the file name is the same as in the driver store (excluding subdirectories).
This allows the driver to have different names in the host driver store and in the guest. 

### Example 1:
INF [service-install-section] section  
HKR, "softgpukmd\CopyToVmOverwrite", SoftGpuFiles, %REG_MULTI_SZ%, "CopyToVm\softgpu1.dll", "softgpu2.dll"  

The directive will create the registry key in the service key:
"HKLM\SYSTEM\CurrentControlSet\Services\softgpukmd\CopyToVmOverwrite", SoftGpuFiles = REG_MULTI_SZ, "CopyToVm\softgpu1.dll", "softgpu2.dll"

The OS will copy \<DriverStorePath>\CopyToVm\softgpu1.dll to %windir%\system32\softgpu2.dll

### Example 2:
INF [DDInstall] section:  
HKR, "CopyToVmOverwrite", SoftGpuFiles1, %REG_MULTI_SZ%, "softgpu1.dll", "softgpu.dll"  
HKR, "CopyToVmOverwrite", SoftGpuFiles2, %REG_SZ%, "softgpu2.dll"  

The directive will create the registry key in the software (adapter) key:  
"HKLM\SYSTEM\CurrentControlSet\Control\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\<number>\CopyToVmOverwrite", SoftGpuFiles1 = REG_MULTI_SZ, "softgpu1.dll", "softgpu.dll"  
"HKLM\SYSTEM\CurrentControlSet\Control\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\<number>\CopyToVmOverwrite", SoftGpuFiles = REG_SZ, "softgpu2.dll"  

The OS will copy \<DriverStorePath>\softgpu1.dll to %windir%\system32\softgpu.dll and \<DriverStorePath>\softgpu2.dll to %windir%\system32\softgpu2.dll

### Example 3:
INF [DDInstall] section:  
HKR, "CopyToVmOverwriteWow64", SoftGpuFiles, %REG_MULTI_SZ%, "Subdir1\Subdir2\softgpu2wow64.dll", "softgpu.dll"  

The directive will create the registry key in the software (adapter) key:  
"HKLM\SYSTEM\CurrentControlSet\Control\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\\<number>\CopyToVmOverwriteWow64", SoftGpuFiles = REG_MULTI_SZ, "Subdir1\Subdir2\softgpu2wow64.dll", "softgpu.dll"  

The OS will copy \<DriverStorePath>\Subdir1\Subdir2\softgpu2wow64.dll to %windir%\syswow64\softgpu.dll

## Driver Modifications to Registry and File Paths
Inside containers, the driver store is not consistently located at the same canonical path as it normally is.
To consistently use the correctly adjusted path, the registry and driver store must be accessed indirectly through
[D3DKMTQueryAdapterInfo](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/nf-d3dkmthk-d3dkmtqueryadapterinfo)
with 
[KMTQAITYPE_QUERYREGISTRY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/ne-d3dkmthk-_kmtqueryadapterinfotype),
and [D3DDDI_QUERYREGISTRY_INFO](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dukmdt/ns-d3dukmdt-_d3dddi_queryregistry_info).

## Honor OS Default Adapter Setting
The default adapter must honor the user's choice that is stored in the OS, which requires:
1. Enumerating adapters through DXGI's [IDXGIFactory::EnumAdapters](https://docs.microsoft.com/windows/desktop/api/dxgi/nf-dxgi-idxgifactory-enumadapters),
as DXGI honors the user's choice. 
Adapter 0 changes based on the [user's settings](https://blogs.windows.com/windowsexperience/2018/02/07/announcing-windows-10-insider-preview-build-17093-pc/).
2. Match the adapter order gotten through [D3DKMTEnumAdapters2](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmthk/nf-d3dkmthk-d3dkmtenumadapters2) to DXGI's.
Adapter identities can be matched up by correlating the LUID between both enumeration techniques.
DXGI returns its LUID through [IDXGIAdapter::GetDesc](https://docs.microsoft.com/windows/desktop/api/dxgi/nf-dxgi-idxgiadapter-getdesc).

## DCHU Design Modifications
Honor as many [universal driver](https://docs.microsoft.com/en-us/windows-hardware/drivers/develop/getting-started-with-universal-drivers) design principals as possible,
which may vary based on the exact device being supported.

## WDK Dependency

Many of the previously mentioned methods and types are exclusively available in the WDK,
which is used to build drivers.
This is an unfortunate oversight in the organization of Microsoft's headers,
as non-DX APIs previously could depend on just the Windows SDK.
If it is too onerous for non-DX APIs to include the WDK or localize the WDK depedency to the runtime or loader component,
then Microsoft gives non-DX API projects permission to effectively sever the WDK dependency.
The WDK dependency can be severed by using Microsoft's public documentation,
and creating binary-compatible types and function declarations into their project.
These typenames must not be identical to those used by Microsoft,
to avoid name conflicts if someone else intentionally leverages the WDK with non-DX API projects.

