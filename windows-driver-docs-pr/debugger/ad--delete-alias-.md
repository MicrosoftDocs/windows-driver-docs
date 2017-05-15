---
title: ad (Delete Alias)
description: The ad command deletes an alias from the alias list.
ms.assetid: 8ff223b6-5cfb-4d87-b45f-ad9bd51faf7f
keywords: ["ad (Delete Alias) Windows Debugging"]
topic_type:
- apiref
api_name:
- ad (Delete Alias)
api_type:
- NA
---

# ad (Delete Alias)


The **ad** command deletes an alias from the alias list.

``` syntax
ad [/q] Name 
ad * 
```

## <span id="ddk_cmd_delete_alias_dbg"></span><span id="DDK_CMD_DELETE_ALIAS_DBG"></span>Parameters


<span id="________q______"></span><span id="________Q______"></span> **/q**   
Specifies quiet mode. This mode hides the error message if the alias that *Name* specifies does not exist.

<span id="_______Name______"></span><span id="_______name______"></span><span id="_______NAME______"></span> *Name*   
Specifies the name of the alias to delete. If you specify an asterisk (\*), all aliases are deleted (even if there is an alias whose name is "\*").

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to use aliases, see [Using Aliases](using-aliases.md).

Remarks
-------

You can use the **ad** command to delete any user-named alias. But you cannot use this command to delete a fixed-name alias ($u0 to $u9).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20ad%20%28Delete%20Alias%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




