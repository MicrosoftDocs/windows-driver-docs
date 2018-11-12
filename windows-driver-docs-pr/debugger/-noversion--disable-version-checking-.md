---
title: .noversion (Disable Version Checking)
description: The .noversion command disables all version checking of extension DLLs.
ms.assetid: ce7fbff4-7936-4bef-8236-a13957ada7f4
keywords: ["Disable Version Checking (.noversion) command", ".noversion (Disable Version Checking) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .noversion (Disable Version Checking)
api_type:
- NA
ms.localizationpriority: medium
---

# .noversion (Disable Version Checking)


The **.noversion** command disables all version checking of extension DLLs.

```dbgcmd
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

```console
*** Extension DLL(1367 Free) does not match target system(1552 Free) 
```

 

 





