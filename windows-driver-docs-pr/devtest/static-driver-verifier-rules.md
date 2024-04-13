---
title: DDI Compliance Rules
description: DDI Compliance Rules
ms.date: 05/21/2018
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

You can use the code analysis tools, [Static Driver Verifier](./static-driver-verifier.md) and [Driver Verifier](./driver-verifier.md) to test a driver for compliance to the DDI usage rules. Static Driver Verifier (SDV) performs static analysis on the driver source code, so you can use SDV early in development cycle. Driver Verifier is integrated with the operating system, so you can test a driver at runtime after it has been built, deployed, and installed.

Using the driver source code, [Static Driver Verifier](./static-driver-verifier.md) creates a model of the driver and the operating system. In this model, SDV places the driver in a hostile environment and systematically tests code paths through the driver by looking for violations of a formalized set of the driver compliance rules ([Static Driver Verifier rules](./static-driver-verifier-rule.md)).

Starting in Windows 8, you can configure [Driver Verifier](./driver-verifier.md) to run some of the same compliance checks on installed drivers by enabling [DDI compliance checking](./ddi-compliance-checking.md).

## Related topics


[Driver Verifier](./driver-verifier.md)
[Static Driver Verifier](./static-driver-verifier.md)
 

