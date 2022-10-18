---
title: SMP Development (Windows Drivers)
description: Learn more about SMP Development.
ms.date: 10/14/2022
---

# SMP Development

## A WMI Provider

Storage Management Provider (SMP) interfaces are WMI based. You can implement a provider using either the existing version of WMI (WMI v1) or the new version being introduced in Windows 8 (WMI v2).

Choosing between WMI v1 and WMI v2:

- WMI v1 has a heavy dependency on COM which can be difficult and time-consuming to learn.
- WMI v2 aligns closer with industry standards than WMI v1; WMI v2 uses WS-Management instead of DCOM.
- Providers can utilize better Error/Eventing in WMI v2.
- Providers can utilize PowerShell extensions and integration in WMI v2.

Although you could write a SMP using WMI v1, it is highly recommended to write a WMI v2 provider using C/C++. We do not recommend using .NET Frameworkfor SMP development because some important functionality may not be available through the .NET platform.

## Development Resource Checklist

<table>
<thead>
<tr class="header">
<th>Item</th>
<th>Location</th>
<th>Note</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Base class MOF files: Storagewmi_provider.mof and all MOF files starting with “msft_” in file name.</td>
<td>Windows Software Development Kit (SDK) for Windows 8</td>
<td>Under %SDK_Installed_Location%\Windows Kits\8.0\Include\um</td>
</tr>
<tr class="even">
<td><p>Other required MOF files:</p>
<p>qualifiers.mof CIM_Error.mof</p></td>
<td>Distributed Management Task Force: <a href="http://dmtf.org/standards/cim" class="uri">http://dmtf.org/standards/cim</a></td>
<td>These are non-Microsoft-defined files. Use CIM Schema version 2.26.</td>
</tr>
<tr class="odd">
<td>Header file: mi.h</td>
<td>Windows SDK for Windows 8</td>
<td>Under %SDK_Installed_Location%\Windows Kits\8.0\Include\um</td>
</tr>
<tr class="even">
<td>Provider skeleton generation tool and .dll file: Convert-MofToProvider.exe</td>
<td>Windows SDK for Windows 8</td>
<td>Under %SDK_Installed_Location%\Windows Kits\8.0\bin\x64\ or …\bin\x86</td>
</tr>
<tr class="odd">
<td>Provider registration tool: Register-CimProvider.exe</td>
<td>%OS_Install_Path%\Windows\System32\</td>
<td></td>
</tr>
</tbody>
</table>

## MOF Definition

Initial SMP development is done in three simple steps:

1. Extend the provider MOF
1. Generate provider skeleton (or stubs)
1. Implement stubs

The following is a discussion of the first step:

The Storage Management Provider MOFs are located in the Windows SDK include folder. They are prefixed with MSFT\_\*. Copy these files to your development directory, along with CIM\_Error.mof and qualifiers.mof. If you open these files, you will notice that each of these MOFs define one or more abstract classes. These form the base for your SMP.

Similar to other languages, an abstract class cannot be implemented directly. It must be derived and implemented in a separate implementation class. Create your own MOF and include all of the relevant provider MOFs. Then, create a derived class for each of the base classes your provider will implement. Be sure to pick a unique prefix for your classes. For example, a company named “Contoso Storage Inc.” could either prefix their classes with CONTOSO\_\* or CSI\_\*. In the case of MSFT\_StorageProvider, this would yield CONTOSO\_StorageProvider. The class should now look like this:

```cpp
    class CONTOSO_StorageProvider : MSFT_StorageProvider
    {
        ...
    }
```

Once you have created these skeleton classes, you must then copy over all of the method declarations for the methods you plan to implement. All methods that are not copied over (regardless of whether implemented or not) will return MI\_RESULT\_NOT\_SUPPORTED. You do not need to copy the class properties. To minimize MOF compilation errors, keep all the qualifiers of the methods and parameters.

Finally, be sure to include these lines at the beginning of your MOF:

```cpp
    #pragma include("storagewmi_provider.mof")
    #pragma include("msft_qualifiers.mof")
```

When you have finished the above steps, you are now ready to generate the provider stubs using Convert-MofToProvider.exe. When providing input to this command, be sure to only specify the derived classes. The headers for the base classes are generated implicitly.

See [SMP Example MOFs](smp-example-mofs.md).

## Provider Skeleton Generation

SMP developers can use the Convert-MofToProvider.exe tool from the WMI SDK to generate a provider skeleton project. This project includes a list of header and C source files prefilled with WMI provider methods. By supplying implementations for these methods, developers can provide support to their storage hardware.

Place all MOFs from the “Development Resource Checklist” section and the MOFs you created into one folder. Next, use the following command in a command prompt to generate provider skeleton (refer to help text for the most update-to-date options):

```
    Convert-MofToProvider.exe
        -MofFile <path to your provider mof>
        -ClassList <list of ALL classes listed in your mof, space separated>
        -IncludePath <path to qualifiers.mof and CIM_Error.mof>
        -SkipQualifiers
        -SkipLocalize
```

Finally, include the *mi.h* header file into your development project.

## Recommended Development Sequence

StorageProvider, StorageSubSystem and VirtualDisk are mandatory classes. Depending on the capabilities of your storage array, StoragePool, ResiliencSetting, PhysicalDisk, MaskingSet, InitiatorId, TargetPort, TargetPortal, OffloadDataTransferSetting and StorageJob are optional.

To ease the development and testing process, a recommended sequence of implementation is the following:

1. **EnumerateInstances**: Support basic queries for required classes StorageProvider, StorageSubSystem, VirtualDisk.
1. **GetInstance**: GetInstance is required for many WMI operations, including method invocation.
1. **Create\*/DeleteObject**: Implement all creation and deletion methods for the objects that your provider supports.
1. **Object Associations**: Associations allow for quick and easy traversal between your array objects. EnumerateInstances, AssociatorsOf, and ReferencesOf on the associator class are required for implementation. GetInstance on the associator is not required, but GetInstance on the source and destination objects are.
1. **Indications**: Indications allow your provider to notify management applications about a change.
1. Remainder of methods.

## Provider Registration

Start a command prompt. Register your provider with the following command:

```
    Register-CimProvider.exe 
    –Namespace root\Microsoft\Windows\Storage\Providers
    –ProviderName <name of your provider>
    –Path <path to your provider’s dll file>
```
