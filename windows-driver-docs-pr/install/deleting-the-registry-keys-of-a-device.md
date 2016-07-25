---
title: Deleting the Registry Keys of a Device
description: Deleting the Registry Keys of a Device
ms.assetid: BA7AB3B4-9751-4e53-98AD-2B920F7223A1
keywords: ["registry WDK device installations , deleting a device's registry keys", "deleting registry keys WDK device installations"]
---

# Deleting the Registry Keys of a Device


You should not use [**SetupDiDeleteDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550991) to delete the [*software keys*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-software-key) or [*hardware keys*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-key) for the device for the following reasons:

-   [**SetupDiDeleteDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550991) removes all custom settings in registry keys. This includes the following:

    -   Settings that were specified during installation.

    -   Settings that were created or modified by the device driver.

    -   Settings that were created or modified by applications or other components.

    [**SetupDiDeleteDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550991) also removes critical device installation state.

-   Software or hardware keys that are opened by using [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079) with a scope of DICS\_FLAG\_GLOBAL contain data about the device installation state. Software or hardware keys that are accessed with a scope of DICS\_FLAG\_CONFIGSPECIFIC do not contain device installation state.

    In either case, deleting these software or hardware keys could have implications for other device installation components.

You should not make assumptions about whether device registry keys are present. When the device is uninstalled, the system automatically deletes all software and hardware keys for the device.

You can safely create and delete registry subkeys under the hardware or software keys by using standard registry functions. By using these functions, you avoid naming collisions between the system and other components. Also, if you create subkeys by using these functions, the subkey inherits the default permissions of the parent registry key. For more information, see [Opening, Creating, and Closing Keys](http://go.microsoft.com/fwlink/p/?linkid=194541).

For more information about the standard registry functions, see [Registry Functions](http://go.microsoft.com/fwlink/p/?linkid=194529).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Deleting%20the%20Registry%20Keys%20of%20a%20Device%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




