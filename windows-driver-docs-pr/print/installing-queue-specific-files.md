---
title: Installing Queue-Specific Files
author: windows-driver-content
description: Installing Queue-Specific Files
ms.assetid: 86cb16d5-6035-4a4d-a6b7-f27ebd3e9f5c
keywords:
- Point and Print WDK , queue-specific files
- queue-specific files WDK printer
- print queues WDK , Point and Print
- queues WDK printer , Point and Print
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing Queue-Specific Files


## <a href="" id="ddk-installing-queue-specific-files-gg"></a>


At printer installation time, a vendor-supplied installation application can specify a set of files, of any type, to be associated with a particular print queue. The files are downloaded to each client that connects to the print server. The installation application specifies the files by placing values in the registry, as illustrated in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Value Name</th>
<th>Value Type</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Directory</strong></p></td>
<td><p>REG_SZ</p></td>
<td><p>Directory path to the files specified by <strong>Files</strong>. Used as both the source path on the server and the destination path on the client. This path is relative to the PRINT$ environment variable.</p></td>
</tr>
<tr class="even">
<td><p><strong>Files</strong></p></td>
<td><p>REG_MULTI_SZ</p></td>
<td><p>File names of the files to be copied to a client when the client connects to the print server. Files can be DLLs, data files, or any other type of file.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Module</strong></p></td>
<td><p>REG_SZ</p></td>
<td><p>Filename of an optional [Point and Print DLL](point-and-print-dlls.md).</p></td>
</tr>
</tbody>
</table>

 

The application should create these values by calling the print spooler's **SetPrinterDataEx** function. The registry key specified with this call should be formatted as:

**CopyFiles\\***ComponentName*

where *ComponentName* is the name of the software component with which the files are associated. For example, files associated with Microsoft Image Color Management (ICM) are specified under the **CopyFiles\\ICM** key. You specify the registry key name as an argument to the **SetPrinterDataEx** function, and the function creates the key as a subkey of the print queue's key on the print server.

### <a href="" id="ddk-installation-example-gg"></a>Installation Example

As an example, suppose that an HP Color LaserJet printer is installed on a print server and is assigned the print queue name of "HpColor". Also suppose that Microsoft ICM requires the following two files to be associated with the print queue:

-   A color profile named hpclrlsr.icm, located in PRINT$\\Color on the server.

-   A DLL named Mscms.dll, located in PRINT$\\Color on the server.

An installation application would call the ICM API function **AssociateColorProfileWithDevice**, which in turn calls **SetPrinterDataEx** to create the following server registry entries:

```
CopyFiles\ICM\Directory: Color
CopyFiles\ICM\Files: hpclrsr.icm
CopyFiles\ICM\Module: mscms.dll
```

The Mscms.dll module is a [Point and Print DLL](point-and-print-dlls.md) that exports **GenerateCopyFilePaths** and **SpoolerCopyFileEvent** functions.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20Queue-Specific%20Files%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


