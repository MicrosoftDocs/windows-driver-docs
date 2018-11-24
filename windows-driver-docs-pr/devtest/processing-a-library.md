---
title: Processing a Library
description: Processing a Library
ms.assetid: 8ae9ae3b-885d-4eb5-b55b-415edcfc041a
keywords:
- library WDK Static Driver Verifier , processing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing a Library


Before running a verification, process the libraries that the driver requires.

 **To process a library**

1.  Start Static Driver Verifier. From the **Driver** menu in Visual Studio, click **Launch Static Driver Verifier...**.
2.  Click the **Libraries** tab and click **Add Library** to add the library.
3.  Navigate to the directory that stores the project file for the library.
4.  Repeat these steps for each library your driver uses.

Static Driver Verifier keeps a cache of the libraries that you add. Only libraries required by the driver and present in the cache will be used for verification. Libraries are processed with the same configuration and platform settings that the driver uses.

You can also process libraries from a Visual Studio Command Prompt window using the **msbuild t:/sdv p:"/Inputs=/lib"** *libraryproject.vcxproj* option. For information about the command options, see [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md).

If you are unable to process a required library for any reason, you can still verify the driver that uses it. However, the results are less reliable.

 

 





