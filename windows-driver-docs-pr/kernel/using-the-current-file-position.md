---
title: Using the Current File Position
description: Using the Current File Position
ms.assetid: d342d973-8fff-4d00-a275-114012c17727
keywords: ["files WDK kernel", "file objects WDK kernel", "objects WDK file objects", "file handles WDK kernel", "handle to file WDK kernel", "current file positions WDK kernel", "file positions WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using the Current File Position





When you create or open a file, you can cause the I/O manager to create a current file-position pointer that is associated with the file handle. Once you have done so, you can read and write data to the current file position, and the I/O manager will automatically update the position by the number of bytes that were read or written.

By default, the I/O manager does not maintain a current file-position pointer. This default provides efficiency—because correctly maintaining the current file position requires the I/O manager to synchronize every read and write operation on the file object.

To create a handle that has an associated current file-position pointer, specify the SYNCHRONIZE access right in the *DesiredAccess* parameter to [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424), [**IoCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff548418), or [**ZwOpenFile**](https://msdn.microsoft.com/library/windows/hardware/ff567011), and either FILE\_SYNCHRONOUS\_IO\_ALERT or FILE\_SYNCHRONOUS\_IO\_NONALERT in the *CreateOptions* or *OpenOptions* parameter. Be sure that you do not also specify the FILE\_APPEND\_DATA access right.

[**ZwReadFile**](https://msdn.microsoft.com/library/windows/hardware/ff567072) and [**ZwWriteFile**](https://msdn.microsoft.com/library/windows/hardware/ff567121) automatically update the current file-position pointer so that it points just beyond the data affected by the operation. For example, if you read 20 bytes starting at byte offset 101, **ZwReadFile** will update the current file position to 121.

You can examine or change the current file position by calling [**ZwQueryInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567052) or [**ZwSetInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567096), respectively. In either case, set the *FileInformationClass* parameter to **FilePositionInformation**.

 

 




