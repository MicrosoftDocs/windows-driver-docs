---
title: Installing Queue-Specific Files
description: Installing Queue-Specific Files
ms.assetid: 86cb16d5-6035-4a4d-a6b7-f27ebd3e9f5c
keywords:
- Point and Print WDK , queue-specific files
- queue-specific files WDK printer
- print queues WDK , Point and Print
- queues WDK printer , Point and Print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Queue-Specific Files





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
<td><p>Filename of an optional <a href="point-and-print-dlls.md" data-raw-source="[Point and Print DLL](point-and-print-dlls.md)">Point and Print DLL</a>.</p></td>
</tr>
</tbody>
</table>

 

The application should create these values by calling the print spooler's **SetPrinterDataEx** function. The registry key specified with this call should be formatted as:

**CopyFiles\\**<em>ComponentName</em>

where *ComponentName* is the name of the software component with which the files are associated. For example, files associated with Microsoft Image Color Management (ICM) are specified under the **CopyFiles\\ICM** key. You specify the registry key name as an argument to the **SetPrinterDataEx** function, and the function creates the key as a subkey of the print queue's key on the print server.

### <a href="" id="ddk-installation-example-gg"></a>Installation Example

As an example, suppose that an HP Color LaserJet printer is installed on a print server and is assigned the print queue name of "HpColor". Also suppose that Microsoft ICM requires the following two files to be associated with the print queue:

-   A color profile named hpclrlsr.icm, located in PRINT$\\Color on the server.

-   A DLL named Mscms.dll, located in PRINT$\\Color on the server.

An installation application would call the ICM API function **AssociateColorProfileWithDevice**, which in turn calls **SetPrinterDataEx** to create the following server registry entries:

```cpp
CopyFiles\ICM\Directory: Color
CopyFiles\ICM\Files: hpclrsr.icm
CopyFiles\ICM\Module: mscms.dll
```

The Mscms.dll module is a [Point and Print DLL](point-and-print-dlls.md) that exports **GenerateCopyFilePaths** and **SpoolerCopyFileEvent** functions.

 

 




