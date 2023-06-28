---
title: Installing queue-specific files
description: Installing queue-specific files
keywords:
- Point and Print WDK , queue-specific files
- queue-specific files WDK printer
- print queues WDK , Point and Print
- queues WDK printer , Point and Print
ms.date: 06/26/2023
---

# Installing queue-specific files

At printer installation time, a vendor-supplied installation application can specify a set of files, of any type, to be associated with a particular print queue. The files are downloaded to each client that connects to the print server. The installation application specifies the files by placing values in the registry, as illustrated in the following table.

| Value Name | Value Type | Value |
|--|--|--|
| **Directory** | REG_SZ | Directory path to the files specified by **Files**. Used as both the source path on the server and the destination path on the client. This path is relative to the PRINT\$ environment variable. |
| **Files** | REG_MULTI_SZ | File names of the files to be copied to a client when the client connects to the print server. Files can be DLLs, data files, or any other type of file. |
| **Module** | REG_SZ | Filename of an optional [Point and Print DLL](point-and-print-dlls.md). |

The application should create these values by calling the print spooler's **SetPrinterDataEx** function. The registry key specified with this call should be formatted as:

**CopyFiles**\\_ComponentName_

where _ComponentName_ is the name of the software component with which the files are associated. For example, files associated with Microsoft Image Color Management (ICM) are specified under the **CopyFiles\\ICM** key. You specify the registry key name as an argument to the **SetPrinterDataEx** function, and the function creates the key as a subkey of the print queue's key on the print server.

## Installation example

As an example, suppose that an HP Color LaserJet printer is installed on a print server and is assigned the print queue name of "HpColor". Also suppose that Microsoft ICM requires the following two files to be associated with the print queue:

- A color profile named hpclrlsr.icm, located in PRINT$\\Color on the server.

- A DLL named Mscms.dll, located in PRINT$\\Color on the server.

An installation application would call the ICM API function **AssociateColorProfileWithDevice**, which in turn calls **SetPrinterDataEx** to create the following server registry entries:

```cpp
CopyFiles\ICM\Directory: Color
CopyFiles\ICM\Files: hpclrsr.icm
CopyFiles\ICM\Module: mscms.dll
```

The Mscms.dll module is a [Point and Print DLL](point-and-print-dlls.md) that exports **GenerateCopyFilePaths** and **SpoolerCopyFileEvent** functions.
