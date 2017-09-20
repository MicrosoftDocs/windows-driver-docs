---
title: Overview of the Logging Manifest
description: Overview of the Logging Manifest
ms.assetid: abf550c5-6b70-4043-b2e9-d3dc5096cc4e
keywords: ["LogViewer, manifest", "LogViewer, manifest, overview"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Overview of the Logging Manifest


## <span id="ddk_overview_of_the_logging_manifest_dtoolq"></span><span id="DDK_OVERVIEW_OF_THE_LOGGING_MANIFEST_DTOOLQ"></span>


The logging manifest is the group of "header" files that define the functions and COM interfaces that are intercepted and logged. These are not true C++ header files -- they are in a slightly different format that explicitly declares the information needed by Logger.

For example, the manifest format facilitates the following features:

-   Designation of OUT parameters. These are parameters that should be logged both on their way into an function and also on their way out.

-   Definition of flag masks. This feature allows LogViewer to break a DWORD flag into its constituent bit labels for easier reading.

-   Definition of failure cases. This feature allows LogViewer to shade the rows of functions that have returned a failure status code or another error code. Also, if the function sets the "LastError" value for the thread, LogViewer can store away the error code and expand it to its corresponding human-readable error message.

-   Designation of parameters that can be aliased for log differencing. This feature gives LogViewer the option of assigning a constant string to a value that changes from execution to execution like pointers and handles when it exports the data to a file. You can then use a differencing tool to compare two execution logs for discrepancies. If pointers and handle values were not aliased, they would produce uninteresting discrepancies when the two files are compared.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Overview%20of%20the%20Logging%20Manifest%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




