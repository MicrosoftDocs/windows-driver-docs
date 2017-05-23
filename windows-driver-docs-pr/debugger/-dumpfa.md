---
title: dumpfa
description: The dumpfa extension displays the contents of a failure analysis entry.
ms.assetid: 4516252d-b6c9-4bf4-b435-6c0b3cb0fbc3
keywords: ["failure analysis entries, display", "failure analysis entries", "dumpfa Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- dumpfa
api_type:
- NA
---

# !dumpfa


The **!dumpfa** extension displays the contents of a failure analysis entry.

``` syntax
!dumpfa Address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the failure analysis entry that is displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **.dumpfa** extension is useful only to debug the [**!analyze**](-analyze.md) extension, as the following example shows.

``` syntax
0:000> !dumpfa 0x00a34140
DataUsed 3b0
Type =        DEBUG_FLR_MARKER_BUCKET 00010016 - Size = 9
Type =          DEBUG_FLR_MARKER_FILE 0001000d - Size = 16
Type =      DEBUG_FLR_SYSXML_LOCALEID 00004200 - Size = 4
Type =      DEBUG_FLR_SYSXML_CHECKSUM 00004201 - Size = 4
Type =         DEBUG_FLR_READ_ADDRESS 0000000e - Size = 8
Type =          DEBUG_FLR_FAULTING_IP 80000000 - Size = 8
Type =     DEBUG_FLR_MM_INTERNAL_CODE 00001004 - Size = 8
Type = DEBUG_FLR_CPU_MICROCODE_VERSION 0000301f - Size = 28
Type = DEBUG_FLR_CUSTOMER_CRASH_COUNT 0000300b - Size = 8
Type =    DEBUG_FLR_DEFAULT_BUCKET_ID 00010008 - Size = 12
Type =         DEBUG_FLR_BUGCHECK_STR 00000600 - Size = 5
Type = DEBUG_FLR_LAST_CONTROL_TRANSFER 0000000a - Size = 18
Type =           DEBUG_FLR_TRAP_FRAME c0000002 - Size = 8
Type =           DEBUG_FLR_STACK_TEXT 00010005 - Size = 1fb
Type =        DEBUG_FLR_STACK_COMMAND 00010004 - Size = 17
Type =        DEBUG_FLR_OS_BUILD_NAME 0000301e - Size = 9
Type =          DEBUG_FLR_MODULE_NAME 00010006 - Size = 8
Type =           DEBUG_FLR_IMAGE_NAME 00010001 - Size = c
Type =      DEBUG_FLR_IMAGE_TIMESTAMP 80000002 - Size = 8
```

You can also use the [**!asd**](-asd.md) extension to debug the [**!analyze**](-analyze.md) extension.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!dumpfa%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




