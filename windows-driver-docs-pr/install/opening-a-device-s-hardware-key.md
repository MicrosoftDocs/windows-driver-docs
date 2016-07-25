---
title: Opening a Device's Hardware Key
description: Opening a Device's Hardware Key
ms.assetid: FED22F37-D09C-4207-8C2C-FB6484A8D19D
keywords: ["hardware keys WDK device installations , opening", "opening hardware keys WDK device installations"]
---

# Opening a Device's Hardware Key


You must not directly open a device?s [*hardware key*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-key). As with any registry key, the location or format of these keys might change between different versions of Windows.

**Note**  You should open a device's hardware key only after the corresponding device has been found. For more information about this procedure, see [Enumerating Installed Devices](enumerating-installed-devices.md).

 

To open or create a device's hardware key, follow these guidelines:

-   To open an existing hardware key, use [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079). To create a hardware key, use [**SetupDiCreateDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550973). In either case, you must set the *KeyType* parameter to DIREG\_DEV.

    **Note**  You must set the *samDesired* parameter to the minimal access permissions that are required. You must not set this parameter to KEY\_ALL\_ACCESS. For more information about how to specify access permissions for registry access, see [Accessing Registry Keys Safely](accessing-registry-keys-safely.md).

     

-   Kernel-mode callers should use [**IoOpenDeviceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549443) and set the *DevInstKeyType* parameter to PLUGPLAY\_REGKEY\_DEVICE.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Opening%20a%20Device's%20Hardware%20Key%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




