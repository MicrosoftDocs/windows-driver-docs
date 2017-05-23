---
title: ~s (Change Current Processor)
description: The ~s command sets which processor is debugged on a multiprocessor system.In kernel mode, ~s changes the current processor.
ms.assetid: bd036a25-1e3c-4b57-9c7c-5f1730008cd7
keywords: ["Change Current Processor (~s) command", "multiprocessor computer, Change Current Processor (~s) command", "processors", "~s (Change Current Processor) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ~s (Change Current Processor)
api_type:
- NA
---

# ~s (Change Current Processor)


The **~s** command sets which processor is debugged on a multiprocessor system.

In kernel mode, **~s** changes the current processor. Do not confuse this command with the [**~s (Set Current Thread)**](-s--set-current-thread-.md) command (which works only in user mode), the [**|s (Set Current Process)**](-s--set-current-process-.md) command, the [**||s (Set Current System)**](--s--set-current-system-.md) command, or the [**s (Search Memory)**](s--search-memory-.md) command.

``` syntax
~Processor s
```

## <span id="ddk_cmd_change_current_processor_dbg"></span><span id="DDK_CMD_CHANGE_CURRENT_PROCESSOR_DBG"></span>Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the number of the processor to debug.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can specify processors only in kernel mode. In user mode, the tilde (~) refers to a thread.

You can immediately tell when you are working on a multiple processor system by the shape of the kernel debugging prompt. In the following example, 0: means that you are debugging the first processor in the computer.

``` syntax
0: kd>
```

Use the following command to switch between processors:

``` syntax
0: kd> ~1s
1: kd>
```

Now the second processor in the computer that is being debugged.

## <span id="see_also"></span>See also


[Multiprocessor Syntax](multiprocessor-syntax.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20~s%20%28Change%20Current%20Processor%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





