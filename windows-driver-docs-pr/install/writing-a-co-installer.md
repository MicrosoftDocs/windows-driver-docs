---
title: Writing a Co-installer
description: Writing a Co-installer
ms.assetid: d5637321-9cff-4b24-8941-d3ca16b0d8c1
keywords: ["Device setup WDK device installations , co-installers", "device installations WDK , co-installers", "installing devices WDK , co-installers", "co-installers WDK device installations , about co-installers", "coinstallers WDK"]
---

# Writing a Co-installer


## <a href="" id="ddk-writing-a-co-installer-dg"></a>


**Note**  Features described in this section are not supported in universal or mobile driver packages. See [Using a Universal INF File](using-a-configurable-inf-file.md).

 

A co-installer is a Microsoft Win32 DLL that assists in device installation. Co-installers are called by SetupAPI as "helpers" for Class Installers. For example, a vendor can provide a co-installer to write device-specific information to the registry that cannot be handled by the INF file.

This section includes the following topics:

[Co-installer Operation](co-installer-operation.md)

[Co-installer Interface](co-installer-interface.md)

[Co-installer Functionality](co-installer-functionality.md)

[Handling DIF Codes](handling-dif-codes.md)

[Registering a Co-installer](registering-a-co-installer.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Writing%20a%20Co-installer%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




