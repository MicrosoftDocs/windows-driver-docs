---
title: Modifying Registry Keys by Class Installers and Co-installers
description: Modifying Registry Keys by Class Installers and Co-installers
ms.assetid: A7F41F97-5E06-41d8-B80F-DDBC41A62BB3
keywords: ["registry WDK device installations , modifying registry keys", "registry WDK device installations , modifying registry keys, class installers", "registry WDK device installations , modifying registry keys, co-installers", "class installers WDK device installations , modifying registry keys", "co-installers WDK device installations , modifying registry keys"]
---

# Modifying Registry Keys by Class Installers and Co-installers


**Note**  Features described in this section are not supported in universal or mobile driver packages. See [Using a Universal INF File](using-a-configurable-inf-file.md).

 

Except under certain conditions, [*class installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-installer) and [*co-installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) should not use the standard registry functions to create, change, or delete registry keys. In most cases, registry keys should only be modified by using directives that are put in [INF files](inf-files.md). For more information about these directives, see [Summary of INF Directives](summary-of-inf-directives.md).

The following are exceptions to this rule:

-   When it is necessary, class installers and co-installers can use the standard registry functions to modify registry keys in the **HKLM\\Software** subtree.

    **Note**  We highly recommend that class installers and co-installers save custom device properties as entries within the device's [*software keys*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-software-key).

     

-   Class installers and co-installers are permitted to modify subkeys in the **HKLM\\System\\CurrentControlSet\\Control\\CoDeviceInstallers** registry key.

The following guidelines should be followed to safely modify registry keys by class installers or co-installers:

-   Class installers and co-installers must first use [**SetupDiCreateDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550973) or [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079) to open handles to the registry keys that will be modified. After a handle has been opened, class installers and co-installers can use the standard registry functions to modify registry keys.

-   Class installers and co-installers must not use [**SetupDiDeleteDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550991) to delete [*software keys*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-software-key) or [*hardware keys*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-key) for the device. For more information, see [Deleting the Registry Keys of a Device](deleting-the-registry-keys-of-a-device.md).

For more information about the standard registry functions, see [Registry Functions](http://go.microsoft.com/fwlink/p/?linkid=194529).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Modifying%20Registry%20Keys%20by%20Class%20Installers%20and%20Co-installers%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




