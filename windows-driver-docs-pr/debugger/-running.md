---
title: running
description: The running extension displays a list of running threads on all processors of the target computer.
ms.assetid: 08fd9806-36e9-4589-bf92-87dc02efebac
keywords: ["running Windows Debugging"]
topic_type:
- apiref
api_name:
- running
api_type:
- NA
---

# !running


The **!running** extension displays a list of running threads on all processors of the target computer.

``` syntax
!running [-i] [-t]
```

## <span id="ddk__running_dbg"></span><span id="DDK__RUNNING_DBG"></span>Parameters


<span id="_______-i______"></span><span id="_______-I______"></span> **-i**   
Causes the display to include idle processors as well.

<span id="_______-t______"></span><span id="_______-T______"></span> **-t**   
Causes a stack trace to be displayed for each processor.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about debugging multiprocessor computers, see [Multiprocessor Syntax](multiprocessor-syntax.md).

Remarks
-------

With no options, **!running** will display the affinity of all active processors and all idle processors. For all active processors, it will also display the current and next thread fields from the process control block (PRCB) and the state of the 16 built-in queued spin locks.

Here is an example from a multiprocessor Itanium system:

``` syntax
0: kd> !running
 
System Processors 3 (affinity mask)
 Idle Processors 0
 
     Prcb              Current           Next
  0  e0000000818f8000  e0000000818f9e50  e0000000866f12f0  ................
 1  e000000086f16010  e00000008620ebe0  e000000086eddbc0  .O..............
```

The 16 characters at the end of each line indicate the built-in queued spin locks (the LockQueue entries in the PRCB). A period ( . ) indicates that the lock is not in use, **O** means the lock is owned by this processor, and **W** means the processor is queued for the lock. To see more information about the spin lock queue, use [**!qlocks**](-qlocks.md).

Here is an example that shows active and idle processors, along with their stack traces:

``` syntax
0: kd> !running -it
 
System Processors f (affinity mask)
  Idle Processors f
All processors idle.
 
     Prcb      Current   Next
  0  ffdff120  805495a0            ................
 
ChildEBP RetAddr
8053e3f0 805329c2 nt!RtlpBreakWithStatusInstruction
8053e3f0 80533464 nt!_KeUpdateSystemTime+0x126
ffdff980 ffdff980 nt!KiIdleLoop+0x14
 
 1  f87e0120  f87e2e60            ................
 
ChildEBP RetAddr
f87e0980 f87e0980 nt!KiIdleLoop+0x14
 
 2  f87f0120  f87f2e60            ................
 
ChildEBP RetAddr
f87f0980 f87f0980 nt!KiIdleLoop+0x14
 
  3  f8800120  f8802e60            ................
 
ChildEBP RetAddr
f8800980 f8800980 nt!KiIdleLoop+0x14
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!running%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




