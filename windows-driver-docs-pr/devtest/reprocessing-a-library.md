---
title: Reprocessing a Library
description: Reprocessing a Library
ms.assetid: 8d9f5890-cbe1-4240-ab23-76b6008fe686
keywords:
- library WDK Static Driver Verifier , reprocessing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reprocessing a Library


You typically need to process the code for libraries that your driver requires only once. However, you need to process a library again in the following situations:

-   **Added library**. If changes in the driver code require a library that SDV has not processed, you must process that library.

-   **Library change**. If the code has changed in a library that the driver requires, or in a library required by one of those libraries, you must reprocess all libraries affected by the change.

-   **Delete processed libraries**. If you removed all the libraries from the libraries cache, by using either the **Remove Libraries** button on the **Libraries** tab or by running the **/clean** option in the library directory in MSBuild.

If you cannot process a required library for any reason, you can still run a verification, but the results are less reliable.

**To reprocess a library**

1.  Start Static Driver Verifier. From the **Driver** menu in Visual Studio, click **Launch Static Driver Verifier...**.
2.  On the **Main** tab, click **Clean**.
3.  Click the **Libraries** tab and click **Add Library** to add the library.
4.  Navigate to the library directory and select the project file for the library.

**To re-process all libraries**

1.  Start Static Driver Verifier. From the **Driver** menu in Visual Studio, click **Launch Static Driver Verifier...**.
2.  Click the **Libraries** tab to select the library (or libraries), and click **Remove Libraries** to remove the library or libraries from the cache.
3.  For each library that you need to re-process, click **Add Library**.
4.  Navigate to the library directory and select the project file for the library.
5.  Repeat the steps to add and select project files for each library your driver uses.

You can also reprocess a library from in an MSBuild command by using the /clean and /lib parameter options. For more information, see [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md).

 

 





