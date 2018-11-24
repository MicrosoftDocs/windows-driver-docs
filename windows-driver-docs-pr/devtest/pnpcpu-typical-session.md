---
title: PNPCPU Typical Session
description: PNPCPU Typical Session
ms.assetid: d0c1b6aa-fe23-4d01-aecf-897aba3672c9
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





