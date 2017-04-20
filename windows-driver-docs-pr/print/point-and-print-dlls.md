---
title: Point and Print DLLs
author: windows-driver-content
description: Point and Print DLLs
ms.assetid: 7ead940e-8426-4756-890f-f3607dc1f9ca
keywords:
- Point and Print WDK , DLLs
- DLLs WDK Point and Print
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Point and Print DLLs


## <a href="" id="ddk-point-and-print-dlls-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Point%20and%20Print%20DLLs%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


