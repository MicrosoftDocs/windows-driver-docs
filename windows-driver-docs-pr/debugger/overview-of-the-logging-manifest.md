---
title: Overview of the Logging Manifest
description: Overview of the Logging Manifest
ms.assetid: abf550c5-6b70-4043-b2e9-d3dc5096cc4e
keywords: ["LogViewer, manifest", "LogViewer, manifest, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Overview of the Logging Manifest


## <span id="ddk_overview_of_the_logging_manifest_dtoolq"></span><span id="DDK_OVERVIEW_OF_THE_LOGGING_MANIFEST_DTOOLQ"></span>


The logging manifest is the group of "header" files that define the functions and COM interfaces that are intercepted and logged. These are not true C++ header files -- they are in a slightly different format that explicitly declares the information needed by Logger.

For example, the manifest format facilitates the following features:

-   Designation of OUT parameters. These are parameters that should be logged both on their way into an function and also on their way out.

-   Definition of flag masks. This feature allows LogViewer to break a DWORD flag into its constituent bit labels for easier reading.

-   Definition of failure cases. This feature allows LogViewer to shade the rows of functions that have returned a failure status code or another error code. Also, if the function sets the "LastError" value for the thread, LogViewer can store away the error code and expand it to its corresponding human-readable error message.

-   Designation of parameters that can be aliased for log differencing. This feature gives LogViewer the option of assigning a constant string to a value that changes from execution to execution like pointers and handles when it exports the data to a file. You can then use a differencing tool to compare two execution logs for discrepancies. If pointers and handle values were not aliased, they would produce uninteresting discrepancies when the two files are compared.

 

 





