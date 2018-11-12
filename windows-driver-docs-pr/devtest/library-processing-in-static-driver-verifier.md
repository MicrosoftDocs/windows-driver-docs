---
title: Library Processing in Static Driver Verifier
description: Library Processing in Static Driver Verifier
ms.assetid: d95ccdc2-aa00-4671-87fb-6f0f77d2ba8d
keywords:
- Static Driver Verifier WDK , libraries
- StaticDV WDK , libraries
- SDV WDK , libraries
- library WDK Static Driver Verifier
- library WDK Static Driver Verifier , about library processing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Library Processing in Static Driver Verifier


Many drivers depend on dynamically and statically linked libraries of functions. Typically, the libraries include general processing functions, but in some situations, they include functionality that is integral to the driver.

Libraries are essential for determining whether the driver complies with interface rules. For example, without library code, a driver might appear to have missed a required call that is included in the library. Or, the library might include a call that the driver duplicates, causing a repeat error, such as releasing a lock twice.

To include a library in the verification of a driver, SDV must first [process the library](processing-a-library.md) to prepare it for use in verifying the driver.

SDV tries to automatically detect and process all libraries on which the driver depends, but because it does not know the location of some library source files, it cannot automatically process these libraries and include them in the driver verification. To ensure SDV provides the most accurate analysis for your driver, you should manually add any libraries your driver references to SDV's library cache by clicking the **Libraries** tab and selecting **Add Library** to process the libraries.  If you are running in the command line, you may add a library by running sdv with the **/lib** command against the library project.

After SDV has processed a library, it retains its processing files for that library and automatically includes the library code in verifications of all drivers that require the library. You do not need to reprocess the library unless the library code changes. For instructions on reprocessing a library, see [Reprocessing a Library](reprocessing-a-library.md).

This section includes:

[Processing a Library](processing-a-library.md)

[Reprocessing a Library](reprocessing-a-library.md)

### <span id="comments"></span><span id="COMMENTS"></span>Comments

SDV includes processed library files for system libraries. You do not need to direct SDV to process these libraries. When SDV detects that a driver depends on these libraries, it uses its processed files for these libraries without displaying a warning message. For information about library requirements, see [Determining if Static Driver Verifier supports your driver or library](determining-if-static-driver-verifier-supports-your-driver-or-library.md).

 

 





