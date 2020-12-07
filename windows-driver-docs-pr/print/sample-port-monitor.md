---
title: Sample Port Monitor
description: Sample Port Monitor
keywords:
- port monitors WDK print , samples
ms.date: 08/25/2020
ms.localizationpriority: medium
---

# Sample Port Monitor

The functions that LOCALMON  exports are incorporated into Localspl.dll, the Local Print Provider. Port monitors are divided into two DLLs: a port monitor server DLL, and a port monitor user interface DLL.

> [!NOTE]
> LOCALMON (Localmon.dll) print monitor samples for previous versions of Windows have been archived as outlined below. LOCALMON (Localmon.dll) print monitor sample code is not available in the Windows Driver Kit (WDK) 10 samples on GitHub.

For previous versions of Windows, sample source code for LOCALMON (Localmon.dll) is available in the following locations:

- For Windows 7, sample source code for Localmon.dll is included with the [Windows Driver Kit Version 7.1.0](https://www.microsoft.com/download/details.aspx?id=11800) installation download. The sample is located in the **\\src\\print\\monitors\\localmon** subdirectory (for example, C:\WinDDK\7600.16385.1\src\print\monitors\localmon).

- For Windows 8, the sample source code for Localmon.dll is available in the [localmon](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Driver%20Kit%20Sample/Windows%20Driver%20Kit%20(WDK)%208.0%20Samples/%5BC%2B%2B%5D-Windows%20Driver%20Kit%20(WDK)%208.0%20Samples/C%2B%2B/WDK%208.0%20Samples/Print%20Monitors%20Samples/Solution/localmon) directory in the Windows Driver Kit (WDK) 8.0 samples archive repo on GitHub.

- For Windows 8.1, the sample source code for Localmon.dll is available in the [localmon](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Driver%20Kit%20Sample/Windows%20Driver%20Kit%20(WDK)%208.1%20Samples/%5BC%2B%2B%5D-windows-driver-kit-81-cpp/WDK%208.1%20C%2B%2B%20Samples/Print%20Monitors%20Samples/C%2B%2B/localmon) directory in the Windows Driver Kit (WDK) 8.1 samples archive repo on GitHub.
