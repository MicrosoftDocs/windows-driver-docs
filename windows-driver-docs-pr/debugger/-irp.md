---
title: irp extension command
description: The irp extension displays information about an I/O request packet (IRP).
ms.assetid: 2260255d-813b-4b89-8dbe-6ce7e5596ccf
keywords: ["IRP", "IRP", "IO Request Packet", "irp Windows Debugging"]
ms.author: domars
ms.date: 08/23/2018
topic_type:
- apiref
api_name:
- irp
api_type:
- NA
ms.localizationpriority: medium
---

# !irp


The **!irp** extension displays information about an I/O request packet (IRP).

```dbgcmd
!irp Address [Detail] 
```

## <span id="ddk__irp_dbg"></span><span id="DDK__IRP_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the IRP.

<span id="_______Detail______"></span><span id="_______detail______"></span><span id="_______DETAIL______"></span> *Detail*   
If this parameter is included with any value, such as 1, the output includes the status of the IRP, the address of its memory descriptor list (MDL), its owning thread, and stack information for all of its I/O stacks, and information about each stack location for the IRP, including hexadecimal versions of the major function code and the minor function code. If this parameter omitted, the output includes only a summary of the information.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

See [Plug and Play Debugging](plug-and-play-debugging.md) and [Debugging Interrupt Storms](debugging-an-interrupt-storm.md) for applications of this extension command. For information about IRPs, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. For further information on the major and minor function codes, see the Windows Driver Kit (WDK) documentation. (These resources may not be available in some languages and countries.)

This topic describes the IRP structure, [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694).

For detailed information on decoding the IRP structure including the returned Args, see the following resources.

- Windows Internals by Mark E. Russinovich, David A. Solomon and Alex Ionescu
- Developing Drivers with the Windows Driver Foundation Guy Smith and Penny Orwick


Remarks
-------

The output also indicates under what conditions the completion routine for each stack location will be called once the IRP has completed and the stack location is processed. There are three possibilities:

<span id="________Success"></span><span id="________success"></span><span id="________SUCCESS"></span> **Success**  
Indicates that the completion routine will be called when the IRP is completed with a success code.

<span id="________Error"></span><span id="________error"></span><span id="________ERROR"></span> **Error**  
Indicates that the completion routine will be called when the IRP is completed with an error code.

<span id="________Cancel"></span><span id="________cancel"></span><span id="________CANCEL"></span> **Cancel**  
Indicates that the completion routine will be called if an attempt was made to cancel the IRP.

Any combination of these three may appear, and if any of the conditions shown are satisfied, the completion routine will be called. The appropriate values are listed at the end of the first row of information about each stack location, immediately after the **Completion-Context** entry.

Here is an example of the output from this extension for Windows 10:

```dbgcmd
0: kd> !irp ac598dc8
Irp is active with 2 stacks 1 is current (= 0xac598e38)
 No Mdl: No System Buffer: Thread 8d1c7bc0:  Irp stack trace.  
     cmd  flg cl Device   File     Completion-Context
>[IRP_MJ_FILE_SYSTEM_CONTROL(d), N/A(0)]
            1 e1 8a6434d8 ac598d40 853220cb-a89682d8 Success Error Cancel pending
           \FileSystem\Npfs fltmgr!FltpPassThroughCompletion
            Args: 00000000 00000000 00110008 00000000
 [IRP_MJ_FILE_SYSTEM_CONTROL(d), N/A(0)]
            1  0 8a799710 ac598d40 00000000-00000000    
           \FileSystem\FltMgr
            Args: 00000000 00000000 0x00110008 00000000
```

Starting with Windows 10 the IRP major and minor code text is displayed, for example, "IRP\_MJ\_FILE\_SYSTEM\_CONTROL" The code value is also shown in hex, in this example "(d)".

The third argument displayed in the output, is the IOCTL code. Use the [**!ioctldecode**](-ioctldecode.md) command to display information about the IOCTL.

Here is an example of the output from this extension from Windows Vista.

