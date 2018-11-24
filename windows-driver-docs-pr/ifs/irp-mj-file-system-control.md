---
title: IRP_MJ_FILE_SYSTEM_CONTROL
description: IRP\_MJ\_FILE\_SYSTEM\_CONTROL
ms.assetid: 9df42b58-5820-44fd-8e55-0195807be951
keywords: ["IRP_MJ_FILE_SYSTEM_CONTROL Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_FILE_SYSTEM_CONTROL
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_FILE\_SYSTEM\_CONTROL


## When Sent


The IRP\_MJ\_FILE\_SYSTEM\_CONTROL request is sent by the I/O Manager and other operating system components, as well as other kernel-mode drivers. It can be sent, for example, when a user-mode application has called the Microsoft Win32 [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function to send a file system I/O control (FSCTL) request.

## Operation: File System Drivers


The file system driver or recognizer should check the minor function code to determine which file system control operation is requested.

File system drivers should handle the following minor function codes:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IRP_MN_KERNEL_CALL</p></td>
<td align="left"><p>This request is the same as IRP_MN_USER_FS_REQUEST (described following), except that the source of the request is a trusted kernel component.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_MOUNT_VOLUME</p></td>
<td align="left"><p>Indicates a volume mount request. If a file system driver receives this IRP for a volume whose format does not match that of the file system, the file system driver should return STATUS_UNRECOGNIZED_VOLUME.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_USER_FS_REQUEST</p></td>
<td align="left"><p>Indicates an FSCTL request, possibly on behalf of a user-mode application that has called the Microsoft Win32 DeviceIoControl function or on behalf of a kernel-mode component that has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff566441" data-raw-source="[&lt;strong&gt;ZwDeviceIoControlFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566441)"><strong>ZwDeviceIoControlFile</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548318" data-raw-source="[&lt;strong&gt;IoBuildDeviceIoControlRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548318)"><strong>IoBuildDeviceIoControlRequest</strong></a>.</p>
<p>For detailed information about FSCTL requests, see &quot;Device Input and Output Control Codes&quot; in the Microsoft Windows SDK documentation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_VERIFY_VOLUME</p></td>
<td align="left"><p>Indicates a volume verification request. For removable media, the file system must verify the volume when it detects that the media has been removed and returned to ensure that it is still the same volume that the file system was previously working with. If the volume has changed, the file system should invalidate all outstanding handles. It will also return an error if the file system on this new media has changed. This request is most often used for floppy drives.</p></td>
</tr>
</tbody>
</table>

 

File system recognizers must handle the following minor function code:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IRP_MN_LOAD_FILE_SYSTEM</p></td>
<td align="left"><p>Indicates a load-file system request.</p></td>
</tr>
</tbody>
</table>

 

After performing the requested operation, the file system driver or recognizer should complete the IRP.

## Operation: Files System Filter Drivers


The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a file system control request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  
Pointer to a system-supplied input buffer to be passed to the file system or file system filter driver for the target volume. Used for METHOD\_BUFFERED or METHOD\_DIRECT I/O. Whether this parameter is required depends on the specific file system control code.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irp--mdladdress"></a>*Irp-&gt;MdlAddress*  
Address of a memory descriptor list (MDL) describing an output buffer to be passed to the file system or file system filter driver for the target volume. Used for METHOD\_DIRECT I/O. Whether this parameter is required depends on the specific I/O control code.

<a href="" id="irp--userbuffer"></a>*Irp-&gt;UserBuffer*  
Pointer to a caller-supplied output buffer to be passed to the file system or file system filter driver for the target volume. Used for METHOD\_BUFFERED or METHOD\_NEITHER I/O. Whether this parameter is optional or required depends on the specific I/O control code.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_FILE\_SYSTEM\_CONTROL and should not be used.

<a href="" id="irpsp--flags"></a>*IrpSp-&gt;Flags*  
The following flag can be set for IRP\_MN\_VERIFY\_VOLUME:

SL\_ALLOW\_RAW\_MOUNT

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_FILE\_SYSTEM\_CONTROL.

<a href="" id="irpsp--minorfunction"></a>*IrpSp-&gt;MinorFunction*  
One of the following:

-   IRP\_MN\_KERNEL\_CALL
-   IRP\_MN\_LOAD\_FILE\_SYSTEM
-   IRP\_MN\_MOUNT\_VOLUME
-   IRP\_MN\_USER\_FS\_REQUEST
-   IRP\_MN\_VERIFY\_VOLUME

<a href="" id="irpsp--parameters-filesystemcontrol-fscontrolcode"></a>*IrpSp-&gt;Parameters.FileSystemControl.FsControlCode*  
FSCTL function code to be passed to the file system or file system filter driver for the target volume. For use with IRP\_MN\_USER\_FS\_REQUEST only.

For detailed information about IOCTL and FSCTL requests, see [Using I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff565406) in the *Kernel Mode Architecture Guide* and "Device Input and Output Control Codes" in the Microsoft Windows SDK documentation.

<a href="" id="irpsp--parameters-filesystemcontrol-inputbufferlength"></a>*IrpSp-&gt;Parameters.FileSystemControl.InputBufferLength*  
Size in bytes of the buffer pointed to by *Irp-&gt;AssociatedIrp.SystemBuffer*.

<a href="" id="irpsp--parameters-filesystemcontrol-outputbufferlength"></a>*IrpSp-&gt;Parameters.FileSystemControl.OutputBufferLength*  
Size in bytes of the buffer pointed to by *Irp-&gt;UserBuffer*.

<a href="" id="irpsp--parameters-filesystemcontrol-type3inputbuffer"></a>*IrpSp-&gt;Parameters.FileSystemControl.Type3InputBuffer*  
Input buffer for kernel-mode requests using METHOD\_NEITHER.

<a href="" id="irpsp--parameters-mountvolume-deviceobject"></a>*IrpSp-&gt;Parameters.MountVolume.DeviceObject*  
Pointer to the device object for the actual device on which the volume is to be mounted. File system filter drivers should not use this parameter.

<a href="" id="irpsp--parameters-mountvolume-vpb"></a>*IrpSp-&gt;Parameters.MountVolume.Vpb*  
Pointer to the volume parameter block (VPB) for the volume to be mounted. File systems that support removable media might substitute a previously used VPB for the one passed in this parameter. On such file systems, after the volume is mounted, this pointer can no longer be assumed to be valid. File system filter drivers that filter these file systems should use this parameter as follows: Before sending the IRP down to lower-level drivers, the filter should save the value of *IrpSp-&gt;Parameters.MountVolume.Vpb-&gt;RealDevice*. After the volume is successfully mounted, the filter can use this pointer to the storage device object to obtain the correct VPB pointer.

<a href="" id="irpsp--parameters-verifyvolume-deviceobject"></a>*IrpSp-&gt;Parameters.VerifyVolume.DeviceObject*  
Pointer to the device object for the volume to be verified.

<a href="" id="irpsp--parameters-verifyvolume-vpb"></a>*IrpSp-&gt;Parameters.VerifyVolume.Vpb*  
Pointer to the VPB for the volume to be verified.

## See also


[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoBuildAsynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548310)

[**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318)

[**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**ZwDeviceIoControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566441)

 

 






