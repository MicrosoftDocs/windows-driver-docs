---
title: Point and Print DLLs
description: Point and Print DLLs
ms.assetid: 7ead940e-8426-4756-890f-f3607dc1f9ca
keywords:
- Point and Print WDK , DLLs
- DLLs WDK Point and Print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Point and Print DLLs





You can optionally supply a special Point and Print DLL by associating its name with the **Module** registry value. This DLL must export the following two functions:

<a href="" id="generatecopyfilepaths"></a>[**GenerateCopyFilePaths**](https://msdn.microsoft.com/library/windows/hardware/ff549896)  
This function, which is called by both the server's spooler and the client's spooler, can be used to modify the directory path specified by the **Directory** registry value. Either the source path (on the server) or the destination path (on the client), or both, can be modified.

<a href="" id="spoolercopyfileevent"></a>[**SpoolerCopyFileEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562681)  
This function, also called by both the server's spooler and the client's spooler, receives an event code indicating the occurrence of certain connection-related printer events.

A Point and Print DLL need not export only these functions. For example Mscms.dll, which is used by Microsoft's ICM component, also exports a set of ICM API functions.

Note that you can specify other DLLs in addition to, or instead of, a Point and Print DLL that exports **GenerateCopyFilePaths** and **SpoolerCopyFileEvent**. To do so, assign the DLL file names to the **Files** registry key instead of the **Module** registry key. (See [Installing Queue-Specific Files](installing-queue-specific-files.md)).

After the installation application has placed the DLL's name in the server's registry by calling **SetPrinterDataEx**, all subsequent calls to **SetPrinterDataEx** result in a call to the DLL's [**SpoolerCopyFileEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562681) function, with a supplied event code of COPYFILE\_EVENT\_SET\_PRINTER\_DATAEX.

Unlike the files listed under the **Files** registry key (see [Installing Queue-Specific Files](installing-queue-specific-files.md)), the Point and Print DLL is not copied from the print server to the client when the client connects to a printer. Instead, the DLL is assumed to already be client-resident when a connection to the print server is made. As a result, the DLL can be used for additional purposes not related to Point and Print functionality.

One method for installing the Point and Print DLL on a client is to specify its name in a [printer INF file](printer-inf-files.md) as a dependent file, so the file can be copied to the client's driver directory during [downloading of driver-specific files](downloading-driver-specific-files.md).

 

 




