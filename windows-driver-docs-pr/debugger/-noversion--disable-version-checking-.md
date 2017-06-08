---
title: .noversion (Disable Version Checking)
description: The .noversion command disables all version checking of extension DLLs.
ms.assetid: ce7fbff4-7936-4bef-8236-a13957ada7f4
keywords: ["Disable Version Checking (.noversion) command", ".noversion (Disable Version Checking) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .noversion (Disable Version Checking)
api_type:
- NA
---

# .noversion (Disable Version Checking)


The **.noversion** command disables all version checking of extension DLLs.

``` syntax
.noversion
```

## <span id="ddk_meta_disable_version_checking_dbg"></span><span id="DDK_META_DISABLE_VERSION_CHECKING_DBG"></span>


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

 

Remarks
-------

The build number of extension DLLs should match the build number of the computer that you are debugging, because the DLLs are compiled and linked with dependencies on specific versions of data structures. If the versions do not match, you typically receive the following message.

``` syntax
*** Extension DLL(1367 Free) does not match target system(1552 Free) 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.noversion%20%28Disable%20Version%20Checking%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




