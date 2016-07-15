---
Description: COM in the Kernel
MS-HAID: 'audio.com\_in\_the\_kernel'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: COM in the Kernel
---

# COM in the Kernel


## <span id="com_in_the_kernel"></span><span id="COM_IN_THE_KERNEL"></span>


Audio port and miniport drivers export device driver interfaces (DDIs) that conform to the Component Object Model (COM). For background information about COM interfaces, see the COM section of the Microsoft Windows SDK documentation.

All COM interfaces inherit from the **IUnknown** interface, which has the methods **AddRef**, **QueryInterface**, and **Release**. Because these methods are common to all COM interfaces, the reference pages for the WDM audio driver interfaces do not explicitly describe them.

This section discusses the following topics:

[Function Tables for Miniport Drivers](function-tables-for-miniport-drivers.md)

[Creating Audio Driver Objects](creating-audio-driver-objects.md)

[Reference-Counting Conventions for COM Objects](reference-counting-conventions-for-com-objects.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20COM%20in%20the%20Kernel%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


