---
title: Processing a Library
description: Processing a Library
ms.assetid: 8ae9ae3b-885d-4eb5-b55b-415edcfc041a
keywords: ["library WDK Static Driver Verifier , processing"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Processing%20a%20Library%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




