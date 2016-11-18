---
title: Library Processing in Static Driver Verifier
description: Library Processing in Static Driver Verifier
ms.assetid: d95ccdc2-aa00-4671-87fb-6f0f77d2ba8d
keywords: ["Static Driver Verifier WDK , libraries", "StaticDV WDK , libraries", "SDV WDK , libraries", "library WDK Static Driver Verifier", "library WDK Static Driver Verifier , about library processing"]
---

# Library Processing in Static Driver Verifier


Many drivers depend on dynamically and statically linked libraries of functions. Typically, the libraries include general processing functions, but in some situations, they include functionality that is integral to the driver.

Libraries are essential for determining whether the driver complies with interface rules. For example, without library code, a driver might appear to have missed a required call that is included in the library. Or, the library might include a call that the driver duplicates, causing a repeat error, such as releasing a lock twice.

To include a library in the verification of a driver, SDV must first [process the library](processing-a-library.md) to prepare it for use in verifying the driver.

SDV tries to automatically detect and process all libraries on which the driver depends, but because it does not know the location of some library source files, it cannot automatically process these libraries and include them in the driver verification. When SDV detects a library dependency but cannot find the library code, it displays a warning message: "[Process &lt;library name&gt;](process--library-name-.md)". You can respond by clicking the **Libraries** tab and click **Add Library** to process the libraries.

After SDV has processed a library, it retains its processing files for that library and automatically includes the library code in verifications of all drivers that require the library. You do not need to reprocess the library unless the library code changes. For instructions on reprocessing a library, see [Reprocessing a Library](reprocessing-a-library.md).

This section includes:

[Processing a Library](processing-a-library.md)

[Reprocessing a Library](reprocessing-a-library.md)

### <span id="comments"></span><span id="COMMENTS"></span>Comments

SDV includes processed library files for system libraries. You do not need to direct SDV to process these libraries. When SDV detects that a driver depends on these libraries, it uses its processed files for these libraries without displaying a warning message. For information about library requirements, see [Determining if Static Driver Verifier supports your driver or library](determining-if-static-driver-verifier-supports-your-driver-or-library.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Library%20Processing%20in%20Static%20Driver%20Verifier%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




