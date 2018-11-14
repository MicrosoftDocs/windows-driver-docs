---
title: Using AgeStore
description: Using AgeStore
ms.assetid: 188eac5c-e84c-45a4-a4ea-1c9bfaa93cca
keywords: ["AgeStore, using"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using AgeStore


AgeStore is a tool that deletes files in a directory or directory tree, based on their last access dates. Its primary use is for removing old files from the downstream store used by a symbol server or a source server, in order to conserve disk space. It can also be used as a general file deletion tool.

AgeStore can delete all files in a single directory (the *target directory*), or in all the directories within a tree (the *target tree*). The -s option indicates that an entire tree is to be targeted.

There are three ways to specify which files within the target directory or target tree are to be deleted. The agestore -date=Month-Day-Year command deletes all files that were last accessed prior to the specified date. The agestore -days=NumberOfDays command deletes all files that were last accessed more than the specified number of days ago. The agestore -size=SizeRemaining command deletes all files in the target directory or target tree, beginning with the least-recently-accessed files, until the total size of the remaining files is less than or equal to *SizeRemaining*.

For example, the following command deletes all files in C:\\MyDir that were last accessed prior to January 7, 2008:

```console
agestore c:\mydir -date=01-07-2008
```

The following command deletes all files in the directory tree subordinate to C:\\symbols\\downstreamstore that were last accessed over thirty days ago:

```console
agestore c:\symbols\downstreamstore -days=30 -s
```

The following command deletes files in the directory tree subordinate to C:\\symbols\\downstreamstore, beginning with those accessed longest ago, until the total size of all files in this tree is less than or equal to 50,000 bytes:

```console
agestore c:\symbols\downstreamstore -size=50000 -s
```

The -l option causes AgeStore to delete no files, but merely to list all the files that would be deleted without this option. Before you use any AgeStore command you should run the intended command with the -l option added, to verify that it will delete exactly those files you intend it to delete.

For the complete command line syntax, see [**AgeStore Command-Line Options**](agestore-command-line-options.md).

### <span id="running_agestore_on_windows_vista_and_later"></span><span id="RUNNING_AGESTORE_ON_WINDOWS_VISTA_AND_LATER"></span>Running AgeStore on Windows Vista and Later

Because AgeStore deletes files based on the last time that they were accessed, it can run successfully only if your file system stores Last Access Time (LAT) data. In the NTFS file system, LAT data storage can be either enabled or disabled. If it is disabled, AgeStore will not run, but will display the following error message instead:

```console
Last-Access-Time support is disabled on this computer.
Please read the documentation for more details.
```

In Windows Vista and later versions of Windows, LAT data storage is disabled by default, and therefore AgeStore will not run unless you first enable this data.

In Windows Vista and later versions of Windows, you can use the FSUtil (Fsutil.exe) tool to enable the gathering of LAT data. From a Command Prompt window, issue the following command:

```console
fsutil behavior set disablelastaccess 0 
```

To disable the gathering of LAT data, using the following command:

```console
fsutil behavior set disablelastaccess 1 
```

These changes take effect after the next restart of Windows.

The FAT32 file system always stores LAT information (although only the date, and not the time, are stored). Therefore, AgeStore works with FAT32 file systems. However, since AgeStore will not run when the NTFS LAT is disabled, you must enable NTFS LAT even if your file system is FAT32.

 

 





