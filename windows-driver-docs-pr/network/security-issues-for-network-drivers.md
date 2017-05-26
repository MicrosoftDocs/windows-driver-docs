---
title: Security Issues for Network Drivers
description: This section describes security issues specific to network drivers
ms.assetid: 04400213-9bd4-4dbe-b302-24917450829f
keywords:
- network drivers WDK , security
- security WDK networking
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Security Issues for Network Drivers

For a general discussion on writing secure drivers, see [Creating Reliable Kernel-Mode Drivers](https://msdn.microsoft.com/library/windows/hardware/ff542904).

Beyond following safe coding practices and the general device driver guidance, network drivers should do the following to enhance security:

- All network drivers should validate values that they read from the registry. Specifically, the caller of [**NdisReadConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564511) or [**NdisReadNetworkAddress**](https://msdn.microsoft.com/library/windows/hardware/ff564512) must not make any assumptions about values read from the registry and must validate each registry value that it reads. If the caller of **NdisReadConfiguration** determines that a value is out of bounds, it should use a default value instead. If the caller of **NdisReadNetworkAddress** determines that a value is out of bounds, it should use the permanent medium access control (MAC) address or a default address instead.

## OID-specific issues

- A miniport driver, in its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) or [**MiniportCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559362) functions, should validate any object identifier (OID) value that the driver is requested to set. If the driver determines that the value to be set is out of bounds, it should fail the set request. For more information about object identifiers, see [Obtaining and Setting Miniport Driver Information and NDIS Support for WMI](obtaining-and-setting-miniport-driver-information-and-ndis-support-for.md).

- If an intermediate driver's *MiniportOidRequest* function does not pass a set operation to an underlying miniport driver, the function should validate the OID value. For more information, see [Intermediate Driver Query and Set Operations](intermediate-driver-query-and-set-operations.md).

### Query OID security guidelines

Most Query OIDs can be issued by any usermode application on the system. Follow these specific guidelines for Query OIDs.

1. Always validate the size of the buffer is large enough for the output. Any query OID handler without an output buffer size check has a security bug.

```c++
if (oid->DATA.QUERY_INFORMATION.InformationBufferLength < sizeof(ULONG)) {
    oid->DATA.QUERY_INFORMATION.BytesNeeded = sizeof(ULONG);
    return NDIS_STATUS_INVALID_LENGTH;
}
```

2. Always write a correct and minimal value to BytesWritten. It is a red flag to assign `oid->BytesWritten = oid->InformationBufferLength` like the following example does.

```c++
  // ALWAYS WRONG
  oid->DATA.QUERY_INFORMATION.BytesWritten = DATA.QUERY_INFORMATION.InformationBufferLength; 
```
The OS will copy BytesWritten bytes back to a usermode application. If BytesWritten is larger than the number of bytes the driver actually wrote, then the OS might end up copying back uninitialized kernel memory to usermode, which would be an information disclosure vulnerability. Instead, use code similar to this:

```c++
oid->DATA.QUERY_INFORMATION.BytesWritten = sizeof(ULONG);
``` 

3. Never read values back from the buffer. In some cases, the output buffer of an OID is directly mapped into a hostile usermode process. The hostile process can change your output buffer after you’ve written to it. For example, the code below can be attacked, because an attacker can change NumElements after it is written:

```c++
output->NumElements = 4;
for (i = 0 ; i < output->NumElements ; i++) {
    output->Element[i] = . . .;
}
```
To avoid reading back from the buffer, keep a local copy. For example, to fix the above example, introduce a new stack variable:

```c++
ULONG num = 4;
output->NumElements = num;
for (i = 0 ; i < num; i++) {
    output->Element[i] = . . .;
}
```

With this approach, the for loop reads back from the driver’s stack variable `num` and not from its output buffer. The driver should also mark the output buffer with the `volatile` keyword, to prevent the compiler from silently undoing this fix.

### Set OID security guidelines

Most Set OIDs can be issued by a usermode application running in the Administrators or System security groups. Although these are generally trusted applications, the miniport driver still must not permit memory corruption or injection of kernel code. Follow these specific rules for Set OIDs:

1.  Always validate the input is large enough. Any OID set handler without an input buffer size check has a security vulnerability.

```c++
if (oid->DATA.SET_INFORMATION.InformationBufferLength < sizeof(ULONG)) {
    return NDIS_STATUS_INVALID_LENGTH;
}
```

2. Whenever validating an OID with an embedded offset, you must validate that the embedded buffer is within the OID payload. This requires several checks. For example, [OID_PM_ADD_WOL_PATTERN](https://msdn.microsoft.com/en-us/library/windows/hardware/ff569764) may deliver an embedded pattern, that needs to be checked. Correct validation requires checking:

    1. InformationBufferSize >= sizeof(NDIS_PM_PACKET_PATTERN)

    ```c++
    PmPattern = (PNDIS_PM_PACKET_PATTERN) InformationBuffer;
    if (InformationBufferLength < sizeof(NDIS_PM_PACKET_PATTERN))
    {
        Status = NDIS_STATUS_BUFFER_TOO_SHORT;
        *BytesNeeded = sizeof(NDIS_PM_PACKET_PATTERN);
        break;
    }
    ```

    2. Pattern->PatternOffset + Pattern->PatternSize does not overflow

    ```c++
    ULONG TotalSize = 0;
    if (!NT_SUCCESS(RtlUlongAdd(Pattern->PatternOffset, Pattern->PatternSize, &TotalSize) ||
        TotalSize > InformationBufferLength) 
    {
        return NDIS_STATUS_INVALID_LENGTH;
    }
    ```

    These two checks can be combined using code like the following example:

    ```c++
    ULONG TotalSize = 0;
    if (InformationBufferLength < sizeof(NDIS_PM_PACKET_PATTERN) ||
        !NT_SUCCESS(RtlUlongAdd(Pattern->PatternSize, Pattern->PatternOffset, &TotalSize) ||
        TotalSize > InformationBufferLength) 
    {
        return NDIS_STATUS_INVALID_LENGTH;
    }
    ```
   
   3. InformationBuffer + Pattern->PatternOffset + Pattern->PatternLength does not overflow

    ```c++
    ULONG TotalSize = 0;
    if (!NT_SUCCESS(RtlUlongAdd(Pattern->PatternOffset, Pattern->PatternLength, &TotalSize) ||
        (!NT_SUCCESS(RtlUlongAdd(TotalSize, InformationBuffer, &TotalSize) ||
        TotalSize > InformationBufferLength) 
    {
        return NDIS_STATUS_INVALID_LENGTH;
    }
    ```

    4. Pattern->PatternOffset + Pattern->PatternLength <= InformationBufferSize

    ```c++
    ULONG TotalSize = 0;
    if(!NT_SUCCESS(RtlUlongAdd(Pattern->PatternOffset, Pattern->PatternLength, &TotalSize) ||
        TotalSize > InformationBufferLength)) 
    {
        return NDIS_STATUS_INVALID_LENGTH;
    }
    ```
   
### Method OID security guidelines

Method OIDs can be issued by a usermode application running in the Administrators or System security groups. They are a combination of a Set and a Query, so both preceding lists of guidance also apply to Method OIDs.

### Other network driver security issues

- Many NDIS miniport drivers expose a control device by using NdisRegisterDeviceEx. Those that do this must audit their IOCTL handlers, with all the same security rules as a WDM driver. For more information, see [Security Issues for I/O Control Codes](https://msdn.microsoft.com/en-us/library/windows/hardware/ff563700(v=vs.85).aspx).

- Well-designed NDIS miniport drivers should not rely on being called in a particular process context, nor interact very closely with usermode (with IOCTLs & OIDs being the exception). It would be a red flag to see a miniport that opened usermode handles, performed usermode waits, or allocated memory against usermode quota. That code should be investigated.

- Most NDIS miniport drivers should not be involved in parsing packet payloads. In some cases, though, it may be necessary. If so, this code should be audited very carefully, as the driver is parsing data from an untrusted source.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")