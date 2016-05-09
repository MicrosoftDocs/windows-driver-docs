---
title: Filter Device Object Attached to a Volume
author: windows-driver-content
description: Filter Device Object Attached to a Volume
ms.assetid: cf152065-fc03-4f5f-b65b-13a76e83d745
keywords: ["filter device objects WDK file system", "filter drivers WDK file system , device object I/O requests", "file system filter drivers WDK , device object I/O requests", "volumes WDK file system , device object I/O requests", "device object I/O requests WDK file system"]
---

# Filter Device Object Attached to a Volume


## <span id="ddk_a_filter_device_object_attached_to_a_volume_if"></span><span id="DDK_A_FILTER_DEVICE_OBJECT_ATTACHED_TO_A_VOLUME_IF"></span>


To filter a volume, a filter driver creates a filter device object and attaches it above the volume device object for the volume.

### <span id="types_of_i_o_requests_that_are_sent_to_a_volume"></span><span id="TYPES_OF_I_O_REQUESTS_THAT_ARE_SENT_TO_A_VOLUME"></span>Types of I/O Requests That Are Sent to a Volume

A filter device object that is attached above a volume can generally expect to receive the following types of I/O requests:

[**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff548608)

[**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff548621)

[**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630)

[**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548649)

[**IRP\_MJ\_DIRECTORY\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548658)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548670)

[**IRP\_MJ\_FLUSH\_BUFFERS**](https://msdn.microsoft.com/library/windows/hardware/ff549235)

[**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff549241)

[**IRP\_MJ\_LOCK\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff549251)

[**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff549268)

[**IRP\_MJ\_QUERY\_EA**](https://msdn.microsoft.com/library/windows/hardware/ff549279)

[**IRP\_MJ\_QUERY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff549283)

[**IRP\_MJ\_QUERY\_QUOTA**](https://msdn.microsoft.com/library/windows/hardware/ff549293)

[**IRP\_MJ\_QUERY\_SECURITY**](https://msdn.microsoft.com/library/windows/hardware/ff549298)

[**IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff549318)

[**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff549327)

[**IRP\_MJ\_SET\_EA**](https://msdn.microsoft.com/library/windows/hardware/ff549346)

[**IRP\_MJ\_SET\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff549366)

[**IRP\_MJ\_SET\_QUOTA**](https://msdn.microsoft.com/library/windows/hardware/ff549401)

[**IRP\_MJ\_SET\_SECURITY**](https://msdn.microsoft.com/library/windows/hardware/ff549407)

[**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff549415)

[**IRP\_MJ\_SHUTDOWN**](https://msdn.microsoft.com/library/windows/hardware/ff549423)

[**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff549427)

**FastIoCheckIfPossible**

**FastIoDetachDevice**

**FastIoDeviceControl**

**FastIoLock**

**FastIoQueryBasicInfo**

**FastIoQueryNetworkOpenInfo**

**FastIoQueryOpen**

**FastIoQueryStandardInfo**

**FastIoRead**

**FastIoReadCompressed**

**FastIoUnlockAll**

**FastIoUnlockAllByKey**

**FastIoUnlockSingle**

**FastIoWrite**

**FastIoWriteCompressed**

**MdlRead**

**MdlReadComplete**

**MdlReadCompleteCompressed**

**MdlWriteComplete**

**MdlWriteCompleteCompressed**

**PrepareMdlWrite**

File system filter device objects, attached to volumes, are required to pass all unrecognized or unwanted IRPs to the next-lower driver on the driver stack by default. In addition, they must implement **FastIoDetachDevice**.

**Note**   On Microsoft Windows XP and later, the following fast I/O callback routines are obsolete and should not be used by file system filter drivers:
**AcquireForCcFlush**

**AcquireFileForNtCreateSection**

**AcquireForModWrite**

**ReleaseForCcFlush**

**ReleaseFileForNtCreateSection**

**ReleaseForModWrite**

For more information, see the reference entry for [**FsRtlRegisterFileSystemFilterCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff547172).

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Filter%20Device%20Object%20Attached%20to%20a%20Volume%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


