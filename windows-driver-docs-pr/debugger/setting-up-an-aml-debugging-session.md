---
title: Setting Up an AML Debugging Session
description: Setting Up an AML Debugging Session
ms.assetid: 04a44b92-215c-4735-9724-2b9f173f76a2
keywords: ["AMLI Debugger, setup", "checked build (debug build), of acpi.sys", "acpi.sys"]
---

# Setting Up an AML Debugging Session


## <span id="ddk_setting_up_an_aml_debugging_session_dbg"></span><span id="DDK_SETTING_UP_AN_AML_DEBUGGING_SESSION_DBG"></span>


The AMLI Debugger code is contained in Acpi.sys. In order to fully perform AML debugging, this driver must be installed on your target computer.

To activate breaking into debugger on free builds, use the **!amli set dbgbrkon** command, that is part of the AMLI Debugger extensions. For more information, see [**!amli set**](-amli-set.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Up%20an%20AML%20Debugging%20Session%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




