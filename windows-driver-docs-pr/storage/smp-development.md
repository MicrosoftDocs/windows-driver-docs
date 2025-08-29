---
title: SMP Development (Windows Drivers)
description: Learn more about SMP Development.
ms.date: 11/21/2024
ms.topic: concept-article
---

# SMP Development

## A WMI Provider

Storage Management Provider (SMP) interfaces are WMI based. Although you could write an SMP using WMI v1, we highly recommended that you write a WMI v2 provider using C/C++. We don't recommend using .NET Framework for SMP development because some important functionality might not be available through the .NET platform. In addition:

* WMI v1 has a heavy dependency on COM which can be difficult and time-consuming to learn.
* WMI v2 aligns closer with industry standards than WMI v1; WMI v2 uses WS-Management instead of DCOM.
* Providers can utilize better Error/Eventing in WMI v2.
* Providers can utilize PowerShell extensions and integration in WMI v2.

## Development Resource Checklist

| Item | Location | Note |
| ---- | -------- | ---- |
| Base class MOF files: Storagewmi_provider.mof and all MOF files starting with “msft_” in file name. | Windows Software Development Kit (SDK) | Under %SDK_Installed_Location%\Windows Kits\x.x\Include\um |
| Other required MOF files: qualifiers.mof and CIM_Error.mof | Distributed Management Task Force: [http://dmtf.org/standards/cim](http://dmtf.org/standards/cim) | These files are non-Microsoft-defined. |
| Header file: mi.h | Windows SDK | Under %SDK_Installed_Location%\Windows Kits\x.x\Include\um |
| Provider skeleton generation tool and .dll file: Convert-MofToProvider.exe | Windows SDK | Under %SDK_Installed_Location%\Windows Kits\x.x\bin\x64\ or …\bin\x86 |
| Provider registration tool: Register-CimProvider.exe | %OS_Install_Path%\Windows\System32\ | |

## MOF Definition

Initial SMP development is done in three simple steps:

1. Extend the provider MOF.
1. Generate a provider skeleton (or stubs).
1. Implement stubs.

### Extending the Provider MOF

The SMP MOFs are located in the Windows SDK include folder. They're prefixed with MSFT\_\*. Copy these files to your development directory, along with CIM\_Error.mof and qualifiers.mof. Each MOF defines one or more abstract classes that form the base for your SMP.

Similar to other languages, an abstract class can't be implemented directly. It must be derived and implemented in a separate implementation class. Create your own MOF and include all of the relevant provider MOFs. Then, create a derived class for each of the base classes your provider will implement. Be sure to pick a unique prefix for your classes. For example, a company named “Contoso Storage Inc.” could either prefix their classes with CONTOSO\_\* or CSI\_\*. For example, for MSFT\_StorageProvider, a prefix of "CONTOSO_" would yield CONTOSO\_StorageProvider. The class should now look like this:

```cpp
    class CONTOSO_StorageProvider : MSFT_StorageProvider
    {
        ...
    }
```

Once you create these skeleton classes, you must then copy over all of the method declarations for the methods you plan to implement. All methods that aren't copied over (regardless of whether implemented or not) will return MI_RESULT_NOT_SUPPORTED. You don't need to copy the class properties. To minimize MOF compilation errors, keep all the qualifiers of the methods and parameters.

Finally, be sure to include these lines at the beginning of your MOF:

```cpp
    #pragma include("storagewmi_provider.mof")
    #pragma include("msft_qualifiers.mof")
```

When you finish Step 1, you're now ready to generate the provider stubs using Convert-MofToProvider.exe. When providing input to this command, be sure to only specify the derived classes. The headers for the base classes are generated implicitly.

See [SMP Example MOFs](smp-example-mofs.md).

## Provider Skeleton Generation

SMP developers can use the Convert-MofToProvider.exe tool from the WMI SDK to generate a provider skeleton project. This project includes a list of header and C source files prefilled with WMI provider methods. By supplying implementations for these methods, developers can provide support to their storage hardware.

Place all MOFs from the “Development Resource Checklist” section and the MOFs you created into one folder. Next, use the following command in a command prompt to generate provider skeleton (refer to help text for the most update-to-date options):

``` command
    Convert-MofToProvider.exe
        -MofFile <path to your provider mof>
        -ClassList <list of ALL classes listed in your mof, space separated>
        -IncludePath <path to qualifiers.mof and CIM_Error.mof>
        -SkipQualifiers
        -SkipLocalize
```

Finally, include the *mi.h* header file into your development project.

## Recommended Development Sequence

StorageProvider, StorageSubSystem, and VirtualDisk are mandatory classes. Depending on the capabilities of your storage array, StoragePool, ResiliencSetting, PhysicalDisk, MaskingSet, InitiatorId, TargetPort, TargetPortal, OffloadDataTransferSetting and StorageJob are optional.

To ease the development and testing process, a recommended sequence of implementation follows:

1. **EnumerateInstances**: Support basic queries for required classes StorageProvider, StorageSubSystem, VirtualDisk.
1. **GetInstance**: GetInstance is required for many WMI operations, including method invocation.
1. **Create\*/DeleteObject**: Implement all creation and deletion methods for the objects that your provider supports.
1. **Object Associations**: Associations allow for quick and easy traversal between your array objects. EnumerateInstances, AssociatorsOf, and ReferencesOf on the associator class are required for implementation. GetInstance on the associator isn't required, but GetInstance on the source and destination objects are.
1. **Indications**: Indications allow your provider to notify management applications about a change.
1. Remainder of methods.

## Provider Registration

Start a command prompt. Register your provider with the following command:

``` command
    Register-CimProvider.exe 
    –Namespace root\Microsoft\Windows\Storage\Providers
    –ProviderName <name of your provider>
    –Path <path to your provider’s dll file>
```
