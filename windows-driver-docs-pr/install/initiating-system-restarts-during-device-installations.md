---
title: Initiating System Restarts During Device Installations
description: Initiating System Restarts During Device Installations
ms.assetid: 52db2894-e759-4382-97de-5db7f268ff59
---

# Initiating System Restarts During Device Installations


In the rare cases in which it is necessary for the system to be restarted to complete a device installation, use the following rules:

-   During initial installations, a device's installer or co-installer can request a system restart by setting DI\_NEEDRESTART in the [**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346) structure, which is received along with [device installation function codes](https://msdn.microsoft.com/library/windows/hardware/ff541307). (This should not be done unless absolutely necessary.)

-   During update installations, a device's installation application can call [**UpdateDriverForPlugAndPlayDevices**](https://msdn.microsoft.com/library/windows/hardware/ff553534), which determines whether a system restart is necessary.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Initiating%20System%20Restarts%20During%20Device%20Installations%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




