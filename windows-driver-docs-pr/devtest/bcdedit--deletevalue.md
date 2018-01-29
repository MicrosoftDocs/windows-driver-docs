---
title: BCDEdit /deletevalue
description: The BCDEdit /deletevalue command deletes or removes a boot entry option (and its value) from the Windows boot configuration data store (BCD).
ms.assetid: 70833A12-B1F7-4AF6-952F-02A70718E870
keywords: ["BCDEdit /deletevalue Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /deletevalue
api_type:
- NA
---

# BCDEdit /deletevalue


The **BCDEdit /deletevalue** command deletes or removes a boot entry option (and its value) from the Windows boot configuration data store (BCD). Use the **BCDEdit /deletevalue** command to remove options that were added using [**BCDEdit /set**](bcdedit--set.md) command. You might need to remove boot entry options when you are testing and debugging your driver for Windows 7, Windows 8, Windows 8.1, Windows 10 and later versions of Windows.

``` syntax
     bcdedit  /deletevalue [{ID}] datatype  

   
```

To delete a boot option value that you have set, use the **BCDEdit /deletevalue** command.

For example, if you change the processor group option, **groupsize**, to a new value for testing purposes, you can revert to the default value of 64 by typing the following command and then restarting the computer.

``` syntax
bcdedit /deletevalue groupsize
```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows Vista</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2008</p></td>
</tr>
</tbody>
</table>

See also
--------

[**BCDEdit /set**](bcdedit--set.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20BCDEdit%20/deletevalue%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




