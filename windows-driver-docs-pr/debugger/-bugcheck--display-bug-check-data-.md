---
title: .bugcheck (Display Bug Check Data)
description: The .bugcheck command displays the data from a bug check on the target computer.
ms.assetid: 4b453b5a-4a3c-4056-92e7-b6a17f987fa4
keywords: [".bugcheck (Display Bug Check Data) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .bugcheck (Display Bug Check Data)
api_type:
- NA
---

# .bugcheck (Display Bug Check Data)


The **.bugcheck** command displays the data from a bug check on the target computer.

```
    .bugcheck 
```

## <span id="ddk_meta_display_bug_check_data_dbg"></span><span id="DDK_META_DISPLAY_BUG_CHECK_DATA_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about bug checks, see [Bug Checks (Blue Screens)](bug-checks--blue-screens-.md). For a description of individual bug checks, see the [Bug Check Code Reference](bug-check-code-reference2.md) section.

Remarks
-------

This command displays the current bug check data. (This bug check data will be accessible until the crashed machine is rebooted.)

You can also display bug check data on 32-bit systems by using **dd NT!KiBugCheckData L5**, or on 64-bit systems by using **dq NT!KiBugCheckData L5**. However, the .bugcheck command is more reliable, because it works in some scenarios that the [**d\* (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command will not (such as user-mode minidumps).

The [**!analyze**](-analyze.md) extension command is also useful after a bug check occurs.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.bugcheck%20%28Display%20Bug%20Check%20Data%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




