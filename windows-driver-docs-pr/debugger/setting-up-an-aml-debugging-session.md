---
title: Setting Up an AML Debugging Session
description: Setting Up an AML Debugging Session
ms.assetid: 04a44b92-215c-4735-9724-2b9f173f76a2
keywords: ["AMLI Debugger, setup", "checked build (debug build), of acpi.sys", "acpi.sys"]
ms.author: domars
ms.date: 11/07/2018
ms.localizationpriority: medium
---

# Setting Up an AML Debugging Session


## <span id="ddk_setting_up_an_aml_debugging_session_dbg"></span><span id="DDK_SETTING_UP_AN_AML_DEBUGGING_SESSION_DBG"></span>


The AMLI Debugger code is contained in Acpi.sys. In order to fully perform AML debugging, this driver must be installed on your target computer, which it normally is.

To activate breaking into debugger on free builds, use the **!amli set dbgbrkon** command, that is part of the AMLI Debugger extensions. For more information, see [**!amli set**](-amli-set.md).

 
## See Also

[The AMLI Debugger](the-amli-debugger.md)

