---
title: ioctldecode
description: The ioctldecode extension displays the Device Type, Required Access, Function Code and Transfer Type as specified by the given IOCTL code. 
ms.assetid: 50B12034-E5C7-43F2-A31E-AAC824A05D46
keywords: ["ioctldecode Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ioctldecode
api_type:
- NA
ms.localizationpriority: medium
---

# !ioctldecode


The **!ioctldecode** extension displays the *Device Type*, *Required Access*, *Function Code* and *Transfer Type* as specified by the given IOCTL code. For more information about IOCTL control codes, see [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023).

```dbgcmd
!ioctldecode IoctlCode 
```

## <span id="ddk__ioresdes_dbg"></span><span id="DDK__IORESDES_DBG"></span>Parameters


<span id="_______IoctlCode______"></span><span id="_______ioctlcode______"></span><span id="_______IOCTLCODE______"></span> *IoctlCode*   
Specifies the hexadecimal IOCTL Code. The [**!irp**](-irp.md) command displays the IOCTL code in its output.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

To see information on the IOCTL, we first locate an IRP of interest. You can use the [**!irpfind**](-irpfind.md) command to locate an irp of interest.

Use the [**!irp**](-irp.md) command to display information about the irp.

```dbgcmd
0: kd> !irp ffffd581a6c6cd30
Irp is active with 6 stacks 6 is current (= 0xffffd581a6c6cf68)
No Mdl: No System Buffer: Thread 00000000:  Irp stack trace.  
     cmd  flg cl Device   File     Completion-Context
[N/A(0), N/A(0)]
            0  0 00000000 00000000 00000000-00000000    

                                                Args: 00000000 00000000 00000000 00000000
[N/A(0), N/A(0)]
            0  0 00000000 00000000 00000000-00000000    

                                                Args: 00000000 00000000 00000000 00000000
[N/A(0), N/A(0)]
            0  0 00000000 00000000 00000000-00000000    

                                                Args: 00000000 00000000 00000000 00000000
[N/A(0), N/A(0)]
            0  0 00000000 00000000 00000000-00000000    

                                                Args: 00000000 00000000 00000000 00000000
[N/A(0), N/A(0)]
            0  0 00000000 00000000 00000000-00000000    

                                                Args: 00000000 00000000 00000000 00000000
>[IRP_MJ_INTERNAL_DEVICE_CONTROL(f), N/A(0)]
            0 e1 ffffd581a5fbd050 00000000 fffff806d2412cf0-ffffd581a5cce050 Success Error Cancel pending
                       \Driver\usbehci        (IopUnloadSafeCompletion)
                                                Args: ffffd581a6c61a50 00000000 0x220003 00000000
```

The third argument displayed, in this case *0x220003*, is the IOCTL code. Use the IOCTL code to display information about the IOCTL, in this case [**IOCTL\_INTERNAL\_USB\_SUBMIT\_URB**](https://msdn.microsoft.com/library/windows/hardware/ff537271).

```dbgcmd
0: kd> !ioctldecode 0x220003

IOCTL_INTERNAL_USB_SUBMIT_URB

Device Type    : 0x22 (FILE_DEVICE_WINLOAD) (FILE_DEVICE_USER_MODE_BUS) (FILE_DEVICE_USB) (FILE_DEVICE_UNKNOWN)
Method         : 0x3 METHOD_NEITHER 
Access         : FILE_ANY_ACCESS
Function       : 0x0
```

If you provide an IOCTL code that is not available, you will see this type of output.

```dbgcmd
0: kd> !ioctldecode 0x1280ce

Unknown IOCTL  : 0x1280ce 

Device Type    : 0x12 (FILE_DEVICE_NETWORK)
Method         : 0x2 METHOD_OUT_DIRECT 
Access         : FILE_WRITE_ACCESS 
Function       : 0x33
```

Although the IOCTL is not identified, information about the IOCTL fields are displayed.

Note that only a subset of publically defined IOCTLs are able to be identified by the **!ioctldecode** command.

For more information about IOCTLs see [Introduction to I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff548059).

For more general information about IRPs and IOCTLs, refer to *Windows Internals* by Mark E. Russinovich, David A. Solomon and Alex Ionescu.

 

 





