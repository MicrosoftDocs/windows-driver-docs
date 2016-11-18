---
title: Using Kernel Mode Performance Counters
description: Using Kernel Mode Performance Counters
ms.assetid: b740dd92-ad75-4dea-98d4-dce04b273d2f
---

# Using Kernel Mode Performance Counters


Kernel-mode PCW is an extension to the existing performance counter version 2 platform, which allows kernel-mode components to easily expose performance counters. To incorporate this new extension, you need to make minimal additions to the manifest that describes version 2 counters, and you need to use the kernel-mode performance counter interface.

Use the following steps to develop new counters:

1.  Write a manifest that describes the provider and its counter sets.

    For more information about the elements and attributes in the manifest, see [Performance Counters Schema](http://go.microsoft.com/fwlink/p/?linkid=147029). The counter manifest is an XML-format file that defines the performance counter provider and its counter sets.

    The manifest can be created manually or created by using the manifest generator tool, Ecmangen.exe. The tool is included in the WDK and is available in a build environment window (type **ecmangen** at the command prompt).

2.  Use the [CTRPP tool](http://go.microsoft.com/fwlink/p/?linkid=144441) to generate the registration code and string resources from the manifest.

    The Counter Preprocessor (CTRPP) tool is included in the WDK and is available in a build environment window (type **ctrpp** at the command prompt).

3.  Add code to register and unregister the counter sets.

    For more information, see the [**PcwRegister**](https://msdn.microsoft.com/library/windows/hardware/ff550323) and [**PcwUnregister**](https://msdn.microsoft.com/library/windows/hardware/ff550326) functions.

4.  Add code to expose the instances.

5.  Build a binary that contains the new code and the string resources.

For an example of a kernel-mode PCW provider, see the [Kernel Counter Sample (Kcs)](http://go.microsoft.com/fwlink/p/?LinkId=617718) in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Using%20Kernel%20Mode%20Performance%20Counters%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




