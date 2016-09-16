---
title: Details of the IPrintCoreHelperPS Interface
author: windows-driver-content
description: Details of the IPrintCoreHelperPS Interface
MS-HAID:
- 'drvarch\_dc9b41ef-f0ca-47da-8d9e-a23a6f45e93a.xml'
- 'print.details\_of\_the\_iprintcorehelperps\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0e00012c-6ced-4369-b367-675465e29d93
keywords: ["IPrintCoreHelperPS"]
---

# Details of the IPrintCoreHelperPS Interface


Pscript5 does not have an equivalent to the GDL parser, so for Pscript5 drivers, additional methods are provided to read data that appears in the PPD file. In addition to all of the methods of the base **IPrintCoreHelper** interface, the **IPrintCoreHelperPS** interface contains the following methods, which provide access to the data in the PPD file:

-   [**IPrintCoreHelperPS::GetFeatureAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff551998)

-   [**IPrintCoreHelperPS::GetGlobalAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff552899)

-   [**IPrintCoreHelperPS::GetOptionAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff552903)

Because the PPD information does not depend on the configuration, you do not need to supply an input [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) parameter to these methods.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Details%20of%20the%20IPrintCoreHelperPS%20Interface%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


