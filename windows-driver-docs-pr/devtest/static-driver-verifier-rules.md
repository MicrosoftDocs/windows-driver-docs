---
title: DDI Compliance Rules
description: DDI Compliance Rules
ms.assetid: f020fff9-f880-4aa8-b422-5452728d2fdd
---

# DDI Compliance Rules


This section lists and describes the Windows Device Driver Interface (DDI) Compliance Rules that you can use to verify Windows Driver Model (WDM), Kernel Mode Driver Framework (KMDF), Audio (PortCls), AVStream (KS), NDIS, and Storport drivers. The DDI Compliance rules define requirements for the proper interaction between a driver and the kernel interface of the operating system.

[Rules for Audio Drivers](rules-for-audio-drivers.md)  
[Rules for AVStream Drivers](rules-for-avstream-drivers.md)  
[Rules for WDM Drivers](sdv-rules-for-wdm-drivers.md)  
[Rules for KMDF Drivers](sdv-rules-for-kmdf-drivers.md)  
[Rules for NDIS Drivers](sdv-rules-for-ndis-drivers.md)  
[Rules for Storport Drivers](sdv-rules-for-storport-drivers.md)  

### Driver Verification Tools

You can use the code analysis tools, [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) to test a driver for compliance to the DDI usage rules. Static Driver Verifier (SDV) performs static analysis on the driver source code, so you can use SDV early in development cycle. Driver Verifier is integrated with the operating system, so you can test a driver at runtime after it has been built, deployed, and installed.

Using the driver source code, [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) creates a model of the driver and the operating system. In this model, SDV places the driver in a hostile environment and systematically tests code paths through the driver by looking for violations of a formalized set of the driver compliance rules ([Static Driver Verifier rules](https://msdn.microsoft.com/library/windows/hardware/ff552839)).

Starting in Windows 8, you can configure [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) to run some of the same compliance checks on installed drivers by enabling [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208).

## Related topics


[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)
[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20DDI%20Compliance%20Rules%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




