---
title: Using Kernel Mode Performance Counters
description: Using Kernel Mode Performance Counters
ms.date: 08/05/2020
---

# Using Kernel Mode Performance Counters

Kernel-mode components provide performance counters using the Performance Counters for Windows (PCW) APIs.

Use the following steps to develop new counter data providers:

1. [Write a counter manifest](/windows/win32/perfctrs/performance-counters-schema) that describes the provider and its countersets. The counter manifest is an XML-format file that defines the performance counter provider and its countersets.
   - Set the `applicationIdentity` attribute to the name of a binary that will be installed as part of your kernel-mode component and that will contain the string resources needed by performance data consumers.
   - Set the `providerType` attribute to `kernelMode`.
   - Define at least one `struct` element (under `counterSet/structs`) with the name of a C/C++ structure that will be used when passing counter values from your component to the PCW APIs.
   - In each `counter`, define the `struct` and `field` from which PCW should read the counter value.
2. As part of the build process for your component, use the [CTRPP tool](/windows/win32/perfctrs/ctrpp) to compile the counter manifest. (The Counter Preprocessor (CTRPP) tool is included in the WDK and is available at the [Developer Command Prompt](/dotnet/framework/tools/developer-command-prompt-for-vs) by typing `ctrpp`.) The CTRPP tool will generate a `.rc` file and a `.h` file.
   - The CTRPP-generated `.rc` file must be compiled by the Resource Compiler (RC.exe) tool, and the resulting `.res` file must be linked into the binary named in the `applicationIdentity` attribute. You can either directly compile the CTRPP-generated `.rc` file or you can `#include` the CTRPP-generated `.rc` file into an existing `.rc` file that is being compiled into the binary.
   - The CTRPP-generated `.h` file contains helper functions that wrap the underlying PCW APIs. For example, the CTRPP-generated `.h` file will contain a **Register***Xxx* function that calls `PcwRegister` on your behalf. In most cases, you will call the CTRPP-generated helper functions instead of calling any PCW APIs directly, but you can refer to the documentation for the PCW APIs to understand what the corresponding CTRPP-generated functions are doing. The helper functions manage translating the component's counter data layout into the `PCW_DATA` layout expected by the PCW APIs.
3. At component initialization, invoke the CTRPP-generated **Register***Xxx* function, which calls [**PcwRegister**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pcwregister). At component shutdown, invoke the CTRPP-generated **Unregister***Xxx* function, which calls [**PcwUnregister**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pcwunregister).
4. Add code to provide counter data. This is done by either implementing a [*PCW_CALLBACK*](/windows-hardware/drivers/ddi/wdm/nc-wdm-pcw_callback) callback function or by maintaining data structures with counter values for each instance and invoking the CTRPP-generated **CreateInstance***Xxx* and **CloseInstance***Xxx* functions as instances are created and destroyed.
5. At component installation, use `lodctr /m:<CounterManifest> <InstallPath>` to install the provider. At component uninstall, use `unlodctr` (with `/m` or `/g` parameters) to uninstall the provider. Installing the provider adds the provider's countersets to a system-wide repository of available countersets so that the countersets can be used by performance data consumers such as perfmon, typeperf, or WMI. In particular, installing the provider records the full path to the binary (DLL, SYS, or EXE file) that contains the provider's string table. The full path to the binary is determined by combining the manifest's `applicationIdentity` attribute with the `<CounterManifest>` and `<InstallPath>` values used on the `lodctr` command-line as follows:
   - If the `applicationIdentity` attribute is a full path, it will be used.
   - Otherwise, if the `<InstallationPath>` parameter is a full path, it will be used.
   - Otherwise, if the `<CounterManifest>` parameter is a full path, the directory from `<CounterManifest>` will be combined with the filename from the `applicationIdentity` attribute.
   - Otherwise, current working directory will be combined with the filename from the `applicationIdentity` attribute.

For an example of a kernel-mode PCW provider, see the [Kernel Counter Sample (Kcs)](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/perfcounters/kcs) in the [Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) repository on GitHub.

## Related topics

[About Kernel Mode Performance Counters](about-kernel-mode-performance-counters.md)

[Performance Counters Schema](/windows/win32/perfctrs/performance-counters-schema)

[CTRPP tool](/windows/win32/perfctrs/ctrpp)

[**PcwRegister**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pcwregister)

[*PCW_CALLBACK*](/windows-hardware/drivers/ddi/wdm/nc-wdm-pcw_callback)
