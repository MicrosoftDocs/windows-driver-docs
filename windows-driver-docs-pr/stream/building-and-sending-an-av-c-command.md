---
title: Building and Sending an AV/C Command
description: Building and Sending an AV/C Command
ms.assetid: 0f5bb205-7ffe-4007-bb66-a77889af2eed
keywords:
- Avc.sys function driver WDK , command building and sending
- command building WDK AV/C
- command sending WDK AV/C
- AV/C WDK , commands
- IRPs WDK AV/C
- I/O WDK AV/C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Building and Sending an AV/C Command

The following procedure outlines the process to build and send an AV/C command:

1. The subunit driver must allocate and initialize an IRP that is appropriate for the number of drivers below itself (as specified in the next lower driver's DEVICE\_OBJECT-&gt;**StackSize** member). The style of IRP management that is implemented by the driver writer influences how to obtain an IRP to use with *Avc.sys*. Typically, a minidriver calls [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) to allocate a new IRP for an AV/C Command. Do not call [**IoInitializeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549315) on an IRP allocated in a subunit driver by **IoAllocateIrp**. Rather than trying to reinitialize and reuse an old IRP, call [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113) on the existing IRP, and then call **IoAllocateIrp** to allocate a new IRP.

    > [!NOTE]
    > For readability, the following code examples do not demonstrate error handling.

    ```cpp
    PIRP Irp;
    Irp = IoAllocateIrp(DeviceExtension->ParentDeviceObject->StackSize, FALSE);
    ```

2. The subunit driver then allocates an AVC\_COMMAND\_IRB or AVC\_MULTIFUNC\_IRB structure that is appropriate for the type of AV/C function desired and fills in the block with the desired AV/C request parameters. The reference page for each IOCTL\_AVC\_CLASS function describes which IRB the function requires. The IRB is a block of data that describes the AV/C opcode and operation to perform. Each function supported by *Avc.sys* is associated with a specific IRB structure. The memory for the IRB must be allocated from nonpaged pool. When the memory for the IRB has been allocated, fill in the parameters for the function according to its associated structure definition.

    For the list of available functions and their associated structure definitions, see [AV/C Protocol Driver Function Codes](https://msdn.microsoft.com/library/windows/hardware/ff556389), [AV/C Structures](https://msdn.microsoft.com/library/windows/hardware/ff556422), and [AV/C Enumerations](https://msdn.microsoft.com/library/windows/hardware/ff556375).

    The following is a code sample that shows how the AVC\_COMMAND\_IRB structure might be allocated and initialized for an AV/C control command that consists of a single operand byte:

    ```cpp
    #include <avc.h>
    ...
    /* Define a custom pool tag to identify your subunit driver's memory allocations */
    #define CUSTOM_DRIVER_POOL_TAG 'C/VA'
    ...
    PAVC_COMMAND_IRB  AvcIrb;
    ...
    AvcIrb = ExAllocatePoolWithTag(NonPagedPool, sizeof(AVC_COMMAND_IRB), CUSTOM_DRIVER_POOL_TAG);
    ...
    RtlZeroMemory(AvcIrb, sizeof(AVC_COMMAND_IRB));

    #ifdef __cplusplus
    AvcIrb->Common.Function = AVC_FUNCTION_COMMAND;
    #else
    AvcIrb->Function = AVC_FUNCTION_COMMAND;
    #endif

    /*++ Do this to override the default time-out and retry values
    AvcIrb->TimeoutFlag = 1;
    AvcIrb->RetryFlag = 1;
    AvcIrb->Timeout.Quadpart = DEFAULT_AVC_TIMEOUT * 5;
    AvcIrb->Retries = 1;
    --*/
    AvcIrb->CommandType = AVC_CTYPE_CONTROL;
    AvcIrb->Opcode = Opcode;
    AvcIrb->OperandLength = 1;
    AvcIrb->Operand[0] = Operand;
    ```

3. The subunit driver must specify the IRP's **MajorFunction** and **Parameters.DeviceIoControl.IoControlCode** members as well as the pointer to the IRB that was allocated in step 2. After you allocate an IRP from the operating system, then allocate nonpaged memory for a corresponding IRB, and then set up the parameters for the IRB, you must associate the IRB with the IRP. Depending on the IRB's function code, the correct dispatch routine must be specified in the IRP. For AV/C function codes that correspond to IOCTL\_AVC\_CLASS (that is, the **Parameters.DeviceIoControl.IoControlCode** member is set to IOCTL\_AVC\_CLASS), IRP\_MN\_INTERNAL\_DEVICE\_CONTROL must be specified as the allocated IRP's **MajorFunction** value. All other AV/C function codes supported by *Avc.sys*, such as [**IOCTL\_AVC\_UPDATE\_VIRTUAL\_SUBUNIT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff560798), [**IOCTL\_AVC\_REMOVE\_VIRTUAL\_SUBUNIT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff560793), and [**IOCTL\_AVC\_BUS\_RESET**](https://msdn.microsoft.com/library/windows/hardware/ff560783), must specify IRP\_MJ\_DEVICE\_CONTROL as the allocated IRP's **MajorFunction** value.

    The following code sample shows how to set up the IRP for *Avc.sys* to process:

    ```cpp
    #include <avc.h>
    ...
    PAVC_COMMAND_IRB  AvcIrb;
    PIRP Irp;
    PIO_STACK_LOCATION NextIrpStack;
    ...
    AvcIrb = ExAllocatePoolWithTag(NonPagedPool, sizeof(AVC_COMMAND_IRB), 'C/VA');
    ...
    Irp = IoAllocateIrp(DeviceExtension->ParentDeviceObject->StackSize, FALSE);
    ...
    NextIrpStack = IoGetNextIrpStackLocation(Irp);
    NextIrpStack->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;
    NextIrpStack->Parameters.DeviceIoControl.IoControlCode = IOCTL_AVC_CLASS;
    NextIrpStack->Parameters.Others.Argument1 = AvcIrb;
    ```

4. The subunit driver must specify an I/O completion routine for the IRP that, at a minimum, parses the response. The completion routine can also free the IRP and IRB resources allocated earlier for IRPs that do not complete synchronously (that is, the completion routine only frees the IRP and IRB resources if the IRP was marked as pending earlier).

    An I/O completion routine is required because subunit drivers must allocate IRPs to communicate with *Avc.sys*. The completion routine prevents the I/O manager from continuing to process the subunit driver's allocated IRP after the subunit's call to the lower driver completes. The I/O completion routine must always return STATUS\_MORE\_PROCESSING\_REQUIRED. Beyond that requirement, a subunit driver may implement its control flow and resource management mechanisms.

    When a subunit driver sets the I/O completion routine, it can include a PVOID context parameter. This parameter can be a pointer to anything, as long as the completion routine is written specifically to deal with it. If the subunit driver is sure to make AV/C requests that never involve *interim processing*, then the I/O completion routine can be very simple: use it to trigger a [**KSEVENT**](https://msdn.microsoft.com/library/windows/hardware/ff561744) (passed as the PVOID context). The main code path that calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) (described in step 5) provides the storage for the event, and uses [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) to synchronize with the completion routine. The IRP and IRB are freed by the main code path.

    If, however, the subunit driver is sending a request that is likely to involve interim processing, the completion routine is responsible for handling the response and freeing the IRP and IRB resources. The main code path relinquishes all IRP processing responsibility to the completion routine.

5. The subunit driver then calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) and passes the next lower driver (as returned by the call to [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300) in the subunit driver's **AddDevice** routine) and the IRP to be processed to *Avc.sys*.

    ```cpp
    status = IoCallDriver( DeviceExtension->NextLowerDriver, Irp );
    ```

Repeat Steps 1 through 5 as necessary.

*Avc.sys* attempts to guarantee that an AV/C request is made and at least an interim response is received within the span of the call. The following table describes the possible **IoCallDriver** return codes that indicate how the AV/C request was handled.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>STATUS_SUCCESS</p></td>
<td><p>The request was made, and a final response was received within the bounds of the AV/C specification&#39;s time-out and retry parameters. The subunit&#39;s response code (the <strong>ResponseCode</strong> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554140" data-raw-source="[&lt;strong&gt;AVC_COMMAND_IRB&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554140)"><strong>AVC_COMMAND_IRB</strong></a> structure) must still be examined to determine the true result of the operation. STATUS_SUCCESS simply means that a round-trip request and response cycle was completed in less than 100 ms (assuming the default timeout was not changed from 100 ms).</p></td>
</tr>
<tr class="even">
<td><p>STATUS_TIMEOUT</p></td>
<td><p>The request was made, but no response was received before all time-out and retry processing was complete. Note, the target AV/C device ignores requests if a previous request is still being processed. Some AV/C devices do not comply and refuse to respond within the 100-ms time-out, even after several successive attempts. The AVC_COMMAND_IRB structure permits the adjustment of the default <strong>Timeout</strong> and <strong>Retries</strong> members (100 ms and 9 ms, respectively), but these default settings have been sufficient for all known implementations.</p></td>
</tr>
<tr class="odd">
<td><p>STATUS_PENDING</p></td>
<td><p>The request was made, and an interim response was received. It is the responsibility of the subunit driver&#39;s I/O completion routine to handle the final response and then free the IRP and IRB resources.</p></td>
</tr>
<tr class="even">
<td><p>STATUS_REQUEST_ABORTED</p></td>
<td><p><em>Avc.sys</em> has ended the operation, which can happen for several reasons.</p>
<p>The AV/C command/request was waiting for a response after an interim response had been received, but the IEEE 1394 bus was reset (and these commands would silently be dropped by the subunit).</p>
<p>Internal AV/C IRP processing has been abnormally terminated, so any outstanding commands are stopped, although the commands might still be in progress on the device).</p>
<p>The subunit was unplugged, or <em>Avc.sys</em> was disabled (for example from Device Manager).</p>
<p>In all these scenarios, the subunit driver should retry the command in case the error condition is transient.</p></td>
</tr>
</tbody>
</table>

Any other return value from **IoCallDriver** indicates that an error occurred that was beyond the scope of the AV/C protocol. For example:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>STATUS_NO_SUCH_DEVICE</p></td>
<td><p>The device has been unplugged.</p></td>
</tr>
<tr class="even">
<td><p>STATUS_INSUFFICIENT_RESOURCES</p></td>
<td><p>The system is low on memory.</p></td>
</tr>
<tr class="odd">
<td><p>STATUS_INVALID_PARAMETER</p></td>
<td><p>An invalid parameter was passed to <em>Avc.sys</em>.</p></td>
</tr>
</tbody>
</table>

Basic IRP processing allows for a lower driver to either complete the IRP synchronously (immediately), or defer its completion until later. When the operation is deferred, the IRP is marked pending, and the lower driver returns STATUS\_PENDING from that driver's respective dispatch routine, which comes back to the subunit driver as the return code from **IoCallDriver**. *Avc.sys* translates the AV/C command/response protocol to this model.

Any AV/C *Status* or *inquiry* request that results in an immediate (synchronous) response is fully complete during the span of the **IoCallDriver** call. An immediate return from **IoCallDriver** indicates that the response occurs within the 100 ms AV/C response time-out constraint detailed in the AV/C specification.

A *notify* request responds immediately only if there is an error condition.

Some *control* and all *notify* requests acknowledge, but may not necessarily complete, the request within 100 ms. The acknowledgment is through an interim response, which is referred to in this documentation as *interim processing*. The result of an interim response is that **IoCallDriver** returns STATUS\_PENDING. If this result occurs, then the I/O completion routine specified in step 4 above is the point of notification when the request is finally completed by the AV/C subunit.

For more information about IRPs and IOCTLs, see [Handling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff546847).
