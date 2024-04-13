---
title: Qualifying and Distributing PSHED Plug-Ins
description: Qualifying and Distributing PSHED Plug-Ins
keywords:
- digital signatures WDK WHEA), PSHED plug-ins
- PSHED plug-ins WDK WHEA , qualifying
- PSHED plug-ins WDK WHEA , distributing
ms.date: 03/03/2023
---

# Qualifying and Distributing PSHED Plug-Ins


To ensure the quality and integrity of the driver, a PSHED plug-in must be digitally signed. Platform vendors must follow these guidelines when digitally signing a PSHED plug-in:

-   To minimize the system startup time, we recommend embedding an [Authenticode](../install/authenticode.md) digital signature into the PSHED plug-in file. For more information about this procedure, see [Release-Signing a Driver through an Embedded Signature](../install/release-signing-a-driver-through-an-embedded-signature.md).

-   Before the hardware platform can undergo additional verification through the server logo testing process, the plug-in's [driver package](../install/driver-packages.md) must have a Windows Hardware Quality Labs (WHQL) digital signature. To obtain this digital signature, you must test and submit the driver package by using the WHQL Unclassified test category.

    **Note**  You must obtain a WHQL digital signature for the driver package regardless of whether the PSHED plug-in was embedded with an [Authenticode](../install/authenticode.md) digital signature.

     

For more information about how to digitally sign a PSHED plug-in, see [Signing Drivers for Public Release](../install/signing-drivers-for-public-release--windows-vista-and-later-.md).

After a PSHED plug-in has obtained a WHQL digital signature, the plug-in can be used in any system for which you request a system logo certification. For more information about the server logo certification process, see [Windows Logo Program](/windows-hardware/test/hlk/).

PSHED plug-ins will be qualified using a "family" approach, where a specific PSHED plug-in can be qualified for deployment across a class, or family, of hardware platforms.

PSHED plug-ins should be distributed to customers by hardware vendors in a manner similar to how BIOS and system firmware updates are distributed. Also, PSHED plug-ins should interface with the platform firmware in such a way that a single PSHED plug-in can be deployed across a family of hardware platforms.

**Note**  PSHED plug-ins are not distributed to customers through Windows Update.

 