```dbgcmd
0: kd> !irp 0x831f4a00
Irp is active with 8 stacks 5 is current (= 0x831f4b00)
 Mdl = 82b020d8 Thread 8c622118:  Irp stack trace.
     cmd  flg cl Device   File     Completion-Context
 [  0, 0]   0  0 00000000 00000000 00000000-00000000

                        Args: 00000000 00000000 00000000 00000000
 [  0, 0]   0  0 00000000 00000000 00000000-00000000

                        Args: 00000000 00000000 00000000 00000000
 [  0, 0]   0  0 00000000 00000000 00000000-00000000

                        Args: 00000000 00000000 00000000 00000000
 [  0, 0]   0  0 00000000 00000000 00000000-00000000

                        Args: 00000000 00000000 00000000 00000000
>[  3,34]  40 e1 828517a8 00000000 842511e0-00000000 Success Error Cancel pending
               \Driver\disk     partmgr!PmReadWriteCompletion
 Args: 00007000 00000000 fe084e00 00000004
 [  3, 0]  40 e0 82851450 00000000 842414d4-82956350 Success Error Cancel
 \Driver\PartMgr  volmgr!VmpReadWriteCompletionRoutine
                        Args: 129131bb 000000de fe084e00 00000004
 [  3, 0]   0 e0 82956298 00000000 847eeed0-829e2ba8 Success Error Cancel
 \Driver\volmgr   Ntfs!NtfsMasterIrpSyncCompletionRoutine
                        Args: 00007000 00000000 1bdae400 00000000
 [  3, 0]   0  0 82ac2020 8e879410 00000000-00000000
               \FileSystem\Ntfs
                        Args: 00007000 00000000 00018400 00000000
```

Note that the completion routine next to the driver name is set on that stack location, and it was set by the driver in the line below. In the preceding example, **Ntfs!NtfsMasterIrpSyncCompletionRoutine** was set by **\\FileSystem\\Ntfs**. The **Completion-Context** entry above **Ntfs!NtfsMasterIrpSyncCompletionRoutine**, **847eeed0-829e2ba8**, indicates the address of the completion routine, as well as the context that will be passed to **Ntfs!NtfsMasterIrpSyncCompletionRoutine**. From this we can see that the address of **Ntfs!NtfsMasterIrpSyncCompletionRoutine** is **847eeed0**, and the context that will be passed to this routine when it is called is **829e2ba8**.

**IRP major function codes**

The following information is included to help you interpret the output from this extension command.

The IRP major function codes are as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Major Function Code</th>
<th align="left">Hexadecimal Code</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IRP_MJ_CREATE</p></td>
<td align="left"><p>0x00</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_CREATE_NAMED_PIPE</p></td>
<td align="left"><p>0x01</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_CLOSE</p></td>
<td align="left"><p>0x02</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_READ</p></td>
<td align="left"><p>0x03</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_WRITE</p></td>
<td align="left"><p>0x04</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_QUERY_INFORMATION</p></td>
<td align="left"><p>0x05</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_SET_INFORMATION</p></td>
<td align="left"><p>0x06</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_QUERY_EA</p></td>
<td align="left"><p>0x07</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_SET_EA</p></td>
<td align="left"><p>0x08</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_FLUSH_BUFFERS</p></td>
<td align="left"><p>0x09</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_QUERY_VOLUME_INFORMATION</p></td>
<td align="left"><p>0x0A</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_SET_VOLUME_INFORMATION</p></td>
<td align="left"><p>0x0B</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_DIRECTORY_CONTROL</p></td>
<td align="left"><p>0x0C</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_FILE_SYSTEM_CONTROL</p></td>
<td align="left"><p>0x0D</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_DEVICE_CONTROL</p></td>
<td align="left"><p>0x0E</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
IRP_MJ_INTERNAL_DEVICE_CONTROL
IRP_MJ_SCSI</td>
<td align="left"><p>0x0F</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_SHUTDOWN</p></td>
<td align="left"><p>0x10</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_LOCK_CONTROL</p></td>
<td align="left"><p>0x11</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_CLEANUP</p></td>
<td align="left"><p>0x12</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_CREATE_MAILSLOT</p></td>
<td align="left"><p>0x13</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_QUERY_SECURITY</p></td>
<td align="left"><p>0x14</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_SET_SECURITY</p></td>
<td align="left"><p>0x15</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_POWER</p></td>
<td align="left"><p>0x16</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_SYSTEM_CONTROL</p></td>
<td align="left"><p>0x17</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_DEVICE_CHANGE</p></td>
<td align="left"><p>0x18</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_QUERY_QUOTA</p></td>
<td align="left"><p>0x19</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_SET_QUOTA</p></td>
<td align="left"><p>0x1A</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
IRP_MJ_PNP
IRP_MJ_MAXIMUM_FUNCTION</td>
<td align="left"><p>0x1B</p></td>
</tr>
</tbody>
</table>

 

