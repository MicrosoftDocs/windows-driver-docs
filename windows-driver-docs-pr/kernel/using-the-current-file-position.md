---
title: Using the Current File Position
author: windows-driver-content
description: Using the Current File Position
MS-HAID:
- 'Other\_dd894af7-08dd-4274-bbf7-7bc41384c3d4.xml'
- 'kernel.using\_the\_current\_file\_position'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d342d973-8fff-4d00-a275-114012c17727
keywords: ["files WDK kernel", "file objects WDK kernel", "objects WDK file objects", "file handles WDK kernel", "handle to file WDK kernel", "current file positions WDK kernel", "file positions WDK kernel"]
---

# Using the Current File Position


## <a href="" id="ddk-using-the-current-file-position-kg"></a>


When you create or open a file, you can cause the I/O manager to create a current file-position pointer that is associated with the file handle. Once you have done so, you can read and write data to the current file position, and the I/O manager will automatically update the position by the number of bytes that were read or written.

By default, the I/O manager does not maintain a current file-position pointer. This default provides efficiency—because correctly maintaining the current file position requires the I/O manager to synchronize every read and write operation on the file object.

To create a handle that has an associated current file-position pointer, specify the SYNCHRONIZE access right in the *DesiredAccess* parameter to [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424), [**IoCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff548418), or [**ZwOpenFile**](https://msdn.microsoft.com/library/windows/hardware/ff567011), and either FILE\_SYNCHRONOUS\_IO\_ALERT or FILE\_SYNCHRONOUS\_IO\_NONALERT in the *CreateOptions* or *OpenOptions* parameter. Be sure that you do not also specify the FILE\_APPEND\_DATA access right.

[**ZwReadFile**](https://msdn.microsoft.com/library/windows/hardware/ff567072) and [**ZwWriteFile**](https://msdn.microsoft.com/library/windows/hardware/ff567121) automatically update the current file-position pointer so that it points just beyond the data affected by the operation. For example, if you read 20 bytes starting at byte offset 101, **ZwReadFile** will update the current file position to 121.

You can examine or change the current file position by calling [**ZwQueryInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567052) or [**ZwSetInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567096), respectively. In either case, set the *FileInformationClass* parameter to **FilePositionInformation**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20the%20Current%20File%20Position%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


