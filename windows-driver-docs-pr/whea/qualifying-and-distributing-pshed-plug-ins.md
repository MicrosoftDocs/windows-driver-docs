---
title: Qualifying and Distributing PSHED Plug-Ins
author: windows-driver-content
description: Qualifying and Distributing PSHED Plug-Ins
ms.assetid: fe6cbb01-552f-4b24-b300-168d6311a596
keywords: ["digital signatures WDK WHEA), PSHED plug-ins", "PSHED plug-ins WDK WHEA , qualifying", "PSHED plug-ins WDK WHEA , distributing"]
---

# Qualifying and Distributing PSHED Plug-Ins


To ensure the quality and integrity of the driver, a PSHED plug-in must be digitally signed. Platform vendors must follow these guidelines when digitally signing a PSHED plug-in:

-   To minimize the system startup time, we recommend embedding an [Authenticode](https://msdn.microsoft.com/library/windows/hardware/ff686697) digital signature into the PSHED plug-in file. For more information about this procedure, see [Release-Signing a Driver through an Embedded Signature](https://msdn.microsoft.com/library/windows/hardware/ff549832).

-   Before the hardware platform can undergo additional verification through the server logo testing process, the plug-in's [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) must have a Windows Hardware Quality Labs (WHQL) digital signature. To obtain this digital signature, you must test and submit the driver package by using the WHQL Unclassified test category.

    **Note**  You must obtain a WHQL digital signature for the driver package regardless of whether the PSHED plug-in was embedded with an [Authenticode](https://msdn.microsoft.com/library/windows/hardware/ff686697) digital signature.

     

For more information about how to digitally sign a PSHED plug-in, see [Signing Drivers for Public Release](https://msdn.microsoft.com/library/windows/hardware/ff552289).

After a PSHED plug-in has obtained a WHQL digital signature, the plug-in can be used in any system for which you request a system logo certification. For more information about the server logo certification process, see [Windows Logo Program](http://go.microsoft.com/fwlink/p/?linkid=26144).

PSHED plug-ins will be qualified using a "family" approach, where a specific PSHED plug-in can be qualified for deployment across a class, or family, of hardware platforms.

PSHED plug-ins should be distributed to customers by hardware vendors in a manner similar to how BIOS and system firmware updates are distributed. Also, PSHED plug-ins should interface with the platform firmware in such a way that a single PSHED plug-in can be deployed across a family of hardware platforms.

**Note**  PSHED plug-ins are not distributed to customers through Windows Update.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Qualifying%20and%20Distributing%20PSHED%20Plug-Ins%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


