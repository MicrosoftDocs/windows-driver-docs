---
title: .leave
description: The .leave token is used to exit from a .catch block.
ms.assetid: 82c5cbf7-bccd-4abf-b52a-2db65e0a0c2c
keywords: [".leave Windows Debugging"]
topic_type:
- apiref
api_name:
- .leave
api_type:
- NA
---

# .leave


The **.leave** token is used to exit from a [**.catch**](-catch.md) block.

``` syntax
    .catch { ... ; .if (Condition) .leave ; ... } 
```

## <span id="ddk_token_leave_dbg"></span><span id="DDK_TOKEN_LEAVE_DBG"></span>


### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about other control flow tokens and their use in debugger command programs, see [Using Debugger Command Programs](using-debugger-command-programs.md).

Remarks
-------

When a **.leave** token is encountered within a [**.catch**](-catch.md) block, the program exits from the block, and execution resumes with the first command after the closing brace.

Since there is no control flow token equivalent to the C **goto** statement, you will usually use the **.leave** token within an [**.if**](-if.md) conditional, as shown in the syntax examples above. However, this is not actually required.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.leave%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