The Plug and Play minor function codes are as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Minor Function Code</th>
<th align="left">Hexadecimal Code</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IRP_MN_START_DEVICE</p></td>
<td align="left"><p>0x00</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_QUERY_REMOVE_DEVICE</p></td>
<td align="left"><p>0x01</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_REMOVE_DEVICE</p></td>
<td align="left"><p>0x02</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_CANCEL_REMOVE_DEVICE</p></td>
<td align="left"><p>0x03</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_STOP_DEVICE</p></td>
<td align="left"><p>0x04</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_QUERY_STOP_DEVICE</p></td>
<td align="left"><p>0x05</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_CANCEL_STOP_DEVICE</p></td>
<td align="left"><p>0x06</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_QUERY_DEVICE_RELATIONS</p></td>
<td align="left"><p>0x07</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_QUERY_INTERFACE</p></td>
<td align="left"><p>0x08</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_QUERY_CAPABILITIES</p></td>
<td align="left"><p>0x09</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_QUERY_RESOURCES</p></td>
<td align="left"><p>0x0A</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_QUERY_RESOURCE_REQUIREMENTS</p></td>
<td align="left"><p>0x0B</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_QUERY_DEVICE_TEXT</p></td>
<td align="left"><p>0x0C</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_FILTER_RESOURCE_REQUIREMENTS</p></td>
<td align="left"><p>0x0D</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_READ_CONFIG</p></td>
<td align="left"><p>0x0F</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_WRITE_CONFIG</p></td>
<td align="left"><p>0x10</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_EJECT</p></td>
<td align="left"><p>0x11</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_SET_LOCK</p></td>
<td align="left"><p>0x12</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_QUERY_ID</p></td>
<td align="left"><p>0x13</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_QUERY_PNP_DEVICE_STATE</p></td>
<td align="left"><p>0x14</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_QUERY_BUS_INFORMATION</p></td>
<td align="left"><p>0x15</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_DEVICE_USAGE_NOTIFICATION</p></td>
<td align="left"><p>0x16</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_SURPRISE_REMOVAL</p></td>
<td align="left"><p>0x17</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_QUERY_LEGACY_BUS_INFORMATION</p></td>
<td align="left"><p>0x18</p></td>
</tr>
</tbody>
</table>

 

The WMI minor function codes are as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Minor Function Code</th>
<th align="left">Hexadecimal Code</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IRP_MN_QUERY_ALL_DATA</p></td>
<td align="left"><p>0x00</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_QUERY_SINGLE_INSTANCE</p></td>
<td align="left"><p>0x01</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_CHANGE_SINGLE_INSTANCE</p></td>
<td align="left"><p>0x02</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_CHANGE_SINGLE_ITEM</p></td>
<td align="left"><p>0x03</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_ENABLE_EVENTS</p></td>
<td align="left"><p>0x04</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_DISABLE_EVENTS</p></td>
<td align="left"><p>0x05</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_ENABLE_COLLECTION</p></td>
<td align="left"><p>0x06</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_DISABLE_COLLECTION</p></td>
<td align="left"><p>0x07</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_REGINFO</p></td>
<td align="left"><p>0x08</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_EXECUTE_METHOD</p></td>
<td align="left"><p>0x09</p></td>
</tr>
</tbody>
</table>

 

The power management minor function codes are as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Minor Function Code</th>
<th align="left">Hexadecimal Code</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IRP_MN_WAIT_WAKE</p></td>
<td align="left"><p>0x00</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_POWER_SEQUENCE</p></td>
<td align="left"><p>0x01</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_SET_POWER</p></td>
<td align="left"><p>0x02</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_QUERY_POWER</p></td>
<td align="left"><p>0x03</p></td>
</tr>
</tbody>
</table>

 

The SCSI minor function codes are as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Minor Function Code</th>
<th align="left">Hexadecimal Code</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IRP_MN_SCSI_CLASS</p></td>
<td align="left"><p>0x01</p></td>
</tr>
</tbody>
</table>

 

## <span id="see_also"></span>See also


[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**!irpfind**](-irpfind.md)

[**!ioctldecode**](-ioctldecode.md)

 

 






