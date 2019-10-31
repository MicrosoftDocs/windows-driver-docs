---
title: Using Kernel Mode Performance Counters
description: Using Kernel Mode Performance Counters
ms.assetid: b740dd92-ad75-4dea-98d4-dce04b273d2f
ms.date: 10/31/2019
ms.localizationpriority: medium
---

# Using Kernel Mode Performance Counters

Kernel-mode PCW is an extension to the existing performance counter version 2 platform, which allows kernel-mode components to easily expose performance counters. To incorporate this new extension, you need to make minimal additions to the manifest that describes version 2 counters, and you need to use the kernel-mode performance counter interface.

Use the following steps to develop new counters:

1. [Write an information manifest](https://docs.microsoft.com/windows/win32/wes/writing-an-instrumentation-manifest) that describes the provider and its counter sets.

    For more information about the elements and attributes in the manifest, see [Performance Counters Schema](https://go.microsoft.com/fwlink/p/?linkid=147029). The counter manifest is an XML-format file that defines the performance counter provider and its counter sets.

    The manifest can be created manually or created by using the manifest generator tool **Ecmangen.exe** included in the WDK. It is available in the [Developer Command Prompt](https://docs.microsoft.com/dotnet/framework/tools/developer-command-prompt-for-vs) by typing **ecmangen** at the command prompt.

2. Use the [CTRPP tool](https://go.microsoft.com/fwlink/p/?linkid=144441) to generate the registration code and string resources from the manifest.

    The Counter Preprocessor (CTRPP) tool is included in the WDK and is available in a [Developer Command Prompt](https://docs.microsoft.com/dotnet/framework/tools/developer-command-prompt-for-vs) by typing **ctrpp** at the command prompt).

3. Add code to register and unregister the counter sets.

    For more information, see the [**PcwRegister**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-pcwregister) and [**PcwUnregister**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-pcwunregister) functions.

4. Add code to expose the instances.

5. Build a binary that contains the new code and the string resources.

For an example of a kernel-mode PCW provider, see the [Kernel Counter Sample (Kcs)](https://go.microsoft.com/fwlink/p/?LinkId=617718) in the [Windows driver samples](https://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.
