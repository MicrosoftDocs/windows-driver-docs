---
title: .netsyms (Disable Network Symbol Loading)
description: .netsyms (Disable Network Symbol Loading)
ms.date: 11/28/2017
---

# .netsyms (Disable Network Symbol Loading)


## <span id="ddk_apc_meta_netsyms_dbg"></span><span id="DDK_APC_META_NETSYMS_DBG"></span>


Use the .netsyms command to allow or disallow loading symbols from a network path.

### <span id="kd_syntax"></span><span id="KD_SYNTAX"></span>Syntax

**.netsyms** *{yes|no}*

### <span id="parameters"></span><span id="PARAMETERS"></span>Parameters

<span id="yes"></span><span id="YES"></span>*yes*  
Enables network symbol loading. This is the default.

<span id="no"></span><span id="NO"></span>*no*  
Disables network symbol loading.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### <span id="remarks"></span><span id="REMARKS"></span>Remarks

Use .netsyms with no argument to display the current state of this setting.

Use [**!sym noisy**](-sym.md) or the *-n* [**WinDbg Command-Line Option**](windbg-command-line-options.md) to display additional detail as symbols are loaded.

 

 





