---
title: .noversion (Disable Version Checking)
description: The .noversion command disables all version checking of extension DLLs.
keywords: ["Disable Version Checking (.noversion) command", ".noversion (Disable Version Checking) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .noversion (Disable Version Checking)
api_type:
- NA
---

# .noversion (Disable Version Checking)


The **.noversion** command disables all version checking of extension DLLs.

```dbgcmd
.noversion
```

## <span id="ddk_meta_disable_version_checking_dbg"></span><span id="DDK_META_DISABLE_VERSION_CHECKING_DBG"></span>


### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

The build number of extension DLLs should match the build number of the computer that you are debugging, because the DLLs are compiled and linked with dependencies on specific versions of data structures. If the versions do not match, you typically receive the following message.

```console
*** Extension DLL(1367 Free) does not match target system(1552 Free) 
```

 

 





