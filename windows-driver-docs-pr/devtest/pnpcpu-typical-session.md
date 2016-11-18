---
title: PNPCPU Typical Session
description: PNPCPU Typical Session
ms.assetid: d0c1b6aa-fe23-4d01-aecf-897aba3672c9
---

# PNPCPU Typical Session


When you run the **-install** command, PNPCPU does the following:

-   Installs the bus enumerator driver.

-   Marks all existing processors with problem code 28 - visible in the Device Manager.

-   Adds ONECPU to the Boot Configuration Data (BCD) settings.

-   Saves the number of processors that Windows is using when **-install** is run.

-   Pre-installs the INF file for the processor driver.

After the installation is completed, you will see the following message:

```
Enabled hot add cpu...
Please reboot the system before proceeding with the test
```

Restart the system either by executing shutdown from the command line, or from a system menu option.

After you restart your computer, Windows will only be using one logical processor. You can confirm this in Device Manager by finding processors with error code 28.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PNPCPU%20Typical%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




