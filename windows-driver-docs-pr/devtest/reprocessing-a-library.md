---
title: Reprocessing a Library
description: Reprocessing a Library
ms.assetid: 8d9f5890-cbe1-4240-ab23-76b6008fe686
keywords: ["library WDK Static Driver Verifier , reprocessing"]
---

# Reprocessing a Library


You typically need to process the code for libraries that your driver requires only once. However, you need to process a library again in the following situations:

-   **Added library**. If changes in the driver code require a library that SDV has not processed, you must process that library.

-   **Library change**. If the code has changed in a library that the driver requires, or in a library required by one of those libraries, you must reprocess all libraries affected by the change.

-   **Delete processed libraries**. If you removed all the libraries from the libraries cache, by using either the **Remove Libraries** button on the **Libraries** tab or by using the **/cleanalllibs** option in an MSBuild command.

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

You can also reprocess a library from in an MSBuild command by using the /clean and /cleanalllibs parameter options. For more information, see [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Reprocessing%20a%20Library%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




