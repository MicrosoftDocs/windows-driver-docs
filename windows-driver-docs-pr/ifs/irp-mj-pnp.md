---
title: IRP_MJ_PNP
description: IRP\_MJ\_PNP
ms.assetid: aec2f309-02a1-460a-b674-33ad18286347
keywords: ["IRP_MJ_PNP Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_PNP
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_PNP


## When Sent


The Plug and Play Manager sends the IRP\_MJ\_PNP request whenever Plug and Play activity occurs on the system. Other operating system components, as well as other kernel-mode drivers, can also send certain IRP\_MJ\_PNP requests, depending on the minor function code.

For more information about Plug and Play IRP processing requirements for drivers, see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125).

For reference information about IRP\_MJ\_PNP minor function codes, see [Plug and Play Minor IRPs](https://msdn.microsoft.com/library/windows/hardware/ff558807).

## Operation: File System Drivers


The file system should check the minor function code to determine which operation is requested. File systems must handle the following minor function codes:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IRP_MN_CANCEL_REMOVE_DEVICE</p></td>
<td align="left"><p>Indicates that a previous query-remove device request was canceled. This request is sent to alert the file system in case it needs to perform any cleanup related to the cancellation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_QUERY_REMOVE_DEVICE</p></td>
<td align="left"><p>Indicates that a device is about to be removed. If a file system is mounted on the device, the PnP Manager sends this request to the file system and to any file system filters. If there are open handles to the device, the file system typically fails the query-remove request. If not, the file system typically locks the volume to prevent future create requests from succeeding. If a mounted file system does not support a query-remove request, the PnP Manager fails the query-remove request for the device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_REMOVE_DEVICE</p></td>
<td align="left"><p>Indicates that a device is about to be removed. If a file system is mounted on the device, the PnP Manager sends this IRP to the file system and to any file system filters. The file system should immediately pass this IRP to the storage driver for the device, setting a completion routine in which the file system then dismounts the volume.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_START_DEVICE</p></td>
<td align="left"><p>Indicates that a device is being started. The file system should pass this IRP to the storage driver for the device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_SURPRISE_REMOVAL</p></td>
<td align="left"><p>Indicates that a device has been removed. If a file system was mounted on the device, the PnP Manager sends this IRP to the file system and to any file system filters. The file system should immediately pass this IRP to the storage driver for the device, setting a completion routine in which the file system then dismounts the volume.</p></td>
</tr>
</tbody>
</table>

 

## Operation: File System Filter Drivers


File system filter drivers should handle PnP IRPs according to the following guidelines:

-   When a volume is about to be removed gracefully by the user, the PnP Manager sends an IRP\_MN\_QUERY\_REMOVE\_DEVICE request. On receiving this IRP, the filter must close all open handles on the volume and pass the IRP down to the next-lower driver on the stack. This is very important. If the driver fails to close all open handles, this prevents the volume from being dismounted, which in turn prevents the physical device from being ejected.

    &gt; \[!Note\]
    &gt;  On receiving an IRP\_MN\_QUERY\_REMOVE\_DEVICE request, the FAT file system immediately dismounts all volumes that it can safely remove. Thus any filter attached to a FAT volume should expect that its filter device object will be freed before the filter's completion routine is called. The NTFS file system does not do this. Thus a filter attached to an NTFS volume can expect that its device object will still be attached to the volume when the filter's completion routine is called.

     

-   IRPs that are received after an IRP\_MN\_QUERY\_REMOVE\_DEVICE request, but before an IRP\_MN\_CANCEL\_REMOVE\_DEVICE or IRP\_MN\_REMOVE\_DEVICE request is received, can safely be passed down the stack (to be failed by the storage device stack) or held in a queue until the cancel-remove or remove-device request is received.

-   If a filter receives an IRP\_MN\_CANCEL\_REMOVE\_DEVICE request after it has already closed all open handles for a volume in response to an IRP\_MN\_QUERY\_REMOVE\_DEVICE request, it can reopen the handles. However, the filter can only do this in its completion routine, after the IRP has been completed successfully by the drivers below it in the stack.

-   When a filter receives an IRP\_MN\_REMOVE\_DEVICE request, it typically does not need to perform any processing on the IRP, unless it has been holding IRPs in a queue since receiving the IRP\_MN\_QUERY\_REMOVE\_DEVICE request. If it is holding IRPs in a queue, the filter must dequeue all IRPs for the volume and &lt;i&gt;fail&lt;/i&gt; them before passing the IRP down to the next-lower driver on the stack.

-   On receiving an IRP\_MN\_SURPRISE\_REMOVAL request, the filter should do the following:

    -   Close all open handles to the volume, because the file system cannot clean up the stack until there are no outstanding references.

    -   If the filter is holding IRPs in a queue, it can either fail them or pass them down the stack (to be failed by the storage device stack).

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a Plug and Play request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
This pointer should be **NULL** for PnP IRPs.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_PNP.

<a href="" id="irpsp--minorfunction"></a>*IrpSp-&gt;MinorFunction*  
One of the following:

-   IRP\_MN\_CANCEL\_REMOVE\_DEVICE
-   IRP\_MN\_QUERY\_REMOVE\_DEVICE
-   IRP\_MN\_REMOVE\_DEVICE
-   IRP\_MN\_START\_DEVICE
-   IRP\_MN\_SURPRISE\_REMOVAL

## See also


[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_PNP (WDK Kernel Reference)**](https://msdn.microsoft.com/library/windows/hardware/ff550772)

[**IRP\_MN\_CANCEL\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff550823)

[**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705)

[**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738)

[**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749)

[**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760)

 

 






